<!-- fleet job=pin-audit id=tests-piece-017-rs status=nothing_found turns=2 usd=0.0007 tokens(read,write,in,out)=[1814, 2744, 6, 717] model=claude-haiku-5-5 -->
# tests/piece_017.rs

No findings in `prototype/osfr-tools/tests/piece_017.rs`.

- **piece_017.rs:229 private_cooking_native_midround_disconnect_conserves_materials - not a finding.** `json!(110)` is compared against `after["gameplay"]["inventory"]["coins"]` from the captured `character-after.json` in the private lab run `runs/client-baseline-20261008T162238Z`. The 110 is an observed character state from that capture, not a value read from `data/content/*.json`, and the test does not compute it from a reward or price. Retuning shipped data would not change it, so it does not pin a tunable. It is evidence-pinned, like the instance ids on lines 224-227. The test is `#[ignore]`d and reads only private lab evidence.

Note: if a reviewer wants this assertion to survive a re-capture, the better shape is a bound (for example `coins >= 0` and that `before` minus `after` matches the cleared run's cost), not the literal 110. That is a robustness choice, not a data-tunable violation.
