<!-- fleet job=test-audit id=tests-harvesting-border-rs-L1 status=done turns=8 usd=0.0075 tokens(read,write,in,out)=[97822, 24108, 18, 6968] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/harvesting_border.rs lines 1-254 of 254

Window: `prototype/osfr-tools/tests/harvesting_border.rs` lines 1-254. Read against `src/harvesting.rs` (`board_spec` 930-1014, `padded_engine_shape` 910-921, `validate_border` 1300-1320, `RULE_NOTICE` 800) and `src/mining.rs` 1335-1354 (board fill from shape). The shape, bounds, and notice assertions are sound; the findings below are the weak spots.

- **[medium] tests/harvesting_border.rs:180 padded_content_starts_on_the_real_engine_with_inert_edges - the name claims edges are "inert" on the running engine, but the body only inspects the initial board right after `start_level`; no fall or gravity step runs.**
  - Why it cannot catch a regression: an engine change that lets tiles move into row 0 or column 0 after the first tick (for example, a fall loop that starts at index 0, or a refill that writes into the border) would still pass, because the board is checked only once before any movement. The top-of-file doc ("row 0 and column 0 can therefore never move") is also not exercised by any test in this window.
  - Fix: after `start_level`, drive at least one gravity/tick step (or a move that vacates a playable cell), then re-assert `run.board[index]` and `run.board[index * PADDED]` are 0 for all index 0..PADDED. Alternatively, rename the test to say "initial board" so the name matches what is checked.

- **[low] tests/harvesting_border.rs:215-219 padded_geometry_preserves_parameters_and_playable_cell_count - the parameter checks compare `spec.duration_seconds`, `spec.seed`, `spec.wildcard_percent`, `spec.collectable_percent` and `spec.powerup_percent` with the `RECONSTRUCTED_*` constants, and `board_spec` writes those same constants straight into the spec (`src/harvesting.rs:1003-1009`).**
  - Why it cannot catch a regression: if someone changes a `RECONSTRUCTED_*` value, both sides move together and the test still passes. The checks only notice a literal or unrelated value replacing the constant in `board_spec`, so they do not pin the reconstructed values the test name refers to.
  - Fix: pin literal values, for example `assert_eq!(spec.duration_seconds, 120)` and the recovered seed literal, so a change to the constant is a visible, deliberate test update.

- **[low] tests/harvesting_border.rs:227 and :234 padded_geometry_preserves_parameters_and_playable_cell_count - exact cell counts (90 regular cells, 10 dropzone cells) are checked in a test about parameters, and the same geometry is already pinned positionally in `emitted_shape_pads_the_original_zero_edges`.**
  - Why it cannot catch a regression: it is not a regression check for parameters. An unrelated change that adds or removes one playable tile in a different test would fail this test with no link to the parameter contract, which causes churn rather than catching a real bug.
  - Fix: drop the two counts from this test, or keep only the parameter assertions. Leave the positional checks in the shape test.
