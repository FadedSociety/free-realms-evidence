<!-- fleet job=test-audit id=tests-npc-interaction-vendors-rs-L1 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[9381, 15382, 8, 3652] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_interaction_vendors.rs lines 1-295 of 295

Window reviewed: `prototype/osfr-tools/tests/npc_interaction_vendors.rs` lines 1-295 (whole file). Fixtures exist (`lab/content/startup-snapshot/startup.json` and `lab/reports/round70-native-20261016T061000Z/content` are referenced across the repo), so there is no silent skip. The main checks on `vendors.json` (prices, runtime lists, coverage counts recomputed from items) are not tautological: they compare the generated file against `stores.json`, the NPC roles and the recomputed counts. The findings below are the weak spots.

- **[medium] prototype/osfr-tools/tests/npc_interaction_vendors.rs:241-259 vendor_stock_is_loadable_and_supported_by_content_evidence - `vendors_with_grantable_stock` is computed over the unresolved vendors but is only printed in the coverage line at 289, never asserted.**
  - Why it cannot catch a regression: if `inventory.has_definition` stopped mattering, or every unresolved vendor's `item_ids` were emptied or pointed at undefined items, the counter would drop to 0 and the test would still pass. The "grantable stock" half of the name is never checked.
  - Fix: assert the value directly, e.g. `assert_eq!(vendors_with_grantable_stock, <expected>)` or, better, assert that each unresolved vendor with runtime `item_ids` has every id defined (`assert!(item_ids.iter().all(...))` inside the loop, with the loop's `continue` for missing vendors replaced by an explicit expectation).

- **[low] prototype/osfr-tools/tests/npc_interaction_vendors.rs:228 vendor_stock_is_loadable_and_supported_by_content_evidence - `assert_eq!(unresolved_keys.len(), 192)` pins an exact count of unrelated records.**
  - Why it cannot catch a regression: it is not a check on vendor stock. Any content change that adds or removes an unresolved vendor fails here even when the stock logic is correct, which causes churn rather than catching a bug.
  - Fix: drop the literal, or check that the count equals the number of `unresolved` rows already in the file and that the unresolved set is disjoint from `vendor_keys` with matching `coverage` fields.

- **[low] prototype/osfr-tools/tests/npc_interaction_vendors.rs:145-147 vendor_stock_is_loadable_and_supported_by_content_evidence - `stock_source.is_object()`, `name_id.as_i64().is_some()` and `english_text.as_str().is_some()` only check that a field has a type, not that it carries evidence.**
  - Why it cannot catch a regression: a `stock_source` of `{}`, a `name_id` of any integer, or an empty `english_text` string would pass, so a provenance regression that blanks the evidence still passes.
  - Fix: assert non-empty content, e.g. `!english_text.trim().is_empty()`, and that `stock_source` contains the expected source key (for example a `source` field that names the vendor's NPC file, as F178 requires for `vendors_unresolved.json`).</result>
