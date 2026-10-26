<!-- fleet job=testaudit-infer id=piece_028-v1 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[11719, 20301, 6, 1760] model=claude-haiku-5-5 -->
# tests/piece_028.rs

{"file": "tests/piece_028.rs",
 "tests": [
  {"name": "current_snapshot_restores_every_lot_and_fixture", "verdict": "keep", "covered_by": null, "reason": "Only round-trip check of the current-schema migrate/restore path for owned lots and fixtures; no similar file exercises the housing save migration (housing_service.rs tests runtime service state, not migrate())."},
  {"name": "legacy_versionless_snapshot_migrates_and_keeps_every_owned_lot_and_fixture", "verdict": "keep", "covered_by": null, "reason": "Legacy migration with source-not-rewritten and no-staging-file assertions; unique to this module and guards persistence."},
  {"name": "explicit_version_zero_migrates_to_the_same_bytes_as_the_versionless_form", "verdict": "keep", "covered_by": null, "reason": "Pins equivalence of explicit and implicit legacy version; distinct assertion (byte equality) not made elsewhere."},
  {"name": "legacy_build_areas_come_from_the_recovered_property_rows", "verdict": "keep", "covered_by": null, "reason": "Checks build areas filled from recovered Houses.json rows; unique data-provenance check."},
  {"name": "legacy_lot_without_a_recovered_property_row_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check: unknown property refused and live lot left intact."},
  {"name": "legacy_property_row_that_disagrees_with_the_lot_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check on zone/name mismatch with exact error fields."},
  {"name": "legacy_declared_count_is_repaired_from_the_fixture_list", "verdict": "keep", "covered_by": null, "reason": "Repair behaviour for stale derived count; not covered by another file."},
  {"name": "future_schema_version_is_refused_and_the_source_is_never_rewritten", "verdict": "keep", "covered_by": null, "reason": "Refusal and no-rewrite check for newer documents, plus u64::MAX edge; security-relevant, keep."},
  {"name": "malformed_and_non_document_inputs_are_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal coverage for the migrator; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Partial read: lines 1-229 (pack excerpt) and 230-529 were reviewed; lines 530-714 (current_documents_missing_the_added_fields..., a_document_the_real_loader_refuses..., duplicate_property_rows..., oversized_documents..., evidence_export...) were not read and are not individually classified; by name they are refusal/persistence/canary tests and default to keep. The similar-file list (housing_service, kart_service, coin_store_siblings, piece_056, piece_021) tests runtime services and other migrations, and no test name there duplicates the save-migration path. Searching the tests tree for schema_version/build_areas found no other migration test over the housing snapshot. Nothing removable identified."}
