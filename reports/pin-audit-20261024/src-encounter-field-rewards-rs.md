<!-- fleet job=pin-audit id=src-encounter-field-rewards-rs status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[23667, 16050, 10, 2058] model=claude-haiku-5-5 -->
# src/encounter/field_rewards.rs

Lines 379-381 are not findings: `bands_pay_their_levels_and_the_override_wins` builds its own table with `band(1, 2, 2, 5)`, `band(3, 4, 4, 10)` and a 3156 override of 1/3, so those numbers come from the test's fixture, not the shipped file.

- **prototype/osfr-tools/src/encounter/field_rewards.rs:532 the_shipped_table_covers_the_high_band_and_pays_nothing_past_20 - pins `(12, 25)` from `data/content/field_kill_rewards.json` `level_rewards[min_level 9, max_level 13]` `coins` / `job_xp`.**
  **Fix:** read it through the row. Load the band whose min_level/max_level covers level 10 from `field_kill_rewards.json` (or use the shared loader in `tests/common/field_reward_fixture.rs`), then assert against its `coins` and `job_xp`. Or bound it: coins > 0 and job_xp > coins.

- **prototype/osfr-tools/src/encounter/field_rewards.rs:533 the_shipped_table_covers_the_high_band_and_pays_nothing_past_20 - pins `(12, 25)` from `data/content/field_kill_rewards.json` `level_rewards[min_level 9, max_level 13]` `coins` / `job_xp`.**
  **Fix:** same as line 532: take the expected pair from the level-9-to-13 row for level 13 instead of the literal.

- **prototype/osfr-tools/src/encounter/field_rewards.rs:534 the_shipped_table_covers_the_high_band_and_pays_nothing_past_20 - pins `(18, 35)` from `data/content/field_kill_rewards.json` `level_rewards[min_level 14, max_level 20]` `coins` / `job_xp`.**
  **Fix:** read the row covering level 14 (min_level 14, max_level 20) and use its `coins` / `job_xp`.

- **prototype/osfr-tools/src/encounter/field_rewards.rs:535 the_shipped_table_covers_the_high_band_and_pays_nothing_past_20 - pins `(18, 35)` from `data/content/field_kill_rewards.json` `level_rewards[min_level 14, max_level 20]` `coins` / `job_xp`.**
  **Fix:** read the row covering level 20 (the same 14-to-20 band) and use its `coins` / `job_xp`.

- **prototype/osfr-tools/src/encounter/field_rewards.rs:538 the_shipped_table_covers_the_high_band_and_pays_nothing_past_20 - pins `(2, 5)` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156]` `coins` / `job_xp`.**
  **Fix:** read the 3156 row from `definition_overrides` in the shipped file and use its `coins` / `job_xp`.

Lines 379-381 were not included, as the fixture builds those values.
