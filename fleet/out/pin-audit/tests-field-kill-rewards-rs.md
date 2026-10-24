<!-- fleet job=pin-audit id=tests-field-kill-rewards-rs status=done turns=12 usd=0.0096 tokens(read,write,in,out)=[238620, 30994, 26, 6683] model=claude-haiku-5-5 -->
# tests/field_kill_rewards.rs

Findings (all values come from the shipped `data/content/field_kill_rewards.json`, which these tests load through `RewardFixture::new`, which copies the bundled content; none of these tests writes its own reward table before the assertion):

- **prototype/osfr-tools/tests/field_kill_rewards.rs:155 a_solo_field_kill_pays_once_and_only_the_active_job - pins `2` from `data/content/field_kill_rewards.json` `level_rewards[min_level 1-2].coins`.**
  **Fix:** read it through the row: load `data/content/field_kill_rewards.json` (the same way lines 352-358 already do), find the `level_rewards` entry with `min_level == 1`, and compare against its `coins`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:156 a_solo_field_kill_pays_once_and_only_the_active_job - pins `5` from `data/content/field_kill_rewards.json` `level_rewards[min_level 1-2].job_xp`.**
  **Fix:** read it through the same `min_level == 1` row's `job_xp`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:214 the_mid_level_farnum_camp_pays_the_kind_override_rate - pins `2` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156].coins`.**
  **Fix:** read it through the override row for `definition_id` 3156 in the same file's `definition_overrides`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:261 a_shared_kill_pays_each_credited_player_once - pins `2` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156].coins`** (WOLF is definition 3156, so the override wins over the level-3 band).
  **Fix:** read it through the definition 3156 override row.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:262 a_shared_kill_pays_each_credited_player_once - pins `5` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156].job_xp`.**
  **Fix:** read it through the definition 3156 override row's `job_xp`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:283 a_shared_kill_pays_each_credited_player_once - pins `2` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156].coins`.**
  **Fix:** read it through the definition 3156 override row.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:284 a_shared_kill_pays_each_credited_player_once - pins `5` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156].job_xp`.**
  **Fix:** read it through the definition 3156 override row's `job_xp`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:290 a_shared_kill_pays_each_credited_player_once - pins `2` from `data/content/field_kill_rewards.json` `definition_overrides[definition_id 3156].coins`.**
  **Fix:** read it through the definition 3156 override row.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:583 a_field_kill_credit_survives_an_unrelated_content_reload - pins `2` from `data/content/field_kill_rewards.json` `level_rewards[min_level 1-2].coins`.** The carried pair is computed at kill time from the shipped table (the test's `levels(9, 9)` rewrite happens after the kill and must not change it).
  **Fix:** read it through the `min_level == 1` row's `coins`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:584 a_field_kill_credit_survives_an_unrelated_content_reload - pins `5` from `data/content/field_kill_rewards.json` `level_rewards[min_level 1-2].job_xp`.**
  **Fix:** read it through the `min_level == 1` row's `job_xp`.

- **prototype/osfr-tools/tests/field_kill_rewards.rs:637 a_credit_survives_a_reconnect_and_expires_once - pins `2` from `data/content/field_kill_rewards.json` `level_rewards[min_level 1-2].coins`.**
  **Fix:** read it through the `min_level == 1` row's `coins`.

Not in the screened list but the same pattern, same fix: **field_kill_rewards.rs:640 a_credit_survives_a_reconnect_and_expires_once - pins `5` from `level_rewards[min_level 1-2].job_xp`** (read through that row).

Checked and not findings:
- 417, 434, 435, 444, 478, 564: the values come from a table the test writes itself (`levels(1000, 1)`, `levels(1, 1000)`, `levels(9, 9)`) or from the test's own job XP fixture (1000 `b_xp`), not from the shipped file.
- 262/284 etc. in the solo-kill test: already listed above.
- 784 `battle 12310 pays its 25 coins`: no structured coin field exists for battle 12310. `field_battles.json` only mentions "25 coins" in prose evidence, and no `coins` key exists in that file, so there is no data value the test can read. Left as not a finding; if battle rewards get a data field later, this line should read it.
