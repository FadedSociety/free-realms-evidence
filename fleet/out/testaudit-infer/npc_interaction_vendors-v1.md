<!-- fleet job=testaudit-infer id=npc_interaction_vendors-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[8699, 10484, 6, 1296] model=claude-haiku-5-5 -->
# tests/npc_interaction_vendors.rs

{"file": "tests/npc_interaction_vendors.rs",
 "tests": [
  {"name": "vendor_stock_is_loadable_and_supported_by_content_evidence", "verdict": "keep", "covered_by": null, "reason": "Single long audit test. It checks the production NPC loader on the shipped content, vendor role authorization, unique vendor and item IDs, client source tags, store price matching, runtime_eligible and item_ids consistency, unresolved-vendor reasons, and coverage counters. vendor_stock_coverage.rs overlaps on grantable stock and no-fuzzy-substitute themes, but none of its tests cross-checks the vendors.json runtime item_ids against stores.json prices and the NPC role table. Not clearly covered elsewhere, so kept under the conservative rule."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The file has one test that is really a data-consistency audit. It reads external inputs: the startup snapshot under ../../../lab/content and the inventory content under ../../../lab/reports/round70-native-20261016T061000Z/content, or the OSFR_VENDOR_CONTENT env var. It will fail if those paths are absent, so it is environment-sensitive. It hard-codes 192 unresolved vendors, which will need updating whenever the content regenerates. Partial overlap with tests/vendor_stock_coverage.rs (the_selected_hub_vendors_have_nonempty_grantable_stock, at_least_twenty_more_vendor_rows_are_fully_grantable, no_vendor_stock_row_uses_a_fuzzy_or_family_substitute) was noted but I did not read those bodies in full, so I did not mark any part as superseded. Worth a follow-up comparison of assertions if the suite time matters."}
