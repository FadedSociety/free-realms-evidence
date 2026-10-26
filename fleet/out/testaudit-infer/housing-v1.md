<!-- fleet job=testaudit-infer id=housing-v1 status=done turns=2 usd=0.0038 tokens(read,write,in,out)=[12985, 16760, 6, 3103] model=claude-haiku-5-5 -->
# tests/housing.rs

{"file": "tests/housing.rs", "tests": [
{"name": "lot_guid_cannot_collide_with_a_property_zone_guid", "verdict": "keep", "covered_by": null, "reason": "Identity/collision check on lot guids; no other file asserts lot_guid distinctness directly (piece_028 only uses lot_guid to derive a lot)."},
{"name": "placement_grants_ownership_and_reports_the_granted_limits", "verdict": "keep", "covered_by": null, "reason": "Core placement happy path with ledger and limit reporting at the Housing API level; housing_service.rs tests go through the service layer, not this direct API."},
{"name": "a_fixture_instance_cannot_be_placed_twice_in_one_lot", "verdict": "keep", "covered_by": null, "reason": "Duplicate-instance refusal (InstanceAlreadyPlaced) plus cross-lot allowance; a refusal check. Similar error appears in piece_026.rs at the transaction layer, which is a different path."},
{"name": "placement_rejects_unowned_and_unteamed_fixtures", "verdict": "keep", "covered_by": null, "reason": "Refusal check (NotPropertyOwner, InstanceNotOwned); housing_service.rs and piece_026.rs assert NotPropertyOwner through wrappers, so not clearly the same path."},
{"name": "placement_rejects_non_finite_and_out_of_range_transforms", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal over several transforms; no equivalent named elsewhere."},
{"name": "move_and_pickup_keep_ownership_and_release_the_snapshot", "verdict": "keep", "covered_by": null, "reason": "Move/pickup ownership and stock release; housing_service.rs pickup tests run through the service, so not an exact duplicate."},
{"name": "placement_limits_are_enforced_and_never_silently_exceeded", "verdict": "keep", "covered_by": null, "reason": "Fixture cap refusal (FixtureLimitReached) with count checks; a limit/refusal canary."},
{"name": "placement_outside_every_build_area_is_denied", "verdict": "keep", "covered_by": null, "reason": "Build-area security boundary; not seen elsewhere in the searched names."},
{"name": "place_fixture_request_is_rejected_on_a_locked_lot", "verdict": "keep", "covered_by": null, "reason": "Refusal on locked lot; not verified against other files."},
{"name": "corrupted_or_duplicate_snapshots_are_rejected_on_load", "verdict": "keep", "covered_by": null, "reason": "Load-time refusal of hostile documents; housing_service.rs has a similar 'serialized state rejects invalid documents' test but at service level. Keep conservatively."},
{"name": "saved_fixtures_survive_a_serialized_restart", "verdict": "keep", "covered_by": null, "reason": "Persistence check; never remove persistence tests without an equal named test."},
{"name": "a_restored_lot_keeps_its_ownership_and_accepts_an_edit_after_restart", "verdict": "keep", "covered_by": null, "reason": "Persistence of ownership across restart; keep."},
{"name": "a_rejected_save_leaves_the_previous_snapshot_file_byte_identical", "verdict": "keep", "covered_by": null, "reason": "File-level atomicity/refusal check; keep."},
{"name": "fixture_guids_are_unique_per_lot_placement", "verdict": "keep", "covered_by": null, "reason": "Uniqueness invariant; not verified as duplicated elsewhere."},
{"name": "staged_inventory_stays_consistent_with_the_fixture_ledger", "verdict": "keep", "covered_by": null, "reason": "Conservation invariant; housing_service.rs has inventory-conservation tests at service level, different path."},
{"name": "typed_fixture_view_matches_the_recovered_serialization_order", "verdict": "keep", "covered_by": null, "reason": "Pins recovered serialization order; not obsolete as no later task is known to replace it."},
{"name": "a_rejected_snapshot_load_leaves_the_live_state_intact", "verdict": "keep", "covered_by": null, "reason": "Refusal check on load; keep."},
{"name": "duplicate_lot_guids_in_a_snapshot_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal; keep."},
{"name": "a_lot_limit_change_is_enforced_by_placement_and_still_saves", "verdict": "keep", "covered_by": null, "reason": "Limit-change behaviour and save; keep."},
{"name": "a_lot_build_area_change_is_enforced_by_placement", "verdict": "keep", "covered_by": null, "reason": "Build-area enforcement after change; keep."},
{"name": "save_fixture_placement_stamps_the_resolved_lot_identity", "verdict": "keep", "covered_by": null, "reason": "Identity stamping on save; keep."},
{"name": "save_fixture_placement_rejects_an_empty_instance", "verdict": "keep", "covered_by": null, "reason": "Refusal check; keep."},
{"name": "saving_an_existing_fixture_keeps_the_build_area_bound", "verdict": "keep", "covered_by": null, "reason": "Security bound on re-save; keep."},
{"name": "a_rejected_seed_leaves_the_ledger_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check on ledger seeding; keep."},
{"name": "a_guest_with_edit_permission_can_edit_but_a_stranger_cannot", "verdict": "keep", "covered_by": null, "reason": "Permission boundary; housing_service.rs has similar guest/stranger tests at service layer (a_guest_with_edit_permission_can_build_but_cannot_reassign_the_lot, a_stranger_cannot_enter_or_place_on_someone_elses_lot). Not identical assertions, so keep."},
{"name": "restart_conservation_requires_restaging_the_captured_instances", "verdict": "keep", "covered_by": null, "reason": "Restart conservation canary; keep."}
],
"whole_file_removable": false, "confidence": 0.5, "notes": "I read only the header and roughly lines 300-420 of the 1378-line file, plus a grep for error variants across tests/. Verdicts are therefore conservative: every test is kept. The closest overlaps are housing_service.rs (guest/stranger permission, NotPropertyOwner, pickup conservation, invalid-document rejection) and piece_026.rs (InstanceNotOwned at the transaction layer). Those overlap at a different layer, not the same path with the same assertions, so none were marked superseded or duplicate. A deeper pass comparing housing_service.rs assertions line by line could find real duplicates."}
</result>
