<!-- fleet job=test-audit id=tests-chess-rs-L1 status=done turns=5 usd=0.0086 tokens(read,write,in,out)=[64146, 29695, 12, 8576] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/chess.rs lines 1-1133 of 1133

Window reviewed: `prototype/osfr-tools/tests/chess.rs` lines 1-1133. Most assertions are sound (perft counts, Fool's mate, threefold/stalemate/50-move positions, ledger cap and restore, zero-window refusal checked against `chess_service.rs:155` and `chess.rs:1075`). Four findings:

- **[medium] tests/chess.rs:1029-1036 `a_recorded_winning_game_does_not_replay_against_fresh_tables` - the "OS-seeded table" arm does not show that `ChessService::with_state(_, None)` is OS-seeded; it only asserts the replay is not a win.**
  - Why it cannot catch a regression: if `with_state(None)` were changed to a fixed seed (for example 0), the test still passes whenever that seed does not win the line. The loop at 1020-1023 shows most seeds do not win, so the odds favour a pass. `replay` also returns `None` on divergence, so `assert_ne!` passes for any non-win.
  - Fix: build two `with_state(_, None)` services and assert they answer the same opening move differently over many tries (e.g. the `computer_replies_vary_between_fresh_tables` pattern), or assert on the seed source directly. Keep the non-win check as well.

- **[medium] tests/chess.rs:247-263 `discovered_queen_check_is_detected_and_black_must_answer_it` - the name says "discovered" check but the line (e4, f5, Qd1-h5) is a direct queen check; the queen itself moves onto the diagonal.**
  - Why it cannot catch a regression: a bug that breaks only discovered-check detection (a slider revealed by another piece moving off a line) would still pass, because no discovered check occurs. Also, `all(...)` at 258-262 is vacuously true if `legal_moves()` returns an empty list, so a generator bug that drops all moves would pass.
  - Fix: use a real discovered-check position (a piece moves off a line to uncover a check), and assert `!position.legal_moves().is_empty()` before the `all`. Or rename the test to "direct queen check".

- **[low] tests/chess.rs:720-738 `chess_mode_and_move_encoding_cover_client_castling_events` - the name promises client castling events, but the body never inspects any event; the final `Status::Draw` assertion (K+K) is about insufficient material and unrelated to castling.**
  - Why it cannot catch a regression: a change to the castling event packets (`OnChessEventMsg` for castling) would still pass, since only `engine_move_bytes`, the rook location and a draw status are checked.
  - Fix: either rename it to cover move bytes and the rook relocation only, or assert the castling event text from `ChessTables::handle_payload` for the same move, and move the K+K draw check into the draw-rules test.

- **[low] tests/chess.rs:448 `threefold_draw...` no, the relevant one is `a_recorded_winning_game...`-adjacent; concretely, tests/chess.rs:448 `fools_mate_emits_checkmate_and_settles_one_reward_once` - `assert_eq!(won.reward_packets.len(), 2)` pins an exact packet count that is incidental to the test's claim (one reward settled once).**
  - Why it cannot catch a regression: it is not a hole, but any added display or summary packet churns this test without any change in payout behaviour.
  - Fix: assert that a reward packet carrying the 7 coins exists (or that the 39/18 settle packet is present), not the total count.
