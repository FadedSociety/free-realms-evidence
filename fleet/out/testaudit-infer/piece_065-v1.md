<!-- fleet job=testaudit-infer id=piece_065-v1 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[11318, 17707, 6, 2113] model=claude-haiku-5-5 -->
# tests/piece_065.rs

{"file": "tests/piece_065.rs",
 "tests": [
  {"name": "replay_wire_rows_match_their_recovered_sources", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the REPLAY_WIRE opcode/direction table and the provenance-source requirement for piece_065. No similar file exercises piece_065's wire table (the similar files cover kart, housing, encounter and piece_030)."},
  {"name": "synthetic_reference_replay_closes_every_gate", "verdict": "keep", "covered_by": null, "reason": "Only positive end-to-end check that the reconstructed reference replay passes all six gates in piece_065. No other test file drives piece_065::evaluate."},
  {"name": "fresh_entry_requires_a_world_start_and_a_quiet_load_window", "verdict": "keep", "covered_by": null, "reason": "Refusal check: starting inside the cave, or damage/enemy motion before the start, must fail FreshEntry. Unique to piece_065."},
  {"name": "fresh_entry_is_not_evidenced_without_the_launch_sequence", "verdict": "keep", "covered_by": null, "reason": "Checks the NotEvidenced path when the 41/114 launch details are missing. Unique to piece_065."},
  {"name": "fresh_entry_rejects_damage_before_the_first_client_attack", "verdict": "keep", "covered_by": null, "reason": "Refusal and regression check for the 073831 failure mode (engagement and damage before the first client attack). Security-style refusal; no equivalent elsewhere."},
  {"name": "an_earlier_loss_does_not_invalidate_the_winning_attempt", "verdict": "keep", "covered_by": null, "reason": "Verifies that the gates grade the last result row, not earlier losses. Unique behavioural check for piece_065."},
  {"name": "combat_gate_requires_player_damage_motion_and_survival", "verdict": "keep", "covered_by": null, "reason": "Negative checks on the Combat gate (stationary enemies, no player hit, player defeated). Unique to piece_065."},
  {"name": "boss_gate_requires_the_tallest_enemy_dead_and_displayed", "verdict": "keep", "covered_by": null, "reason": "Negative checks on the Boss gate (boss alive, no boss display). Unique to piece_065."},
  {"name": "rewards_gate_requires_a_win_real_defeat_counts_and_score_rows", "verdict": "keep", "covered_by": null, "reason": "Negative checks on the Rewards gate (loss, missing 39/47 rows, wrong defeat count, no reward). Unique to piece_065."},
  {"name": "exit_gate_requires_a_genuine_client_exit_then_the_world_return", "verdict": "keep", "covered_by": null, "reason": "Refusal checks on the Exit gate (no 41/109 close, no world return). Unique to piece_065."},
  {"name": "reconnect_gate_requires_a_later_session_with_preserved_state", "verdict": "keep", "covered_by": null, "reason": "Refusal checks on the Reconnect gate (single session, repeated reward, different identity, still inside, reward only in the last session). Unique to piece_065."},
  {"name": "preserved_native_runs_are_not_reported_as_native_acceptance", "verdict": "keep", "covered_by": null, "reason": "Canary: asserts that no preserved historical transcript in lab/reports satisfies every gate without lead confirmation. It skips silently when lab/reports is absent, so it is conditional, but it is the only guard of its kind."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The pack's similar files (kart_service, kart_npc_entry, housing_service, encounter, piece_030) test different systems. Their overlap is in shared vocabulary such as encounter/combat and the piece_030 gate-style structure, not in the piece_065 evaluate() path, so no test here is superseded or duplicate. I did not open the similar files' assertions because the names already show a different subject. The file includes src/restoration/piece_065.rs via #[path] and is not registered in src/lib.rs; the header marks that as a lead-owned integration step, so it is not a redundancy issue. The reconnect and rewards tests have several small assertions each; splitting them would not remove coverage, and merging them is not a removal."}
