<!-- fleet job=bug-hunt id=src-startup-snapshot-rs-L801 status=nothing_found turns=7 usd=0.0068 tokens(read,write,in,out)=[64241, 24531, 16, 6099] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/startup_snapshot.rs lines 801-918 of 918

Reviewed `prototype/osfr-tools/src/startup_snapshot.rs` lines 801-918 (end of `parse_catalogues`, `read_coin_entries`, `decode_hex`, `encode_hex`) and the helpers they rely on (`Reader` at 559-619, `read_capture_inner` at 640-650, `header` at 652-662, `validate` at 254-300). I found no defect that meets the criteria.

What I checked:

- **Length-controlled allocations and reads (lines 829, 850-851, 874-876):** every count comes from `Reader::count()` (lines 598-604), which rejects anything outside `0..=MAX_ROWS` (100,000). `Vec::with_capacity` is therefore bounded. `reader.take(length)` uses `checked_add` and `slice::get`, so it cannot panic or read past the buffer.
- **Panics (lines 802-811, 877-879, 890-906, 910-917):** all `unwrap`s are on fixed-size `try_into` slices that the preceding `take` guarantees. Odd-length or non-hex input returns `Err`. Non-ASCII input in `decode_hex` is handled byte-wise and errors without panicking. The `encode_hex` indexes are masked to 0..15. The i64→i32 conversion uses `try_from`.
- **Trust/authority:** the inputs are the operator's lab reference captures and `rust-gameplay/inventory.json` (read via `parse_reference` and `export_from_reference`), not network packets. The consumer `StartupSnapshot::load` runs `validate()`, which re-checks the stored item record IDs against their typed keys, the ability kinds, and the effect blobs. No client packet reaches this code.
- **Atomicity:** this is a pure parse with no state mutation, so there is no partial-save hazard.
- **Logic:** the ability parser rejects any non-zero kind. The header and subtype checks match the file's own `header` calls. `finish()` rejects trailing bytes. None of these contradicts its doc comment or tests.

Non-window observations, not reported as findings: the item definitions have no duplicate-ID check at parse time (the capture mirrors the source, so this is not a defect by itself). `read_capture_inner` computes `7 + length` (line 646), which could overflow only on 32-bit targets and is outside my window.
