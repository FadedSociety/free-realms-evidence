<!-- fleet job=test-audit id=tests-common-forging-movie-rs-L1 status=done turns=8 usd=0.0042 tokens(read,write,in,out)=[59100, 12797, 18, 4069] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/forging_movie.rs lines 1-133 of 133

Reviewed `prototype/osfr-tools/tests/common/forging_movie.rs` lines 1-133. This is a shared driver with no `#[test]` functions of its own. Its callers are `forging_gameplay.rs`, `opening_gateway.rs`, `s6_characterization.rs` and `crafting_stations_route.rs`. Checked against `src/forging.rs`: the `game_id = -1` sentinel written by `text()` (bytes 11..15) is accepted for native payloads (forging.rs:422-425), so it is not a masked bug. `reach_quota` is bounded and panics on timeout. `play` checks `completed == prior + 1` against an independent snapshot, and its `active.is_none()` check runs after a real state change. Nothing restates the code under test.

- **[low] tests/common/forging_movie.rs:37 `start` - `assert_eq!(send(g, &b, now).replies.len(), 2)` pins an exact reply count on the start-game request.**
- **Why it cannot catch a regression:** this count is incidental to the start-game transaction. The movie tests are about reaching the quota and completing, so unrelated work that adds or drops a reply, such as a broadcast, breaks every caller of `start`/`play` without any real defect. It also does not check what the replies contain, so a reply-content regression with the same count passes.
- **Fix:** Replace the count with a content check on the start-game reply (for example, that the reply header is the expected sub-opcode for the game-start). Alternatively, assert only that the reply is non-empty and that the snapshot's active phase moved past `Offered`.

No high or medium findings in this window.
