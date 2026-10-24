<!-- fleet job=pin-audit id=tests-mining-rs status=done turns=7 usd=0.0034 tokens(read,write,in,out)=[37897, 11608, 16, 3194] model=claude-haiku-5-5 -->
# tests/mining.rs

Audit of `prototype/osfr-tools/tests/mining.rs` (3 screened lines). One finding.

- **prototype/osfr-tools/tests/mining.rs:812 default_mining_spec_is_consistent_and_marks_reconstructed_rules - pins `40` from `prototype/osfr-tools/data/content/mining.json` `collectable_percent` (line 16).**
  The test reads `mining::mining_spec()`, whose `collectable_percent: 40` is the code default at `src/mining.rs:1037`. That default is the same value that ships in `mining.json`, and the `rule_notice` at `src/mining.rs:1042` calls the 40% rate "local tuning". Retuning the shipped value would make this assertion fail even though the code still works.
  **Fix:** read the expected value from the data row (load `data/content/mining.json` and compare `spec.collectable_percent` to its `spec.collectable_percent`), or bound it, e.g. `assert!((1..=100).contains(&spec.collectable_percent))`. The `1..=20` range check in `src/forging.rs:1031` is an example of a bound rather than a pinned value.

Not findings:
- **mining.rs:390 `remaining_ms == before + 6000`.** The 6000 is `bonus * 1000` with `bonus = 2 * chain.len()` and a 3-tile chain, computed in `src/mining.rs:739-744`. It is a code formula, and `mining.json` has no time-bonus field, so it is not a data-file value.
- **mining.rs:391 `score == 400`.** This is `CHAIN_SCORE = 400` (`src/mining.rs:115`), a code constant. `mining.json` has no score field.
