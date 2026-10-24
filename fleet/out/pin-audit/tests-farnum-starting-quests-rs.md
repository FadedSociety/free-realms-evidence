<!-- fleet job=pin-audit id=tests-farnum-starting-quests-rs status=nothing_found turns=4 usd=0.0017 tokens(read,write,in,out)=[10122, 7745, 10, 1235] model=claude-haiku-5-5 -->
# tests/farnum_starting_quests.rs

No findings. The screened line `prototype/osfr-tools/tests/farnum_starting_quests.rs:464 copper quest test - assert_eq!(xp_before, 5 * MINING_XP_PER_WIN)` does not pin a shipped data value.

- `MINING_XP_PER_WIN` is defined in `prototype/osfr-tools/tests/support/mining_quest_chain.rs:34` as an alias of `mining::lifecycle::RECONSTRUCTED_MINER_XP_PER_WIN`.
- That value is a compiled constant in code: `prototype/osfr-tools/src/mining_lifecycle.rs:22`, `pub const RECONSTRUCTED_MINER_XP_PER_WIN: u32 = 25;`. It is not read from any file under `data/content`. The data files contain no per-win mining XP field.
- The test expects 5 wins times that constant, so it already goes through the shared constant and does not hardcode 25. Retuning a data file would not affect it.

No change is needed. The constant is a code-side reconstruction value, which is outside this audit's data-file rule.
