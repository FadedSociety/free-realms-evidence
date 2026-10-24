<!-- fleet job=pin-audit id=tests-mining-review-rs status=nothing_found turns=4 usd=0.0020 tokens(read,write,in,out)=[13468, 7920, 10, 1700] model=claude-haiku-5-5 -->
# tests/mining_review.rs

No findings for `prototype/osfr-tools/tests/mining_review.rs:713` (`default_spec_completes_with_the_reconstructed_ore_mapping`, `assert_eq!(spec.collectable_percent, 40)`).

Where the 40 comes from:
- The test calls `mining::mining_spec()`. That function (`prototype/osfr-tools/src/mining.rs:951-1044`) builds the spec in code and hardcodes `collectable_percent: 40` at line 1037. It does not read `data/content/mining.json`.
- `data/content/mining.json` `spec.collectable_percent` is also 40, but nothing in this test loads that file. Retuning the JSON would not change `mining_spec()`, so it would not break this assertion.

Why it is not a finding under the rule: the number is a code constant, not a value the test reads from a shipped data file, and retuning the data file would not break this test. The code-side hardcode is itself a tuning value living outside the data files (the `rule_notice` on line 1042 calls the 40% rate "local tuning"). That is a source-code issue to raise separately, not a test fix.

Possible follow-up, outside this test's scope: if `mining_spec()` should be data-driven, the test could then read `spec.collectable_percent` from `mining.json` (`spec.collectable_percent` row) or assert a bound such as `(1..=100).contains(&spec.collectable_percent)`.
