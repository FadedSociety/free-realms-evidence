<!-- fleet job=pin-audit id=tests-fisherman-entry-chain-rs status=done turns=8 usd=0.0076 tokens(read,write,in,out)=[121380, 26226, 18, 6242] model=claude-haiku-5-5 -->
# tests/fisherman_entry_chain.rs

Every listed line pins a tunable reward from shipped data. The quest rewards come from `quests/fisherman.json` (records 3070003 and 3070004: `rewards[0].coins` = 10, `rewards[0].job_xp["137"]` = 25). The catch XP comes from `fishing_spots.json` (`spots[].fisherman_xp` = 10). The file's own `turn_in(…, 10, 25)` calls hand the same literals to `support/npc_quest_chain.rs::finish_quest` as expected values, so those literals are also data copies. Sums such as `+20`, `+60` and `+35` are built from the same values. No `tests/common` helper loads quest reward rows; the file's own `read_json`/`content_dir` are available.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:569 learning_… (the test containing line 569) - pins `10` from `quests/fisherman.json` `records[3070003].rewards[0].coins`.**
  **Fix:** read it through the record: `let reward = &learn_record["rewards"][0];` then use `reward["coins"].as_u64()` for the expected delta, and pass that value into `turn_in` instead of the literal `10`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:570 (same test) - pins `25` from `quests/fisherman.json` `records[3070003].rewards[0].job_xp["137"]`.**
  **Fix:** read it through the record: `reward["job_xp"]["137"]`, and pass it into `turn_in` as well.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:608 the_chapter_is_gated_on_the_active_fisherman - pins `25` from `quests/fisherman.json` `records[3070003].rewards[0].job_xp["137"]`.**
  **Fix:** read it through the record: `reward["job_xp"]["137"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:674 learning_then_catching_and_turning_in_pays_once - pins `10` from `quests/fisherman.json` `records[3070003].rewards[0].coins`.**
  **Fix:** read it through the record: `reward["coins"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:675 (same test) - pins `25` from `quests/fisherman.json` `records[3070003].rewards[0].job_xp["137"]`.**
  **Fix:** read it through the record: `reward["job_xp"]["137"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:694 (same test) - pins `10` from `quests/fisherman.json` `records[3070003].rewards[0].coins`.**
  **Fix:** read it through the record: `reward["coins"]`. The "catch pays no coins" claim is a zero fishing-spot coin row (`fishing_spots.json` `coins: 0`), so only the quest coin delta belongs here.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:704 (same test) - pins `10` from `quests/fisherman.json` `records[3070003].rewards[0].coins`.**
  **Fix:** read it through the record: `reward["coins"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:708 (same test) - pins `20` (= 10 + 10) from `quests/fisherman.json` `coins` in records 3070003 and 3070004.**
  **Fix:** read both records' `rewards[0].coins` and assert `coins + learn_coins + testing_coins`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:709 (same test) - pins `60` (= 25 + 25 + 10) from `quests/fisherman.json` `job_xp["137"]` (both records) and `fishing_spots.json` `fisherman_xp`.**
  **Fix:** read the two quest `rewards[0].job_xp["137"]` values and the spot's `fisherman_xp` (for the catch), and sum them.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:723 (same test) - pins `20` from `quests/fisherman.json` `coins` (both records).**
  **Fix:** same as line 708, using the stored values from the test's earlier reads.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:724 (same test) - pins `60` from `quests/fisherman.json` `job_xp["137"]` plus `fishing_spots.json` `fisherman_xp`.**
  **Fix:** same as line 709.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:901 a_quit_escape_or_disconnect_does_not_count_the_catch - pins `10` from `fishing_spots.json` `spots[].fisherman_xp`.**
  **Fix:** read it through the Reed spot row: `spot["fisherman_xp"]`, where `spot["npc"] == REED`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:1025 the_two_records_load_with_the_real_game_id_and_giver (`assert_reward_shape`) - pins `10` from `quests/fisherman.json` `rewards[0].coins`.**
  **Fix:** bound it instead of pinning the data value, e.g. `rewards[0]["coins"].as_u64().is_some()` (a non-negative integer).

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:1027 (same helper) - pins `{"137": 25}` from `quests/fisherman.json` `rewards[0].job_xp`.**
  **Fix:** bound it: assert `job_xp` is an object with key `"137"` whose value is a non-negative integer, instead of comparing to `25`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:1072 two_independent_sessions_fish_the_same_spot - pins `10` from `quests/fisherman.json` `rewards[0].coins`.**
  **Fix:** read it through the record: `reward["coins"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:1073 (same test) - pins `10` from `quests/fisherman.json` `rewards[0].coins`.**
  **Fix:** read it through the record: `reward["coins"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:1074 (same test) - pins `25` from `quests/fisherman.json` `rewards[0].job_xp["137"]`.**
  **Fix:** read it through the record: `reward["job_xp"]["137"]`.

- **prototype/osfr-tools/tests/fisherman_entry_chain.rs:1075 (same test) - pins `35` (= 25 + 10) from `quests/fisherman.json` `job_xp["137"]` plus `fishing_spots.json` `fisherman_xp`.**
  **Fix:** read the quest XP and the spot's `fisherman_xp` and sum them.
