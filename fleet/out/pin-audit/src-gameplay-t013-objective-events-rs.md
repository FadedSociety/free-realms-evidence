<!-- fleet job=pin-audit id=src-gameplay-t013-objective-events-rs status=nothing_found turns=13 usd=0.0060 tokens(read,write,in,out)=[132524, 19528, 28, 4552] model=claude-haiku-5-5 -->
# src/gameplay/t013_objective_events.rs

Neither screened line pins a number from a shipped data file.

- **t013_objective_events.rs:1073-1074 (`coins, 40`, the kart-gate payout in `kart_completion_reaches_quests_only_after_a_paid_claim`)**: the 40 is set by the test's own fixture. Line 494 builds `KartServiceContent` inline with `reward: Some(RewardSchedule { coins: 40, xp: 60 })`. The shipped track reward in `data/content/kart_entry.json` `race.reward` is 50 coins / 25 XP, which the test does not read, so retuning data does not affect this assertion. No change needed.
- **t013_objective_events.rs:1346 (`job_level(profile), 2`, "75 + 25 XP is rank 2")**: the expected rank 2 comes from the code's local 100-XP curve (`profiles.rs` `rank()`: `1 + xp / 100`, capped at 20). The 75 is set by the test (line 1343). The 25 XP is the discovery reward the test describes in its comment, but the assertion's expected value is a level, not a data number, so it is not a pinned tunable. No change needed.
