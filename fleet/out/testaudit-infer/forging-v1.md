<!-- fleet job=testaudit-infer id=forging-v1 status=done turns=2 usd=0.0040 tokens(read,write,in,out)=[10630, 20984, 6, 2441] model=claude-haiku-5-5 -->
# tests/forging.rs

{"file": "tests/forging.rs",
 "tests": [
  {"name": "shared_native_go_sentinel_is_bound_to_offered_forging_instance", "verdict": "keep", "covered_by": null, "reason": "Byte-exact native vector check plus hostile-offset and stale-instance refusals that must change nothing. The sibling smelting/cooking tests are for other crafting modules, so this is not the same path."},
  {"name": "unused_generic_stat_and_stop_reports_cannot_change_authoritative_forging", "verdict": "keep", "covered_by": null, "reason": "Refusal check: unused generic stat/stop/score messages must not mutate authoritative state. Similar smelting test covers a different message set."},
  {"name": "native_header_info_payload_launch_and_finish_match_compiled_community", "verdict": "keep", "covered_by": null, "reason": "Compiled-community vector oracle for info/payload/launch/finish packets, plus duplicate-start idempotence. Unique to forging."},
  {"name": "native_results_ack_waits_for_actual_close_and_never_repeats_board_reward", "verdict": "keep", "covered_by": null, "reason": "Security/persistence check that a board reward is never repeated and the ack is bound to the exact instance. Analogous to cooking/smelting ack tests but for forging state; not clearly covered elsewhere."},
  {"name": "original_handshake_initializes_grid_mappings_queues_and_mold_once", "verdict": "keep", "covered_by": null, "reason": "Only check of forging handshake grid, queue and mold initialisation, and that a repeated start is a no-op."},
  {"name": "chain_gravity_matches_right_to_left_bottom_to_top_queue_order", "verdict": "keep", "covered_by": null, "reason": "Unique behavioural check of forging gravity/refill order and score/time accounting."},
  {"name": "quota_then_native_next_level_awards_fixed_recipe_once_even_after_reload", "verdict": "keep", "covered_by": null, "reason": "Reward-once and persistence canary: spoofed GameWon rejected, reward granted once across reload, cross-checked against recipes.json."},
  {"name": "forging_recipe_rejections_leave_state_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check for unknown or bad recipe requests; state must be unchanged."},
  {"name": "playable_generated_board_reaches_five_hammer_pieces_through_real_messages", "verdict": "keep", "covered_by": null, "reason": "End-to-end playability canary driving real messages to a reward. Not a duplicate of the private-reference test, which is ignored and needs private inputs."},
  {"name": "malformed_chains_packets_and_claimed_grids_roll_back_all_state", "verdict": "keep", "covered_by": null, "reason": "Hostile-input rollback check across many malformed packets and prefixes. Security-type test; keep."},
  {"name": "no_moves_reshuffles_through_original_clear_build_queue_protocol", "verdict": "keep", "covered_by": null, "reason": "Unique check of the no-moves reshuffle protocol for forging."},
  {"name": "pause_server_deadline_cancel_and_pending_queue_reconnect_never_award", "verdict": "keep", "covered_by": null, "reason": "Never-award and persistence check across pause, deadline, cancel and reconnect. Security-type test."},
  {"name": "content_and_persisted_bounds_fail_closed_with_explicit_reconstruction_labels", "verdict": "keep", "covered_by": null, "reason": "Fail-closed content and persisted-state validation. Refusal and security check; no equivalent named elsewhere."},
  {"name": "private_original_content_movie_metadata_and_real_board_roundtrip", "verdict": "keep", "covered_by": null, "reason": "Ignored test that requires private OSFR_OPENING_REFERENCE inputs. Not run in the default suite, and it is the only check against the real original board."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The similar files (smelting.rs, cooking.rs, kart_service.rs, encounter.rs, mining.rs) test sibling crafting or minigame modules with analogous test names. They do not drive the forging module, so no test is superseded or duplicate. Shared-score similarity comes from naming and helper structure. I did not check every assertion in the similar files; a finer pass could find overlap in the shared crafting_results vectors. Verdicts are conservative as the brief requires."}
