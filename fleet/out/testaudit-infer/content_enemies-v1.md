<!-- fleet job=testaudit-infer id=content_enemies-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[8366, 10407, 6, 1081] model=claude-haiku-5-5 -->
# tests/content_enemies.rs

{"file": "tests/content_enemies.rs",
 "tests": [
  {"name": "enemy_definitions_load_and_model_assets_match_client_tables", "verdict": "keep", "covered_by": null, "reason": "Only check that cross-validates enemies.json definitions against the client locale table, Models.txt, the extracted asset catalog, and the documented model-asset gaps and coverage counts. No similar test in the pack (recipes, pets, power_up_drops, enemy_rows_for_quest_targets) reads enemies_unresolved.json or the model bindings."},
  {"name": "every_dungeon_enemy_name_is_crosswalked_or_listed_unresolved", "verdict": "keep", "covered_by": null, "reason": "Only test that checks every dungeon enemy/boss name occurrence against the enemy_refs crosswalk and the unresolved list, and that the coverage counters match. Nothing in the similar files drives dungeons/*.json. Its assertions are data-audit invariants, not a duplicate of any other test."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Only two tests, both audits of shipped content data, and neither is duplicated by the similar files. Both read lab/ and data/content outputs, so they can break on data regeneration rather than code change; that is a maintenance concern, not a redundancy one. Nothing removable. I read the full file but only grepped the similar files for the data file names; I did not open enemy_rows_for_quest_targets.rs or power_up_drops.rs to compare assertions. Their names suggest different paths, so this is a judgment, not a line-by-line check."}
