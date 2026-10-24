<!-- fleet job=bug-hunt id=src-main-rs-L1 status=nothing_found turns=3 usd=0.0037 tokens(read,write,in,out)=[9797, 10901, 8, 4451] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/main.rs lines 1-307 of 307

Reviewed `prototype/osfr-tools/src/main.rs` lines 1-307 in full, plus the callers of `read_index`, `copy_asset`, `export_name` and `collect_packs`. I found no defect that meets the criteria.

Checks that came out clean:
- **`read_index` (29-73):** Block offsets are validated before use: `block+8 <= file_size` (line 34), and `visited` stops cycles. The subtraction `file_size - block - 8` at line 40 cannot underflow, because line 34 guarantees `block + 8 <= file_size`. Entry count is capped at `(file_size-block-8)/16`. Name length is capped at 4096 (line 45). Each asset's `offset+size` is checked against `file_size` with `checked_add` (line 57). Reads are `read_exact`, so truncation returns an error rather than panicking. Memory growth is bounded by bytes actually read from the pack.
- **CRC check (131):** `!crc != asset.crc` parses as `(!crc) != asset.crc`, which is correct.
- **`copy_asset` (105-138):** Seek and read are bounded by the validated `offset/size`, and the buffer is fixed at 64 KiB. Output uses `create_new`, so it will not follow or overwrite existing files. A CRC mismatch returns an error and aborts the run, so there is no false success. The leftover partial file is a minor usability issue, not a defect worth reporting.
- **`export_name` (140-150):** Output names are numeric (`{index:06}.{ext}`), so asset names never reach filesystem paths. The extension is restricted to ≤16 ASCII alphanumerics. Path traversal is blocked.
- **Catalog TSV (control-char check at line 51):** Rejects tabs and newlines, so the TSV cannot be broken by asset names.
- **`run` (152-232):** `strip_prefix(&root).unwrap()` (line 203) and `file_name().unwrap()` (line 215) are safe. Every path came from `collect_packs(&root)`, and collected entries are always `.pack` files. `collect_packs` uses `file_type()`, which does not follow symlinks, so it cannot loop.
- **Tests (241-307):** Not in scope for defects. The fixture is consistent with the parser, and the cycle and out-of-bounds cases exercise the guards above.

This is an offline extraction CLI that reads the shipped client's pack files. Nothing in the window is reachable from a remote player's packets.
