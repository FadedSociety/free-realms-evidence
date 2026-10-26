<!-- fleet job=testaudit-infer id=item_bar-v1 status=done turns=2 usd=0.0036 tokens(read,write,in,out)=[12860, 16846, 6, 2674] model=claude-haiku-5-5 -->
# tests/item_bar.rs

{"file": "tests/item_bar.rs", "tests": [
{"name": "assigning_an_owned_potion_binds_the_slot_and_renders_all_four_slots", "verdict": "keep", "covered_by": null, "reason": "Only file driving 42/6 slot binding and four-slot render; no equivalent elsewhere in the similar files."},
{"name": "a_refused_assignment_changes_nothing_and_snaps_the_bar_back", "verdict": "keep", "covered_by": null, "reason": "Refusal check (no stack, unknown definition, non-consumable, out-of-range slot) with a live-stack canary; refusal behaviour, keep."},
{"name": "assigning_zero_clears_and_clearing_an_empty_slot_is_a_no_op", "verdict": "keep", "covered_by": null, "reason": "Clear/no-op behaviour specific to the item bar; not found in other test files."},
{"name": "assigning_by_record_resolves_definition_and_tint_to_an_owned_stack", "verdict": "keep", "covered_by": null, "reason": "Distinct 42/8 record route; no other file exercises it."},
{"name": "malformed_and_foreign_messages_are_not_taken", "verdict": "keep", "covered_by": null, "reason": "Hostile/foreign-route refusal test; security-style check, keep."},
{"name": "using_a_bar_slot_spends_exactly_one_potion_and_asks_for_the_heal", "verdict": "keep", "covered_by": null, "reason": "Core use path (one potion spent, heal percent, slot update); not duplicated in the similar files."},
{"name": "the_recast_window_blocks_replays_and_ends_on_its_boundary", "verdict": "keep", "covered_by": null, "reason": "Cooldown boundary behaviour specific to the bar; keep."},
{"name": "the_last_potion_unbinds_its_slot", "verdict": "keep", "covered_by": null, "reason": "Unique state transition; keep."},
{"name": "bar_use_refusals_spend_nothing_and_each_has_a_canary", "verdict": "keep", "covered_by": null, "reason": "Refusal with canaries, explicitly a refusal check; keep."},
{"name": "the_check_then_use_flow_confirms_once_and_only_for_the_checked_instance", "verdict": "keep", "covered_by": null, "reason": "Confirmation flow for 42/16 to 38/30; unique to this file."},
{"name": "the_check_refuses_with_a_chat_line_not_the_chest_dialog", "verdict": "keep", "covered_by": null, "reason": "Refusal shape pin; no equivalent found in the similar files."},
{"name": "the_bar_persists_and_runtime_state_does_not", "verdict": "keep", "covered_by": null, "reason": "Persistence check; never removable without an equal test."},
{"name": "a_tampered_saved_bar_is_refused_at_load", "verdict": "keep", "covered_by": null, "reason": "Tamper/security refusal at load; keep."},
{"name": "schema_one_still_loads_the_potion_rule", "verdict": "keep", "covered_by": null, "reason": "Migration/back-compat check for item bar schema 1; roles.rs schema-one test concerns accounts, not this bar."},
{"name": "schema_two_rows_load_within_sanity_bounds", "verdict": "keep", "covered_by": null, "reason": "Schema-two content bounds; keep."},
{"name": "the_shipped_rows_all_fit_the_effect_stack", "verdict": "keep", "covered_by": null, "reason": "Shipped-content check; not clearly covered elsewhere (bandit_hideout_dungeon has a similarly named test but for a different content table)."},
{"name": "a_schema_two_aura_row_is_used_and_sweeps_its_thirty_minute_recast", "verdict": "keep", "covered_by": null, "reason": "Aura effect path unique to this file."},
{"name": "a_transform_row_is_refused_while_a_transform_is_live", "verdict": "keep", "covered_by": null, "reason": "Refusal while transformed; unique, keep."},
{"name": "a_refused_check_keeps_the_pending_confirmation", "verdict": "keep", "covered_by": null, "reason": "Refusal preserving state; keep."},
{"name": "a_heal_row_needs_health_tracking_and_a_visual_row_does_not", "verdict": "keep", "covered_by": null, "reason": "Capability gating for heal vs visual rows; keep."},
{"name": "a_rental_item_with_a_row_stays_unusable", "verdict": "keep", "covered_by": null, "reason": "Rental refusal; keep."},
{"name": "hostile_bytes_never_panic", "verdict": "keep", "covered_by": null, "reason": "Hostile-input no-panic canary; trade_unavailable has a similar test but for a different module, so not a duplicate."}
],
"whole_file_removable": false, "confidence": 0.6, "notes": "Only a partial read was done (lines 300-420 of a file the pack lists as 1211 lines; the tool reports 768), so verdicts rest on test names, the excerpt and grep. Similar-file list contained no other item_bar test file; boombox_catalogue.rs and job_trainers.rs use the item_bar module but were not compared in depth. Nothing was judged removable; a deeper comparison with boombox_catalogue.rs (ItemBar::load, use_wire) could surface superseded use-path tests."}
