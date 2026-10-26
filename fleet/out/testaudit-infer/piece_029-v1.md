<!-- fleet job=testaudit-infer id=piece_029-v1 status=done turns=2 usd=0.0037 tokens(read,write,in,out)=[12322, 20068, 6, 2201] model=claude-haiku-5-5 -->
# tests/piece_029.rs

{"file": "tests/piece_029.rs", "tests": [
{"name": "recovered_action_names_and_interaction_ids_match_the_client", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered interaction ids, action vocabulary and NO_FIXTURE_SELECTED sentinel; no other test file drives piece_029 (only the Python mirror tests/pieces/test_piece_029.py exists, which is a different harness)."},
{"name": "radial_interaction_maps_to_the_recovered_house_call", "verdict": "keep", "covered_by": null, "reason": "Sole check of the radial-id to House.* Lua call mapping in the Rust module; not covered elsewhere."},
{"name": "guid_selection_resolves_the_addressed_instance", "verdict": "keep", "covered_by": null, "reason": "Only check that a GUID addresses the correct instance among identical items; targeting correctness."},
{"name": "definition_only_selection_refuses_an_ambiguous_instance", "verdict": "keep", "covered_by": null, "reason": "Refusal check (ambiguous selection must not pick the wrong instance); security/refusal, no equivalent elsewhere."},
{"name": "definition_only_selection_resolves_a_unique_instance", "verdict": "keep", "covered_by": null, "reason": "Positive counterpart to the ambiguity refusal; the only check of unique-definition resolution."},
{"name": "a_fixture_from_another_lot_is_not_selectable", "verdict": "keep", "covered_by": null, "reason": "Cross-lot isolation refusal; not covered by any other file's tests for this module."},
{"name": "duplicate_guid_in_the_same_lot_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal on duplicate guid; security-relevant input check, keep conservatively."},
{"name": "no_selection_refuses_the_interaction", "verdict": "keep", "covered_by": null, "reason": "Refusal when SelectedFixture is -1; sole coverage of that path."},
{"name": "unknown_interaction_ids_are_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal over out-of-range ids; keep."},
{"name": "a_fixture_whose_definition_never_arrived_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal when definition row is missing; sole check of UnknownDefinition."},
{"name": "interaction_without_the_declared_action_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal for undeclared action plus gated-action positive case; unique to this module."},
{"name": "farming_area_gates_every_interaction_on_move_fixture", "verdict": "keep", "covered_by": null, "reason": "Pins the farming-area gate rule; no other coverage of ClientArea::Farming gating for piece_029."},
{"name": "unknown_requirement_is_refused_instead_of_allowed", "verdict": "keep", "covered_by": null, "reason": "Fail-closed refusal on unknown RequirementId; security check, keep."},
{"name": "members_only_fixture_offers_only_removal_to_a_guest", "verdict": "keep", "covered_by": null, "reason": "Membership refusal plus guest pickup allowance; sole check of this rule."},
{"name": "read_only_lot_requires_edit_permission", "verdict": "keep", "covered_by": null, "reason": "Permission refusal for read-only viewers; keep."},
{"name": "plans_are_pure_and_repeatable", "verdict": "keep", "covered_by": null, "reason": "Purity/no-mutation canary for the planner; not duplicated elsewhere."},
{"name": "private_decoration_vocabulary_matches_shipped_client_files", "verdict": "keep", "covered_by": null, "reason": "Ignored canary that re-derives vocabulary from shipped client files; only runs with env vars, cannot be replaced by a non-ignored test; keep."}
],
"whole_file_removable": false, "confidence": 0.8, "notes": "The file tests a standalone module (src/restoration/piece_029.rs) pulled in via #[path]; no other Rust test file exercises it, and the similar files (housing_service, housing, piece_030, kart_service, npc_interaction) test different modules. The Python mirror tests/pieces/test_piece_029.py overlaps conceptually but is a different harness, not a Rust test, so it does not count as a superseding check. Only the 'housing'/'housing_service' neighbours touch fixture placement and were not compared line-by-line since no same-path drive was found. Verdicts are all keep; the file is a candidate for a later consolidation only after the lead registers the module in src/lib.rs, at which point overlap with housing_service could be re-checked."}
