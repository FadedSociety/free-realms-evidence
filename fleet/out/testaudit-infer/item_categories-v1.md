<!-- fleet job=testaudit-infer id=item_categories-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7131, 14488, 6, 1371] model=claude-haiku-5-5 -->
# tests/item_categories.rs

{"file": "tests/item_categories.rs",
 "tests": [
  {"name": "dictionary_keys_values_booleans_and_group_order_match_evidenced_layout", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the byte layout of the category initialization packet from a hand-built fixture (header, two category rows, three group rows with the group8/group44 ordering). No similar test in the pack covers ItemCategories; inventory.rs and kart_racing.rs test other packets. Also checks clone() yields the same bytes."},
  {"name": "conflicting_duplicate_or_invalid_rows_and_changed_proof_reject", "verdict": "keep", "covered_by": null, "reason": "Refusal test: duplicate category id, dangling group category_id, negative display, zero group id, wrong packet_sha256, wrong schema_version, empty categories. Hostile/invalid input; no equivalent elsewhere in the pack."},
  {"name": "oversized_and_malformed_private_content_reject", "verdict": "keep", "covered_by": null, "reason": "Refusal test for the 256 KiB content cap (MAX_CONTENT in src/item_categories.rs) and invalid JSON. Security/size bound, not duplicated in the pack (boombox_catalogue.rs has an analogous size test for a different module, not the same path)."},
  {"name": "private_community_serializer_packet_matches_exactly", "verdict": "keep", "covered_by": null, "reason": "Ignored canary that compares against the private unmodified C# serializer output and checks the 2675-byte length. It only runs with private env vars. Similar in spirit to inventory.rs::private_catalog_matches_compiled_original_community_serializer but for a different packet; not a duplicate."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All four tests are the only checks for the ItemCategories module as far as the pack shows. The ignored private test is a canary and must stay. Minor issues only: the println in the last test has a typo ('categories and74 group associations'), and the 98-length assertion in test 1 is a fixed size check that would need updating if the fixture changes. Neither justifies removal. Notes in notes/Autopilot/F188.md and F211.md reference this file as holding fixtures, which is consistent with it being unique."}
