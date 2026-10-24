<!-- fleet job=test-audit id=tests-piece-024-rs-L1 status=done turns=4 usd=0.0049 tokens(read,write,in,out)=[19240, 11711, 10, 6551] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_024.rs lines 1-216 of 216

Window: `prototype/osfr-tools/tests/piece_024.rs` lines 1-216. I read the window in full and the code under test in `src/restoration/piece_024.rs` (lines 1-280). Most tests in the window are sound. I checked the fixture arithmetic and the `analyze` paths and found no tautologies, no silent early returns, and no skips without a reason. The `#[ignore]` test has a reason and panics on missing env vars rather than passing. Three findings:

- **[medium] prototype/osfr-tools/tests/piece_024.rs:110 icon_relationship_is_an_exact_model_stem_prefix - the name claims an exact stem match, but the body only checks the string returned by `icon_asset_prefix`, never the matching that `analyze` performs.**
  - Why it cannot catch a regression: `analyze` matches icons with `has_prefixed_name` (src/restoration/piece_024.rs:237-242), which is a plain `starts_with(prefix)`. A furniture model `hsg_chair_01.adr` therefore counts as having an icon when the pack only holds `icon_item_hsg_chair_010_x_64.dds`. That over-match is present today, and no test in the window exercises it. The only icon-positive case in the window is the `hsg_chair_lodge_01` icon, which has no sibling stem. A change that makes the matching exact would not be caught, and neither would the current over-match.
  - Fix: add a case to this test or a new one. Use `analyze` with stock model `hsg_chair_01.adr` and assets `{"icon_item_hsg_chair_010_x_64.dds"}`, and assert `missing_icon_assets == vec![id]`. Also assert that the exact-stem icon `icon_item_hsg_chair_01_x_64.dds` clears it. Alternatively, rename the test so it no longer claims exactness.

- **[low] prototype/osfr-tools/tests/piece_024.rs:204-215 private_furniture_catalogue_matches_preserved_lab_inputs - `stock_only.len() == 1136` is a second golden number that duplicates the 1167 and 31 counts above it.**
  - Why it is churn-prone: it is only `furniture - reconstructed_furniture` given the other asserts, so a change to any one count will fail several lines at once with no extra information about what changed.
  - Fix: keep the 1167 and 31 golden counts, and replace the 1136 check with `assert_eq!(findings.stock_only.len(), findings.furniture - findings.reconstructed_furniture)`, or drop it.

- **[low] prototype/osfr-tools/tests/piece_024.rs:28-43 row / 119-127 missing_assets_locale_and_icons_are_reported - every fixture furniture row has `description_id: Some(..)`, so the `description_id.is_none_or(..)` branch in `analyze` (src/restoration/piece_024.rs:166) is never exercised with a missing description.**
  - Why it cannot catch a regression: flipping `is_none_or` to `is_some_and`, which would wrongly treat a missing description as missing locale, still passes every test in the window. The test name does not claim this case, so the gap is in coverage rather than the name.
  - Fix: add a stock row with `description_id: None` and a valid `name_id`, and assert it is absent from `missing_locale`.
