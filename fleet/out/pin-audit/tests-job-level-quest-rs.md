<!-- fleet job=pin-audit id=tests-job-level-quest-rs status=nothing_found turns=8 usd=0.0050 tokens(read,write,in,out)=[65389, 21745, 18, 3234] model=claude-haiku-5-5 -->
# tests/job_level_quest.rs

No findings in `prototype/osfr-tools/tests/job_level_quest.rs` for the three screened lines. Each expected number comes from the test's own fixture, not from a shipped data file:

- **317 `real_xp_to_level_five_completes_it_once` (300):** three field kills at 100 job XP each. The test writes that rate into its own `field_kill_rewards.json` fixture (lines 250-260, marked "test-only 100 XP per field kill rate"). It is not read from `data/content`.
- **604 `a_live_change_before_the_turn_in_survives` (before + 7):** the 7 is the argument of the test's own `realm coins 7` chat command. It is an input, not a tunable value.
- **887 `a_quest_turn_in_job_xp_completes_it_too` ((0, 100)):** quest 3150906 is a synthetic quest the test builds (line 1012 onward), with `"job_xp": {"32": 100}` at line 1025. It is not the shipped quest 3150005, whose data file has `coins: 15` and `job_xp: {}`.

Shipped-data-backed values in this file (`W5_REWARD_COINS = 15`, `RANK_FIVE_XP = 400`) are not among the screened lines, so I left them out.
