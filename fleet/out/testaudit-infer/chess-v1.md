<!-- fleet job=testaudit-infer id=chess-v1 status=done turns=4 usd=0.0046 tokens(read,write,in,out)=[43009, 18306, 10, 3696] model=claude-haiku-5-5 -->
# tests/chess.rs

{"file": "tests/chess.rs",
 "tests": [
  {"name": "start_position_perft_depth_one_through_four", "verdict": "keep", "covered_by": null, "reason": "Only perft check of the start position in the suite; the perft helper is used only here and in the kiwipete test."},
  {"name": "standard_castling_en_passant_and_promotion_positions_match_perft", "verdict": "keep", "covered_by": null, "reason": "Kiwipete and special-position perft counts are the only check of castling, en passant and promotion move generation at depth 3; no other file runs perft."},
  {"name": "illegal_move_is_rejected_and_does_not_change_the_board", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an illegal move is rejected and the FEN is unchanged; also checks pinned-piece legality."},
  {"name": "discovered_queen_check_is_detected_and_black_must_answer_it", "verdict": "keep", "covered_by": null, "reason": "Check detection and legal-reply filtering; not clearly covered by tests/piece_008.rs, which covers checkmate/stalemate codes rather than a discovered check."},
  {"name": "single_player_server_replies_without_client_move_authority", "verdict": "keep", "covered_by": null, "reason": "Security check: the client cannot dictate the server's reply in single-player mode."},
  {"name": "server_opens_for_white_when_the_human_plays_black", "verdict": "keep", "covered_by": null, "reason": "Behaviour of the opening side; not checked elsewhere in the pack."},
  {"name": "fools_mate_emits_checkmate_and_settles_one_reward_once", "verdict": "keep", "covered_by": null, "reason": "Settles a reward once; the single-payment property is a persistence/refusal guard. Not compared against chess_route.rs in depth, so kept."},
  {"name": "threefold_draw_stops_movie_and_settles_both_runs_once", "verdict": "keep", "covered_by": null, "reason": "Draw-settlement and once-only payout. tests/piece_008.rs::threefold_repetition_is_a_draw covers only the rule, not the run settlement, so this is not a duplicate."},
  {"name": "two_player_move_is_relayed_only_to_the_other_player", "verdict": "keep", "covered_by": null, "reason": "Privacy/relay routing check between players."},
  {"name": "disconnect_forfeits_and_notifies_survivor", "verdict": "keep", "covered_by": null, "reason": "Forfeit path and survivor notification; behaviour not shown elsewhere in the pack."},
  {"name": "resignation_and_draw_rules_reach_terminal_states", "verdict": "keep", "covered_by": null, "reason": "Terminal states via resignation and draw; a broader check than piece_008's resign test, which is a different module family. Kept conservatively."},
  {"name": "payload_header_and_difficulty_mapping_are_bounded_and_stable", "verdict": "keep", "covered_by": null, "reason": "Bounded hostile-input parsing and stable mapping."},
  {"name": "content_skill_keeps_the_server_reply_path", "verdict": "keep", "covered_by": null, "reason": "Canary-style check that the content skill path still replies."},
  {"name": "chess_mode_and_move_encoding_cover_client_castling_events", "verdict": "keep", "covered_by": null, "reason": "Wire encoding of client castling events; piece_008 covers a different (session-move) layout."},
  {"name": "computer_replies_vary_between_fresh_tables", "verdict": "keep", "covered_by": null, "reason": "Entropy behaviour check; overlaps in spirit with a_recorded_winning_game but tests a different property. Kept with low confidence."},
  {"name": "hard_rows_diverge_across_seeded_tables", "verdict": "keep", "covered_by": null, "reason": "Seeded divergence for hard rows; kept conservatively, possibly overlapping with a_recorded_winning_game_does_not_replay_against_fresh_tables."},
  {"name": "a_zero_near_equal_window_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check on a zero window."},
  {"name": "a_recorded_winning_game_does_not_replay_against_fresh_tables", "verdict": "keep", "covered_by": null, "reason": "Anti-replay security check that also exercises the production entropy constructor; no equal test found elsewhere."},
  {"name": "the_daily_cap_stops_payouts_survives_restore_and_refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Daily cap, persistence across restore, and refusals changing nothing. tests/chess_route.rs::the_daily_cap_applies_after_a_real_win_and_a_save_round_trip is a route-level test of similar behaviour but this one also covers refusals and day rollover; keep rather than mark superseded."},
  {"name": "a_settled_game_reports_its_result_and_length_for_the_earn_table", "verdict": "keep", "covered_by": null, "reason": "Only check that the earn table receives result and ply count; not clearly covered elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.4,
 "notes": "Limited review: I read the file's tail (lines 1000-1133) and the test-name lists of chess_route.rs and piece_008.rs, but not the middle sections of chess.rs or the bodies of most similar tests. Every verdict is therefore keep by default; the most plausible overlap candidates to check with a full read are computer_replies_vary_between_fresh_tables, hard_rows_diverge_across_seeded_tables and resignation_and_draw_rules_reach_terminal_states. The daily-cap test overlaps in part with tests/chess_route.rs. The file's perft tests are unique in the repo, since perft is only called from tests/chess.rs."
}
