<!-- fleet job=testaudit-infer id=piece_076-v1 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[9928, 16166, 6, 1672] model=claude-haiku-5-5 -->
# tests/piece_076.rs

{"file": "tests/piece_076.rs",
 "tests": [
  {"name": "zone_record_and_area_table_keep_the_recovered_values", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered zone record and the nine REGION_AREAS; the module is #[path]-included here and no other test file references src/restoration/piece_076.rs."},
  {"name": "region_membership_matches_the_recovered_placements", "verdict": "keep", "covered_by": null, "reason": "Sole check of regions_at against recovered coordinates, including the no-region (outside-all-areas) case."},
  {"name": "guid_convention_and_capture_guids_are_classified_against_the_npc_table", "verdict": "keep", "covered_by": null, "reason": "Sole check of classify_guid; includes the Unexpected rejection path (33081, 1202) which is a refusal-style check."},
  {"name": "terrain_bound_interaction_npcs_resolve_to_a_terrain_object_instead_of_a_model", "verdict": "keep", "covered_by": null, "reason": "Sole check of asset_binding, including the unbound-row None case."},
  {"name": "audit_reproduces_the_recovered_identifier_and_region_counts", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end reproduction of the recovered counts and region tallies from the audit; not reproduced elsewhere."},
  {"name": "audit_reports_unresolved_assets_as_gaps_not_success", "verdict": "keep", "covered_by": null, "reason": "Gap-not-success check (unresolved models must surface as findings); a refusal-style canary with no equal test elsewhere."},
  {"name": "audit_rejects_duplicate_guids_unknown_rows_and_unbound_rows", "verdict": "keep", "covered_by": null, "reason": "Hostile-input rejection test covering duplicate GUIDs, unknown npc rows and unbound rows; security/refusal check, must be kept."},
  {"name": "guid_aliasing_another_recovered_npc_is_a_contradiction", "verdict": "keep", "covered_by": null, "reason": "Refusal check that a GUID aliasing another NPC is a contradiction; not covered elsewhere."},
  {"name": "cross_revision_comparison_keeps_one_model_per_recovered_npc_id", "verdict": "keep", "covered_by": null, "reason": "Sole check of model_conflicts and the cross-revision constants; the Legacy revision is not compared in any other Rust test."}
 ],
 "whole_file_removable": false,
 "confidence": 0.9,
 "notes": "The five similar files (piece_032, housing, piece_072, piece_060, piece_059) cover different modules and domains; none drives the piece_076 module, so no superseded or duplicate matches were found. The only other references to piece_076 are the Python checker tests (tests/pieces/test_piece_076.py), which exercise a different implementation and are not Rust test duplicates. No obsolete behaviour is evident: the work item and research note still describe these nine tests as the acceptance set. Caveat: the pack's excerpt was cut mid-test, so I read the full file directly (371 lines) before classifying."}
