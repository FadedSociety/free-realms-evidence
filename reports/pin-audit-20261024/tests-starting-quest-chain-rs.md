<!-- fleet job=pin-audit id=tests-starting-quest-chain-rs status=done turns=9 usd=0.0057 tokens(read,write,in,out)=[90193, 20543, 20, 4509] model=claude-haiku-5-5 -->
# tests/starting_quest_chain.rs

Three findings. All three expected values are sums of quest-reward coin amounts, each one a `"coins": 5` in the quest's `rewards[0]` row. The test's `finish_quest(..., 5)` argument carries the same pinned 5 per quest, and the helper asserts `outcome.rewards[0].coins == expected_reward`, so retuning the data would break these tests while the code is still right.

- **repo:prototype/osfr-tools/tests/starting_quest_chain.rs:540 starting_quest_chain (Highroad/Raceway chain test, the one that finishes 3000020, 3080001, 3080002) - pins `15` (= 3 × 5) from `data/content/quests/adventurer.json` `rewards[0].coins` (quest 3000020, line ~1598) and `data/content/quests/kart_driver.json` `rewards[0].coins` (quests 3080001 line 96, 3080002 line 220).**
  **Fix:** read each quest's reward through its row, e.g. `coins_of(quest_id)` from the quest JSON, and assert `starting_coins + sum(row coins)`; or bound it as `>= starting_coins + 3`, plus the per-quest equality already made by `finish_quest` reading the row instead of the literal 5.

- **repo:prototype/osfr-tools/tests/starting_quest_chain.rs:606 cobblestone_post_opening_chain_finishes_and_is_not_rewarded_twice - pins `15` (= 3 × 5) from `data/content/quests/adventurer.json` `rewards[0].coins` for quests 3000021 (line ~1698), 3000059 (block at line ~4252), and 3000060 (line 4364).**
  **Fix:** read each quest's `rewards[0].coins` from the row in `quests/adventurer.json` and sum them for the expected delta, instead of `+ 15` and the literal 5 passed to `finish_quest`.

- **repo:prototype/osfr-tools/tests/starting_quest_chain.rs:772 (the test containing the 3080002 end-reply, around line 720-790) - pins `5` from `data/content/quests/kart_driver.json` `rewards[0].coins` (quest 3080002, line 220).**
  **Fix:** read the reward with the quest row (`rewards[0].coins` for 3080002 from `quests/kart_driver.json`) and assert `coins_before + that value`, or bound it as a positive delta equal to the row's value.

No existing helper under `tests/common/` loads quest reward rows, so the fix is reading the JSON row in the test itself.
