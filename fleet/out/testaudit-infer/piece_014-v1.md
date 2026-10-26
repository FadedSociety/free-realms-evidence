<!-- fleet job=testaudit-infer id=piece_014-v1 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[8364, 12002, 6, 1855] model=claude-haiku-5-5 -->
# tests/piece_014.rs

{"file": "tests/piece_014.rs",
 "tests": [
  {"name": "pattern_catalogue_matches_recovered_class58_records", "verdict": "keep", "covered_by": null, "reason": "Pins the 28-entry pattern catalogue in src/restoration/piece_014.rs. piece_040 checks a different module (its own RECIPE_ITEMS, 49 rows), and only partly overlaps on records 2506 and 869, so it is not the same path."},
  {"name": "spunky_family_is_one_weapon_definition_with_ten_tints", "verdict": "keep", "covered_by": null, "reason": "Only test in the pack that checks the ten hammer variants 30280-30289 as one definition, plus the substitute mallet and Blacksmith tool records. No similar file asserts these."},
  {"name": "item_class_owners_follow_the_recovered_profile_column", "verdict": "keep", "covered_by": null, "reason": "Checks class-to-profile ownership for classes 58, 71, 34 and 25. piece_040 covers classes 58 and 59 through shard_class, a different function, so this is not a duplicate."},
  {"name": "blacksmith_crafts_the_pattern_but_only_brawler_equips_the_hammer", "verdict": "keep", "covered_by": null, "reason": "Equip-permission check that rejects a wrong-profile equip. It is a refusal check, and no equally strong test elsewhere was found."},
  {"name": "slot_seven_is_the_recovered_weapon_slot", "verdict": "keep", "covered_by": null, "reason": "Pins the slot-7 weapon definition and per-profile slot lists. Not seen elsewhere in the pack."},
  {"name": "unknown_definitions_profiles_and_slots_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Fail-closed refusal check for unknown definition, profile and definition ids. Keep as a refusal test."},
  {"name": "a_profile_without_the_weapon_slot_rejects_the_hammer", "verdict": "keep", "covered_by": null, "reason": "Refusal check using a fixture profile without the weapon slot. Unique to this file."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Based on the pack and a partial read of tests/piece_040.rs only. piece_040::recipe_catalogue_is_the_recovered_class_58_and_59_records overlaps lightly with pattern_catalogue_matches_recovered_class58_records (records 2506 and 869), but the two tests target different modules, so I kept both. piece_033 covers warrior equip rules, a different job, so it does not supersede the equip tests here. Nothing in this file looks obsolete. I did not read the source modules, so the overlap call rests on test names and the assertions I read."}
