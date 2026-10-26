<!-- fleet job=testaudit-infer id=players_reference-v1 status=nothing_found turns=3 usd=0.0018 tokens(read,write,in,out)=[18106, 9808, 8, 853] model=claude-haiku-5-5 -->
# tests/players_reference.rs

{"file": "tests/players_reference.rs",
 "tests": [],
 "whole_file_removable": false,
 "confidence": 0.9,
 "notes": "This file contains no #[test] functions (grep for #[test] returns none; the pack's test list is empty). It is a frozen reference implementation of the pre-W96 players.rs algorithm (InterestPolicy, PlayerRegistry with join/leave/update_pose and visible_sets/diff_messages, plus wire builders build_add_pc / build_position_update / build_remove_player) meant to be included via #[path] by other test binaries. It is compiled in as a module by tests/players_differential.rs and tests/load_players.rs, so it is not a removable test file; deleting it would break those two binaries. Nothing to classify per test. The similar-file list (player_trade, player_radial, players, shared_field_interest) is only a name-overlap signal and does not show duplicate assertions here. Any redundancy question belongs to players_differential.rs and load_players.rs, not this file."}
