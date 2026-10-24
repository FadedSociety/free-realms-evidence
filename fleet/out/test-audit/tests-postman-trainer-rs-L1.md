<!-- fleet job=test-audit id=tests-postman-trainer-rs-L1 status=nothing_found turns=5 usd=0.0052 tokens(read,write,in,out)=[32084, 16827, 12, 5636] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/postman_trainer.rs lines 1-234 of 234

Reviewed `prototype/osfr-tools/tests/postman_trainer.rs` lines 1-234 against the code under test (`profiles.rs` `load_trainers`, `rewards.rs` `locked_job_profile`, `data/content/job_trainers.json` rows 55-104, and the quest `"job"` fields under `data/content/quests`). No finding meets the five categories:

- **Cannot fail:** the expected values are literals or constants (`(5, 5)`, XP `5`, the Postman/Adventurer/Brawler job ids, the starter piece ids). The learn-path audit has a sanity canary (`needed.contains((POSTMAN, QUEST))`), and the trainer loop terminates because `learnable` only grows.
- **Asserts nothing:** `assert_refused` compares the full saved state before and after, so `Err` or an unchanged `Ok` both count as a refusal with no mutation. The `is_ok_and` form is not a hole because of that save comparison.
- **Name overclaims:** each test body exercises what its name and doc claim. The replay, relog and second-lesson paths all compare saved state.
- **Silently skipped:** no `#[ignore]`. The only early exit is the `None` branch in `load_trainers`, which the audit does not take because `job_trainers.json` exists.
- **Over-pinned:** the 26/13 reply check uses a raw prefix `[38, 0, 21, 0]`, which is wire-level, but it is paired with an `active_job` assertion, so it is not an incidental-detail churn risk worth reporting.

One design note, not reported as a finding: the learn-path audit treats any trainer row as teaching its profile without checking that the NPC is spawned in a reachable zone. The doc comment defines "learnable" as a trainer row, so this matches the stated contract rather than overclaiming it.
