<!-- fleet job=testaudit-infer id=piece_009-v1 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[10634, 13948, 6, 1840] model=claude-haiku-5-5 -->
# tests/piece_009.rs

{"file": "tests/piece_009.rs",
 "tests": [
  {"name": "recovered_constants_match_the_movie", "verdict": "keep", "covered_by": null, "reason": "Only check of the recovered event codes, game id and bootstrap side order; no other file exercises checkers constants."},
  {"name": "initial_layout_matches_recovered_setup", "verdict": "keep", "covered_by": null, "reason": "Only test of the checkers starting layout and fresh-session phase; no other checkers test exists in the repo."},
  {"name": "pawn_geometry_matches_movie_offsets", "verdict": "keep", "covered_by": null, "reason": "Pins the BoardProxy offset math used only by this module; not covered elsewhere."},
  {"name": "pawns_move_forward_only_and_kings_keep_all_four_diagonals", "verdict": "keep", "covered_by": null, "reason": "Unique check of pawn direction and king movement rules."},
  {"name": "capture_needs_an_enemy_target_and_an_empty_landing", "verdict": "keep", "covered_by": null, "reason": "Unique capture-validity check including negative cases (same colour, blocked landing)."},
  {"name": "compulsory_capture_forbids_quiet_moves", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a quiet move is rejected and the board is asserted unchanged."},
  {"name": "jump_removes_the_enemy_and_emits_movie_events", "verdict": "keep", "covered_by": null, "reason": "Unique check of jump effects and exact emitted event sequence."},
  {"name": "double_jump_chain_must_run_to_completion", "verdict": "keep", "covered_by": null, "reason": "Refusal of an incomplete multi-jump chain plus the full event sequence; unique to this module."},
  {"name": "promotion_emits_the_king_event_and_a_king_may_move_backwards", "verdict": "keep", "covered_by": null, "reason": "Unique promotion event and king backward-move check."},
  {"name": "a_side_without_legal_moves_loses_and_the_session_closes", "verdict": "keep", "covered_by": null, "reason": "Terminal-state check; no equivalent elsewhere in the repo."},
  {"name": "a_king_stepping_back_onto_a_promotion_row_re_emits_the_king_event", "verdict": "keep", "covered_by": null, "reason": "Specific edge case of the king event; not duplicated elsewhere."},
  {"name": "turn_replay_and_bounds_are_enforced_without_state_change", "verdict": "keep", "covered_by": null, "reason": "Security/refusal check (replay and out-of-range input change nothing)."},
  {"name": "late_replays_after_later_turns_are_still_rejected", "verdict": "keep", "covered_by": null, "reason": "Replay-refusal canary; no equivalent elsewhere."},
  {"name": "illegal_destinations_and_wrong_pieces_are_named", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check naming error variants; unique to this module."},
  {"name": "move_payload_matches_the_movie_send_move_text", "verdict": "keep", "covered_by": null, "reason": "Wire-format check for the checkers move payload; the chess and piece_008 wire tests cover different games and formats."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The five similar files are chess (chess.rs), piece_008 (chess board), piece_010 (match scoring), piece_048 (slots) and kart_service; none exercises the checkers module. A repository-wide search found no other test that calls CheckersSession, EV_MOVE_KING or the checkers wire format. The only other checkers artefact is the Python checker tests/pieces/test_piece_009.py, which is a different language and not a Rust duplicate. The pack excerpt cuts off inside move_payload and the tail of the file, so I judged the last test from its name and the work-item notes, not its body. Every test is keep, so there is nothing to prune."}
