<!-- fleet job=testaudit-infer id=piece_051-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[28904, 19231, 8, 1866] model=claude-haiku-5-5 -->
# tests/piece_051.rs

{"file": "tests/piece_051.rs",
 "tests": [
  {"name": "models_schema_matches_the_recovered_original_header", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 17-column Models.txt schema and the 5 definition fields of piece_051; no other test drives this module (the only file that includes src/restoration/piece_051.rs is this one)."},
  {"name": "models_parser_binds_real_rows_and_rejects_malformed_input", "verdict": "keep", "covered_by": null, "reason": "Only parser test; includes a malformed-row refusal (MalformedRow line 2), which is a refusal check."},
  {"name": "combat_descriptor_is_an_exact_original_enemy_marker", "verdict": "keep", "covered_by": null, "reason": "Only test of the exact-match enemy marker and the 5 flagged rows; includes negative cases (near-miss descriptors) that guard against over-matching."},
  {"name": "applied_enemies_match_original_models_and_locale", "verdict": "keep", "covered_by": null, "reason": "Only test that validates all 7 applied enemies against the model and locale tables and checks the Hooligan Wolf binding."},
  {"name": "unbound_definition_ids_are_reported_as_local_only", "verdict": "keep", "covered_by": null, "reason": "Pins which applied definition ids are local-only versus community-bound; no equivalent elsewhere."},
  {"name": "actor_validation_rejects_model_and_name_drift", "verdict": "keep", "covered_by": null, "reason": "Refusal test: wrong model file, wrong name, unknown name/model and missing model binding are all rejected. Security-style refusal check, not duplicated."},
  {"name": "name_lookup_tolerates_only_the_recovered_trailing_space", "verdict": "keep", "covered_by": null, "reason": "Pins a narrow tolerance (trailing space only) and refuses a real name drift; refusal check, unique to this file."},
  {"name": "missing_bindings_are_explicit_about_what_was_never_recovered", "verdict": "keep", "covered_by": null, "reason": "Asserts the explicit list of unrecovered bindings (skills, stats, faction, definition id). Weak, prose-matching assertions, but it is the only check of that catalogue and is a stated evidence-boundary guard; kept conservatively."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The similar files in the pack (piece_048, piece_032, npc_interaction, housing_service, piece_056) cover different pieces and different code paths; none includes src/restoration/piece_051.rs or asserts on Models.txt parsing or enemy validation, so no superseded or duplicate verdicts apply. The file has no created_by/last_changed_by metadata and no later task replaced its behaviour, so nothing is obsolete. The excerpt was truncated mid-test; I read lines 236-294 to classify the remaining tests. Weakest candidate is missing_bindings_are_explicit_about_what_was_never_recovered (substring checks on prose), but it is kept under the conservative rule."}
