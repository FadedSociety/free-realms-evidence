<!-- fleet job=pin-audit id=tests-investigate-the-wolves-rs status=done turns=6 usd=0.0030 tokens(read,write,in,out)=[37455, 10994, 14, 2471] model=claude-haiku-5-5 -->
# tests/investigate_the_wolves.rs

Findings (quest 3000061 reward data is `data/content/quests/adventurer.json`, id 3000061, `rewards[0]`: `coins: 20`, `job_xp: {}`). The test's `const COINS: u32 = 20;` (investigate_the_wolves.rs:96) is a hand-copied duplicate of that field.

- **prototype/osfr-tools/tests/investigate_the_wolves.rs:274 accept_at_anne - pins `20` from `data/content/quests/adventurer.json` `quests[id=3000061].rewards[0].coins`.**
  **Fix:** read it through the quest row (load adventurer.json, find id 3000061, take `rewards[0].coins`) instead of `COINS`; or keep `COINS` only as a bound (e.g. `> 0`). No shared loader helper was found under `tests/common/`, so the test needs to read the row itself.

- **prototype/osfr-tools/tests/investigate_the_wolves.rs:275 accept_at_anne - pins `0` from `data/content/quests/adventurer.json` `quests[id=3000061].rewards[0].job_xp`.**
  The `0` is the empty `job_xp` map on the same row. Retuning the XP reward would break this assertion while the code is correct.
  **Fix:** read it through the same row: expected = sum of `job_xp` values (0 today), or assert the displayed XP equals the row's `job_xp` total.

- **prototype/osfr-tools/tests/investigate_the_wolves.rs:515 test body (49/14 turn-in) - pins `20` from `data/content/quests/adventurer.json` `quests[id=3000061].rewards[0].coins`** via the `COINS` constant.
  **Fix:** read it through the quest row's `rewards[0].coins` and use that in `coins_before + ...`.

Not a finding: line 983 `coins_before + 100` uses the literal 100 passed to the test's own `realm coins 100` grant, so it is a fixture value, not data.
