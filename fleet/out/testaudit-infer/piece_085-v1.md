<!-- fleet job=testaudit-infer id=piece_085-v1 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[11573, 16127, 6, 1811] model=claude-haiku-5-5 -->
# tests/piece_085.rs

{"file": "tests/piece_085.rs",
 "tests": [
  {"name": "recovered_trade_opcode_table_matches_the_native_constructors", "verdict": "keep", "covered_by": null, "reason": "Only Rust check of the 0x3b base opcode and the 18-row sub-opcode table; the similar Python checks (tests/pieces/test_piece_099.py, test_piece_085.py) are not in the Rust suite and check a different artifact."},
  {"name": "offer_wire_round_trips_through_the_recovered_frame", "verdict": "keep", "covered_by": null, "reason": "Pins exact OfferItem byte layout and round trip for the piece_085 module; no other test file drives this wire."},
  {"name": "cancel_and_end_session_carry_the_session_id", "verdict": "keep", "covered_by": null, "reason": "Exact encoded bytes for Cancel and EndSession session-id carriage; unique to this module."},
  {"name": "update_lock_wire_round_trips_and_rejects_a_truncated_frame", "verdict": "keep", "covered_by": null, "reason": "Contains a hostile/truncated-input refusal check; no equivalent elsewhere."},
  {"name": "item_removed_wire_round_trips_three_recovered_fields", "verdict": "keep", "covered_by": null, "reason": "Only check of ItemRemoved wire layout in the Rust suite."},
  {"name": "frame_decode_rejects_a_foreign_base_opcode_and_an_unknown_sub_opcode", "verdict": "keep", "covered_by": null, "reason": "Refusal check for foreign opcode, unknown sub-opcode and empty input; keep per refusal rule."},
  {"name": "session_commits_both_offers_atomically_on_confirm", "verdict": "keep", "covered_by": null, "reason": "Canonical atomic two-inventory transfer check for the reconstructed session; tests/player_trade.rs covers a different trade service, not this state machine."},
  {"name": "confirm_before_both_sides_lock_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check on confirm ordering; unique to this module."},
  {"name": "changing_an_offer_after_lock_invalidates_the_lock", "verdict": "keep", "covered_by": null, "reason": "Stale-lock rule check; the analogous player_trade test (a_changed_offer_resets_both_locks_and_both_accepts) drives a different implementation, so not clearly the same path."},
  {"name": "cancel_and_disconnect_close_the_session_without_moving_items", "verdict": "keep", "covered_by": null, "reason": "Refusal/no-effect check for cancel and disconnect; not covered by a same-path test elsewhere."},
  {"name": "an_offer_the_owner_does_not_have_fails_atomically", "verdict": "keep", "covered_by": null, "reason": "Atomicity refusal check; keep."},
  {"name": "a_replayed_complete_does_not_transfer_twice", "verdict": "keep", "covered_by": null, "reason": "Replay/duplication security check; keep."},
  {"name": "a_lock_frame_for_another_session_is_stale", "verdict": "keep", "covered_by": null, "reason": "Stale session-id refusal from the recovered binary's staleness check; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Only Rust test target for src/restoration/piece_085.rs (module included via #[path]). The most similar file tests/player_trade.rs exercises a different trade service with different names and paths, so no superseding found. Excerpt was truncated, so the final test body was only partly visible; the verdict relies on its name. No test is a duplicate of another Rust test. Python tests for the same opcode table live outside the cargo suite and were not counted."}
