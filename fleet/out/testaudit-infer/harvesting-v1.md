<!-- fleet job=testaudit-infer id=harvesting-v1 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[11206, 19451, 6, 2329] model=claude-haiku-5-5 -->
# tests/harvesting.rs

{"file": "tests/harvesting.rs",
 "tests": [
  {"name": "original_spawn_row_roundtrips_with_original_column_order", "verdict": "keep", "covered_by": null, "reason": "Golden 14-column spawn row parse and roundtrip; no other test in the repo pins SpawnRow column order."},
  {"name": "original_level_row_roundtrips_with_original_column_order", "verdict": "keep", "covered_by": null, "reason": "Golden 18-column LevelRow parse and roundtrip; unique to this file."},
  {"name": "original_progression_and_timer_rows_roundtrip", "verdict": "keep", "covered_by": null, "reason": "Pins ProgressionRow columns and TimerRow /10 scaling; not found elsewhere."},
  {"name": "original_grid_templates_parse_rows_of_codes", "verdict": "keep", "covered_by": null, "reason": "Grid template parser behaviour; no equivalent in the similar files."},
  {"name": "schema_parsers_reject_wrong_column_counts", "verdict": "keep", "covered_by": null, "reason": "Hostile-input rejection check for the schema parsers; keep as refusal check."},
  {"name": "recovered_produce_sets_match_original_locale_descriptions", "verdict": "keep", "covered_by": null, "reason": "Pins region produce sets against locale evidence; unique data canary."},
  {"name": "recovered_item_ids_match_pinned_client_definitions", "verdict": "keep", "covered_by": null, "reason": "Pins produce NameId/ItemId/icon mapping against pinned client definitions; unique."},
  {"name": "score_formulas_match_original_gamedata_as", "verdict": "keep", "covered_by": null, "reason": "Scoring formula pins for the harvesting module; no duplicate found in the similar files (mining/forging test their own formulas)."},
  {"name": "result_requires_every_quota_goal_and_counts_bundles", "verdict": "keep", "covered_by": null, "reason": "Completion rule (every goal must meet quota) is a refusal-style check on evaluate()."},
  {"name": "goal_progress_reports_clusters_like_the_original_bins", "verdict": "keep", "covered_by": null, "reason": "Unique GoalProgress cluster/complete behaviour."},
  {"name": "observed_diamond_shape_and_engine_rectangle_stay_separate", "verdict": "keep", "covered_by": null, "reason": "Pins the observed diamond artifact and the padded engine rectangle; unique geometry canary."},
  {"name": "recovered_constants_match_the_original_movie_and_inventory", "verdict": "keep", "covered_by": null, "reason": "Constants pin against original movie/inventory; not duplicated."},
  {"name": "content_json_matches_the_frozen_type8_contract", "verdict": "keep", "covered_by": null, "reason": "Contract shape check for the emitted JSON; the wrapper-field half overlaps only loosely with bundle_activity_content.rs, which loads the file through Type8Engine rather than checking fields, so it is not a strict duplicate."},
  {"name": "content_guards_reject_unknown_or_mutated_configuration", "verdict": "keep", "covered_by": null, "reason": "Refusal/tamper checks (bad game_id, shape, outputs, goals, movie, preload path traversal, non-zero border). Security-relevant; no equally strong test elsewhere named."},
  {"name": "generic_and_unnamed_entries_refuse_an_unsupported_launch", "verdict": "keep", "covered_by": null, "reason": "Refusal check for unsupported gap profiles; must keep."},
  {"name": "emitted_spec_is_consumable_by_a_type8_engine_loader", "verdict": "keep", "covered_by": null, "reason": "Mirror-struct contract check. Its name suggests a loader test, but it does not drive the real loader; bundle_activity_content.rs does load the real engine, so this is partly overlapping but it also pins many field values. Kept conservatively."},
  {"name": "write_content_lands_in_the_shared_content_directory", "verdict": "keep", "covered_by": null, "reason": "Filesystem write-path check for CONTENT_FILE in a temp dir; persistence-style check, keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Pure-module golden/pin file with almost no overlap in the similar files (kart_service, piece_008, forging, mining, piece_032 test other modules). The closest overlap is bundle_activity_content.rs (loads harvesting.json through Type8Engine and validate_content) and app_fuzz.rs (harvesting content in the gateway); those cover integration, not the pinned values here. Candidate for trimming only if the team wants to drop emitted_spec_is_consumable_by_a_type8_engine_loader in favour of bundle_activity_content.rs; I did not read bundle_activity_content.rs in full, so that is unverified. Nothing removed."}
