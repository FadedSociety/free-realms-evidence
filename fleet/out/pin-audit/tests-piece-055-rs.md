<!-- fleet job=pin-audit id=tests-piece-055-rs status=nothing_found turns=4 usd=0.0019 tokens(read,write,in,out)=[14879, 8355, 10, 1383] model=claude-haiku-5-5 -->
# tests/piece_055.rs

No findings for the screened line.

- **tests/piece_055.rs:92 out_of_range_target_never_enters_the_cast** - not a finding. The range `30.0` is the test's own fixture, passed to the local `profile(1500, 400, 30.0)` helper (tests/piece_055.rs:45, :91). The `30.5` distance is the test's own over-range input. Neither is read from `data/content`. The code (`src/restoration/piece_055.rs:244`) compares `distance_units > profile.range_units`, so the assertion stays correct for any fixture range.
