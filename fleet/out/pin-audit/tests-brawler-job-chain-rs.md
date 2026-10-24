<!-- fleet job=pin-audit id=tests-brawler-job-chain-rs status=done turns=4 usd=0.0017 tokens(read,write,in,out)=[10736, 6839, 10, 1573] model=claude-haiku-5-5 -->
# tests/brawler_job_chain.rs

**prototype/osfr-tools/tests/brawler_job_chain.rs:1200 test_name (not captured by the screener; test name not extracted, read at line 1200) - pins `5` (`3 * QUEST_REWARD_COINS`) from `data/content/quests/brawler.json` `coins`.**
- Source: `QUEST_REWARD_COINS: u32 = 5` is a hardcoded local constant at line 39. It mirrors the `"coins": 5` reward on the chain quests 3030006, 3030007, 3030008 and 3030009 in `quests/brawler.json` (lines 206/302/371/461/545/634). Retuning those rewards would break the assertion while the code is still correct.
- **Fix:** read the reward per quest from the quest data (the `coins` value on each quest row in `data/content/quests/brawler.json`), or compare the balance delta against the reward the quest grants as loaded from data. If a shared loader exists under `tests/common/`, use it. Otherwise bound it (for example, assert the delta is greater than 0 and matches the sum of the loaded rewards).

**prototype/osfr-tools/tests/brawler_job_chain.rs:1357 test_name (not captured by the screener; test name not extracted, read at line 1357) - pins `5` (`3 * QUEST_REWARD_COINS`) from `data/content/quests/brawler.json` `coins`.**
- Same source and cause as line 1200: the local `QUEST_REWARD_COINS = 5` constant duplicates the shipped `coins` reward on the chain quests in `quests/brawler.json`.
- **Fix:** same as line 1200. Read each quest's `coins` from `data/content/quests/brawler.json` instead of using the local constant.

Note: the constant `QUEST_REWARD_COINS` is also used at lines 518, 972, 1035, 1051, 1326, 1562, 1606, 1787, 1847, 1911, 1939 and 2135. Those were not on the screened list, so I have not assessed them. They have the same root cause if they are reward assertions.
