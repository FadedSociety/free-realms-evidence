<!-- fleet job=testaudit-infer id=content_npc_spawns-v1 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[24946, 15293, 8, 1682] model=claude-haiku-5-5 -->
# tests/content_npc_spawns.rs

{"file": "tests/content_npc_spawns.rs",
 "tests": [
  {"name": "npc_spawn_models_names_positions_and_capture_matches_are_valid", "verdict": "keep", "covered_by": null, "reason": "Whole-dataset validity check over npcs/*.json, npc_spawns_extra.json and the startup capture: model files against catalog and Assets_manifest, Models.txt model_id mapping, locale ids, finite positions, Legacy provenance, capture matches within 0.6 m, and exact row counts (1201 regional, 3307 extra, 9 captured actors). The similar world.rs tests (extra_spawn_display_fields_*, shipped_extra_spawns_carry_legacy_skins_and_sanctuary_subtitles) check display fields for specific rows, not the full set, so nothing equally strong was found elsewhere. Its count assertions are brittle but they guard content drift, so they are not redundant."},
  {"name": "retired_legacy_spawns_stay_out_of_the_world", "verdict": "keep", "covered_by": null, "reason": "Listed in the pack (T468 refusal-style check that npc_spawns_retired.json is never read by world.rs), but the current repo file has no such test and no reference to npc_spawns_retired.json exists anywhere under tests/. The body could not be read, so it is not classified as removable. Conservative keep, since it is a refusal/security-style check and no equal test was named."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Discrepancy: the pack says the file is 378 lines with two tests, but the repo file is 259 lines and contains only npc_spawn_models_names_positions_and_capture_matches_are_valid. The pack's second test (retired_legacy_spawns_stay_out_of_the_world) does not exist in the repo at this tip, so it may be stale or unmerged. Reconcile the pack with the tip before acting. The pack's excerpt also appears to match the 259-line file, so the excerpt is not from the 378-line version. Neither test is redundant with a named test elsewhere."}
