<!-- fleet job=test-audit id=tests-player-trade-rs-L1 status=done turns=6 usd=0.0076 tokens(read,write,in,out)=[95035, 30690, 14, 5542] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/player_trade.rs lines 1-1200 of 1453

Window reviewed: `prototype/osfr-tools/tests/player_trade.rs` lines 1-1200. Most tests in the window are sound: the refusal canaries compare full `TradeService` state, the settlement deltas are hard-coded, and nothing is `#[ignore]`d or returns early. The findings below are the ones I confirmed against `src/trade.rs`.

- **[medium] tests/player_trade.rs:1082 `a_battle_the_host_sees_cancels_a_session_and_an_invite` - the invite half checks only message sub-ids, not the close status that the comment says matters.**
  - Why it cannot catch a regression: at 1096-1098, `set_away(A, true)` on a pending invite asserts `subs(&end) == [15,5,15,5]` and `free(A) && free(B)`. Those pass whatever status byte the sub-15 close carries. `cancel_for` on a pending invite goes through `close_pending`, which uses `TradeStatus::PartnerDisconnected` (`src/trade.rs:1088`). A change to that status, or to the invite-withdraw path in `close_pending_with_status`, would still pass. The comment "status 2 is what clears the toast" is never checked.
  - Fix: replace the subs assertion at 1097 with `assert_eq!(closes(&end), [(sess(B), 2), (sess(A), 2)])` or whatever recipient/status pair the code is meant to produce, with the expected byte written as a literal 2, not derived from the code.

- **[medium] tests/player_trade.rs:1070 `zoning_into_another_instance_cancels_and_covers_a_battle_instance` - the name claims battle-instance coverage, but the body only moves A to `zone(9)` and calls `maintain()`.**
  - Why it cannot catch a regression: no battle path runs (`set_away`, `enter_instanced_zone` with a battle flag, or any battle-specific entry point). Removing battle handling in `set_away` or `enter_instanced_zone` would still pass, because the test never calls them. The `assert_cancelled_clean` at 1078 only verifies a zone-change cancel.
  - Fix: either drop "covers a battle instance" from the name, or add a step that calls `world.trades.set_away(A, true)` (or the instanced-zone hook) and asserts the cancel with statuses `[1,1]` and the inventory unchanged. That is what the name promises.

- **[low] tests/player_trade.rs:1118 `the_plain_cancel_hook_covers_a_session_and_an_invite` - the pending-invite cancel asserts only the sub sequence, so the status the comment calls "what clears the toast" is never checked.**
  - Why it cannot catch a regression: `cancel_for(A)` on the pending invite at 1117 gets `subs == [15,5,15,5]` and nothing about the status byte. Changing the invite-withdraw status from 2 to some other value, or sending the wrong recipient order, would still pass. The same gap exists at 1145-1155 (`expiry_closes_stale_invites...`), which checks only subs for the expired invite.
  - Fix: assert the statuses and recipients for the invite close, e.g. `closes(&end)` equal to `[(sess(B), 2), (sess(A), 2)]` (or the correct pair per the spec), in both 1117-1118 and 1155.

- **[low] tests/player_trade.rs:151 `World::open` (used throughout) - exact sub-id sequence `[4, 4]` pins the invite-accept reply shape, which is incidental to most callers.**
  - Why it cannot catch a regression: it is not wrong, but every test that calls `open()` inherits this exact-shape check, so an unrelated change to the start-of-trade message count (for example, adding a status echo) breaks dozens of tests at once. Those tests are about settlement, cancel, or refusal, not the start packet.
  - Fix: keep the `[4, 4]` check in one dedicated start test. In `open()`, assert only that the session id is returned and that both sides get a start (`started.messages.len() == 2`), or drop the strict equality.
