<!-- fleet job=testaudit-infer id=piece_008-v1 status=done turns=3 usd=0.0044 tokens(read,write,in,out)=[28006, 19438, 8, 3344] model=claude-haiku-5-5 -->
# tests/piece_008.rs

{"file": "tests/piece_008.rs",
 "tests": [
  {"name": "launch_contract_matches_the_recovered_client_rows", "verdict": "keep", "covered_by": null, "reason": "Pins the client row ids, game type and difficulty codes for the unit module; no other test asserts these constants."},
  {"name": "board_coordinates_match_the_clients_a8_origin", "verdict": "keep", "covered_by": null, "reason": "a8-origin square mapping and start FEN in the piece_008 codec; chess.rs tests run through a different Position type and do not pin this frame."},
  {"name": "network_event_and_piece_codes_match_the_shipped_movie", "verdict": "keep", "covered_by": null, "reason": "Wire event and piece code constants checked against the movie; a canary for protocol drift. Not seen elsewhere in this form."},
  {"name": "status_and_winner_codes_match_the_recovered_native_switch", "verdict": "keep", "covered_by": null, "reason": "Status and winner code mapping from get_winner; unique pin of the codes."},
  {"name": "opening_position_has_the_twenty_legal_pawn_and_knight_moves", "verdict": "keep", "covered_by": null, "reason": "Opening move count is also in chess.rs start_position_perft (depth 1 = 20), but that asserts on chess::Position, not piece_008::Position; kept as a separate-engine check."},
  {"name": "positions_reject_moves_that_leave_the_king_in_check", "verdict": "keep", "covered_by": null, "reason": "Pin-free check legality is a refusal check on the codec; kept conservatively."},
  {"name": "castling_requires_rights_and_an_attack_free_path", "verdict": "keep", "covered_by": null, "reason": "Refusal check for castling rights and attacked transit squares; chess.rs perft covers castling counts on another engine only."},
  {"name": "castling_rights_follow_a8_origin_corner_indices", "verdict": "keep", "covered_by": null, "reason": "Corner-index castling-rights update after rook move and capture; specific regression guard for the a8 frame."},
  {"name": "en_passant_and_promotion_are_generated_and_encoded", "verdict": "keep", "covered_by": null, "reason": "Special move generation and encoding; chess.rs perft covers generation counts, not this codec encoding."},
  {"name": "special_codes_follow_the_recovered_native_move_encoder", "verdict": "keep", "covered_by": null, "reason": "Encoder special codes pinned to the native encoder; unique."},
  {"name": "session_move_bytes_follow_the_client_four_byte_layout", "verdict": "keep", "covered_by": null, "reason": "Four-byte move layout canary; no equivalent byte-layout check found in chess.rs (which checks chess_mode and move encoding at the server level, a different layer)."},
  {"name": "checkmate_and_stalemate_are_detected_with_recovered_status_codes", "verdict": "keep", "covered_by": null, "reason": "Terminal detection with status codes; chess.rs fools_mate covers checkmate end-to-end but not stalemate at codec level."},
  {"name": "threefold_repetition_is_a_draw", "verdict": "keep", "covered_by": null, "reason": "Codec-level threefold draw; chess.rs threefold_draw_stops_movie_and_settles_both_runs_once is a server-level check that also settles rewards, so it is not an equal substitute."},
  {"name": "sessions_alternate_turns_and_lock_after_the_result", "verdict": "keep", "covered_by": null, "reason": "Turn alternation and computer-side flag; chess.rs single_player/server_opens tests cover related behaviour at a different layer."},
  {"name": "resign_records_the_recovered_status_and_close_blocks_moves", "verdict": "keep", "covered_by": null, "reason": "Resign status and post-close refusal; chess.rs resignation_and_draw_rules_reach_terminal_states is similar in spirit but at server level. Kept conservatively."},
  {"name": "reconnect_restores_the_live_session_and_rejects_unknown_ids", "verdict": "keep", "covered_by": null, "reason": "Snapshot fidelity and unknown-id refusal; a refusal check, kept."},
  {"name": "a_finished_session_stays_finished_across_reconnect_and_player_left", "verdict": "keep", "covered_by": null, "reason": "Persistence of finished state across reconnect and departure with no invented winner; a persistence check, kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "No test is clearly superseded or duplicated. The file targets the standalone piece_008 codec module (not chess::Position used by tests/chess.rs), so chess.rs overlaps mostly at the level of perft counts and end-to-end terminal states, which is a different layer. Overlap candidates worth a second look if the lead wants pruning: opening move count (vs chess.rs start_position_perft depth 1), threefold draw (vs chess.rs threefold_draw_stops_movie...), and resign/terminal states (vs chess.rs resignation_and_draw_rules_reach_terminal_states). I did not read those chess.rs bodies in full, so confidence is moderate. The file is unregistered in src/lib.rs and includes the source via #[path]; that is a structural note, not a removal reason. piece_010 and piece_009 were not read in depth."}
