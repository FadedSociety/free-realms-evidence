<!-- fleet job=test-audit id=tests-chess-route-rs-L1 status=done turns=6 usd=0.0091 tokens(read,write,in,out)=[88365, 31409, 14, 8632] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/chess_route.rs lines 1-884 of 884

Reviewed `prototype/osfr-tools/tests/chess_route.rs` lines 1-884. Most tests are sound: they compare full `Gameplay` state before and after refusals, check the payout against content, and check that the ack-gated payout fires once. No `#[ignore]` and no early-return skips in the window. The fixtures it depends on exist (the cooking objective and station are looked up from content, and the chat strings it matches are in `activity_portal.rs`, `gameplay.rs:2235`, and `chess_service.rs:80`). Two findings:

- **[medium] prototype/osfr-tools/tests/chess_route.rs:600 active_chess_blocks_recipe_start_and_preserves_both_activities - the name claims both activities are preserved, but cooking is never active while chess runs.**
  - Why it cannot catch a regression: the body starts cooking in a separate `idle` game and never has cooking in progress in the game where chess is open. It only checks that a 26/24 request is refused (`!changed`, `!cooking_active`, state equal to `before`) and that a chess move still works. A change that discards or resets an in-flight cooking run when chess opens would still pass, because that state never exists in this test.
  - Fix: start cooking first (the idle `recipe_start` at 604 succeeds), then call `running_game_at` with that same game and assert that `cooking_active` is still true and the cooking state is unchanged after the chess Play and the refused requests. If the portal refuses Play while cooking is active, the test should assert that refusal instead and rename the test to match what it checks.

- **[low] prototype/osfr-tools/tests/chess_route.rs:712 refusals_and_illegal_traffic_change_nothing - the wrong-instance payload is checked only by `is_err()` and the coin balance, though the test name says nothing changes.**
  - Why it cannot catch a regression: the board state is not compared, so a change that alters the live table's state and still returns an error would pass. `handle_chess` stages the change on a clone and only commits it on success, so this is unlikely in practice, but the assertion does not prove it.
  - Fix: capture `let before_wrong = game.state();` before line 712 and add `assert_eq!(game.state(), before_wrong, "a wrong-instance payload changed the table");`. This also covers the earlier illegal-move and forged-move checks in the same test, which only compare coins.

- **[low] prototype/osfr-tools/tests/chess_route.rs:677-681 refusals_and_illegal_traffic_change_nothing - the unknown-id loop asserts `out.replies.len() == 1`, an exact reply count that is not what the test is about.**
  - Why it cannot catch a regression: it is not a regression check. An unrelated change that adds a second system or quest line to a refusal would fail the test without changing chess behaviour, which is churn.
  - Fix: drop the exact count and assert that `chat_text(&out)` contains "not available" and that the packets are empty, which the test already does. Keep `!out.changed`.
