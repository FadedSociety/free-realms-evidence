<!-- fleet job=testaudit-infer id=piece_044-v1 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[10571, 16859, 6, 1680] model=claude-haiku-5-5 -->
# tests/piece_044.rs

{"file": "tests/piece_044.rs",
 "tests": [
  {"name": "recovered_opcodes_and_animation_immediates_match_the_original_evidence", "verdict": "keep", "covered_by": null, "reason": "Pins the wire constants (26/38, sub-opcodes 13/36/26/1/21, animation 3001, composite 4005) against the recovered client/server evidence. No other Rust test in the repo drives this module; the only other references are the Python piece script and notes."},
  {"name": "switch_request_parses_only_the_recovered_four_byte_payload", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and strict-length parsing check (wrong family, wrong sub-command, short and trailing bytes, non-positive ids). Security/refusal-style check with no equivalent elsewhere."},
  {"name": "unlocked_profile_switches_and_an_unowned_profile_is_refused_without_mutation", "verdict": "keep", "covered_by": null, "reason": "Ownership gate and refusal path for the switch decision; the only test of decide_switch in the repo."},
  {"name": "refusal_selects_the_recovered_failure_command_and_never_fabricates_a_reason", "verdict": "keep", "covered_by": null, "reason": "Refusal check: asserts the failure frame is [26,0][26,0][id][0] with no invented reason and no activation. Refusal test, cannot be removed without an equal test elsewhere, none exists."},
  {"name": "switching_carries_health_gear_and_the_active_profile_through_unchanged", "verdict": "keep", "covered_by": null, "reason": "Preservation guard positive case for health, gear and abilities. Unique to this module."},
  {"name": "preservation_guard_reports_the_exact_field_that_changed", "verdict": "keep", "covered_by": null, "reason": "Refusal check that each changed field produces its specific error and that an unchanged profile is rejected. Unique; keep."},
  {"name": "switch_decision_and_guard_compose_into_one_accepted_activation", "verdict": "keep", "covered_by": null, "reason": "End-to-end composition of decide_switch and preserve. Body was truncated in the excerpt so it could not be fully read; kept conservatively, and it is the only composed-path check."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The similar files (piece_046, piece_048, piece_020, kart_service, housing_service) cover different features (assign/activate slots, activity groups, kart races, housing). None drives decode_switch_request, decide_switch, or preserve, so there is no superseding or duplicate test. The only other reference is tests/pieces/test_piece_044.py, a Python script rather than a Rust test, so it does not count. No test is obsolete: the command IDs and the 3001/4005 animation values are still the recovered ones. Overlap inside the file (the hard-coded [1,58] case inside the unlocked-profile test, and the composition test versus the preservation tests) is minor and was kept. The last test was only partly visible in the excerpt, so its verdict is less certain."}
