<!-- fleet job=testaudit-infer id=piece_027-v1 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[10019, 13596, 6, 1780] model=claude-haiku-5-5 -->
# tests/piece_027.rs

{"file": "tests/piece_027.rs",
 "tests": [
  {"name": "grid_pair_is_the_recovered_25_and_5_centimeters", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the recovered 25/5 cm grid pair; no other Rust test in the suite references GridSnap or GRID_SPACING_*. The Python checker tests/pieces/test_piece_027.py is a different language and not a duplicate."},
  {"name": "grid_divisions_match_the_recovered_100_over_centimeters_formula", "verdict": "keep", "covered_by": null, "reason": "Unique check of the 100/cm divisions formula; no equivalent elsewhere in the suite."},
  {"name": "toggle_switches_between_the_recovered_pair", "verdict": "keep", "covered_by": null, "reason": "Unique check of the on/off toggle behaviour of the grid."},
  {"name": "snap_quantises_x_and_z_and_leaves_y_alone", "verdict": "keep", "covered_by": null, "reason": "Unique check that snapping touches only X and Z; the Y-untouched property is not checked anywhere else."},
  {"name": "snap_truncates_toward_zero_and_keeps_exact_multiples", "verdict": "keep", "covered_by": null, "reason": "Unique check of the (int) truncation semantics and of the fine grid; it pins a recovered-behaviour detail."},
  {"name": "snap_rejects_a_non_positive_spacing", "verdict": "keep", "covered_by": null, "reason": "Refusal check (zero spacing rejected); no equivalent elsewhere."},
  {"name": "rotation_step_is_fifteen_degrees_and_signed_by_direction", "verdict": "keep", "covered_by": null, "reason": "Unique check of the 15-degree step and clockwise sign, recovered from FUN_00ab1e30."},
  {"name": "quarter_turn_constant_matches_the_same_function", "verdict": "keep", "covered_by": null, "reason": "Unique pin of the 90-degree constant; small but not covered elsewhere."},
  {"name": "bounds_validate_rejects_inverted_or_non_finite_boxes", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check (inverted and NaN boxes); no equivalent elsewhere."},
  {"name": "bounds_contain_their_closed_edges", "verdict": "keep", "covered_by": null, "reason": "Unique check of closed-edge containment and an outside point refusal."},
  {"name": "limits_follow_the_server_supplied_maximum_counts", "verdict": "keep", "covered_by": null, "reason": "Unique check of fixture/landmark denial against server-supplied maxima; refusal behaviour."},
  {"name": "a_zero_maximum_allows_nothing_without_inventing_a_constant", "verdict": "keep", "covered_by": null, "reason": "Refusal/edge check that a zero maximum denies everything; unique."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "The similar-file list (kart_service, piece_056, piece_037, coin_store_siblings, piece_091) covers unrelated domains and none exercises the housing grid, rotation, bounds or fixture limits. No test is duplicate, superseded or obsolete. The file is a #[path] include of src/restoration/piece_027.rs; the work-item notes say the lead will later register the module, and the test would then need its import path changed. That is a maintenance note, not a removal reason. Note that the header claims ORIGINAL evidence the pack did not let me verify. The verdicts rely on the test names and the similar-file list, not on a grep of every test in the 5,600-test suite."}
