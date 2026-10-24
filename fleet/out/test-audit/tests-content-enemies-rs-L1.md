<!-- fleet job=test-audit id=tests-content-enemies-rs-L1 status=done turns=5 usd=0.0056 tokens(read,write,in,out)=[36719, 19484, 12, 5514] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/content_enemies.rs lines 1-338 of 338

Window: `prototype/osfr-tools/tests/content_enemies.rs` lines 1-338. Read in full, plus `data/content/dungeons/*.json` shape checks and `row_names` (lines 20-33). Most assertions in this window check recorded data against independent sources (locale table, catalog.tsv, Models.txt via `support/models.rs`, and a recount of dungeon rows), so I found no "cannot fail" tests. The findings below are the weaker spots.

- **[medium] tests/content_enemies.rs:209-211 every_dungeon_enemy_name_is_crosswalked_or_listed_unresolved - `let Some(source_rows) = detail[field]["value"].as_array() else { continue; }` silently skips a whole enemies/bosses field whose `value` is not an array.**
  - Why it cannot catch a regression: if a dungeon's `enemies.value` (or `bosses.value`) becomes `null`, none of its names are counted or cross-checked against `enemy_refs`. If the same change regenerates `enemies_unresolved.json` (`dungeon_rows` and `coverage`) consistently, every assertion at lines 253-277 still passes, and that dungeon is no longer checked at all.
  - Fix: when `detail[field]` exists but `value` is null, assert that no `enemy_refs` entry references that `source_field` for that dungeon, and assert that `dungeon_name_occurrences` agrees with an independent count of the `enemy_refs` rows. Alternatively, require that `value` is an array for every dungeon, using `.expect()` in place of `continue`.

- **[low] tests/content_enemies.rs:213 every_dungeon_enemy_name_is_crosswalked_or_listed_unresolved - `row_names(row)` (lines 20-33) returns an empty Vec for a row with neither `names` nor `name`, so that row is silently excluded from `all`.**
  - Why it cannot catch a regression: a row whose name key is renamed or nested differently produces no `all` increment and no `expected_unresolved` entry. The coverage check at lines 254-259 uses a number from the same generated data, so it passes if the generator drops the row the same way.
  - Fix: assert in the loop that `row_names(row)` is non-empty for every row in `enemies`/`bosses`, or count rows and names separately and compare the row count to a value that is not derived from the same generated file.

- **[low] tests/content_enemies.rs:316 every_dungeon_enemy_name_is_crosswalked_or_listed_unresolved - `assert_eq!(world_rows.len(), 82)` pins an exact row count that is unrelated to the crosswalk invariant.**
  - Why it cannot catch a regression: it is not a regression check for statuses or ids. Any legitimate addition of a world row (for example a new zone) fails the test even though every row is still valid, which causes churn.
  - Fix: remove the hard-coded 82. Keep the per-row checks at lines 296-314 and the sum check against `coverage.world_rows_resolved` and `world_rows_partial`, and optionally assert `world_rows.len() == resolved + partial + unresolved_count` using the same JSON.

Not reported, on purpose: `assert_eq!(missing.len(), 2)` at line 142 is a fixed count, but it does sit beside the set-equality check at line 141 and so is a meaningful, if brittle, assertion. The `capture["sha256"].is_some()` presence check at line 125 is weak, but the test name does not claim hash verification.
