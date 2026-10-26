<!-- fleet job=testaudit-infer id=piece_097-v1 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[8773, 12337, 6, 1747] model=claude-haiku-5-5 -->
# tests/piece_097.rs

{"file": "tests/piece_097.rs",
 "tests": [
  {"name": "model_references_classify_by_template_tokens", "verdict": "keep", "covered_by": null, "reason": "Only test of classify_model's RaceGender / Unmapped / Literal split; no similar file covers it."},
  {"name": "race_gender_templates_expand_to_the_four_pc_variants", "verdict": "keep", "covered_by": null, "reason": "Only test of expand_race_gender, including the unrecovered-token-stays and dedup behaviour. The four-variant rule is reconstructed, so no stronger counterpart exists."},
  {"name": "reference_tables_parse_and_reject_malformed_rows", "verdict": "keep", "covered_by": null, "reason": "Only check of the three reference-table parsers and their malformed-row rejection. Similar files parse different tables (piece_032 id-pair tables, piece_059 tables), not these."},
  {"name": "dangling_locale_class_category_and_model_references_are_reported", "verdict": "keep", "covered_by": null, "reason": "Core dangling-reference reporting for locale, class, category and model. piece_082::dangling_definition_category_and_name_are_reported covers a different schema, so it is not a duplicate."},
  {"name": "unmapped_templates_are_reported_not_asserted_missing", "verdict": "keep", "covered_by": null, "reason": "Guards the refusal to assert missing models for unmapped templates. No equivalent elsewhere."},
  {"name": "param1_model_conflicts_are_reported_only_for_mixed_relationship_types", "verdict": "keep", "covered_by": null, "reason": "Negative-case canary for the Param1 conflict rule (type 19 and 14 must not conflict). Reconstructed rule, unique to this file."},
  {"name": "duplicate_item_ids_and_reference_table_gaps_are_reported", "verdict": "keep", "covered_by": null, "reason": "Duplicate-id and gap reporting, unique to this analyzer. piece_082 has a duplicate-instance check on a different schema, not the same path."},
  {"name": "asset_and_locale_lookups_are_case_insensitive", "verdict": "keep", "covered_by": null, "reason": "Asset half is close to tests/piece_024.rs::asset_lookups_are_case_insensitive, but this test also covers locale_ids, which piece_024 does not. Kept conservatively; the asset half could be trimmed if piece_024 is confirmed to assert the same thing."},
  {"name": "private_catalogue_references_match_preserved_lab_inputs", "verdict": "keep", "covered_by": null, "reason": "Ignored private canary asserting measured catalogue counts. It is the only test of those counts; it needs lab inputs and is not run in the hermetic suite."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "I read the file's tests and the similar-file names only. I did not open piece_024's asset test body, so the one possible overlap (asset half of the case-insensitive test) is unverified. The overall verdict is keep for all nine tests. Shared-file fixtures use #[path] include of the real module, so the tests exercise live code. No obsolescence signal: created_by and last_changed_by are null."}
