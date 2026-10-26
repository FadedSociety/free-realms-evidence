<!-- fleet job=testaudit-infer id=mining_dead_board-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[24486, 18339, 8, 1712] model=claude-haiku-5-5 -->
# tests/mining_dead_board.rs

{"file": "tests/mining_dead_board.rs",
 "tests": [
  {"name": "chainless_board_with_bottom_ore_rebuilds_after_chain", "verdict": "keep", "covered_by": null, "reason": "Only test that drives the chain-update path with a bottom-row collectable on a chainless board and asserts the rebuild (reshuffles == 1, OnLevelEventMsg 11, OnBuildMapMsg). mining_move_detection.rs drives the fall/collect path with a background of 601 tiles, not a chain update with a bottom ore, so it does not cover this path. Refusal-style regression guard for a captured dead board; keep."},
  {"name": "chainless_board_with_bottom_ore_rebuilds_after_collect", "verdict": "keep", "covered_by": null, "reason": "Collect-update path with a second bottom ore remaining. Closest is mining_move_detection.rs::chain21_snapshot_with_no_legal_path_must_reshuffle and the fall_and_reshuffles vectors, which check the reshuffle counter after a fall but not the bottom-ore-remaining case, score 3500, or the quota notice. Not clearly covered elsewhere; keep."},
  {"name": "board_with_a_move_does_not_rebuild", "verdict": "keep", "covered_by": null, "reason": "Negative guard that a legal connected group suppresses the rebuild even with a bottom ore. Similar in spirit to mining_move_detection.rs::valid_three_tile_paths_keep_the_board_and_ignore_idle, but on a different path (chain update, bottom ore present, no reshuffle notice). Guards against over-rebuilding; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "All three tests are regression guards for a captured dead-board bug, and no other test in the 445-file suite was found asserting reshuffle with a bottom-row collectable on either update path. Minor: the board_with comment says '(10,8)=602-style' while the code places ORE (601) at column 8, which is a stale comment, not a test defect. Fixture uses a private temp dir and synthetic state, so no shared-state risk."}
