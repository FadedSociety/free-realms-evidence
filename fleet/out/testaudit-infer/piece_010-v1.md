<!-- fleet job=testaudit-infer id=piece_010-v1 status=done turns=2 usd=0.0039 tokens(read,write,in,out)=[12103, 21029, 6, 2377] model=claude-haiku-5-5 -->
# tests/piece_010.rs

{"file": "tests/piece_010.rs",
 "tests": [
  {"name": "recovered_packet_opcodes_match_the_client_and_catalogue", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the TCG packet opcodes and WIN_SCORE/UNDECLARED_DIFFICULTY constants in the Rust module; no equivalent elsewhere in the suite."},
  {"name": "deck_names_classify_into_the_recovered_row_families", "verdict": "keep", "covered_by": null, "reason": "Only classifier test for RowKind; no other test drives piece_010 row classification."},
  {"name": "archetype_vocabulary_is_the_four_shipped_decks", "verdict": "keep", "covered_by": null, "reason": "Only test of the Archetype vocabulary and its string forms."},
  {"name": "deck_row_parses_opponent_archetype_difficulty_and_reward", "verdict": "keep", "covered_by": null, "reason": "Only test of DeckRow.parse happy-path fields; not duplicated anywhere in the suite."},
  {"name": "round_rows_keep_their_opponent_and_target", "verdict": "keep", "covered_by": null, "reason": "Only test of Round-row parsing; distinct from the deck-row case."},
  {"name": "a_challenge_without_a_target_keeps_its_gaps", "verdict": "keep", "covered_by": null, "reason": "Pins gap reporting for incomplete rows; no equivalent test found."},
  {"name": "undeclared_difficulty_is_not_a_valid_difficulty", "verdict": "keep", "covered_by": null, "reason": "Sentinel-handling check on hostile/undeclared input; keep as refusal-style check."},
  {"name": "a_match_only_counts_points_after_the_start_packet", "verdict": "keep", "covered_by": null, "reason": "Refusal check (NotStarted) on the match state machine; no other test covers it."},
  {"name": "the_first_player_to_twelve_points_wins_and_nothing_scores_after", "verdict": "keep", "covered_by": null, "reason": "Core win-condition test for TcgMatch; no other test drives this path."},
  {"name": "a_side_that_reaches_the_target_first_wins_the_rest_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Refusal check after a finished match; only test of this path."},
  {"name": "point_events_are_positive_and_bounded_by_the_target", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check that must leave state unchanged; not covered elsewhere."},
  {"name": "event_ids_must_strictly_increase_so_a_replay_cannot_score_again", "verdict": "keep", "covered_by": null, "reason": "Replay/anti-cheat canary for scoring; security check with no equivalent elsewhere."},
  {"name": "a_match_target_must_be_reachable_in_whole_point_events", "verdict": "keep", "covered_by": null, "reason": "Constructor bounds check; only test of InvalidTarget."},
  {"name": "the_winner_receives_the_reward_named_by_that_deck_row_only_once", "verdict": "keep", "covered_by": null, "reason": "Reward-once security/economy check; piece_043 uses TcgMatch in src but no test covers this reward path."},
  {"name": "an_unfinished_match_grants_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check that no reward is granted before finish; keep."},
  {"name": "a_session_round_trips_through_its_snapshot_for_reconnect", "verdict": "keep", "covered_by": null, "reason": "Persistence/reconnect round-trip; keep per persistence rule."},
  {"name": "a_finished_snapshot_restores_with_its_winner", "verdict": "keep", "covered_by": null, "reason": "Persistence check on finished state; keep."},
  {"name": "an_out_of_range_snapshot_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-snapshot refusal check; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "This is the only Rust integration test for src/restoration/piece_010.rs (included by path). A repo search found no other tests/*.rs referencing TcgMatch, DeckRow, or the TCG packet constants. The pack's five most similar files (kart_service, mining, soccer_service, fishing_entry, coin_store_siblings) are about other minigames and share only generic vocabulary (refusal, bounded, restore), so none supersedes these tests. The Python script test tests/pieces/test_piece_010.py covers scripts/pieces/piece_010.py, not the Rust module, so it is not a substitute. piece_043.rs references TcgMatch only in src, not in a test. Nothing is removable."}
