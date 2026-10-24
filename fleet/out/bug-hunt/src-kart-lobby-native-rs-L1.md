<!-- fleet job=bug-hunt id=src-kart-lobby-native-rs-L1 status=nothing_found turns=5 usd=0.0053 tokens(read,write,in,out)=[54287, 21101, 12, 4289] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_lobby_native.rs lines 1-601 of 601

Reviewed `prototype/osfr-tools/src/kart_lobby_native.rs` lines 1-601 in full (plus the cut-off `Cursor` region 282-304). No defect in this window meets the bar.

What I checked:

- **Cursor (282-318):** `remaining()` is `len - pos`, and `pos` never exceeds `len`, so it cannot underflow. `take()` checks `pos + length > len` before slicing. `i32`/`u32` go through `take(4)`.
- **`read_count` (320-339):** rejects negatives, then bounds `count <= remaining / row_bytes`. That caps `Vec::with_capacity` at the bytes actually present, so a client count cannot force a large allocation. Row sizes (20/16/16/16/24) match the wire layout in the module doc and in the encoder.
- **Display rows (380-403):** a negative length is rejected, and a length above `remaining` is rejected before `take`. The per-row minimum of 16 bytes matches `DISPLAY_ROW_FIXED_BYTES`.
- **`decode_inner` (441-484):** the length checks run before the header indexing, and `frame[8..]` is safe after the `len >= 8` check. A negative `i32` body length is rejected before the `as usize` cast. `available - declared` is only computed after `declared <= available`.
- **`decode_tunnel` (487-504):** length checked before indexing, and the `u32` inner length is compared exactly against the remaining bytes.
- **Trailing policy:** Strict rejects at both the frame level (470-476) and the body level (420-426). Tolerant returns the count. Both match the doc comments.
- **Encoders (506-580):** `i32::try_from` / `u32::try_from` guard the length prefixes. Errors return before anything is committed, and the output is a local buffer.

Reachability: the decode functions (`decode_body`, `decode_inner`, `decode_tunnel`) have no production callers under `src/`. Their only callers are tests (`tests/kart_lobby_native.rs`, `tests/kart_lobby_gameplay.rs`). The one production caller, `gameplay.rs:1059-1061`, runs `encode_inner` on a body deserialized from the operator-authored `kart_lobby.json` (capped at 256 KiB). That is not client input. The encoder's `i32`/`u32` conversions return errors rather than panicking.

Minor, not reported: the doc claim that "every variant is reachable from a committed vector" is not fully checked, and `Cursor::take`'s `pos + length` could only overflow on a 32-bit target with a frame near 2 GiB, which is not reachable with real frames.
