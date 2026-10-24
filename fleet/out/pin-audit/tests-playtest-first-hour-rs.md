<!-- fleet job=pin-audit id=tests-playtest-first-hour-rs status=nothing_found turns=2 usd=0.0012 tokens(read,write,in,out)=[1829, 6202, 6, 862] model=claude-haiku-5-5 -->
# tests/playtest_first_hour.rs

No finding for `prototype/osfr-tools/tests/playtest_first_hour.rs:583` (`test` in the listed assertion `assert_eq!(coins(&game), coins_before + QUEST_COINS, "exactly 10 coins")`).

- `QUEST_COINS` is a file-local `const QUEST_COINS: u32 = 10;` at line 102 of this test file. It is not read from `data/content/*.json`.
- It feeds the test's own fixture: line 133 builds the quest with `quest_record(QUEST, &[], QUEST_COINS, true)`. The reward the test checks is the value the test itself seeds, so retuning the shipped quest data would not break this assertion.
- The "exactly 10 coins" message is only a label; the number is the fixture's, not a data value.

No change needed for this line. If the team wants it to stay in sync with real data, the fix would be to read the quest's coin reward from the quest data row instead of the local constant. That is optional, not a pinned-tunable defect.
