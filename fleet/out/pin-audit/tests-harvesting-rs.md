<!-- fleet job=pin-audit id=tests-harvesting-rs status=nothing_found turns=5 usd=0.0050 tokens(read,write,in,out)=[57184, 23122, 12, 3005] model=claude-haiku-5-5 -->
# tests/harvesting.rs

No findings in `prototype/osfr-tools/tests/harvesting.rs`. None of the 23 screened lines pins a number that comes from a shipped data file field, so none needs changing.

- **Lines 21-51 (SpawnRow / LevelRow / ProgressionRow / TimerRow golden strings):** the numbers come from the `SPAWN_GOLDEN` and `golden` string fixtures the test builds itself, which are the original caret-column layouts. They are parse/roundtrip fixtures, not tunables.
- **Lines 70-71 (`timer.chain_m` / `chain_f`):** these come from the `"3^2^30^2^0^1"` fixture row.
- **Lines 166-176 (`chain_score`, `chain_time_bonus_seconds`, `collectable_score`):** the numbers come from `src/harvesting.rs` code constants (`CHAIN_SCORE`, `CHAIN_BONUS_TILE_SCORE`, `MIN_CHAIN_TIME_BONUS_SECONDS`, `COLLECTABLE_SCORE`), not from `data/content/harvesting.json`. That file has no score or chain fields.
- **Lines 259-264 (scoring constants):** these are `src/harvesting.rs` lines 70-75, the GameData.as values, so they are code constants and not data-file values.
- **Line 558 (`c.spec.wildcard_percent`):** the test reads `content_json(109)`, which is built from `RECONSTRUCTED_WILDCARD_PERCENT = 5` in `src/harvesting.rs:786`. The `wildcard_percent: 5` at `data/content/harvesting.json:219` belongs to game 111 and is not read by this test. Retuning that data row would not break this assertion.
