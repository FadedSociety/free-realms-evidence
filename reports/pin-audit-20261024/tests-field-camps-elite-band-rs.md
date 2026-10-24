<!-- fleet job=pin-audit id=tests-field-camps-elite-band-rs status=done turns=10 usd=0.0092 tokens(read,write,in,out)=[172702, 31428, 22, 7111] model=claude-haiku-5-5 -->
# tests/field_camps_elite_band.rs

Each listed number traces to a shipped data file. The reward values are in `field_kill_rewards.json`, the respawn and spawn-area values in `field_enemies.json`. The test already loads both files: `shipped_field()` and `shipped_rewards()` (lines 247-254), plus `group()` and `actor()` (lines 260-276). The `bank()` helper is in `common/field_reward_fixture.rs:279`.

**tests/field_camps_elite_band.rs:419 pin_respawn - pins `180` from `data/content/field_enemies.json` `spawn_groups[elite_trolls|elite_bixies|elite_hooligans].respawn_seconds` (lines 299, 326, 353).**
- **Fix:** read it through the group row: `assert_eq!(row["respawn_seconds"], row["respawn_seconds"])` is circular, so instead bound it: `let s = row["respawn_seconds"].as_u64().unwrap(); assert!((1..=3600).contains(&s));`, which matches the loader's own range check in `src/encounter/field_content.rs:46`. The `ELITE_RESPAWN_MS` constant (line 245, `180_000`) also pins the same data value; it should be derived from the group row, not written as a literal.

**tests/field_camps_elite_band.rs:434 every_elite_camp_... (camp provenance loop) - pins `180 s` prose from `field_enemies.json` `spawn_groups[*].source[reconstructed].evidence` (lines 318, 345, 372).**
- **Fix:** build the expected text from the row: `assert!(evidence.contains(&format!("{} s respawn", row["respawn_seconds"])));`.

**tests/field_camps_elite_band.rs:491 (elite provenance loop) - pins `180 s` prose from `field_enemies.json` spawn group evidence (lines 318, 345, 372).**
- **Fix:** same as 434: `format!("{} s", group_row["respawn_seconds"])` taken from the camp's group row.

**tests/field_camps_elite_band.rs:456 - pins `6.0` from `data/content/field_enemies.json` `enemies[ELITE-T1|T2|Q1|Q2|H1|H2].spawn_area.radius` (lines 1735 and the matching line in each ELITE row).**
- **Fix:** read it through the actor row: `let r = row["spawn_area"]["radius"].as_f64().unwrap(); assert!(r > 0.0 && r <= 12.0);`, or compare with `row["spawn_area"]["radius"]` against the value the loader stores in the engine.

**tests/field_camps_elite_band.rs:528 every_elite_home_is_a_verified_w102_centre - pins `6.0` from `field_enemies.json` `spawn_area.radius` (same ELITE rows).**
- **Fix:** same as 456, bound it or read the row's own radius.

**tests/field_camps_elite_band.rs:594 - pins `18` coins from `data/content/field_kill_rewards.json` `reward_bands[min_level 14, max_level 20].coins` (line 63).**
- **Fix:** read the band through `shipped_rewards()`: find the row where `min_level <= 20 <= max_level` and use its `coins`.

**tests/field_camps_elite_band.rs:595 - pins `35` job XP (job 43) from `field_kill_rewards.json` 14-20 band `job_xp` (line 64).**
- **Fix:** same band lookup via `shipped_rewards()`, reading `job_xp`.

**tests/field_camps_elite_band.rs:706 - pins `18` coins from the 14-20 band `coins` (line 63).**
- **Fix:** read through `shipped_rewards()` band lookup for the level-15 actor.

**tests/field_camps_elite_band.rs:707 - pins `35` job XP (job 43) from the 14-20 band `job_xp` (line 64).**
- **Fix:** read through `shipped_rewards()` band lookup.

**tests/field_camps_elite_band.rs:719 - pins `18` coins from the 14-20 band `coins` (line 63).**
- **Fix:** read through `shipped_rewards()` band lookup for the level-14 HIGH-T2 actor.

**tests/field_camps_elite_band.rs:720 - pins `35` job XP (job 43) from the 14-20 band `job_xp` (line 64).**
- **Fix:** read through `shipped_rewards()` band lookup.

**tests/field_camps_elite_band.rs:732 - pins `12` coins from the 9-13 band `coins` (`field_kill_rewards.json` line 51).**
- **Fix:** read through `shipped_rewards()` band lookup for level 10.

**tests/field_camps_elite_band.rs:733 - pins `25` job XP (job 43) from the 9-13 band `job_xp` (`field_kill_rewards.json` line 52).**
- **Fix:** read through `shipped_rewards()` band lookup for level 10.

**tests/field_camps_elite_band.rs:767 - pins `18` coins from the 14-20 band `coins` (line 63).**
- **Fix:** read through `shipped_rewards()` band lookup.

**tests/field_camps_elite_band.rs:768 - pins `35` job XP (job 43) from the 14-20 band `job_xp` (line 64).**
- **Fix:** read through `shipped_rewards()` band lookup.

**tests/field_camps_elite_band.rs:784 - pins `18` coins from the 14-20 band `coins` (line 63).**
- **Fix:** read through `shipped_rewards()` band lookup.

**tests/field_camps_elite_band.rs:785 - pins `35` job XP (job 35) from the 14-20 band `job_xp` (line 64).**
- **Fix:** read through `shipped_rewards()` band lookup.

**tests/field_camps_elite_band.rs:1067 - pins `2` coins from `field_kill_rewards.json` `definition_overrides[definition_id 3156].coins` (line 76).**
- **Fix:** read through `shipped_rewards()`: find the `definition_overrides` row with `definition_id` 3156 and use its `coins`.

**tests/field_camps_elite_band.rs:1068 - pins `5` job XP (job 43) from `field_kill_rewards.json` `definition_overrides[3156].job_xp` (line 77).**
- **Fix:** read through `shipped_rewards()` override row, `job_xp`.

Not findings: 402-403 (counts of actors and groups, which are protocol-level shape), 417-424 and 440-457 other than those listed (ids, layout, levels from the test's own table), 595-596 beyond the listed values, and 1048-1050 (zero and None checks). The `ELITE`, `CAMPS` and `HIGH_SHAMAN_14` tables are the test's own fixtures.
