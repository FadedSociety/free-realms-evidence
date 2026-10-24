<!-- fleet job=test-audit id=tests-piece-008-rs-L1 status=done turns=5 usd=0.0078 tokens(read,write,in,out)=[52471, 25552, 12, 8080] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_008.rs lines 1-498 of 498

Window `prototype/osfr-tools/tests/piece_008.rs` lines 1-498 reviewed against `src/restoration/piece_008.rs` (special_code, engine_move_bytes, status, play, resign, player_left, snapshot, ChessSessions). Most assertions are real: castle sentinel `[0,0x3e,0,flag]` matches `engine_move_bytes`, the FLAG constants match, threefold/stalemate/insufficient-material fixtures are correct, and no `#[ignore]` or early-return skips exist. Three findings:

- **[medium] tests/piece_008.rs:396 sessions_alternate_turns_and_lock_after_the_result - the name promises a lock after the result, but the body never reaches a result and never checks a locked session.**
  - Why it cannot catch a regression: `play` and `resign` reject with `GameOver` only when `status != InProgress` or `left` is set (src 1208-1211, 1221-1223). Removing that guard would leave this test green, because the test only checks alternation and an illegal second White move (`IllegalMove`, not `GameOver`).
  - Fix: after a mate or resign in this test, assert `session.play(&mv(...)) == Err(ChessError::GameOver)` and that `moves().len()` is unchanged. Otherwise rename the test to `sessions_alternate_turns_and_reject_a_second_move_by_the_same_side`.

- **[medium] tests/piece_008.rs:460 a_finished_session_stays_finished_across_reconnect_and_player_left - `player_left` is never called on a finished session.**
  - The finished game (lines 463-481) only checks reconnect and a `GameOver` play. The `player_left` call at line 489 is on a separate in-progress session (id 30). The `winner()` path with `left` set returns `Winner::None` (src 1200-1206), so a regression where a departure on a finished game rewrites the status or winner would pass.
  - Why it cannot catch a regression: no `player_left` is applied to the finished game, so nothing observes that change.
  - Fix: after line 481, call `sessions.get_mut(20).unwrap().player_left(Side::White)`, then assert `reconnect(20)` still has `status_code == Status::WhiteMated.code()`, `winner_code == Winner::Black.code()`, and `left_side == Some(Side::White)`.

- **[low] tests/piece_008.rs:199 positions_reject_moves_that_leave_the_king_in_check - the name says the move is rejected, but the test only calls `is_legal` and never calls `apply` on the illegal move.**
  - Why it cannot catch a regression: a change in `apply` that accepts a move `is_legal` rejects, or that mutates the position before returning `Err`, would still pass.
  - Fix: assert `position.apply(&mv(e1, e2)) == Err(ChessError::IllegalMove)`, and that `position.to_fen()` is unchanged from before the call.
