<!-- fleet job=test-audit id=tests-matchmaking-routing-rs-L1 status=done turns=11 usd=0.0081 tokens(read,write,in,out)=[141601, 25572, 24, 6981] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/matchmaking_routing.rs lines 1-256 of 256

Window `tests/matchmaking_routing.rs` 1-256. Read the code under test: `gameplay/matchmaking_route.rs:12-33`, `matchmaking.rs:1244-1318` (`handles`, `route`), `matchmaking.rs:1229` (refusal text), `gameplay.rs:917-943` (catalogue load). The core assertions are sound: the join refusal is unconditional and state is compared before and after, the malformed-packet loop hits real `is_err` paths (`matchmaking.rs:1271`, `:1282`, `:1305`), and the 141/1 and 141/13 comparisons are against fixed wire bytes. The findings below are the weak spots.

- **[medium] tests/matchmaking_routing.rs:102 `battle_ids` - the expected queue list is read from `data/content/field_battles.json`, but the server builds its listings from the catalogue loaded out of the `content()` directory (`gameplay.rs:928-940`, via `OSFR_ACTIVITY_CONTENT` or the lab reference path).**
  - Why it cannot catch a regression: if the two files differ, the expectation is wrong for the content the server actually uses. A regression that drops or mis-filters a row in the loaded catalogue would only be caught if the repo copy happens to disagree. The `assert_list_canary` and the 135 equality check then compare against a file that is not the one under test.
  - Fix: derive the expected ids from the same catalogue path that `game()` loads (for example, read `content().join("field_battles.json")`, or expose the `Gameplay` activity catalogue and filter `Kind::Battle` from it).

- **[low] tests/matchmaking_routing.rs:176 `every_join_is_refused_without_state_and_the_list_still_works` - the refusal check is a substring match on "not available" and never checks that `out.replies` holds nothing except that chat line.**
  - Why it cannot catch a regression: any handler that emits some other "... not available." chat line, or that also returns an extra 141 reply on join, still passes, because only `chat_text(&out).contains(...)` is checked.
  - Fix: assert equality with the exact refusal text (`"Matchmaking for that queue is not available."`, `matchmaking.rs:1229`) and assert `out.replies.len() == 1` (the chat line only).

- **[low] tests/matchmaking_routing.rs:229 `malformed_known_requests_are_rejected_and_activity_portal_still_works` - the name claims the activity portal still works, but the only check is that some reply starts with `[167, 0, 1, 1]`.**
  - Why it cannot catch a regression: a portal reply that is empty, or lists the wrong activities, still passes as long as the 4-byte prefix matches.
  - Fix: decode the 167/1 reply (or compare it to the portal list for the same catalogue) and assert that the battle row for `BATTLE` (96) is present. Alternatively, rename the test so it no longer claims the portal behaviour.

- **[low] tests/matchmaking_routing.rs:142-144 `list_and_stats_publish_only_field_battles_and_do_not_mutate` - the test pins raw wire dword indices (`[3..=4]`, `[15]`, `[16]`) and the constants 42059 and 4543, which are layout and data details of the row encoding and not the routing behaviour the test name describes.**
  - Why it is churn: a reordering of unrelated trailing fields, or a regenerated icon or description id, breaks this routing test even though routing is unchanged. This is over-pinned, not a missed bug.
  - Fix: keep the field-level checks in `tests/matchmaking.rs` (the wire-layout file the header points to). Here, assert only that the row for `BATTLE` exists and that `queue_id()`/`member_only` agree with the catalogue entry.
