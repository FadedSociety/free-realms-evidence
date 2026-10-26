<!-- fleet job=testaudit-infer id=world-v1 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[25367, 16547, 8, 2742] model=claude-haiku-5-5 -->
# tests/world.rs

{"file": "tests/world.rs",
 "tests": [
  {"name": "enter_and_leave_public_zone_builds_content_spawn_set", "verdict": "keep", "covered_by": null, "reason": "Only test that checks the public-zone entry packet set, content NPC spawn, and leave cleanup together; no same-path duplicate found in similar files."},
  {"name": "transfer_orders_begin_zoning_before_zone_details_and_npcs", "verdict": "keep", "covered_by": null, "reason": "Pins the ordering of zone-transition, zone details and NPC packets on a child-instance transfer; no equivalent found elsewhere."},
  {"name": "two_players_share_one_public_instance_and_ready_barrier", "verdict": "keep", "covered_by": null, "reason": "Checks shared public instance membership and the all-ready barrier. Related checks exist in shared_world_membership.rs (mark_zone_ready at line 686) but with different setup; not a same-assertion duplicate, so kept."},
  {"name": "encounter_child_waits_for_zone_ready_callback", "verdict": "keep", "covered_by": null, "reason": "Encounter child kind and ready-callback behaviour; only test of this exact path in the file set reviewed. Kept conservatively."},
  {"name": "dungeon_child_is_private_and_expires_after_empty_grace", "verdict": "keep", "covered_by": null, "reason": "Private dungeon child and empty-grace expiry (boundary at 119/120) is a lifecycle check with no equivalent found."},
  {"name": "failed_transfer_keeps_previous_instance_pose_and_membership", "verdict": "keep", "covered_by": null, "reason": "Refusal check: invalid (NaN) pose must change nothing. Refusal tests are kept by policy."},
  {"name": "opening_zone_zero_entry_matches_current_zone_details_frame", "verdict": "keep", "covered_by": null, "reason": "Byte-exact canary for the zone-0 ZoneDetails frame layout; kept as a wire-format canary."},
  {"name": "npc_visibility_loads_content_caps_the_view_and_respects_startup_exclusions", "verdict": "keep", "covered_by": null, "reason": "Large combined check (content load, 64-NPC cap, unrenderable models, exclusion). Covers distinct behaviour; kept, though it could be split if slow."},
  {"name": "zone_less_legacy_regional_npcs_spawn_in_the_open_world_and_teleport_index", "verdict": "keep", "covered_by": null, "reason": "Pins the 50 zone-less regional NPCs and teleport index on open-world zone 0. npc_interaction.rs::zone_less_legacy_vendor_uses_open_world_range_and_shop_options is related but tests a single vendor's range and shop options, not the 50-NPC index; not a full duplicate."},
  {"name": "extra_spawn_display_fields_reach_add_npc_and_plain_rows_keep_the_template", "verdict": "keep", "covered_by": null, "reason": "Display-field propagation to AddNpc and template fallback; no same-path test found in the similar files reviewed."},
  {"name": "extra_spawn_display_fields_out_of_bounds_refuse_the_load", "verdict": "keep", "covered_by": null, "reason": "Refusal check for out-of-bounds content; kept by policy."},
  {"name": "shipped_extra_spawns_carry_legacy_skins_and_sanctuary_subtitles", "verdict": "keep", "covered_by": null, "reason": "Shipped-content canary for legacy skins and Sanctuary subtitles; kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Similar-file pack gave little overlap: the most similar files (kart_service, shared_field_interest, player_trade, piece_060, power_up_drops) test other systems and only reuse the World API. Closest overlaps are shared_world_membership.rs (ready barrier, child instances) and npc_interaction.rs (zone-less vendor). Those were only spot-checked by name, not assertion by assertion, so verdicts are conservative. I did not read the excerpt's 'extra_spawn' tests' bodies beyond names and the file tail, nor the similar files' assertions in full. Confidence is moderate."}
