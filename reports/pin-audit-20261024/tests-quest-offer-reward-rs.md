<!-- fleet job=pin-audit id=tests-quest-offer-reward-rs status=done turns=7 usd=0.0033 tokens(read,write,in,out)=[38149, 12605, 16, 2587] model=claude-haiku-5-5 -->
# tests/quest_offer_reward.rs

**prototype/osfr-tools/tests/quest_offer_reward.rs:297 test_name (not captured by the screen; test fn containing this line) - pins `5` and `20` from `prototype/osfr-tools/data/content/quests/adventurer.json` quest id 3000021 `rewards[0].coins` (line 1698, value 5) and `rewards[0].job_xp["1"]` (line 1701, value 20).**
- The expected pair is the authored reward row for `REWARD_QUEST` (3000021), read straight from the data. The end-screen words it checks at `end[27..35]` are correct, so the problem is only the hard-coded literals.
- **Fix:** read it through the authored bundle the test already uses. `engine(CHARACTER).quest_reward_bundle(REWARD_QUEST)` is already called at lines 162-163, so take `coins = bundle[1..5]` and `xp = bundle[5..9]` as i32 LE from there, and compare `(displayed_coins, displayed_xp)` against that. Alternatively, read the row from `adventurer.json` (`rewards[0].coins` and `rewards[0].job_xp["1"]`). Do not keep the literal `(5, 20)`.

Same source, same issue, on the same test's next call (not in the screened list, but it passes the same literals): **line 300 `finish_quest(..., ADVENTURER, 5, 20, now)`** pins the same data values. Fix it the same way, using the bundle values or the `adventurer.json` row.

Lines 165-180 in the same file (the 69-byte length and the coin/star word checks at 174 and 179) also pin 5 and 20 from the same row. They are outside the screened list, so I am noting them rather than adding them as findings.</result>
