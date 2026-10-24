<!-- fleet job=pin-audit id=tests-field-camps-high-band-rs status=done turns=6 usd=0.0074 tokens(read,write,in,out)=[65293, 22579, 14, 7927] model=claude-haiku-5-5 -->
# tests/field_camps_high_band.rs

The screened lines pin values that ship in data. The reward literals are the band rows in `data/content/field_kill_rewards.json`, and the respawn literals are the spawn-group `respawn_seconds` in `data/content/field_enemies.json`. None comes from the test's own fixture. The existing helpers `shipped_rewards()` and `shipped_field()` / `group()` in the test file already load these files.

**prototype/osfr-tools/tests/field_camps_high_band.rs:430 the_high_camps_use_verified_w102_centres_and_unique_guids - pins `120` / `150` from `data/content/field_enemies.json` `spawn_groups[].respawn_seconds` (the high_farnum_wolves and high_wilds_shamans rows).**
- **Fix:** Read the value from the group row and bound it, e.g. `assert!(group["respawn_seconds"].as_u64().is_some_and(|s| (30..=600).contains(&s)))`. Do not assert the literal 120 or 150.

**prototype/osfr-tools/tests/field_camps_high_band.rs:602 a_level_fourteen_kill_pays_the_new_band_once - pins `18` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].coins`.**
- **Fix:** Read the 14-20 row through `shipped_rewards()` (the row with `min_level` 14) and compare against its `coins`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:603 a_level_fourteen_kill_pays_the_new_band_once - pins `35` job XP from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].job_xp`.**
- **Fix:** Read `job_xp` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:638 the_active_job_not_the_actor_kind_receives_the_xp - pins `18` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].coins`.**
- **Fix:** Read `coins` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:639 the_active_job_not_the_actor_kind_receives_the_xp - pins `35` job XP from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].job_xp`.**
- **Fix:** Read `job_xp` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:681 the_level_thirteen_and_ten_controls_keep_the_nine_thirteen_band - pins `12` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=9].coins`.**
- **Fix:** Read `coins` from the 9-13 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:682 the_level_thirteen_and_ten_controls_keep_the_nine_thirteen_band - pins `25` job XP from `data/content/field_kill_rewards.json` `level_rewards[min_level=9].job_xp`.**
- **Fix:** Read `job_xp` from the 9-13 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:694 the_level_thirteen_and_ten_controls_keep_the_nine_thirteen_band - pins `12` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=9].coins`.**
- **Fix:** Read `coins` from the 9-13 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:695 the_level_thirteen_and_ten_controls_keep_the_nine_thirteen_band - pins `25` job XP from `data/content/field_kill_rewards.json` `level_rewards[min_level=9].job_xp`.**
- **Fix:** Read `job_xp` from the 9-13 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:716 a_level_twenty_actor_pays_the_new_band - pins `18` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].coins`.**
- **Fix:** Read `coins` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:770 an_unclaimed_high_camp_credit_expires_or_is_lost_on_leaving_and_pays_nothing - pins `18` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].coins`.**
- **Fix:** Read `coins` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:833 two_players_share_a_high_camp_kill_and_each_is_paid_once - pins `18` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].coins`.**
- **Fix:** Read `coins` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:834 two_players_share_a_high_camp_kill_and_each_is_paid_once - pins `35` job XP from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].job_xp`.**
- **Fix:** Read `job_xp` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:848 two_players_share_a_high_camp_kill_and_each_is_paid_once - pins `18` coins from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].coins`.**
- **Fix:** Read `coins` from the 14-20 row through `shipped_rewards()`.

**prototype/osfr-tools/tests/field_camps_high_band.rs:849 two_players_share_a_high_camp_kill_and_each_is_paid_once - pins `35` job XP from `data/content/field_kill_rewards.json` `level_rewards[min_level=14].job_xp`.**
- **Fix:** Read `job_xp` from the 14-20 row through `shipped_rewards()`.

Not screened, but the same pattern: `HIGH_BAND = (14, 20, 18, 35)` at line 116 hard-codes the data row, and the check at line 544 compares the data against it. Retuning the row would fail that check, so it should read the row instead.
