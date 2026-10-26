<!-- fleet job=testaudit-infer id=quest_exclusions-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[27425, 19850, 8, 1667] model=claude-haiku-5-5 -->
# tests/quest_exclusions.rs

{"file": "tests/quest_exclusions.rs",
 "tests": [
  {"name": "finishing_one_version_hides_the_other_two", "verdict": "keep", "covered_by": null, "reason": "Only test that drives the mutual-exclusion rule after completion (Cobblestone finished, Merigold and Valerie offers refused, save bytes unchanged). enabled_quest_menu_offers.rs only uses the exclusion to pick a walk key, not to assert refusal after finishing."},
  {"name": "an_active_version_blocks_the_others", "verdict": "keep", "covered_by": null, "reason": "Covers the active-quest block, the forged-accept refusal and the old-save pending-offer refusal in one place. No other file checks these refusals; keep for refusal coverage."},
  {"name": "abandoning_a_version_reopens_the_others", "verdict": "keep", "covered_by": null, "reason": "Only check that abandoning lifts the exclusion (the reopen direction). Nothing else in the suite asserts it."},
  {"name": "an_old_save_with_two_versions_keeps_both", "verdict": "keep", "covered_by": null, "reason": "Persistence/canary for a legacy save holding two exclusive versions; it must load both without repair and still refuse a third. Not covered elsewhere."},
  {"name": "bad_exclusion_data_is_refused_at_load", "verdict": "keep", "covered_by": null, "reason": "Load-time refusal of malformed exclusion data (missing id, self, duplicate, one-sided, 17 ids). piece_067.rs has TableError checks for a different model (branch table, not from_split_content), so it does not supersede this."},
  {"name": "players_are_independent", "verdict": "keep", "covered_by": null, "reason": "Checks that one character's completion does not block another character. Unique in the suite; multiplayer.rs covers unrelated per-character state, not quest exclusion."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "Every test covers the T465 exclusion rule, which no other test file asserts directly. Nearby files touch the same content but on different paths: enabled_quest_menu_offers.rs uses excludes_quest_ids only to build a walk key, and piece_067.rs models branch exclusion without the QuestEngine loader. No duplicate or superseded test was found, and no later task replaced this behaviour. Confidence is limited because I only read the excerpt and grep hits, not the full bodies of the similar files."}
