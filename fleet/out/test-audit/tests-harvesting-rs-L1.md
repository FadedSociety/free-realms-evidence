<!-- fleet job=test-audit id=tests-harvesting-rs-L1 status=done turns=6 usd=0.0093 tokens(read,write,in,out)=[84728, 30939, 14, 9100] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/harvesting.rs lines 1-590 of 590

Window: `prototype/osfr-tools/tests/harvesting.rs` lines 1-590. No `#[ignore]`, no early-return fixture skips in this window. The content-guard mutations (game_id, truncated shape, output definition_id, cleared goals, wrong movie, traversal in preload_file, non-zero border row 0) are each rejected by a real check in `validate_content`/`validate_border` (src/harvesting.rs:1053-1180, 1300-1320), so that test does fail on regression.

- **[medium] tests/harvesting.rs:110 recovered_produce_sets_match_original_locale_descriptions - the name and comment claim the produce sets match the original locale descriptions (94149..94154), but the body never reads the locale table; it only compares `region(id).produce` with a hardcoded slug array.**
  - Why it cannot catch a regression: any change to the locale text or to the locale-id-to-region mapping (e.g. swapping which description id belongs to which region, or a locale entry that no longer names the produce) still passes, because nothing consults locale ids or text here.
  - Fix: resolve each region's description id through the locale table and assert the names it contains match the slug set (or rename the test to `recovered_produce_sets_match_expected_slugs` and add a separate locale-backed test).

- **[medium] tests/harvesting.rs:439 emitted_spec_is_consumable_by_a_type8_engine_loader - the name says the emitted spec is consumable by the type-8 engine loader, but the body only deserializes `content_json(109)` into a test-local `ContentMirror`/`SpecMirror` that the author wrote, with no engine or `validate_content` call (the comment at 440-441 admits this is a mirror, not a link).**
  - Why it cannot catch a regression: the mirror accepts any extra field and any shape the engine would reject (e.g. a border or dropzone violation the engine enforces); if the mirror and emitter drift together, the test is still green. Only serde-required field names are checked.
  - Fix: rename to `emitted_spec_matches_contract_mirror_fields`, and additionally run `validate_content(&typed)` on the deserialized `HarvestContent` plus `#[serde(deny_unknown_fields)]` on the mirror structs so unexpected or missing fields fail.

- **[low] tests/harvesting.rs:227-228 observed_diamond_shape_and_engine_rectangle_stay_separate - the comment says "the bottom row of the playable rectangle must sit above the drop zone", but the assertion only checks every cell is 0 or 1 and never looks at rows or the drop zone.**
  - Why it cannot catch a regression: moving the playable rows or removing the dropzone row from the diamond output would still pass this assertion, so the comment promises a check that is not there.
  - Fix: assert that row `height-1` of `diamond_shape(10,10)` (or of the emitted board, row 10) equals the dropzone code / the expected row pattern, or delete the misleading comment.

- **[low] tests/harvesting.rs:183 result_requires_every_quota_goal_and_counts_bundles - `total_bundles` is compared with `14 / 5 + 10 / 5` and `3 + 2`, which restate the `floor(collected / per_reward)` formula that `GoalProgress::clusters` implements (src/harvesting.rs:713-719).**
  - Why it cannot catch a regression: the expected value is the same arithmetic as the code under test, so a change in rounding semantics that keeps the same formula is invisible; it only pins the formula, not the recovered bin behaviour.
  - Fix: pin literal numbers (`4` and `5`) with a comment citing the recovered bin rule, and add a case with a non-divisible remainder that a ceil/round variant would fail.

- **[low] tests/harvesting.rs:349-355 content_json_matches_the_frozen_type8_contract - the dropzone check hardcodes the last 10 cells as the drop row, assuming width 10, instead of deriving the row width from `width`.**
  - Why it cannot catch a regression: if the emitted width changes (e.g. the padded 11-wide board), the check still looks at a 10-cell slice that no longer aligns to a row, so it can pass or fail for the wrong reason and misses a dropzone that is only partly present.
  - Fix: use `let w = width as usize; emitted_shape[emitted_shape.len() - w..]` (and assert `w == 11` or the row count explicitly) so the check follows the board geometry.
