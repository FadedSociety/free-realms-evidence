<!-- fleet job=pin-audit id=tests-forging-gameplay-rs status=nothing_found turns=13 usd=0.0061 tokens(read,write,in,out)=[143331, 20248, 28, 4360] model=claude-haiku-5-5 -->
# tests/forging_gameplay.rs

No finding for `prototype/osfr-tools/tests/forging_gameplay.rs:347` (test in that file around line 300-360, `private_acceptance_grant_and_native_forging_win_atomic_once_restore_cancel`).

- The `181001` is `movie::start` at 1000 ms plus 180 000 ms of forging play plus 1 ms. The 180 s comes from the forging board's `duration_seconds`, which `src/forging.rs` loads from the content passed in (`remaining_ms = board.duration_seconds * 1000`, line 291).
- That content is `forging-campaign.json`, read from `lab/references/rust-opening-forging` (`paths()`, lines 24-34, overridable with `OSFR_OPENING_REFERENCE`). It is not a shipped file under `data/content/`. The only `duration_seconds` rows in `data/content/` are in `harvesting.json` and `mining.json`, and neither is forging.
- The test is also `#[ignore]`d ("requires private versioned forging campaign").
- `MAX_WALL_MS` (1 800 000, `src/forging.rs:24`) is a code constant and is not what this line hits.

Not a finding under the "shipped data file" rule. If Bryce wants it tunable anyway, the fix would be to read `board.duration_seconds` from the loaded `forging-campaign.json` and use `start + duration*1000 + 1` in place of the literal.
