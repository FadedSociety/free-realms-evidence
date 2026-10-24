<!-- fleet job=pin-audit id=tests-brawler-mongo-chain-rs status=done turns=8 usd=0.0041 tokens(read,write,in,out)=[54104, 15496, 18, 3302] model=claude-haiku-5-5 -->
# tests/brawler_mongo_chain.rs

Two of the three screened lines are findings; line 672 is not.

- **prototype/osfr-tools/tests/brawler_mongo_chain.rs:671 won_once test (the `won.coins` assertion) - pins `19` from `prototype/osfr-tools/data/content/field_battles.json` `reward_coins` (battle id 12400, the Mongo row at line 1455).** The local `const BATTLE_COINS: u32 = 19;` (line 67) is a copy of that data value.
  **Fix:** read it through the field battle row 12400 in `field_battles.json` (`reward_coins`), not a copied literal. Use the same row read at the other `BATTLE_COINS` uses (lines 475, 843, 1163) so they all follow the data.

- **prototype/osfr-tools/tests/brawler_mongo_chain.rs:1282 (the `rewards[0]["job_xp"]["43"]` assertion) - pins `25` from `prototype/osfr-tools/data/content/quests/brawler.json` `rewards[].job_xp["43"]` (quest 3030004, the first reward block at line 204-210).** The `QUEST_XP: u32 = 25` const (line 70) is a copy of that value. Note the same const also feeds lines 402-405, 733, 800, 868, 880.
  **Fix:** read the expected value from the quest's own `rewards[0].job_xp["43"]` in `quests/brawler.json` (the quest record already loaded in this test), or bound it as `> 0`. No shared helper under `tests/common/` loads brawler quest rewards, so read the row in the test.

Not a finding: line 672 `BATTLE_XP` = 50. That value is not in any data file; it is the code constant `BATTLE_JOB_XP: u32 = 50` in `prototype/osfr-tools/src/encounter.rs:76`. The rule only counts values from shipped data files, so it is left alone (a code-side tunable, though it could later be moved into data).
