<!-- fleet job=bug-hunt id=src-forging-rs-L801 status=nothing_found turns=6 usd=0.0150 tokens(read,write,in,out)=[113896, 40455, 14, 17579] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/forging.rs lines 801-1504 of 1504

Reviewed `prototype/osfr-tools/src/forging.rs` lines 801-1504 in full. Lines 1215-1504 are `#[cfg(test)]` and were skipped as out of scope. I found no defect I could tie to a line and show reachable from a client packet or save, so there are no findings.

What I checked (non-test code, 801-1214):

- **`gravity` (800-845):** the in-place compaction followed by the `while target > c.top` refill fully overwrites every vacated cell in the column, so no stale tiles survive. Refill keeps `tile_queue` at 49+ before each `first()`, and `validate_run` (1042-1087) enforces 50..=70 for started runs, so the `ok_or_else` error (after partial mutation) is unreachable. Mutations happen on the `next` clone in the caller, so an error discards them anyway.
- **`validate_chain` (847-875):** bounds are checked with `in_board` before `board[i]`/`idle[i]`. Duplicates, orthogonality, same colour and idle are all enforced against server state, so client coordinates and colours are not trusted.
- **`has_move` / `has_bottom_piece` / `in_board` (877-911):** `x-1` and `y-1` cannot underflow, because `validate_content` (1011-1016) enforces `left,top >= 1`. `x+1` and `y+1` stay below `SIDE`, because `left+width` and `top+height < SIDE` are enforced (1017-1018). The flood fill counts a true connected same-colour component.
- **`random_tile` / `rng` (912-927):** the modulo divisor is `selectable_types.len()`, which `validate_content` makes non-empty. Xorshift cannot reach 0, and `validate_state` (214) rejects `rng == 0`.
- **`validate_content` / `validate_run` (999-1087):** the `quota` short-circuit prevents `100 % 0`. The board-shape and tile-queue checks run before any indexing. `idle.len() == board.len()` is enforced in `validate_state` (212), so `validate_chain`'s `idle[i]` cannot go out of range.
- **`number_list` / `coordinates` / `number` / `boolean` (1089-1122):** the stride and count are checked before parsing. `chunks_exact` leaves no remainder. The u16 to usize casts are bounded by `in_board` or `x >= SIDE` checks at the call sites (`OnChainMsg` 500-501, `OnIdleMsg` 544-547, `OnVerifyMsg` 555-559, `OnLevelEventMsg 50` 566-569).
- **`payload_packet_with_game` / `decode_payload` / `validate_text` (1133-1161):** the 15-byte header and the `read_i32(b, 15)` offset are correct. The `b.len() >= 20` guard covers the read, and `19 + n` and the `[19..len-1]` slice are in range because `n >= 1`. `validate_text` rejects non-ASCII before `from_utf8` results are trusted.
- **`results` / `game_over` / `launch_packet` (1183-1207):** `elapsed` is bounded by `duration <= 300` and `score <= 1e9`, so the `as i32` casts are safe. `read_i32` callers in 408-424 are protected by the exact `inner.len() == 15` check at 389.
- **`initialize_board` (708-798, outside window, read for reach):** `width >= 3` guarantees the `left..left+3` bottom-row writes are in range.
