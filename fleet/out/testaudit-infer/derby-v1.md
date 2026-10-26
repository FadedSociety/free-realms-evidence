<!-- fleet job=testaudit-infer id=derby-v1 status=done turns=4 usd=0.0047 tokens(read,write,in,out)=[50445, 23291, 10, 2500] model=claude-haiku-5-5 -->
# tests/derby.rs

{"file": "tests/derby.rs",
 "tests": [
  {"name": "all_twenty_client_records_roundtrip_with_reader_widths", "verdict": "keep", "covered_by": null, "reason": "Only test that pins the byte length and subtype number of all 20 SUBTYPE_SPECS records plus the Unknown fallback; no equivalent found in the similar files (they exercise these messages only inside flows)."},
  {"name": "solo_offer_registers_npcs_runs_client_gates_through_state_eleven_and_closes_once", "verdict": "keep", "covered_by": null, "reason": "Full solo lifecycle with the GameState(11) close gate and a duplicate-close refusal. tests/derby_chapter.rs has run_to_running/play_to_results helpers that may overlap the happy path, but I did not verify its assertions, so kept conservatively."},
  {"name": "contacts_apply_server_damage_knockout_scores_and_four_second_respawn", "verdict": "keep", "covered_by": null, "reason": "Asserts server-side damage, knockout score, and the 4 s respawn (ResetVehicle at +4000 ms). tests/app_fuzz.rs hit paths and tests/derby_chapter.rs hit_for helper may touch this, but the exact respawn timing is not shown elsewhere in what I checked."},
  {"name": "each_powerup_type_applies_once_and_expiry_uses_client_categories", "verdict": "keep", "covered_by": null, "reason": "Only test covering all five pickup kinds, one-shot application and expiry ItemExpired categories."},
  {"name": "contacts_require_fresh_nearby_poses_and_a_bounded_impact", "verdict": "keep", "covered_by": null, "reason": "Refusal test: stale/absent poses, distance and impact bounds. Security/refusal check; tests/app_fuzz.rs has absent-pose hit cases but not this full matrix."},
  {"name": "refused_contact_does_not_consume_the_pair_cooldown", "verdict": "keep", "covered_by": null, "reason": "Refusal check that a capped (refused) contact leaves the pair cooldown untouched; distinct behaviour not pinned elsewhere."},
  {"name": "pose_is_relayed_only_to_other_humans_and_disconnect_aborts_empty_match", "verdict": "keep", "covered_by": null, "reason": "Checks pose relay recipients (privacy of relay to others only) and abort-on-empty disconnect; no equivalent found."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The similar-file list is dominated by kart/chess/soccer/derby_route files that test other games, so overlap is weak. The real neighbours are tests/derby_chapter.rs (derby flow via Gameplay, with run_to_running/play_to_results helpers) and tests/app_fuzz.rs (derby pose/hit/register/phase packets). I did not read their assertions in full, so the solo-lifecycle and damage/respawn tests could be superseded by them; a follow-up comparison is recommended before removing anything. No test was marked removable."}
