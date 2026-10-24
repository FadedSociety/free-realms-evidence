<!-- fleet job=test-audit id=tests-piece-097-rs-L1 status=done turns=4 usd=0.0048 tokens(read,write,in,out)=[24512, 16955, 10, 4880] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_097.rs lines 1-392 of 392

Window reviewed: `prototype/osfr-tools/tests/piece_097.rs` lines 1-392, checked against `prototype/osfr-tools/src/restoration/piece_097.rs` (lines 270-560). Most hermetic tests are sound: their expected values are hard-coded, and the conflict, coverage, and gap logic they check is exercised. No high-severity holes. Three lower-severity findings:

- **[low] tests/piece_097.rs:314 asset_and_locale_lookups_are_case_insensitive - the name claims case-insensitive locale lookup, but the locale half only checks numeric ids and never exercises case.**
  - Why it cannot catch a regression: `locale_ids` (src line 344) parses integer ids from JSON with no string handling, so case is irrelevant to it. The asset half does exercise `asset_names` lowercasing (src line 336), so the name is only half-true. A locale change that breaks the JSON parse for one entry would still pass as long as ids 10 and 11 parse.
  - Fix: rename to `asset_lookups_are_case_insensitive`, or keep the name and add a locale case that actually varies the input, such as a text field with mixed case whose id must still be returned. Also assert `locale.len() == 2` so a dropped entry fails.

- **[low] tests/piece_097.rs:311 duplicate_item_ids_and_reference_table_gaps_are_reported - `param1_coverage.len() == 0` is incidental to this test's claim.**
  - Why it cannot catch a regression: every item in this test has `param1: None`, so `analyze` (src lines 488-496) never inserts a coverage entry. Any change to how coverage is keyed or filtered, such as also recording `None` item types, would still produce length 0 here, because no item carries a Param1 value. The assertion says nothing about duplicates or gaps.
  - Fix: remove the line, or give one item a positive `param1` and assert the exact `param1_coverage` entry, for example `{Some(1): Param1Coverage { present: 1, resolved: 0 }}`, so the coverage path is actually exercised.

- **[low] tests/piece_097.rs:361-384 private_catalogue_references_match_preserved_lab_inputs - exact measured counts are pinned, so unrelated changes to the classification rules will break this gate.**
  - Why it cannot catch a regression: this is not a missed bug. It is churn. Adjusting template recovery or the reference-table parsing will move counts such as `race_gender_model_rows`, `unmapped_template_rows` and `param1_conflicts.len()`. Those moves are real behaviour changes, but the assertions cannot tell an intended change from a bug. The test is ignored and has a reason, so it is not a silent skip. The `expect` calls on the env vars panic when the inputs are missing, so it is not a silent pass either.
  - Fix: keep the measured counts in a checked-in snapshot file that is regenerated deliberately, and assert the snapshot matches. Alternatively, keep only the invariants (for example `findings.items == stock.len()` and `findings.model_rows == models.len()`) in code and move the pinned numbers to a data file.
