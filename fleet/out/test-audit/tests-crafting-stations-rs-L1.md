<!-- fleet job=test-audit id=tests-crafting-stations-rs-L1 status=done turns=7 usd=0.0045 tokens(read,write,in,out)=[48231, 16739, 16, 3813] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/crafting_stations.rs lines 1-115 of 115

Window reviewed: `prototype/osfr-tools/tests/crafting_stations.rs` 1-115, checked against `src/recipe_book.rs:81-149` (load/world_stations/merge/push_unique) and `data/content/crafting_stations.json`. Tests 1, 2 and 4 are sound: the expected jobs, positions and radius come from the shipped fixture and are not derived from the code under test, and removing the dedupe, the NaN skip, or the zone pass-through would make them fail. The findings are in the malformed-file test and the test-1 coverage.

- **[medium] tests/crafting_stations.rs:78 malformed_station_files_are_refused - the name promises refusal of malformed files, but only one malformation (duplicate `model_id`) is exercised.**
  Why it cannot catch a regression: `load_world_station_rules` (recipe_book.rs:91-103) has separate checks for `schema_version != 1`, an empty `provenance`, `model_id == 0`, a non-finite or out-of-range `interact_range` (0.1..=100.0), an empty `source`, and the 2-part size cap at line 86. Deleting any of those checks still passes this test, because only the duplicate branch is hit.
  Fix: table-drive the malformed cases (bad schema_version, blank provenance, model_id 0, NaN or 500.0 interact_range, blank source, an unknown field, an oversized file), and assert `is_err()` for each. Or rename the test to say it only covers duplicate model ids.

- **[low] tests/crafting_stations.rs:84-100 malformed_station_files_are_refused - the temp directory is removed only on the success path, and the error is never checked for kind or message.**
  Why it cannot catch a regression: if any assertion panics, `remove_dir_all` at line 100 never runs and the directory leaks into the temp dir. `is_err()` at line 99 also passes for any error, including an unrelated I/O failure, not just the duplicate-id rejection.
  Fix: use a drop guard for the directory, and assert `err.kind() == io::ErrorKind::InvalidData` (or match the "invalid world crafting station" message) at line 99.

- **[low] tests/crafting_stations.rs:40-42 shipped_models_register_cooking_smelting_and_forging_stations - the zone and position checks cover only stations 0, 1 and 3, not station 2 (the anvil, model 273).**
  Why it cannot catch a regression: a change that mis-assigns the zone or position for the blacksmith anvil in zone 0 would pass, because `stations[2]` is never checked against `in_world[2]`.
  Fix: add `assert_eq!(stations[2].position, in_world[2].2)` and `assert_eq!(stations[2].zone_id, 0)`.
