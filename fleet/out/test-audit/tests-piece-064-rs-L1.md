<!-- fleet job=test-audit id=tests-piece-064-rs-L1 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[19856, 12512, 10, 4810] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_064.rs lines 1-217 of 217

Window: `prototype/osfr-tools/tests/piece_064.rs` lines 1-217. I read the test file and the code under test (`src/restoration/piece_064.rs`, lines 1-268). The parser, bounds, classify, and tail tests check independently written expected values and do fail on the mutations I traced, so they are not findings. Two findings:

- **[medium] tests/piece_064.rs:177 floor_query_returns_the_highest_walkable_surface_below_the_probe - the name says "highest", but the fixture has only one walkable level (both floor triangles at y=0), so the highest-of-several selection is never exercised.**
  - Why it cannot catch a regression: in `horizontal_floor` (src/restoration/piece_064.rs:263), changing `y > current` to `y < current` (return the lowest surface) still returns 0.0 for every query here, so the test passes. The wall triangles are skipped by the slope filter, so they do not provide a second level either.
  - Fix: add a second walkable surface above the floor over the same (x, z), for example a horizontal quad at y=3 with the probe at 5.0. Assert `Some(3.0)`, then assert `Some(0.0)` with a probe of 2.0. This fails if the selection picks the lowest surface.

- **[medium] tests/piece_064.rs:190 floor_query_ignores_vertical_surfaces - the fixture cannot separate the slope policy from the degenerate-projection guard, so the test does not check the slope filter it names.**
  - Why it cannot catch a regression: any vertical triangle projects to a line in XZ, so `denom` is zero and the `denom.abs() <= 1e-12` guard (src/restoration/piece_064.rs:253) skips it. Deleting the slope check at line 248 (`(ny / length).abs() < limit`), or setting `MAX_SLOPE_DEGREES` to 90, still returns None, and the test still passes.
  - Fix: add a triangle with a non-degenerate XZ projection and a steep but not vertical slope (inclination above 50 degrees, so `|ny|/len < cos(50°)`). Assert `horizontal_floor` returns None for it. Add a shallower ramp below 50 degrees over the same (x, z) and assert it returns Some. The first assertion fails if the slope filter is removed, and the second fails if the threshold is made too strict.

No other findings: no `#[ignore]`, no early-return skips, and no assertions on counts or offsets that unrelated work would change.
