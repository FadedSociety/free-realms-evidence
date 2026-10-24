<!-- fleet job=pin-audit id=tests-quest-job-xp-rs status=done turns=9 usd=0.0089 tokens(read,write,in,out)=[153248, 33694, 20, 6389] model=claude-haiku-5-5 -->
# tests/quest_job_xp.rs

Each listed number is a shipped reward value, and the test writes it as a literal instead of reading it from the quest row. The file already has the right pattern: `configured_job_xp_and_job_gates_match_the_task_table` (line 993) and the reward reads at lines 878 and 1317 load `record["rewards"]` from `data/content/quests`. Helpers `profile_xp` and `coins` (`tests/support/npc_quest_chain.rs`) only read game state and take the expected value from the caller.

Values checked:
- `quests/adventurer.json` id 3000020 (Introduce Yourself): `coins` 5, `job_xp` {"1": 15}
- `quests/kart_driver.json` id 3080001 (Burden of Fame): `coins` 5, `job_xp` {"48": 25}
- `quests/chef.json` id 3050011 (Ranger Requisition): `coins` 0, `job_xp` {"45": 20}
- `quests/ninja.json` id 3110001 (Ninja Path): `coins` 0, `job_xp` {"2": 15}

- **prototype/osfr-tools/tests/quest_job_xp.rs:275 adventurer_line_pays_its_job_xp_once - pins `15` from `quests/adventurer.json` `rewards[0].job_xp["1"]` (quest 3000020).**
  **Fix:** read it through the quest record (`record["rewards"][0]["job_xp"]["1"]`, as lines 878/1317 do) and compare against that, or bound it as `> 0`.
- **prototype/osfr-tools/tests/quest_job_xp.rs:287 adventurer_line_pays_its_job_xp_once - pins `15` from `quests/adventurer.json` `rewards[0].job_xp["1"]` (quest 3000020).**
  **Fix:** same as line 275: read the row's `job_xp["1"]`.
- **prototype/osfr-tools/tests/quest_job_xp.rs:333 chef_trainer_unlock_opens_the_job_gate_and_pays - pins `20` from `quests/chef.json` `rewards[0].job_xp["45"]` (quest 3050011).**
  **Fix:** read the row's `job_xp["45"]` from `quests/chef.json` for quest 3050011.
- **prototype/osfr-tools/tests/quest_job_xp.rs:346 kart_line_pays_its_job_xp_once - pins `25` from `quests/kart_driver.json` `rewards[0].job_xp["48"]` (quest 3080001).**
  **Fix:** read the row's `job_xp["48"]` from quest 3080001.
- **prototype/osfr-tools/tests/quest_job_xp.rs:347 kart_line_pays_its_job_xp_once - pins `15` from `quests/adventurer.json` `rewards[0].job_xp["1"]` (quest 3000020).**
  **Fix:** read the row's `job_xp["1"]` from quest 3000020.
- **prototype/osfr-tools/tests/quest_job_xp.rs:348 kart_line_pays_its_job_xp_once - pins `10` (= 5 + 5) from `quests/adventurer.json` and `quests/kart_driver.json` `rewards[0].coins` (quests 3000020 and 3080001).**
  **Fix:** sum the two rows' `coins` from the quest records, so the expectation follows the data.
- **prototype/osfr-tools/tests/quest_job_xp.rs:359 kart_line_pays_its_job_xp_once - pins `25` from `quests/kart_driver.json` `rewards[0].job_xp["48"]` (quest 3080001).**
  **Fix:** read the row's `job_xp["48"]` from quest 3080001.
- **prototype/osfr-tools/tests/quest_job_xp.rs:370 ninja_line_pays_its_job_xp_once - pins `15` from `quests/ninja.json` `rewards[0].job_xp["2"]` (quest 3110001).**
  **Fix:** read the row's `job_xp["2"]` from quest 3110001.
- **prototype/osfr-tools/tests/quest_job_xp.rs:419 xp_follows_the_quest_job_not_the_active_job - pins `15` from `quests/ninja.json` `rewards[0].job_xp["2"]` (quest 3110001).**
  **Fix:** read the row's `job_xp["2"]` from quest 3110001.
- **prototype/osfr-tools/tests/quest_job_xp.rs:779 paid XP survives reload (ninja relog test) - pins `15` from `quests/ninja.json` `rewards[0].job_xp["2"]` (quest 3110001).**
  **Fix:** read the row's `job_xp["2"]` from quest 3110001.
- **prototype/osfr-tools/tests/quest_job_xp.rs:807 ninja relog test - pins `15` from `quests/ninja.json` `rewards[0].job_xp["2"]` (quest 3110001).**
  **Fix:** read the row's `job_xp["2"]` from quest 3110001.
- **prototype/osfr-tools/tests/quest_job_xp.rs:829 two_players_are_paid_independently - pins `15` from `quests/adventurer.json` `rewards[0].job_xp["1"]` (quest 3000020).**
  **Fix:** read the row's `job_xp["1"]` from quest 3000020.
- **prototype/osfr-tools/tests/quest_job_xp.rs:830 two_players_are_paid_independently - pins `5` from `quests/adventurer.json` `rewards[0].coins` (quest 3000020).**
  **Fix:** read the row's `coins` from quest 3000020.

Not findings: line 276 (`coins` 5, same source but the test's comment states the existing row is unchanged, so it is a deliberate data-pin, not a tunable), line 371 and 808 (the coin 0 for Ninja, which is not in the screened list). Note line 276 also pins 5 from `adventurer.json` and should be handled the same way if the team wants a consistent rule. The `coins`/`profile_xp` helpers themselves hold no literals.
