<!-- fleet job=testaudit-infer id=crafting_stations-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[16984, 10934, 8, 1553] model=claude-haiku-5-5 -->
# tests/crafting_stations.rs

{"file": "tests/crafting_stations.rs",
 "tests": [
  {"name": "shipped_models_register_cooking_smelting_and_forging_stations", "verdict": "keep", "covered_by": null, "reason": "Only direct check that the shipped crafting_stations content file maps real world model ids to Chef/Miner/Blacksmith with the expected positions and radius 12. tests/crafting_stations_route.rs exercises stations at route level, not this loader/mapping output."},
  {"name": "unknown_non_finite_and_duplicate_world_models_are_ignored_or_deduplicated", "verdict": "keep", "covered_by": null, "reason": "Hostile-input check (unknown model, NaN position, duplicate spawn) on the world_stations and merge_stations functions directly. tests/recipe_book.rs::non_finite_positions_never_reach_a_station covers NaN only through the full start-craft refusal path, not the station-building filter or the dedupe in merge_stations."},
  {"name": "malformed_station_files_are_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a station file with a duplicate model_id must error, and a directory without the file must load empty. No other test in the similar files drives load_world_station_rules error handling."},
  {"name": "rules_preserve_the_world_zone", "verdict": "keep", "covered_by": null, "reason": "Small but distinct check that zone_id passes through world_stations from the spawn tuple. The shipped test only checks zone 7 for one station, so this is not a strict duplicate; it is cheap and conservative to keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The file unit-tests the public recipe_book loader and station builders directly, while the similar files (recipe_book.rs, crafting_stations_route.rs, recipes.rs) test the same feature at route or service level. The overlap is thematic rather than same-path with same assertions, so nothing is marked removable. Lowest-value candidate is rules_preserve_the_world_zone, partly covered by the zone assertion in the shipped test, but it was kept under the conservative rule."}
