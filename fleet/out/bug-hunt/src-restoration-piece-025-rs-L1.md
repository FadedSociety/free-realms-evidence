<!-- fleet job=bug-hunt id=src-restoration-piece-025-rs-L1 status=nothing_found turns=6 usd=0.0065 tokens(read,write,in,out)=[69708, 25409, 14, 5248] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_025.rs lines 1-434 of 434

Reviewed `prototype/osfr-tools/src/restoration/piece_025.rs` lines 1-434 in full, plus the callers and tests that touch it (`tests/piece_025.rs`, `piece_030.rs` references, `notes/Build Guides/Gameplay/Housing.md`). No defect in the window meets the bar (panic, unbounded growth, broken atomicity, client-trusted authority, or logic error tied to a line).

What I checked:

- **Bounds in `decode` (lines 178-282):** every slice is guarded by a length check on the same body.
  - Opcode 1 requires `body.len() >= 13` and reads `[0..12]` plus `body[12]`.
  - Opcode 3 requires 8 and reads `[0..8]`.
  - Opcode 5 requires 48 (8+16+16+4+4). Quad reads land at 8..40, value at 40..44, and `trailing_at = body.len() - 4 >= 44`, so `body[44..trailing_at]` is valid and `body[trailing_at..]` is 4 bytes.
  - Opcodes 6, 19, and 20 have their own length checks.
  - The header is checked against `HEADER_LEN` (line 179) before `bytes[0..4]` is read.
- **Subtractions:** `body.len() - used` (line 278) cannot underflow, because every arm checks `body.len()` against its `used` value before returning.
- **`read_u32`/`read_u64` (lines 284-292):** every caller passes an exact-width slice, so the `copy_from_slice` cannot panic.
- **Allocation:** the only client-sized allocation is `tail: body[44..].to_vec()` (line 233). It is proportional to the datagram already in memory and is not amplified.
- **`sample()` panic (line 361):** only reachable with opcodes from the static `schema()` table, never from client input.
- **Encode/decode round trip and schema:** `wire_size` matches the encoder for every entry, and `tests/piece_025.rs` pins the byte layouts and error variants (lines 60-176). Those tests agree with the code.

Non-findings, noted for completeness: `SetEditMode` (line 245) decodes any non-zero byte as `true`, which is lossy but harmless. The opaque-tail design takes the trailing `u32` as the last four body bytes, which is a modelling choice rather than a bounds bug. Neither is a defect under the stated criteria.

Caveat: this file is a pure codec. Whether decoded housing requests are authorised (house guid, fixture guid, item definition id) is decided downstream in `housing.rs` and `piece_030.rs`, which are outside this window, so I did not evaluate that.
