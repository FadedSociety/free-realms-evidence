<!-- fleet job=bug-hunt id=src-chess-rs-L1601 status=nothing_found turns=10 usd=0.0162 tokens(read,write,in,out)=[214858, 44224, 22, 17035] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/chess.rs lines 1601-2185 of 2185

## chess.rs 1601-2185: no reportable defects

I read the whole window and the callers it depends on: `handle_text` (chess.rs:1358-1411), `handle_human_move` (1413), `Position::is_legal` (570), `Kind::from_code` (59), `single_with_skill`/`two_player` (1063/1115), `participant`/`players`/`emit` (1171-1230), and `chess_service.rs` `handle_movie`/`start_table`/`settle` (457-590). Nothing in the window is reachable from a client packet in a way that panics, grows unbounded, corrupts a save, or grants items or coins.

What I checked and ruled out:

- **Payload framing (`parse_payload_packet`, 1955-1978).** The `len >= 20` guard covers every fixed-offset read. `length` is bounded to 128 before the `19 + length` comparison, so nothing overflows. The slice `[19..len-1]` is valid because `len >= 20`. Embedded NULs and non-UTF-8 are rejected without panic.
- **Move parsing (`parse_human_move`, 1995-2066).** `fields[0]` is safe because `split` always yields at least one element. `from`/`to` are range-checked to <64 before `piece_at`. The `from/8*8 + to%8` arithmetic cannot overflow in u8. `Kind::from_code` returns `None` for unknown codes. Castle and en-passant geometry is checked, and the final `is_legal` gate rejects any move not in the generated legal set, so client-supplied squares cannot be trusted as moves.
- **Authority and identity.** The header instance id is compared against the table's own participant. `handle_payload` takes the seat from the table, not from the packet. `validate_participant` rejects player 0 and non-positive instances, and two-player tables require distinct seats.
- **Settlement (`settle_player`, 1689-1735).** The win/grant pairing matches `MinigameRuns::finish` / `finish_win_without_reward`. `settled` is inserted only on acceptance, so a failed save leaves the seat retryable. Score and stars are fixed to 0 by the server. `won` is derived from the server-owned `result.winner`, and the same derivation is used in `chess_service::settle`.
- **Table open (`open_single*`, `open_two_player`).** Row, skill (<=100) and near-equal margin (1..=500) are validated inside `single_with_skill`. Duplicate table ids are rejected before insert. `open_seed` uses wrapping arithmetic.
- **Not reachable, so dropped.** `ChessTables::resign` and `ChessTables::disconnect` have no production caller (`chess_service.rs` never calls them), and no client packet maps to them. Their possible atomicity or settlement gaps are therefore not reachable from client input.
- **Tests (2088-2185)** are excluded by the rules.

No finding meets the bar of a concrete, client-reachable defect with a tied line.
