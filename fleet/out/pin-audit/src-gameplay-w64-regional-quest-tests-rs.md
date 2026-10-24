<!-- fleet job=pin-audit id=src-gameplay-w64-regional-quest-tests-rs status=done turns=11 usd=0.0062 tokens(read,write,in,out)=[138732, 23339, 24, 3752] model=claude-haiku-5-5 -->
# src/gameplay/w64_regional_quest_tests.rs

Two of the five screened assertions pin tunable data values (three lines, two data files). The screened line numbers are one higher than the file's real lines, so I cite the real ones.

- **prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs:1592 troll_summoner_battle_summons_waves_and_is_won_on_the_summoner - pins `25` from `data/content/field_battles.json` `reward_coins` (battle 96, row starts at line 5; its `reward_coins` is at line 154).**
  - **Fix:** read it through the battle row: load `field_battles.json`, find battle `id` 96, and use its `reward_coins` as the expected value (the existing loaders are `load_field_battles` and `tests/common/field_battle_fixture.rs`). Or bound it, e.g. `reward.coins > 0`.

- **prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs:2750 behaviour_presets_drive_enemy_movement - pins `4000` from `data/content/behaviours.json` `presets.skittish.run_ms` and `12.0` from `presets.skittish.leash` (summoner, battle 96 id 100_000_096_001).**
  - **Fix:** read the summoner's values from the `skittish` preset in `behaviours.json`, e.g. `let preset = bundled behaviours.json["presets"]["skittish"]`, and compare `summoner.run_ms` and `summoner.leash` to `preset["run_ms"]` and `preset["leash"]`. The test already loads that file at line 2080 in the same file, so the helper can be reused.

- **prototype/osfr-tools/src/gameplay/w64_regional_quest_tests.rs:2847 behaviour_presets_drive_enemy_movement - pins `4000` from `data/content/behaviours.json` `presets.skittish.run_ms`.**
  - **Fix:** same as above: compare `behaviour(100_000_096_001).run_ms` to `presets.skittish.run_ms` read from `behaviours.json`.

Not findings:
- Line 1593 (`job_xp` 50): comes from the code constant `BATTLE_JOB_XP = 50` in `src/encounter.rs:76`, not a data file.
- Line 2839 (`move_speed` 6.0, screened as 2840): the test's own fixture writes `"move_speed": 6.0` at line 2825 before this assertion.
