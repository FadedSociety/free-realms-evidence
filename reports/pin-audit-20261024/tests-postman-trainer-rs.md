<!-- fleet job=pin-audit id=tests-postman-trainer-rs status=done turns=6 usd=0.0038 tokens(read,write,in,out)=[47088, 17277, 14, 2362] model=claude-haiku-5-5 -->
# tests/postman_trainer.rs

Both screened lines pin tunable values from `prototype/osfr-tools/data/content/quests/postman.json`. Quest 3130032 ("Postman: Trail of Mail") has `rewards[0]` = `{"coins": 5, "items": [], "job_xp": {"4": 5}}`. The test's `QUEST` is 3_130_032 and its `POSTMAN` profile is 4, so the expected 5s are that row's values. The screen's line 154 `finish_quest(..., POSTMAN, 5, 5, ...)` uses the same literals; it is part of the same pin and I have listed it below.

- **postman_trainer.rs:152 postman_trainer test (the test containing this line) - pins `5` (coins) and `5` (stars total, the sum of job XP) from `data/content/quests/postman.json` `rewards[0].coins` and `rewards[0].job_xp["4"]`.**
  **Fix:** read it through the quest row. Load `quests/postman.json`, find the record with `id == QUEST`, and use `rewards[0]["coins"]` and the sum of `rewards[0]["job_xp"]` values for the end-screen tuple. `end_screen_reward` in `tests/support/npc_quest_chain.rs` returns the coin and star words, so compare it to that row. No shared loader exists in `tests/common/`; `adventurer_briarwood.rs:95` has a local `quest_record(id)` helper that can be copied, or lifted into support.

- **postman_trainer.rs:160 postman_trainer test - pins `5` from `data/content/quests/postman.json` `rewards[0].job_xp["4"]`.**
  **Fix:** read it through the same quest row, e.g. `profile_xp(&game, POSTMAN) == xp_before + row.rewards[0].job_xp["4"]`, or use the `expected_xp` value taken from that row.

Related, same pin (not on the screened list): postman_trainer.rs:154 passes literal `5, 5` to `finish_quest`. Fix it the same way, with `coins` and the job XP from the row.
