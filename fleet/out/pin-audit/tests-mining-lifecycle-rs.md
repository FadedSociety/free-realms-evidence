<!-- fleet job=pin-audit id=tests-mining-lifecycle-rs status=nothing_found turns=11 usd=0.0084 tokens(read,write,in,out)=[199464, 34341, 24, 4143] model=claude-haiku-5-5 -->
# tests/mining_lifecycle.rs

No finding for `tests/mining_lifecycle.rs:450` (`seeded_full_round_wins_and_grants_ore_xp_and_quest_events_once`, `count_item(..., ORE_ITEM) == 12`).

Where the 12 comes from:
- The fixture (`Fixture::new`, lines 41-102) builds its engine with `write_content` from `src/mining.rs:1052`. That function writes `mining_spec()` from code (`src/mining.rs` ~lines 1000-1042), not `data/content/mining.json`.
- `mining_spec()` sets goals 601 (quota 6, per_reward 1, cluster_quantity 1) and 602 (quota 6, per_reward 2, cluster_quantity 2). The round ends at collected `[6, 6]`, so the payout is 6×1 + (6/2)×2 = 12.
- The shipped `data/content/mining.json` carries the same values, but the test never reads that file. Retuning `mining.json` would not change this test's fixture, so it would not break the test.

The number is derived from the code default that the fixture writes, not from a shipped data file the test loads. The test is therefore not pinning a data value under the rule. One side note for the team, not a finding in this file: `mining_spec()` in code duplicates the tunables in `data/content/mining.json`, so the two can drift. If Bryce wants the single-source rule enforced, that is a separate change to `mining_spec()`, not to this test.
