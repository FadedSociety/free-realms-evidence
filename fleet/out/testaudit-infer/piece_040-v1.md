<!-- fleet job=testaudit-infer id=piece_040-v1 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[9557, 14373, 6, 2206] model=claude-haiku-5-5 -->
# tests/piece_040.rs

{"file": "tests/piece_040.rs",
 "tests": [
  {"name": "crafting_jobs_are_the_recovered_chef_and_blacksmith_profiles", "verdict": "keep", "covered_by": null, "reason": "Only check of the job/profile identity table (ids 45/16, name ids, shard class owners) in this module; no other file drives crafting_job/shard_class from src/restoration/piece_040.rs."},
  {"name": "recipe_catalogue_is_the_recovered_class_58_and_59_records", "verdict": "keep", "covered_by": null, "reason": "Pins the 49-record recipe catalogue, per-class counts, unique indices and the single absent MinProfileRank row; unique data check not repeated elsewhere."},
  {"name": "two_recovered_records_cross_the_shard_classes", "verdict": "keep", "covered_by": null, "reason": "Pins the two cross-class anomaly records (869, 2518); a data-quality canary for the recovered source that no other test asserts."},
  {"name": "rank_ladder_is_the_recovered_min_profile_rank_data", "verdict": "keep", "covered_by": null, "reason": "Exact rank-gate ladder for both jobs; only test of rank_gated_recipes ordering and content."},
  {"name": "recipe_access_uses_the_recovered_min_profile_rank", "verdict": "keep", "covered_by": null, "reason": "Rank boundary, floor-0 refusal and clamp-above-maximum behaviour of recipe_access; refusal/boundary checks with no equivalent elsewhere for this module. recipes in tests/recipe_book.rs (rank_too_low_is_refused) exercise a different implementation."},
  {"name": "recipe_access_rejects_the_wrong_job_from_the_recovered_class_owner", "verdict": "keep", "covered_by": null, "reason": "Refusal check (WrongJob owner mismatch) for the class-owner rule; security/refusal check, kept."},
  {"name": "unknown_recipes_and_rows_fail_closed", "verdict": "keep", "covered_by": null, "reason": "Fail-closed refusal check for unknown recipe/row ids; kept by policy for refusal checks."},
  {"name": "wiki_gates_carry_the_tutorial_and_starnut_sundae_rows", "verdict": "keep", "covered_by": null, "reason": "Pins the wiki gate rows and wiki_gate_access outcomes; only test of this data path in the module."},
  {"name": "level_titles_are_the_recovered_locale_rows", "verdict": "keep", "covered_by": null, "reason": "Pins the 10 level-title locale rows and clamping; no other file asserts these rows."},
  {"name": "level_gate_quests_pair_the_chef_and_blacksmith_rank_quests", "verdict": "keep", "covered_by": null, "reason": "Pins level-gate quest ids and objective text from recovered data; only check of level_gate_quest."},
  {"name": "accepted_crafting_profiles_mirror_the_live_services_without_grants", "verdict": "keep", "covered_by": null, "reason": "Asserts the validator enum is allow/refuse only (no grant variant) and the accepted profile mapping; a canary-style no-grant check, kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The file #[path]-includes src/restoration/piece_040.rs directly, so it is the only test driving that module's tables and recipe_access/wiki_gate_access logic. The similar files (piece_032, piece_043, piece_046, piece_033) cover different modules (combat ranks, level-up milestones, consumables, warrior). tests/recipe_book.rs (rank_too_low_is_refused, unknown_recipe_ids_are_refused_without_panic) has overlapping concept but drives a different route/module, so it is not a like-for-like duplicate and was not used to mark anything removable. Pack excerpt was truncated; the tail of the file (wiki gate tests) was read directly. Nothing marked removable; a later consolidation pass could fold the data-table tests into the module's own unit tests, but that is not a redundancy finding."}
