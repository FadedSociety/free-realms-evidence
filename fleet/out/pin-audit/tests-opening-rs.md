<!-- fleet job=pin-audit id=tests-opening-rs status=nothing_found turns=5 usd=0.0032 tokens(read,write,in,out)=[32292, 15521, 12, 1898] model=claude-haiku-5-5 -->
# tests/opening.rs

No findings in `prototype/osfr-tools/tests/opening.rs` for the four screened lines.

- **111 `result.rewards[0].coins == 25`** (test `opening` flow, synthetic fixture): the `Reference::new()` fixture (lines 24-31) writes its own content with stage 10 `reward.coins: 25`. The test pins its own fixture value, not a shipped data file. Not a finding.
- **130 `result.rewards[0].coins == 10`**: same fixture, stage 11 `reward.coins: 10` (line 31). Not a finding.
- **326 `engine.initial_profiles() == &[1, 43]`** (`private_opening_content_loads_...`, `#[ignore]`): the value is read from the private `opening.json` under `OSFR_OPENING_REFERENCE`, which is not a shipped file in `data/content`. The values are profile ids (identifiers), not tunable numbers. Not a finding.
- **333 `weapon["reward"]["items"] == [[75030, 1]]`**: 75030 is an item definition id, an identifier, not a tunable value. The reward data itself comes from the private file. Not a finding.

Notes: the same private test's coin assertions (line 332 `weapon reward coins == 16`, line 335 `wolves reward coins == 18`) are not on the screened list, so I did not evaluate them. They also read the private opening.json, not a shipped data file.
