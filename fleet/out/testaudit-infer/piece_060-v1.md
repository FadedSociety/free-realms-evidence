<!-- fleet job=testaudit-infer id=piece_060-v1 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[11028, 14541, 6, 2140] model=claude-haiku-5-5 -->
# tests/piece_060.rs

{"file": "tests/piece_060.rs",
 "tests": [
  {"name": "captured_op41_frames_re_encode_byte_for_byte", "verdict": "keep", "covered_by": null, "reason": "Only test that checks encoder output against retail capture frames (op41 sub2/106/107) with provenance hashes; no equivalent elsewhere."},
  {"name": "required_combat_level_matches_the_recovered_difficulty_table", "verdict": "keep", "covered_by": null, "reason": "Only check of the recovered difficulty-to-level table in piece_060; the dungeon data tests check JSON rows, not this function."},
  {"name": "entering_emits_the_recovered_player_enter_packet_and_records_membership", "verdict": "keep", "covered_by": null, "reason": "Pins the player-enter packet bytes and membership state for this lifecycle; no other file drives piece_060::Lifecycle."},
  {"name": "entry_is_gated_by_difficulty_and_caller_supplied_capacity", "verdict": "keep", "covered_by": null, "reason": "Refusal check (NotEligible, InstanceFull); no equivalent elsewhere."},
  {"name": "duplicate_and_post_close_entry_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check for duplicate and closed-instance entry; unique to this module."},
  {"name": "zone_ready_flips_the_go_packet_only_when_every_connected_member_is_ready", "verdict": "keep", "covered_by": null, "reason": "Gate behaviour with disconnected-member handling; not covered elsewhere."},
  {"name": "start_walks_the_recovered_encounter_states", "verdict": "keep", "covered_by": null, "reason": "Pins the 5/6 state packet bytes and phase walk; unique to piece_060."},
  {"name": "spawn_is_once_per_generation_and_rejects_duplicate_or_reused_actor_ids", "verdict": "keep", "covered_by": null, "reason": "Refusal check on actor id reuse; keep conservatively."},
  {"name": "reset_advances_the_generation_and_never_reuses_an_actor_id", "verdict": "keep", "covered_by": null, "reason": "Security-style invariant (no actor id reuse); keep."},
  {"name": "completion_requires_every_spawned_actor_defeated", "verdict": "keep", "covered_by": null, "reason": "Completion gate check; unique to this lifecycle."},
  {"name": "completion_is_once_only_and_emits_the_recovered_terminal_packets", "verdict": "keep", "covered_by": null, "reason": "Pins terminal op39/op41 bytes and once-only behaviour; unique."},
  {"name": "completion_requires_a_connected_member_and_emits_no_reward_bytes", "verdict": "keep", "covered_by": null, "reason": "Refusal check and no-reward invariant; keep."},
  {"name": "exit_keeps_the_instance_for_the_remaining_members_and_closes_on_the_last", "verdict": "keep", "covered_by": null, "reason": "Membership lifecycle check; not covered elsewhere."},
  {"name": "disconnect_holds_the_slot_and_reconnect_preserves_the_spawn_generation", "verdict": "keep", "covered_by": null, "reason": "Persistence/reconnect check; keep."},
  {"name": "expired_membership_is_reaped_and_reconnect_after_the_deadline_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check on expired grace; keep."},
  {"name": "registry_keeps_one_live_instance_per_player_and_never_reuses_ids", "verdict": "keep", "covered_by": null, "reason": "Invariant check on registry; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Every test drives piece_060's own Lifecycle/Registry/encoders via #[path] include. The five similar files (kart_service, matchmaking, piece_048, piece_020, soccer_match) are other domains: they share only generic group/queue/state-machine vocabulary, not the op41/op39 encounter packets or the difficulty table. piece_020 (group launch readiness) is the nearest analogue and does not duplicate these assertions. No other file in the suite exercises piece_060 directly. Bandit/bixie dungeon tests check content JSON rows only. Confidence is moderate because the similar-file set was not exhaustively searched; the file is a single-consumer acceptance test pending the lead's module registration (the #[path] include should be replaced by pub mod once registered, which is a maintenance note, not a removal reason)."}
