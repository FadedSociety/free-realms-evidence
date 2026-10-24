<!-- fleet job=pin-audit id=tests-warrior-entry-chain-rs status=done turns=7 usd=0.0034 tokens(read,write,in,out)=[40225, 12912, 16, 2822] model=claude-haiku-5-5 -->
# tests/warrior_entry_chain.rs

**prototype/osfr-tools/tests/warrior_entry_chain.rs:939 w5_... (the W5 record check, `assert_eq!(w5["rewards"][0]["coins"].as_u64(), Some(15))`) - pins `15` from `prototype/osfr-tools/data/content/quests/warrior.json` record id 3150005 (`rewards[0].coins`).**
- The test already loads `records` from `quests/warrior.json` (line 825-827), so the expected value is the data file's own value, and retuning the W5 coin payout would break this line while the code stays correct.
- **Fix:** read it through the loaded row, e.g. `assert_eq!(w5["rewards"][0]["coins"].as_u64(), Some(expected))` where the expectation is taken from the same record's data, or bound it as `assert!(w5["rewards"][0]["coins"].as_u64().unwrap() > 0)`. The `items` and `job_xp` checks on the next lines are structural and can stay.

Not a finding:
- **Line 557 (`REWARD_XP`, `2 * REWARD_XP`)**: `REWARD_XP` is a test-local fixture constant (line 68, value 25). The test passes it into `finish_quest` and into the expected reward bundle (lines 184, 235, 431, 549), so the test sets the number itself. The 25 coincidentally matches some shipped `job_xp` rows in other quest files, but this assertion does not read any data value, so it is not pinned to a data file.
