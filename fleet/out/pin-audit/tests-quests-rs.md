<!-- fleet job=pin-audit id=tests-quests-rs status=nothing_found turns=4 usd=0.0019 tokens(read,write,in,out)=[14365, 9247, 10, 1164] model=claude-haiku-5-5 -->
# tests/quests.rs

No findings in `repo:prototype/osfr-tools/tests/quests.rs` for the screened lines. Every value they pin comes from the test's own fixture, not from a shipped file under `data/content`:

- 135, 136 (25 coins, item `[1195,1]`), 162 (item `[1843,1]`), and 232 (10 coins) all read the inline `Reference::new()` JSON at lines 32–42 (`coins`, `items`, `reward_coins`). The test writes that JSON to a temp `quests.json` itself, so retuning `data/content` cannot affect them.
- 233 (`trial_best_ms == Some(6000)`) is the elapsed time between the test's own fake clock timestamps (`on_position` at 1000 and 7000). It is not a data value.

The screened lines are fixture-driven, so no change is needed.
