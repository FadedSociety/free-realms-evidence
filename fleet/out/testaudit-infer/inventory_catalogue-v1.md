<!-- fleet job=testaudit-infer id=inventory_catalogue-v1 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[24082, 15081, 8, 2243] model=claude-haiku-5-5 -->
# tests/inventory_catalogue.rs

{"file": "tests/inventory_catalogue.rs",
 "tests": [
  {"name": "generated_grant_sends_batch_first_and_reload_includes_owned_rows_only", "verdict": "keep", "covered_by": null, "reason": "Only test covering a generated-only item-catalogue.json definition being granted, batch-first reply ordering, and reload of owned rows. Nothing in tests/inventory.rs grants a generated-only row."},
  {"name": "captured_rows_win_and_optional_catalogue_fails_closed", "verdict": "keep", "covered_by": null, "reason": "Fail-closed refusal checks for the optional item-catalogue.json (duplicate generated IDs, bad sha256, wrong schema_version, trailing bytes) and captured-row precedence. tests/inventory.rs::identical_catalog_duplicates_are_allowed_but_conflicts_reject covers a different file (content duplicates), so it does not supersede these."},
  {"name": "definition_requests_reject_malformed_and_oversized_input_without_mutating_state", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input test: every truncation, bad lengths, concatenated requests, oversized packet, and a state-unchanged assertion. tests/inventory.rs::definition_request_is_bounded_and_returns_verified_definition overlaps only the length 1/-1 and unknown-ID cases, and is much thinner, so this test is not a duplicate."},
  {"name": "catalogue_file_row_count_and_row_size_have_independent_limits", "verdict": "keep", "covered_by": null, "reason": "Resource-limit refusal checks (hex size, row limit, byte limit, 128 MiB file cap) that no other visible test drives."},
  {"name": "private_startup_measurement", "verdict": "keep", "covered_by": null, "reason": "#[ignore]d and env-gated (OSFR_ITEM_CATALOGUE); not part of the default suite run. It is a startup measurement and residency canary, which must be kept."},
  {"name": "private_w84_rows_grant_and_reply_byte_exactly", "verdict": "keep", "covered_by": null, "reason": "#[ignore]d and env-gated private byte-exact gate over 58,835 rows; the only exact-bytes check against the W84 output. It is not run by default, so it costs nothing on merge."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Every test is either a refusal/hostile-input check, a unique limit check, or an env-gated ignored private gate. Nothing is clearly superseded or duplicated. Closest overlap is tests/inventory.rs (definition_request_is_bounded_and_returns_verified_definition, identical_catalog_duplicates_are_allowed_but_conflicts_reject), but those exercise different files or are thinner. I did not read the other similar files (coin_store_siblings, housing_service, activity_portal, piece_056) in depth, so the verdicts rest on the inventory.rs comparison alone. Confidence is moderate for that reason."}
