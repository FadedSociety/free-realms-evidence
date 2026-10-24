<!-- fleet job=pin-audit id=tests-soccer-match-rs status=nothing_found turns=2 usd=0.0012 tokens(read,write,in,out)=[1808, 4436, 6, 1155] model=claude-haiku-5-5 -->
# tests/soccer_match.rs

No finding for `prototype/osfr-tools/tests/soccer_match.rs:815` (test `fallback_half_length_is_labelled_reconstructed`).

- The expected value comes from the code constant `HALF_SECONDS` in `prototype/osfr-tools/src/soccer.rs:19` (`pub const HALF_SECONDS: f32 = 180.0;`), imported at line 15 of the test. It is not read from a data file.
- `MatchConfig::new` sets `half_seconds: crate::soccer::HALF_SECONDS` (`src/soccer_match.rs:154`), so the test's default game uses that same code constant.
- `prototype/osfr-tools/data/content/soccer.json:49` also has `"half_seconds": 180.0`, but nothing in the code reads that field into `HALF_SECONDS`. Retuning the JSON would not change the constant, so the assertion would not break. The code constant is the value under test, which the rule exempts.
- The test's own fixture sets 300.0 and 1.0/5.0 for the other cases, so those are not pinned to data either.

Optional hardening: if Bryce wants the test to survive retuning the code constant, bound it (for example `> 0.0 && is_finite()`) rather than compare to 180. That is not required by the data-file rule.
