<!-- fleet job=testaudit-infer id=piece_054-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[9960, 12503, 6, 1927] model=claude-haiku-5-5 -->
# tests/piece_054.rs

{"file": "tests/piece_054.rs",
 "tests": [
  {"name": "production_melee_reach_is_still_the_reviewed_three_units", "verdict": "keep", "covered_by": null, "reason": "Source-pinning canary for the production reach rows, repeat gate and enemy contact rule; no other test in the tests/ tree pins these production strings. Brittle, but it is the only guard for the widened-reach regression."},
  {"name": "far_hits_are_rejected_at_the_reviewed_boundary", "verdict": "keep", "covered_by": null, "reason": "Refusal test: 8-unit hit refused with OutOfReach payload, exact 3.0 accepted, next float refused. Boundary check unique to this file (piece_036 covers a different 20-unit ranged reach)."},
  {"name": "reviewed_capture_distances_are_accepted_and_the_old_reach_would_not_be", "verdict": "keep", "covered_by": null, "reason": "Accepts captured distances from the native run. Its 8.0 refusal repeats far_hits_are_rejected_at_the_reviewed_boundary within this file, but the capture-accept assertions are not elsewhere; keep, optionally trim the duplicated 8.0 line."},
  {"name": "repeat_gate_refuses_a_second_attack_inside_six_hundred_ms", "verdict": "keep", "covered_by": null, "reason": "Repeat-gate refusal with exact RepeatGate payload at 599 ms and acceptance at 600 ms. No melee equivalent elsewhere; piece_036's 600 ms gate is for the ranged cast path, a different function."},
  {"name": "dead_targets_and_invalid_positions_are_refused", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (dead target, NaN attacker position). Not covered elsewhere for resolve_melee_attack."},
  {"name": "swing_animation_follows_the_recovered_wield_table", "verdict": "keep", "covered_by": null, "reason": "Pins the wield-type to animation group table and enemy slot id. Only test of melee_animation_group; overlaps the constants test only on 1099/1001 values."},
  {"name": "animation_and_timing_evidence_matches_the_original_client_resources", "verdict": "keep", "covered_by": null, "reason": "Constant-pinning test for original client rows (slot fields, transition timings). Partly repeats the group ids asserted in swing_animation_follows_the_recovered_wield_table within this file, but adds the slot and timing fields that nothing else checks. Not removable."},
  {"name": "melee_distance_matches_the_production_encounter_math", "verdict": "keep", "covered_by": null, "reason": "Only direct test of the melee_distance helper; three simple cases. Small but unique."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "No other test file in tests/ drives resolve_melee_attack, melee_animation_group or the 3.0 melee reach; the similar files (piece_036, piece_035, kart_service, piece_093, piece_072) cover ranged casting, reach for the Archer kit, or unrelated systems, so no superseded or duplicate verdicts are justified. Within-file overlap exists (the 8.0-unit refusal appears in two tests; the 1099/1001 ids appear in two tests) and could be trimmed, but none of it makes a test removable. Confidence is moderate because I did not read piece_036 or piece_035 in full to compare their reach assertions."}
