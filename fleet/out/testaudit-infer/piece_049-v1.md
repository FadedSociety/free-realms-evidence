<!-- fleet job=testaudit-infer id=piece_049-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[21738, 18509, 8, 1665] model=claude-haiku-5-5 -->
# tests/piece_049.rs

{"file": "tests/piece_049.rs",
 "tests": [
  {"name": "four_creator_character_types_bind_to_the_pc_models", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the four creator character type rows (ids, name ids, model files, race ids). No other test file references CHARACTER_TYPES or the Models.txt PC rows."},
  {"name": "categories_carry_one_mapping_type_and_the_recovered_row_counts", "verdict": "keep", "covered_by": null, "reason": "Only check of the nine creator categories and their per-type row/exclusion counts (253 total, 12 excluded). Not repeated elsewhere."},
  {"name": "twelve_rows_are_excluded_and_they_are_the_class_one_family", "verdict": "keep", "covered_by": null, "reason": "Asserts the twelve excluded creator rows and their class-1 definition/mapping ids. Related allow-list behaviour in tests/creator_allow_list.rs is a server-side check on pinned tables, not this recovered exclusion set, so not a duplicate. Keep as the canary for the exclusion evidence."},
  {"name": "wire_level_lookups_reject_only_the_recovered_unsupported_ids", "verdict": "keep", "covered_by": null, "reason": "Refusal check: confirms skin tone and head lookups reject only the recovered ids and that head id 4 stays an unreported gap. Refusal-type test with no equal counterpart found in the suite."},
  {"name": "unreachable_mapping_rows_are_reported_per_type", "verdict": "keep", "covered_by": null, "reason": "Pins the 223 offered mapping rows and per-type unreachable counts (49 total). Only source for these figures; keep as the reporting canary."},
  {"name": "module_invariants_hold", "verdict": "keep", "covered_by": null, "reason": "Runs the module's validate() self-check. Cheap, and it is the only call to validate() in the suite; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Self-contained #[path] include of src/restoration/piece_049.rs. Searches of tests/ for the creator character types, IS_VALID_FOR_PC, the excluded 78086-78091 definition ids, skin_tone_exclusion/head_exclusion and the 223/49 mapping counts found no other test driving these functions. Nearest similar files (piece_032, piece_097, piece_059, harvesting, piece_040) cover different data sets. Fixed-count assertions (253, 223, 49) will need updating whenever the recovered tables change, but that is maintenance cost, not redundancy."}
