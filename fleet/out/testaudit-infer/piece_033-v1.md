<!-- fleet job=testaudit-infer id=piece_033-v1 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[10025, 14649, 6, 2010] model=claude-haiku-5-5 -->
# tests/piece_033.rs

{"file": "tests/piece_033.rs",
 "tests": [
  {"name": "warrior_job_identity_is_recovered", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the Warrior profile id, locale ids, image sets and trial/members flags from src/restoration/piece_033.rs; no other test in the suite references these WARRIOR_ constants."},
  {"name": "warrior_classes_are_owned_by_warrior_not_brawler", "verdict": "keep", "covered_by": null, "reason": "Only check that Warrior class rows are owned by name id 4664 and that Brawler classes 25/71 are rejected from the Warrior allowlist; a refusal-style boundary check with no equivalent elsewhere."},
  {"name": "warrior_class_allowlist_matches_recovered_profile_packet", "verdict": "keep", "covered_by": null, "reason": "Pins the full allowlist array against the recovered profile packet; no other file exercises WARRIOR_CLASS_ALLOWLIST."},
  {"name": "warrior_creation_kit_is_the_recovered_default_item_list", "verdict": "keep", "covered_by": null, "reason": "Only check of the Warrior DefaultItems creation kit; the similar piece_032 creation-kit test covers a different profile's kit."},
  {"name": "warrior_level_test_equipment_and_gates_are_recovered", "verdict": "keep", "covered_by": null, "reason": "Only check of the Warrior level-test equipment bands and weapon/gear level-gate ladders."},
  {"name": "warrior_equip_checks_ownership_slot_and_level", "verdict": "keep", "covered_by": null, "reason": "Equip refusal test (wrong class, under-level, slot outside spool) for check_warrior_equip; security/refusal check with no equivalent elsewhere."},
  {"name": "warrior_slots_carry_the_recovered_client_names", "verdict": "keep", "covered_by": null, "reason": "Only check of Warrior slot names and weapon flag against EquipmentSlotDefinitions; unique to this module."},
  {"name": "warrior_skills_unlock_at_the_recovered_job_levels", "verdict": "keep", "covered_by": null, "reason": "Only check of Warrior skill unlock levels, rank damage and unlocked_skill_name_ids/skill_unlocked boundaries, including a missing-skill refusal (999999)."},
  {"name": "warrior_weapon_abilities_are_recovered_locale_facts", "verdict": "keep", "covered_by": null, "reason": "Only check of Warrior weapon ability locale ids and tier text; no other test references WARRIOR_WEAPON_ABILITIES."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Every Warrior constant and function used here is referenced only in this file (repo-wide search of osfr-tools). The similar files (piece_032, piece_036, piece_040, piece_042, piece_046) cover other jobs or other pieces and do not drive the piece_033 module paths. Some tests are mostly constant pins (e.g. WARRIOR_CLASSES.len()==4, job name strings), which are weak but are the only checks of recovered data, so kept under the conservative rule. Housekeeping: the file #[path]-includes src/restoration/piece_033.rs with a comment saying it is included until the lead registers the module; once the module is registered the include should be switched to a normal crate import, but that is not a test-redundancy issue. The pack gave no created_by/last_changed_by tasks, so no obsolescence by a later task could be established."}
