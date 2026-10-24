<!-- fleet job=bug-hunt id=src-smelting-rs-L801 status=nothing_found turns=6 usd=0.0034 tokens(read,write,in,out)=[45254, 14306, 14, 2341] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/smelting.rs lines 801-1082 of 1082

Window `prototype/osfr-tools/src/smelting.rs` 801-1082: no defects that I could tie to a reachable client input or save.

What I checked:

- **801-819 (non-test code):** `read_i32` (806-808) slices `b[offset..offset+4]` and unwraps. Its only caller in this file is `handle` (354-356), which returns early at line 347 when `inner.len() < 15`. The largest offset read is 11..15, so the slice is in bounds. `parse_score` (809-815) parses a `u32` and rejects values above 1,000,000,000, so it has no overflow path. Its callers (485, 492, 526) store one score per instance, and nothing sums scores, so the cap is sufficient. `invalid` (816-818) is a plain wrapper.
- **820-1082:** all of this is `#[cfg(test)] mod ordinary_quit`, which is excluded from the review scope. I read it only to confirm it is test-only. Its helpers (`hex`, `Fixture`) use `unwrap` on fixture data that the test controls, which is not a defect under the rules.

No findings to report.
