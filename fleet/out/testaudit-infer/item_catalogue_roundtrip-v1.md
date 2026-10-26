<!-- fleet job=testaudit-infer id=item_catalogue_roundtrip-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[16520, 12190, 8, 1513] model=claude-haiku-5-5 -->
# tests/item_catalogue_roundtrip.rs

{"file": "tests/item_catalogue_roundtrip.rs",
 "tests": [
  {"name": "captured_rows_roundtrip_and_generated_catalogue_use_existing_batch_encoder", "verdict": "keep", "covered_by": null, "reason": "Only test that checks the regenerated roundtrip.json against the private source inventory (per-row id and SHA-256 and hex equality), the 35/37 batch framing with the 1649 unique-id count, and the single-byte mutation canary. tests/inventory_catalogue.rs::private_w84_rows_grant_and_reply_byte_exactly is the closest overlap: it byte-checks each catalogue.json row through Inventory::definition_replies and checks a grant, but it does not validate roundtrip.json or the report-level SHA chain of the roundtrip, and it never exercises the standalone encode_definition_batch_v2 framing. Partial overlap only, so kept. tests/inventory.rs::private_catalog_matches_compiled_original_community_serializer is a further, weaker overlap."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Single #[ignore]d test that only runs when OSFR_ITEM_CATALOGUE points at private W84 output, so it cannot be fully checked in the default run. Its assertions overlap in part with tests/inventory_catalogue.rs::private_w84_rows_grant_and_reply_byte_exactly (same env var, same catalogue.json rows), but the roundtrip.json regeneration check, batch framing and mutation canary are not replicated elsewhere. Consider merging into inventory_catalogue.rs as a later cleanup, not a removal. No created_by or last_changed_by task is recorded for this file."}
