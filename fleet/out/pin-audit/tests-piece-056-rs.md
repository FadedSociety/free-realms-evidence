<!-- fleet job=pin-audit id=tests-piece-056-rs status=nothing_found turns=4 usd=0.0033 tokens(read,write,in,out)=[22033, 19165, 10, 1313] model=claude-haiku-5-5 -->
# tests/piece_056.rs

No findings in `prototype/osfr-tools/tests/piece_056.rs`. None of the seven screened lines pins a value from a shipped data file.

- **Lines 98, 489 (3600):** come from `EffectTagPayload::captured_coin_boost()` (`src/restoration/piece_056.rs:282`), a fixture of the retail capture recorded in the header comments, not a data file.
- **Line 257 (3600):** comes from the test's own `coin_boost_request()` fixture (`duration_seconds: 3600`, line 57).
- **Line 336 (60):** the test's own refresh request sets `duration_seconds = 60` (line 324).
- **Line 376 (3000):** 3600 from the fixture minus the 600 s elapsed at `profile_rows(600_000)`.
- **Lines 385, 389 (2400):** 3600 minus 600 s elapsed before the 600 s restore, computed from the fixture.

A search of `data/content` found no status or buff row with duration 3600 for definition 495 or icon 7334, so there is no data value for these to drift from.
