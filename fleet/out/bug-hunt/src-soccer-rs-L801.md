<!-- fleet job=bug-hunt id=src-soccer-rs-L801 status=done turns=13 usd=0.0131 tokens(read,write,in,out)=[241293, 40035, 28, 11346] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soccer.rs lines 801-1069 of 1069

Window `soccer.rs:801-1069` read in full. No production-reachable defect. `Match::handle` and the reducer methods in this window have no production caller: `Match` is referenced only by `tests/soccer.rs` and `tests/soccer_review.rs`. The live soccer path (`soccer_service.rs`, `soccer_match.rs`, `soccer_entry.rs`) uses `soccer::decode`/`encode` only. The findings below are latent, and each needs a future caller that passes client bytes with `Direction::ServerToClient`.

**[low] `soccer.rs:998` - `fields[0] + fields[1]` is an unchecked `u32` add on client-supplied GoalMade fields, so it panics in debug builds.**
- Failure scenario: `handle(ServerToClient, bytes)` decodes a GoalMade with `fields = [0xFFFF_FFFF, 1, 0]`. In a debug build the add at line 998 panics. In a release build it wraps to 0, and the scoreboard check at lines 1002-1007 then rejects the message, so release does not corrupt state.
- Reach: `handle` (line 835) → `apply_goal` (line 895 → 993). The GoalMade fields come straight from the wire (`GoalMade { fields: [u32; 3] }`, line 124). Nothing before line 998 bounds them. The only guard is the caller-supplied direction label, and no production code calls `handle`.
- Fix: `if fields[0].checked_add(fields[1]) != Some(fields[2]) { return Err(invalid("soccer goal scoreboard inconsistent")); }`

**[low] `soccer.rs:949-954` - the Lobby branch stores `clock.elapsed` before it validates `remaining`, then returns `Err` with the state changed.**
- Failure scenario: a message with `remaining = HALF_SECONDS + 1` and some `elapsed` returns "clock exceeds the reconstructed fallback" after `self.clock.elapsed = elapsed` (line 949) has already run. The phase stays Lobby.
- Impact is negligible: the Lobby→Running transition overwrites `elapsed` with the same packet value, and the Running→Restart→Finished branches each validate `elapsed` before writing it. The fix is to move the `remaining` check above line 949, or assign only after validation.
- Reach: `handle` (ServerToClient) → `apply_game_time` (line 892 → 943). Same latent caveat as above.

**[low] `soccer.rs:867` - `RegisterPlayer` inserts the client-supplied player id into `registered` with no cap and no check against the roster.**
- Failure scenario: a stream of RegisterPlayer packets with distinct ids grows `registered` by one entry per packet for the life of the `Match`, with no bound.
- Reach: `handle` (ServerToClient) → line 866-867. The only limit is the frame count. Same latent caveat. Low, and only relevant if a production caller is added.
