<!-- fleet job=bug-hunt id=src-chess-rs-L801 status=nothing_found turns=14 usd=0.0283 tokens(read,write,in,out)=[427156, 63549, 30, 32185] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/chess.rs lines 801-1600 of 2185

## Window chess.rs 801-1600: no reachable defect found

I read the whole window (801-1600) and the callers and helpers it depends on: `legal_moves`/`apply`/`is_legal` (chess.rs:556-611), `pseudo_moves`/`add_castles` (627-800), `parse_human_move` and `validate_participant` (1995-2073), `handle_payload` (1888-1903), `payload_packet` (1942), and `chess_service.rs` `handle_movie`/`settle` (457-580) and the `player_id == 0` guard at chess_service.rs:356. Candidates I checked and dropped:

- **`apply_unchecked` `unreachable!()` (chess.rs:838).** Client input cannot reach it. `parse_human_move` (2016, 2052) and `is_legal` only admit king moves of two files that `add_castles` generates (to 2, 6, 58, 62 from home squares 4/60). Castling rights are cleared when the king moves, so a king off its home square never has them.
- **`apply_unchecked` en passant and ep-square arithmetic (858-863, 810-811).** Correct for both colours. Values stay within u8.
- **`insufficient_material` (877-896).** Correct for K v K, K+minor v K, and same-colour bishops.
- **`parse_human_move` bounds (2010-2013).** `from`/`to` are range-checked before `piece_at`. Every `fields` access is guarded by the non-empty check in `handle_text`.
- **`server_move` (1300-1329).** The window arithmetic is bounded (margin ≤ 500, skill ≤ 100). `ranked.first()?` and `candidates.max(1)` prevent an empty or zero modulus. The seed comes from OS entropy in production (chess.rs:1755-1798).
- **`score_move` centralisation term (1355).** Odd precedence, but the `ChessScoring` doc at chess.rs:174 says "the origin term is half", so it matches the documented intent. Not a defect.
- **Mutation before `?` in `accept_move`, `start`, `disconnect`, `handle_text` (1374, 1386, 1660).** The only fallible calls after mutation are `emit`/`payload_packet`, which get server-built text and seated recipients, so they cannot fail on client input.
- **`unwrap()`s at 1245, 1268, 1469, 1483, 1533, 1538, 1555.** Each one is guarded by the seating checks (`participant_for_side`, `players()`, two-seat requirement) or the preceding `apply`.
- **Phantom seat for `player_id` 0 (`participant`, 1171-1177).** Unreachable: chess_service.rs:356 rejects player 0.
- **Win/settlement paths (`game_over` 1594-1610, `resign`, `disconnect`, `settle_player` 1689-1735).** Winner is always derived from server state. A `FRServer_GameOver` from a client can only return the table's own stored result, and the `settled` set prevents double payment. A Draw settles as a loss for the mover, which the code documents as intentional (chess.rs:1712).

No finding meets the bar of a concrete, client-reachable failure with a traceable line.
