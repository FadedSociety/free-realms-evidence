<!-- fleet job=pin-audit id=tests-shared-field-kill-quest-credit-rs status=done turns=10 usd=0.0063 tokens(read,write,in,out)=[107860, 24970, 22, 4154] model=claude-haiku-5-5 -->
# tests/shared_field_kill_quest_credit.rs

The screened numbers are not quest rewards. The 2 and 5 are the per-kill field credit for definition 3156 (Hooligan Wolf), paid through `credit_field_kill` → `pay_field_reward` (`src/encounter/field_rewards.rs`). That path resolves the definition override before the level band. The override is in `data/content/field_kill_rewards.json` `definition_overrides[definition_id=3156]`: `coins: 2`, `job_xp: 5`. The starter band (`level_rewards` min 1, max 2) has the same 2 / 5. The test's `WOLF = 3156`, so retuning that row would break these asserts while the code stays right. (The file's `QUEST_COINS = 18` and `QUEST_JOB_XP = 25` constants are the quest's own reward and are not used by these lines.)

- **prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs:823 the_credit_pays_the_contributor_reward_and_quest_event_once - pins `2` from `data/content/field_kill_rewards.json` `definition_overrides[3156].coins`.**
  **Fix:** read it through the shipped-file pattern used in `tests/field_camps_elite_band.rs` (`shipped_rewards()`), taking `definition_overrides` where `definition_id == WOLF` and its `coins`, or bound it as `coins(&b) > 0 && coins(&b) <= the band max (level_rewards[].coins)`.

- **prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs:824 the_credit_pays_the_contributor_reward_and_quest_event_once - pins `5` from `data/content/field_kill_rewards.json` `definition_overrides[3156].job_xp`.**
  **Fix:** read the row via `shipped_rewards()` (as in `tests/field_camps_elite_band.rs`) and compare to its `job_xp`, or bound it as `> 0` and `<=` the band max `job_xp`.

- **prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs:838 the_credit_pays_the_contributor_reward_and_quest_event_once - pins `(2, 5)` from `data/content/field_kill_rewards.json` `definition_overrides[3156].coins` and `.job_xp`.**
  **Fix:** compare against the values read from the override row for `WOLF` (same helper as above), so the "paid once" check holds the value it read before the second tick.

- **prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs:1084 an_expired_or_left_field_credit_advances_nothing (the case starting near line 1000) - pins `2` from `data/content/field_kill_rewards.json` `definition_overrides[3156].coins`.**
  **Fix:** read it through the override row for `WOLF` in `field_kill_rewards.json`, or bound it as `coins(&c) > 0` and no larger than the level band's `coins`.

- **prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs:1085 an_expired_or_left_field_credit_advances_nothing - pins `5` from `data/content/field_kill_rewards.json` `definition_overrides[3156].job_xp`.**
  **Fix:** read it through the override row for `WOLF` in `field_kill_rewards.json`, or bound it as `> 0` and no larger than the band's `job_xp`.

Note: the test file's own comments and the screener both attribute these to the quest reward; the correct source is the field kill override above. The helper `tests/common/field_reward_fixture.rs` writes a reward file for a test and does not read the shipped one, so the read has to be done in the test itself, as `shipped_rewards()` does in the sibling tests.
