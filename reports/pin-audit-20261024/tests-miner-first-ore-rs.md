<!-- fleet job=pin-audit id=tests-miner-first-ore-rs status=done turns=7 usd=0.0095 tokens(read,write,in,out)=[99073, 27383, 16, 10266] model=claude-haiku-5-5 -->
# tests/miner_first_ore.rs

Every listed line is a finding. The reward numbers come from the shipped quest records in `prototype/osfr-tools/data/content/quests/miner.json`, not from fixtures or code. Record 3100002 (`rewards[0]`) pays 5 coins and `job_xp {"14": 15}`. Record 3100003 pays the same, 5 and 15. Record 3100004 (Rush Order) pays 5 and `{"14": 20}`. The test file's own asserts at 977/979, 1614/1616 and 2097/2099 confirm these rows. `MINING_XP_PER_WIN` is a code constant (25, `mining_lifecycle.rs:22`), so it is not a finding; only the quest-reward part of each sum is. Both the `end_screen_reward` helper (`support/npc_quest_chain.rs:538`, a packet reader) and the `coins`/`profile_xp` helpers are fine. The bare literals still pin the data.

Fix for all of these: read the expected reward from the record, for example `let reward = row(&read_json(&content_dir().join("quests/miner.json"))["records"], ID)["rewards"][0];` then use `reward["coins"].as_u64()` and `reward["job_xp"]["14"]`, or add a small `reward_of(quest_id) -> (u32, u32)` helper in the test file next to `row`/`has_source`. Sums (1586–1589, 2247–2248) should be built from the same reads (for example `2 * coins_of(3100002)`, or `coins_of(3100002) + coins_of(3100003) + coins_of(3100004)`). Where a finish_quest call passes the literal `5, 15` or `5, 20`, pass the values read from the record.

- **prototype/osfr-tools/tests/miner_first_ore.rs:341 the_* (49/13 reward bundle) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row, as above.
- **prototype/osfr-tools/tests/miner_first_ore.rs:344 (test containing line 344) - pins `15` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:392 (test containing line 392) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:446 (test containing line 446) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:467 (test containing line 467) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:468 (test containing line 468) - pins `15` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:550 (test containing line 550) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:563 (test containing line 563) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:756 (test containing line 756) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:795 (test containing line 795) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:798 (test containing line 798) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:799 (test containing line 799) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:977 (test containing line 977) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row (the test already has the `quest` value).
- **prototype/osfr-tools/tests/miner_first_ore.rs:979 (test containing line 979) - pins `{"14": 15}` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp`.**
  Fix: read it through the record row, comparing against the row's own `job_xp`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1101 (test containing line 1101) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1102 (test containing line 1102) - pins `15` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp.14` (the `MINING_XP_PER_WIN` part is code and is fine).**
  Fix: read the 15 through the record row; keep `MINING_XP_PER_WIN`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1133 (test containing line 1133) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1134 (test containing line 1134) - pins `15` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp.14`.**
  Fix: read it through the record row; keep `MINING_XP_PER_WIN`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1242 (test containing line 1242) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1249 (test containing line 1249) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1276 (test containing line 1276) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1277 (test containing line 1277) - pins `15` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1307 (test containing line 1307) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1467 (test containing line 1467) - pins `5, 15` from `data/content/quests/miner.json` `records[3100002].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1490 (test containing line 1490) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1491 (test containing line 1491) - pins `15` from `data/content/quests/miner.json` `records[3100002].rewards[0].job_xp.14`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1554 (test containing line 1554) - pins `5, 15` from `data/content/quests/miner.json` `records[3100003].rewards[0]` `coins` / `job_xp.14` (3100003 pays 5 and 15).**
  Fix: read it through the record row for 3100003.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1581 (test containing line 1581) - pins `5, 15` from `data/content/quests/miner.json` `records[3100003].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row for 3100003.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1586 (test containing line 1586) - pins `10` = two 5-coin rungs from `data/content/quests/miner.json` `records[3100002|3100003].rewards[0].coins`.**
  Fix: sum the two coin values read from the records.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1587 (test containing line 1587) - pins `10` = two 5-coin rungs from `data/content/quests/miner.json` `rewards[0].coins` of 3100002 and 3100003.**
  Fix: sum the two coin values read from the records.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1588 (test containing line 1588) - pins `30` = 15 + 15 from `data/content/quests/miner.json` `rewards[0].job_xp.14` of 3100002 and 3100003 (25 from `MINING_XP_PER_WIN` is code).**
  Fix: sum the two XP values read from the records; keep `MINING_XP_PER_WIN`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1589 (test containing line 1589) - pins `30` = 15 + 15 from `data/content/quests/miner.json` `rewards[0].job_xp.14` of 3100002 and 3100003.**
  Fix: sum the two XP values read from the records; keep `MINING_XP_PER_WIN`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1614 (test containing line 1614) - pins `5` from `data/content/quests/miner.json` `records[3100003].rewards[0].coins`.**
  Fix: read it through the record row (the test already has `quest`).
- **prototype/osfr-tools/tests/miner_first_ore.rs:1616 (test containing line 1616) - pins `{"14": 15}` from `data/content/quests/miner.json` `records[3100003].rewards[0].job_xp`.**
  Fix: compare against the record's own `job_xp`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1756 (test containing line 1756) - pins `5` from `data/content/quests/miner.json` `records[3100002].rewards[0].coins`.**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1892 (test containing line 1892) - pins `5, 20` from `data/content/quests/miner.json` `records[3100004].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row for 3100004.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1896 (test containing line 1896) - pins `20` from `data/content/quests/miner.json` `records[3100004].rewards[0].job_xp.14`.**
  Fix: read it through the record row for 3100004.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1907 (test containing line 1907) - pins `5` from `data/content/quests/miner.json` `records[3100002|3100003|3100004].rewards[0].coins` (the test's own quest).**
  Fix: read it through the record row.
- **prototype/osfr-tools/tests/miner_first_ore.rs:1908 (test containing line 1908) - pins `20` from `data/content/quests/miner.json` `records[3100004].rewards[0].job_xp.14`.**
  Fix: read it through the record row; keep `xp_after_mining` and `MINING_XP_PER_WIN` as they are.
- **prototype/osfr-tools/tests/miner_first_ore.rs:2097 (test containing line 2097) - pins `5` from `data/content/quests/miner.json` `records[3100004].rewards[0].coins`.**
  Fix: compare against the record's own `coins`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:2099 (test containing line 2099) - pins `{"14": 20}` from `data/content/quests/miner.json` `records[3100004].rewards[0].job_xp`.**
  Fix: compare against the record's own `job_xp`.
- **prototype/osfr-tools/tests/miner_first_ore.rs:2210 (test containing line 2210) - pins `5, 20` from `data/content/quests/miner.json` `records[3100004].rewards[0]` `coins` / `job_xp.14`.**
  Fix: read it through the record row for 3100004.
- **prototype/osfr-tools/tests/miner_first_ore.rs:2247 (test containing line 2247) - pins `15` = three 5-coin rungs from `data/content/quests/miner.json` `rewards[0].coins` of 3100002, 3100003 and 3100004.**
  Fix: sum the three coin values read from the records.
- **prototype/osfr-tools/tests/miner_first_ore.rs:2248 (test containing line 2248) - pins `50` = 15 + 15 + 20 from `data/content/quests/miner.json` `rewards[0].job_xp.14` of 3100002, 3100003 and 3100004 (`2 * MINING_XP_PER_WIN` is code).**
  Fix: sum the three XP values read from the records; keep `2 * MINING_XP_PER_WIN`.

Note: the test-function names for the unlabelled lines (344, 392, 446, 467/468, 550, 563, 756, 795–799, 1101–1307, 1467–1491, 1554–1581, 1756, 1907–1908, 2210–2248) were not opened individually. The exact quest id each one reads is inferred from the 5/15 or 5/20 values and the same chapter; the rule-level conclusion (a shipped quest-record value is pinned) holds regardless of which of the three records it is. `finish_quest` (`support/npc_quest_chain.rs:551`) also takes the expected values as literal arguments, so the callers that pass `5, 15` or `5, 20` pin them too.</result>
