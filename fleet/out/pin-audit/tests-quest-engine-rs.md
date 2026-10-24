<!-- fleet job=pin-audit id=tests-quest-engine-rs status=nothing_found turns=3 usd=0.0009 tokens(read,write,in,out)=[5174, 3797, 8, 769] model=claude-haiku-5-5 -->
# tests/quest_engine.rs

No findings in `prototype/osfr-tools/tests/quest_engine.rs`.

- **quest_engine.rs:533 duplicate_turnin_retry_uses_the_character_quest_grant_key_once** - the expected `5` coins is set by the test's own fixture. The test calls `definition(88, 8, 9, vec![...], 5)` (line 508), and `definition` (line 156) passes that fifth argument into `reward(coins, ...)` (line 173). The value comes from the test's arguments, not from `data/content/*.json`, so it is not a tunable data value.
- **quest_engine.rs:568 duplicate_turnin_retry_uses_the_character_quest_grant_key_once** - the same `5` carried through `paid` into the retry. It is the same fixture value, so it is not a finding either.

Retuning any shipped data file would not change these assertions.
