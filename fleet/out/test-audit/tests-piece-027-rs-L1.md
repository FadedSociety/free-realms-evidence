<!-- fleet job=test-audit id=tests-piece-027-rs-L1 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[19628, 12701, 10, 4849] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_027.rs lines 1-170 of 170

Reviewed `prototype/osfr-tools/tests/piece_027.rs` lines 1-170 against `prototype/osfr-tools/src/restoration/piece_027.rs` (lines 1-226). Most assertions are real: the snap tests catch floor-vs-trunc and y-axis changes, the toggle, bounds and fixture/landmark boundary tests all exercise the code. Three findings:

- **[medium] tests/piece_027.rs:161 a_zero_maximum_allows_nothing_without_inventing_a_constant - the name says a zero maximum allows nothing, but the only probe is `denial(0, 0)`, which is masked by the fixture-first check in `denial` (src/restoration/piece_027.rs:201-209).**
  - Why it cannot catch a regression: `denial(0, 0)` returns `FixtureLimitReached` before the landmark branch is reached, so the landmark side of a zero maximum is never observed. A change to `allows_landmark` that lets zero landmarks through when `max_landmarks == 0` (for example `current <= max || max == 0`) still returns `FixtureLimitReached` here and passes. It also never checks `allows_fixture(0)` or `allows_landmark(0)` directly.
  - Fix: assert `!limits.allows_landmark(0)` and `!limits.allows_fixture(0)` directly, and add a case with `max_fixtures: 3, max_landmarks: 0` where `denial(0, 0) == Some(PlacementDenial::LandmarkLimitReached)`.

- **[low] tests/piece_027.rs:104 quarter_turn_constant_matches_the_same_function - the name says it matches the function that uses the constant, but the body only compares `QUARTER_TURN_RADIANS` to a literal copied from the doc comment.**
  - Why it cannot catch a regression: the constant is never used by any code path (src/restoration/piece_027.rs:43 says it is "exported as evidence and never applied"). Changing the value and the literal together, or changing the comment, passes. Nothing ties it to `FUN_00ab1e30` or to the 15-degree step beyond the doc text.
  - Fix: rename to something like `quarter_turn_constant_is_recorded_as_evidence_only` so the name stops implying a cross-check. If a real cross-check is wanted, derive it from the 15-degree step via a documented relation, or add a test that `ROTATION_STEP_RADIANS` is not equal to it.

- **[low] tests/piece_027.rs:92 rotation_step_is_fifteen_degrees_and_signed_by_direction - the name claims "fifteen degrees", but the body only compares against the radian literal 0.2617994 and never exercises `RotationDirection::step_degrees()` (src/restoration/piece_027.rs:149-151).**
  - Why it cannot catch a regression: a change that stored the step in degrees with a conversion error, or edited the degrees helper, would still pass because the degree path is never checked. The radian check alone is fine for the step itself.
  - Fix: add `assert!((RotationDirection::CounterClockwise.step_degrees() - 15.0).abs() < 1e-3)` and the clockwise negative equivalent.
