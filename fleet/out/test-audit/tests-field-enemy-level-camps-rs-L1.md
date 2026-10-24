<!-- fleet job=test-audit id=tests-field-enemy-level-camps-rs-L1 status=done turns=9 usd=0.0101 tokens(read,write,in,out)=[146097, 31531, 20, 9446] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_enemy_level_camps.rs lines 1-512 of 512

Window reviewed: `prototype/osfr-tools/tests/field_enemy_level_camps.rs` lines 1-512. No high or medium findings. The four camp tests check the data against hard-coded tables and against the real loader (`engine.field_level`, `engine.behaviour`, the 35/2 `spawned` set), so they can fail on the regressions they name. I confirmed this against `src/encounter/field.rs:70-200`, `data/content/field_enemies.json:133-240` and `:1134-1180`, and `tests/common/field_enemy_fixture.rs:116-128`. Two low-severity items:

- **[low] tests/field_enemy_level_camps.rs:401 the_actor_and_group_counts_stay_inside_the_loader_bounds - pins exact counts (34 actors, 13 groups) in a test whose name promises only that counts stay inside the loader bounds.**
  - Why it cannot catch a regression: it cannot miss a regression. It is churn, not a hole. Any new in-bounds actor or group, such as a future camp, fails this test even though the loader still accepts it.
  - Fix: keep the `<= 64` and `<= 128 * 1024` bound checks at lines 395 and 409-410, and drop the exact `34` and `13` equalities (or move them into a content-count test that is named for them).

- **[low] tests/field_enemy_level_camps.rs:409-410 (and 395) the_actor_and_group_counts_stay_inside_the_loader_bounds - the "loader bounds" are test-local literals (64, 64, 128 KiB), not the loader's limits.**
  - The loader at `src/encounter/field.rs:72` and `:78-79` uses the same literals, so the test passes today. If the loader limit changed, this test would not notice, because it never calls the loader with an oversized file.
  - Fix: add a loader-side case (for example, a temp copy with 65 enemies or a file over 128 KiB, through `Fixture::copied`) asserting `load()` errors, and keep the literal checks as a canary.
