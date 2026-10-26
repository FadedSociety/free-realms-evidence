<!-- fleet job=testaudit-infer id=piece_078-v1 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[32700, 21921, 8, 1698] model=claude-haiku-5-5 -->
# tests/piece_078.rs

{"file": "tests/piece_078.rs",
 "tests": [
  {"name": "captured_capture_and_packet_digests_are_pinned", "verdict": "keep", "covered_by": null, "reason": "Provenance/canary check on the capture constants and frame ordering; no other file references the piece_078 module, so nothing else pins these. Weak (only checks hex format and monotonic frames, not the digests against the capture), but conservatively kept."},
  {"name": "stage_events_map_to_the_recovered_inner_opcodes", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered opcode mapping (31/13/14/10/125/41) for the stage events; no other test in the suite drives this module."},
  {"name": "stages_only_advance_in_the_captured_order", "verdict": "keep", "covered_by": null, "reason": "Only check of the stage state machine ordering and refusal of out-of-order begin/finish calls; a refusal check."},
  {"name": "queued_prior_scene_position_never_moves_the_persisted_location", "verdict": "keep", "covered_by": null, "reason": "Security/persistence check that stale prior-scene position reports are ignored while loading; unique to this module."},
  {"name": "world_entries_return_to_the_exact_stored_origin", "verdict": "keep", "covered_by": null, "reason": "Persistence check of exact f32 bit round-trip of the world origin across encounter and housing; unique."},
  {"name": "prior_zone_actions_are_refused_until_the_new_zone_is_spawned", "verdict": "keep", "covered_by": null, "reason": "Refusal check on zone-action gating during transition; no equivalent elsewhere (accepts_zone_action is not used by other tests)."},
  {"name": "malformed_requests_are_refused_without_mutation", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check (NaN/inf, same zone) asserting no state change; unique to this module."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "Every test drives src/restoration/piece_078.rs via a #[path] include, and no other test file in the repo includes that module or calls persisted_location/accepts_zone_action/IgnoredWhileLoading. The similar files (npc_interaction, kart_service, housing_service, warpstone_travel, player_trade) cover different subsystems (NPC/vendor, kart, housing, warpstone, trade) and share no path with this policy, so no superseded or duplicate verdicts are justified. Nothing is obsolete: the piece_078 work item (notes/WorkItems/078.md) is still the live policy. Maintenance note: the #[path] include should be replaced by a registered module as the file's own docs request; that is a structural cleanup, not a removal."}
