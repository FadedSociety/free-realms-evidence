<!-- fleet job=pin-audit id=tests-piece-011-rs status=nothing_found turns=3 usd=0.0011 tokens(read,write,in,out)=[4722, 4305, 8, 956] model=claude-haiku-5-5 -->
# tests/piece_011.rs

No finding for `prototype/osfr-tools/tests/piece_011.rs:90` (`settings_expose_the_recovered_constants`, `assert_eq!(s.timeout_seconds, 10.0)`).

- The `10` is not read from any data file. `settings()` parses the `RECOVERED_SETTINGS` string constant defined in the test itself (tests/piece_011.rs:45-54, `TIMEOUT_SECONDS^10`). The test's own fixture sets the number, so it is not a finding under the rule.
- A repo-wide search for `TIMEOUT_SECONDS` and `timeout_seconds` finds no row in `data/content/*.json`. The only other sources are code (`src/restoration/piece_011.rs`, which reads the value via `float("TIMEOUT_SECONDS")`), a Python script and notes. So no shipped data value would break this assertion if retuned.
- The adjacent line 100 (`timeout_milliseconds() == 10_000`) derives from the same fixture and is not on the screened list.

Nothing to change for this line.
