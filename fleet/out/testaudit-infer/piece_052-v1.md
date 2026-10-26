<!-- fleet job=testaudit-infer id=piece_052-v1 status=done turns=4 usd=0.0040 tokens(read,write,in,out)=[39861, 18452, 10, 2621] model=claude-haiku-5-5 -->
# tests/piece_052.rs

{"file": "tests/piece_052.rs",
 "tests": [
  {"name": "recovered_contract_constants", "verdict": "keep", "covered_by": null, "reason": "Pins the opcode/size/flag/animation-id constants and the AddNpc Walk/Run/Stand offsets. tests/piece_044.rs::recovered_opcodes_and_animation_immediates_match_the_original_evidence overlaps in part, but it does not cover this module's constants or the locomotion id order, so it is not a clear duplicate."},
  {"name": "movement_packet_matches_the_recovered_125_layout", "verdict": "keep", "covered_by": null, "reason": "Byte-exact check of the 36-byte opcode 125 encoder in src/restoration/piece_052.rs. tests/field_ai_packets.rs pins movement frames, but through the separate src/enemies.rs encoder and a decoded Frame, not this encoder's bytes. Conservative keep; a possible superseded candidate if field_ai_packets is confirmed to decode the full byte layout."},
  {"name": "animation_packet_matches_the_recovered_35_8_layout", "verdict": "keep", "covered_by": null, "reason": "Byte-exact check of the 21-byte 35/8 animation encoder, including the flag-clear path. Same reasoning as the movement layout test: field_ai_packets covers the behaviour through another encoder. Conservative keep."},
  {"name": "patrol_cycles_run_and_stand_between_waypoints", "verdict": "keep", "covered_by": null, "reason": "The only test of PatrolController's dwell, run, arrival and stand cycle. No other test file uses PatrolController."},
  {"name": "patrol_heading_is_always_a_unit_horizontal_vector", "verdict": "keep", "covered_by": null, "reason": "Only check that patrol headings are unit horizontal vectors with the state/unknown bytes set. Not covered elsewhere."},
  {"name": "patrol_step_is_time_bounded", "verdict": "keep", "covered_by": null, "reason": "Anti-teleport bound on a large clock jump, a hostile-input style check. No equivalent elsewhere."},
  {"name": "patrol_rejects_malformed_routes", "verdict": "keep", "covered_by": null, "reason": "Refusal test covering all PatrolError variants on hostile route input. Must be kept under the refusal rule."},
  {"name": "patrol_never_targets_the_player_guid", "verdict": "keep", "covered_by": null, "reason": "Refusal test that a patrol cannot be bound to guid 0 or 1. Security-style check, no equivalent elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The file tests a reconstructed module (src/restoration/piece_052.rs) that no other test file uses, so the patrol tests are unique. The only overlap is the wire-layout tests against tests/field_ai_packets.rs (chase_start_is_movement_then_run_animation), which drives the separate src/enemies.rs encoder. I did not open that file's byte-level assertions in full, so the layout tests are kept conservatively. The similar-file list (piece_048, piece_083, piece_060, piece_088, piece_072) has no overlapping behaviour. piece_044 partly overlaps the constants test."}
