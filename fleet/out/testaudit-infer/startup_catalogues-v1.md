<!-- fleet job=testaudit-infer id=startup_catalogues-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[21976, 13855, 8, 2256] model=claude-haiku-5-5 -->
# tests/startup_catalogues.rs

{"file": "tests/startup_catalogues.rs",
 "tests": [
  {"name": "mapped_catalogue_and_status_messages_reproduce_the_private_capture", "verdict": "keep", "covered_by": null, "reason": "Only byte-level oracle for the captured startup packets (item definitions, coin store lists, ability set, effect tags, stat update, overworld flag, announcement, opcode 14 marker). Ignored by default because it needs the private OSFR_GATEWAY_REFERENCE capture, so it does not run in the normal suite; no equivalent elsewhere. Carries a deliberate T437 (R) deviation (closeWindow vs Exit) that must not be dropped."},
  {"name": "synthetic_item_definitions_change_count_and_records", "verdict": "keep", "covered_by": null, "reason": "Checks count field and record concatenation for build_item_definitions. No other test file drives this builder (grep finds only this file). Not clearly covered."},
  {"name": "synthetic_coin_store_lists_change_with_content", "verdict": "keep", "covered_by": null, "reason": "Only synthetic check of coin store list layout (count, id, words, flags, trailing zero count). Only this file calls build_coin_store_item_lists."},
  {"name": "synthetic_ability_set_changes_id_and_entry_count", "verdict": "keep", "covered_by": null, "reason": "Checks id and entry-count fields for build_ability_set_definition; no other test in the repo calls this builder."},
  {"name": "synthetic_effect_tag_changes_id_and_definition_blob", "verdict": "keep", "covered_by": null, "reason": "Checks id, length and blob placement for build_effect_tag with varying blob lengths. tests/piece_056.rs::<captured effect-tag test> checks only equality with two retail rows (startup[7..] == packet), which does not cover the synthetic length/blob-size layout. Partial overlap only, so kept."},
  {"name": "synthetic_stat_update_changes_target_and_rows", "verdict": "keep", "covered_by": null, "reason": "Checks 64-bit guid split, row count, integer and float value kinds for build_stat_update. Only this file calls the builder."},
  {"name": "synthetic_overworld_combat_flag_changes_only_the_known_flag", "verdict": "keep", "covered_by": null, "reason": "Checks the single known flag byte and the zeroed guid for build_overworld_combat_flag. Tiny, but the only check of the builder's layout; conservative keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The file is a builder layout suite for startup_catalogues. The synthetic tests are shallow change-detection checks (assert_ne plus a few field reads), so they are weak, but none is a clear duplicate: sibling files startup_world.rs and startup_selfdata.rs test other startup builders with their own synthetic_* names, and piece_056.rs only touches build_effect_tag through a captured-row equality. The ignored capture test is the only byte oracle and must stay. Possible future consolidation: fold the synthetic tests into one table-driven test, but that is a refactor, not a removal."}
