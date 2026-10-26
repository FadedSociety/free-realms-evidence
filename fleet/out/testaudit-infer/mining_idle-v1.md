<!-- fleet job=testaudit-infer id=mining_idle-v1 status=done turns=6 usd=0.0044 tokens(read,write,in,out)=[70477, 17963, 14, 2908] model=claude-haiku-5-5 -->
# tests/mining_idle.rs

{"file": "tests/mining_idle.rs",
 "tests": [
  {"name": "single_tile_idle_ack_is_accepted", "verdict": "keep", "covered_by": null, "reason": "Only test that sends a one-tile OnIdleMsg and asserts it is accepted and marks the tile. mining.rs and mining_review.rs only send idle lists of three tiles. This pins the recovered no-minimum idle rule."},
  {"name": "two_tile_idle_ack_is_accepted", "verdict": "keep", "covered_by": null, "reason": "Only test that sends a two-tile OnIdleMsg and asserts both tiles are marked. Other idle uses in mining.rs, mining_review.rs and mining_lifecycle.rs use three tiles."},
  {"name": "chain_still_requires_three_tiles", "verdict": "keep", "covered_by": null, "reason": "Guards that the three-tile minimum still applies to OnChainMsg after the idle relaxation. It also checks that refused chains leave state unchanged. Not clearly duplicated: mining.rs chain tests check orthogonality and matching, not the one- and two-tile refusal alongside an unchanged-state check."},
  {"name": "idle_ack_outside_the_board_is_refused_atomically", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an out-of-board coordinate must be refused with no partial marking. No other test covers out-of-board idle coordinates."},
  {"name": "malformed_idle_lists_are_refused_and_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal check for OnIdleMsg (odd count, empty field, out-of-bound, non-numeric, empty). mining_review::malformed_payloads_are_rejected_without_mutating_state covers only OnChainMsg, OnVerifyMsg and header-level malformations, not idle lists."},
  {"name": "idle_acks_keep_their_non_playing_behaviour", "verdict": "keep", "covered_by": null, "reason": "Pins that terminal runs ignore idle tiles, malformed idle is refused in every phase, and paused play still applies idle. No other file checks these phase rules for idle messages."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Nothing is clearly redundant. The file's fixtures are synthetic and separate from mining.rs and mining_review.rs, which use OnIdleMsg only with three-tile lists inside larger flows. mining_review's malformed-payload test does not cover idle lists. Overlap is partial at most, so every test is kept. I did not read mining_lifecycle.rs or mining_move_detection.rs in full; they only use idle as a helper or in a three-tile case."}
