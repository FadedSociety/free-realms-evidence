<!-- fleet job=testaudit-infer id=collection_nodes_content-v1 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[34129, 13027, 10, 2722] model=claude-haiku-5-5 -->
# tests/collection_nodes_content.rs

{"file": "tests/collection_nodes_content.rs",
 "tests": [
  {"name": "collection_nodes_load_with_the_imported_counts_and_unique_ids", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the imported collection-node counts (12/34/847), unique ids and finite spawn positions; no similar file loads collection_nodes.json."},
  {"name": "pools_reference_types_and_spawns_fit_the_caps_and_respawn_policy", "verdict": "keep", "covered_by": null, "reason": "Only check of the collection-node pool invariants (type references, cap <= spawn count, rare 300s / common 60s respawn). harvest_nodes.rs checks different fields on the Legacy file."},
  {"name": "data_canary_central_flowers_and_the_sanctuary_only_fields", "verdict": "keep", "covered_by": null, "reason": "Explicit canary on the Sanctuary-only central flowers pool and the composite/sub-text fields; nothing else checks these values."},
  {"name": "every_drop_item_resolves_to_one_entry_or_is_a_listed_gap", "verdict": "keep", "covered_by": null, "reason": "Checks drop items against the collection catalogue and the listed gap set. collection_catalogue.rs::every_bound_item_has_a_runtime_definition checks a different direction (catalogue bindings to runtime definitions), so this is not a duplicate."},
  {"name": "legacy_mushroom_and_mining_files_still_load_with_the_new_fields_defaulted", "verdict": "keep", "covered_by": null, "reason": "Asserts the new fields default on legacy files (empty extra effects, no sub-text, empty drop tables on pools). Its count assertion (2,2,76) overlaps tests/harvest_nodes.rs::loaded_harvest_nodes_have_valid_references_and_finite_spawns, but the default-field and mining assertions are not covered there. Kept as a backward-compatibility check."},
  {"name": "collection_nodes_are_dormant_for_the_gathering_loader", "verdict": "keep", "covered_by": null, "reason": "Negative check that GatheringNodes::load ignores collection_nodes.json, with a positive control on the Legacy file. This is a refusal-style check that no other test in the similar set makes."},
  {"name": "provenance_and_policy_tags_are_present", "verdict": "keep", "covered_by": null, "reason": "Provenance tag check; the body was not visible in the pack (the excerpt cuts off mid-test) and no similar file covers it. Kept by default."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Low confidence: the file's last test body was cut off in the excerpt, and the repository search found neither tests/collection_nodes_content.rs nor data/content/collection_nodes.json, so I could not read the full file or confirm the data it checks. The only overlap found is the legacy-count assertion shared with tests/harvest_nodes.rs. The most similar files (housing_service, fishing_entry, progression_extras, item_bar, collection_catalogue) cover unrelated behaviour, apart from collection_catalogue's catalogue-link checks, which the drop-item test does not repeat."}
