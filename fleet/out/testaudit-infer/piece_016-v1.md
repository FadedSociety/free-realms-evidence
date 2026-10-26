<!-- fleet job=testaudit-infer id=piece_016-v1 status=done turns=3 usd=0.0041 tokens(read,write,in,out)=[28342, 20617, 8, 2529] model=claude-haiku-5-5 -->
# tests/piece_016.rs

{"file": "tests/piece_016.rs",
 "tests": [
  {"name": "captured_knockout_frames_decode_and_re_encode_byte_exact", "verdict": "keep", "covered_by": null, "reason": "Byte-exact round trip of two captured original 39/23 frames with SHA-256 pins against preserved packet captures; the only check of this decode/encode path in the suite."},
  {"name": "captured_leave_frames_are_bare_base_headers", "verdict": "keep", "covered_by": null, "reason": "Pins two captured 39/7 leave requests against their recorded digests and state ids; no other test in the suite decodes these captures."},
  {"name": "game_over_frame_carries_the_won_byte_and_three_ints", "verdict": "keep", "covered_by": null, "reason": "Checks the Won byte and layout of the 39/18 game-over body. piece_060 has its own separate encode_game_over in a different module, so this layout is not covered there."},
  {"name": "state_remove_and_game_start_are_bare_headers", "verdict": "keep", "covered_by": null, "reason": "Pins the wire layout of the state-remove and game-start headers in this module; not duplicated in a sibling Rust test."},
  {"name": "start_and_restart_subtypes_are_the_recovered_requests", "verdict": "keep", "covered_by": null, "reason": "Constant pins for subtypes 5, 11 and 7 recovered from the native client; cheap canary against accidental renumbering."},
  {"name": "frame_decoder_rejects_malformed_input", "verdict": "keep", "covered_by": null, "reason": "Hostile-input rejection test covering short, wrong-opcode, wrong-flag, bad-length and truncated frames; refusal check, must keep."},
  {"name": "knockout_remaining_is_max_minus_current", "verdict": "keep", "covered_by": null, "reason": "Small arithmetic check on remaining(); it is the only test of that accessor, so keep despite being thin."},
  {"name": "start_mints_a_fresh_instance_id_and_acks_it", "verdict": "keep", "covered_by": null, "reason": "Ledger start path: fresh id, ack reply, and AlreadyPlaying refusal. The Ledger is local to this file, so no other suite test drives it."},
  {"name": "loss_is_terminal_and_proposes_no_reward", "verdict": "keep", "covered_by": null, "reason": "Refusal and no-reward check on loss (AlreadySettled on a second finish). Unique to this file's Ledger."},
  {"name": "a_win_proposes_exactly_one_reward", "verdict": "keep", "covered_by": null, "reason": "Reward-once guarantee, a security-relevant persistence check on the reward path. Unique to this Ledger."},
  {"name": "stale_finish_after_retry_is_rejected_without_reward", "verdict": "keep", "covered_by": null, "reason": "Stale-state refusal with no reward after retry; a refusal check, must keep."},
  {"name": "retry_requires_a_terminal_instance", "verdict": "keep", "covered_by": null, "reason": "Refusal test for retry on non-terminal or unknown instances; must keep."},
  {"name": "finish_without_a_started_instance_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal test for finish with no current or wrong state id; must keep."},
  {"name": "quitting_abandons_the_instance_without_reward", "verdict": "keep", "covered_by": null, "reason": "Quit path grants no reward and emits a remove; unique behaviour of this Ledger."},
  {"name": "state_ids_are_never_reused_across_many_retries", "verdict": "keep", "covered_by": null, "reason": "Canary for state-id monotonicity over repeated retries; cannot be removed without an equivalent test."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file is self-contained: it includes src/restoration/piece_016.rs by path, and no other Rust test includes that module. Its Ledger and op39 codecs are not exercised elsewhere. The most similar files (kart_service, encounter, piece_060, kart_racing, piece_056) cover different modules. piece_060 has a similarly named encode_game_over and a completion/entry state machine, but its own module and assertions differ. Python tests/pieces/test_piece_016.py exercises the same captures but is not a Rust test, so it does not count as a duplicate in the Rust suite. No test is marked removable; within-file overlap (stale_finish vs retry_requires) is minor and each has a distinct assertion."}
