<!-- fleet job=testaudit-infer id=card_game_content-v1 status=blocked turns=7 usd=0.0043 tokens(read,write,in,out)=[75920, 18662, 16, 2492] model=claude-haiku-5-5 -->
# tests/card_game_content.rs

{"file": "tests/card_game_content.rs",
 "tests": [
  {"name": "the_shipped_file_loads_with_the_seventeen_rows", "verdict": "keep", "covered_by": null, "reason": "Provisional. Pins the shipped row set (17 ids, Treasure War category). Cannot compare against another test because src/card_game.rs and data/content/card_game.json are not in the repo at this tip."},
  {"name": "every_row_equals_its_client_minigame_row", "verdict": "keep", "covered_by": null, "reason": "Provisional. Cross-checks rows against client MiniGameData.txt and ActivityCategories.txt. No other test in the repo reads card_game rows; the nearest analogues (tests/recipes.rs, piece_010/015/075) check MiniGameData for other purposes."},
  {"name": "every_image_is_in_the_client_asset_manifest", "verdict": "keep", "covered_by": null, "reason": "Provisional. Asset-manifest check for card rows. tests/content_npc_spawns.rs does a similar manifest check, but for NPC models, not these rows."},
  {"name": "every_row_carries_legacy_and_client_provenance", "verdict": "keep", "covered_by": null, "reason": "Provisional. Provenance invariant on the data file, with no equivalent found."},
  {"name": "malformed_files_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input check (duplicate id, unknown field, oversize, no rows, bad version). Must be kept unless an equal test is named; none is named."}
 ],
 "whole_file_removable": false,
 "confidence": 0.2,
 "notes": "Blocked. The pack describes tests/card_game_content.rs, but the file does not exist in the repo at this tip (\"not a file\"). Neither the crate module osfr_tools::card_game (src/card_game.rs), nor data/content/card_game.json, nor any reference to 'card_game' exists under prototype/osfr-tools or the repo. The briefs say the file depends on the unmerged brief tcg-activity-rows (see briefs/T545-card-duel-admin-credit.md lines 20, 33, 80), which is the likely cause. The verdicts above are provisional keeps based only on the pack excerpt, not on a real comparison. The closest similar file, tests/activity_portal.rs (card_rows_match_the_client_reader, card_rows_are_refused_in_order_unknown_busy_closed), tests the activity portal's card rows rather than this content loader. Re-run the audit once tcg-activity-rows is merged."}
