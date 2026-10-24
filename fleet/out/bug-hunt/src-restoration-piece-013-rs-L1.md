<!-- fleet job=bug-hunt id=src-restoration-piece-013-rs-L1 status=nothing_found turns=6 usd=0.0069 tokens(read,write,in,out)=[60787, 26451, 14, 6055] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_013.rs lines 1-396 of 396

## Window reviewed: `prototype/osfr-tools/src/restoration/piece_013.rs` lines 1-396 (whole file)

No defect I can tie to a client packet or save. I read the whole window, then checked reachability and cross-checked the Rust against the Python reference (`scripts/pieces/piece_013.py` `classify_phases`, lines 308-470) and the owned tests (`tests/piece_013.rs`).

**Why nothing is reportable**

- **Not reachable from the network.** `classify_phases`, `check_content` and `check_payload_surface` have no callers in `src/` outside this file. The module is not registered in `lib.rs` (`notes/Research/Pieces/013 Smelting recipes/content.md:137`). The only callers are `tests/piece_013.rs`, which includes the file by `#[path]`. The input is operator-prepared JSON (`phases[].stage_type/data`), not a player packet or save.
- **Possible debug-only panic, not client-reachable.** `line 280` calls `data[5].abs()`. For `i32::MIN` this overflows and panics in debug builds, and wraps in release. The value comes from prepared content, not a client. It would only matter if the lead wires `check_content` into content loading and a hand-edited file contains `-2147483648`. Worth a one-line `unsigned_abs()` fix when the module is registered, but it is not a remote defect.
- **Arithmetic and indexing are bounded.** `line 294` `2 * score` is safe because `score` is always `clip(..., 10_000)`. Every `data[cell]` index is a compile-time constant or a loop over 0..=10. `ore_index` is a `position` lookup and `ORES[index]` is only reached with an index it returned. `serde` enforces `[i32; 11]`, so short rows fail to parse. Stage 102 errors out before any mutation, and everything is a local `Vec`, so there is no atomicity issue.
- **Logic matches the Python reference.** Clamp windows (1-5 hits, 0-300 radius, |v| 10-100, chained 50 then 2×previous up to 10000, 100-50000 good score, good ≤ perfect ≤ 50000, 500-50000 spill), precision check `data[2] > data[1]`, and the positive heat and spill checks all agree with `scripts/pieces/piece_013.py`.

**Minor doc mismatch (not reported as a defect):** the module doc at lines 20-23 says the enforcement rejects an "unreachable measure target". The code and the Python both only reject measure values outside 1-100 (line 310). A target such as 90 is accepted, and nothing checks reachability against the ore's `measure_percent`. This is a wording gap in a doc comment, not a behavioural bug the window can demonstrate.
