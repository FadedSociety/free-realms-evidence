<!-- fleet job=testaudit-infer id=piece_053-v1 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[11548, 14799, 6, 1949] model=claude-haiku-5-5 -->
# tests/piece_053.rs

{"file": "tests/piece_053.rs",
 "tests": [
  {"name": "recovered_disposition_values_and_reconstructed_rules_are_pinned", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the piece_053 disposition constants and reconstructed aggro numbers; nothing else in the repo references them (only scripts/pieces/piece_053.py and the module itself). Constant pin is a canary for the module contract."},
  {"name": "hostile_candidate_inside_the_pursuit_range_is_acquired", "verdict": "keep", "covered_by": null, "reason": "Sole acquisition check for piece_053::AggroActor. encounter.rs pursuer test drives a different registered module, not this one."},
  {"name": "non_hostile_actors_never_acquire_a_target", "verdict": "keep", "covered_by": null, "reason": "Refusal check (neutral/ally never aggro) with the NotHostile rejection; no equivalent elsewhere."},
  {"name": "invalid_candidates_are_rejected_with_typed_reasons", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (dead, out of zone, out of range, NaN position) with typed reasons; unique to this module."},
  {"name": "nearest_eligible_player_is_acquired_when_several_are_present", "verdict": "keep", "covered_by": null, "reason": "Target selection ordering check; not covered by any other file for this module."},
  {"name": "pursuit_steps_toward_the_target_without_overshooting_the_stop_margin", "verdict": "keep", "covered_by": null, "reason": "Movement invariant (no overshoot, finite positions) for the pursuit step; unique to this module."},
  {"name": "one_step_is_clamped_to_the_reconstructed_speed", "verdict": "keep", "covered_by": null, "reason": "Step clamp check (250 ms at reconstructed speed); unique to this module."},
  {"name": "leaving_the_pursuit_range_disengages_and_returns_to_the_anchor", "verdict": "keep", "covered_by": null, "reason": "Leash/disengage behaviour, a refusal-like reset check; unique to piece_053. field_ai_packets.rs leash tests cover a different module."},
  {"name": "dead_out_of_zone_and_missing_targets_disengage_with_typed_reasons", "verdict": "keep", "covered_by": null, "reason": "Typed disengage reasons for dead/zone/missing target; unique to this module."},
  {"name": "fast_ticks_and_non_finite_anchors_do_not_move_the_actor", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and tick-rate guard; unique to this module."},
  {"name": "boundaries_include_the_pursuit_range_and_the_melee_reach", "verdict": "keep", "covered_by": null, "reason": "Boundary inclusivity check for range and reach; unique to this module."},
  {"name": "returning_actor_reacquires_only_after_reaching_home", "verdict": "keep", "covered_by": null, "reason": "Leash reset ordering check; unique to this module."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The pack's similar files (soccer_service, kart_service, player_trade, piece_036, mining) share only generic vocabulary (refusal, hostile input, reach, range) and test different modules, so none supersedes these. Repo-wide search found no other test driving piece_053::AggroActor, rejection_for or disengage_reason. encounter.rs (pursuer stops after aggro) and field_ai_packets.rs (leash) exercise separate registered modules and were not judged equivalent. The file is a #[path] include of src/restoration/piece_053.rs, so it is the only coverage for that module; confidence is limited because I did not read the similar files' bodies line by line."}
