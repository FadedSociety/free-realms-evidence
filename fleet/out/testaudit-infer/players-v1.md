<!-- fleet job=testaudit-infer id=players-v1 status=done turns=4 usd=0.0053 tokens(read,write,in,out)=[53279, 22836, 10, 3772] model=claude-haiku-5-5 -->
# tests/players.rs

{"file": "tests/players.rs",
 "tests": [
  {"name": "two_sessions_spawn_move_and_disconnect_with_exact_wire_bytes", "verdict": "keep", "covered_by": null, "reason": "End-to-end spawn/move/despawn with exact wire bytes at registry level; no other file drives PlayerRegistry this way (similar files are trade/housing/kart/npc, different domains)."},
  {"name": "contains_tracks_the_live_registry_membership", "verdict": "keep", "covered_by": null, "reason": "Small membership check, not clearly covered elsewhere; cheap."},
  {"name": "a_live_presentation_change_reaches_a_later_viewer", "verdict": "keep", "covered_by": null, "reason": "Refusal check (snapshot bound to another character, unknown session) and no-change-on-refusal; must stay."},
  {"name": "three_sessions_receive_each_others_spawns_moves_and_despawns", "verdict": "keep", "covered_by": null, "reason": "Multi-viewer fan-out with exact bytes; distinct from the two-session test (third joiner receives backlog)."},
  {"name": "different_zone_instances_have_no_visibility", "verdict": "keep", "covered_by": null, "reason": "Isolation check across zone instances; security-like boundary, not duplicated."},
  {"name": "zone_change_despawns_old_view_and_spawns_new_view", "verdict": "keep", "covered_by": null, "reason": "Unique zone-transition despawn/spawn ordering."},
  {"name": "duplicate_account_or_character_guid_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check on duplicate identity; must stay."},
  {"name": "radius_boundary_is_inclusive_and_one_step_outside_is_hidden", "verdict": "keep", "covered_by": null, "reason": "Boundary-exact interest check; unique."},
  {"name": "visible_count_selects_nearest_then_session_id", "verdict": "keep", "covered_by": null, "reason": "Selection-policy check (max visible count, tie-break); unique."},
  {"name": "add_pc_matches_the_research_oracle_schema_byte_for_byte", "verdict": "keep", "covered_by": null, "reason": "Byte-level schema oracle against research layout; canary."},
  {"name": "a_temporary_model_is_the_add_pc_field_and_zero_without_one", "verdict": "keep", "covered_by": null, "reason": "Field-offset check for temporary model; not covered by the oracle test's default presentation alone."},
  {"name": "a_boombox_transform_overrides_the_consumable_visual_in_add_pc", "verdict": "keep", "covered_by": null, "reason": "Named in pack but not present in the repo copy of tests/players.rs (746-line file, no match for the name). Could not verify; unverified, kept by default."},
  {"name": "add_pc_direction_matches_native_yaw_for_cardinal_headings", "verdict": "keep", "covered_by": null, "reason": "Heading/yaw conversion for cardinal angles; unique in this file."},
  {"name": "state_only_changes_relay_both_opaque_bytes_to_other_viewers", "verdict": "keep", "covered_by": null, "reason": "Relays opaque state bytes and checks no echo to sender and replay-empty behaviour; unique."},
  {"name": "oversized_and_invalid_presentations_are_rejected_without_joining", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal set; must stay."},
  {"name": "jump_relay_window_is_per_session_and_clears_on_leave", "verdict": "keep", "covered_by": null, "reason": "Doc says T266 retired the server-side window; test pins the per-session view clearing on leave and is explicitly marked protected-pass by the lead. Keep."},
  {"name": "a_late_viewer_gets_the_temporary_model_scale_and_auras_in_order", "verdict": "keep", "covered_by": null, "reason": "Named in pack, absent from repo copy; unverified. Ordered visual replay is a canary-like check; kept."},
  {"name": "a_plain_players_add_pc_bytes_are_unchanged", "verdict": "keep", "covered_by": null, "reason": "Byte-identity regression against pre-change capture; absent from repo copy, unverified; kept."},
  {"name": "a_snapshot_refresh_sends_no_visuals_to_a_current_viewer", "verdict": "keep", "covered_by": null, "reason": "Absent from repo copy, unverified; negative check (nothing queued) kept."},
  {"name": "an_expired_visual_clears_the_late_viewers_snapshot", "verdict": "keep", "covered_by": null, "reason": "Absent from repo copy, unverified; expiry behaviour kept."},
  {"name": "a_refused_visual_snapshot_leaves_the_live_presentation_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check; must stay. Absent from repo copy, unverified."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "No similar file tests PlayerRegistry directly; the five neighbours (player_trade, housing_service, kart_service, npc_interaction, multiplayer) are different domains, so no superseded/duplicate verdicts were supported. multiplayer.rs has end-to-end 'two_players_see_each_other...' which is a higher layer and was not treated as covering the unit-level registry checks. Discrepancy: the pack reports 1137 lines and 8 tests (T512 visual/boombox group) that do not exist in the repo copy I read (747 lines). Those verdicts are unverified and defaulted to keep; the pack may be stale relative to the tip. Lines 1-230 were only skimmed (helpers and first test)."}
