<!-- fleet job=testaudit-infer id=weapon_requirements-v1 status=no_submit turns=4 usd=0.0044 tokens(read,write,in,out)=[45844, 20818, 10, 2615] model=claude-haiku-5-5 -->
# tests/weapon_requirements.rs

```json
{"file": "tests/weapon_requirements.rs",
 "tests": [
  {"name": "current_owned_weapon_class_is_required_and_unequip_revokes_it", "verdict": "keep", "covered_by": null,
   "reason": "Unit-level check of equipped_weapon_matches: other-profile equipment is not authority, a wrong-class owned weapon is refused, and a live 42/2 unequip revokes the gate. Hostile-input and revocation checks. Only the unequip-refusal half overlaps job_basic_attacks::unequipped_basic_is_refused_without_combat_change, and that one works at gameplay level with no class or profile-authority assertions."},
  {"name": "private_fresh_outfits_cast_wrong_or_missing_weapons_refuse_every_route", "verdict": "keep", "covered_by": null,
   "reason": "Refusal test for wrong-class and missing weapons across basic, targeted, self and menu routes, plus mid-fight unequip and every executable skill row. Overlaps job_basic_attacks::each_job_row_casts_its_skill_from_its_unlock_level and the fresh-job starter tests on the happy path, but its wrong-weapon and no-weapon refusals are unique. It is #[ignore]d and needs OSFR_PLAY_PACKAGE."},
  {"name": "scratch_wizard_bot_hits_with_wand_then_unequips_and_is_refused", "verdict": "keep", "covered_by": null,
   "reason": "End-to-end live-gateway check (wand hit, live unequip, then no player attack). It is the only test that runs the real network path, and it asserts a loopback-only gateway. It is #[ignore]d and needs OSFR_W113_REFERENCE and OSFR_W113_GATEWAY."},
  {"name": "shipped_combat_rows_require_each_jobs_weapon_class", "verdict": "keep", "covered_by": null,
   "reason": "Static content check. Its basic-row weapon_class assertion duplicates tests/job_basic_attacks.rs::shipped_rows_name_each_jobs_starter_weapon (same file, same class per profile, which also checks weapon_definition_id). Its per-skill weapon_class check over job_abilities.json is not in job_basic_attacks.rs, which reads only the job rows' slot fields for unlock levels. Kept because the per-slot part is not clearly covered elsewhere; the basic-row half could be dropped in a cleanup."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Only a truncated excerpt of the file's first half was in the pack, so I read the full file myself. The heavy overlap is with tests/job_basic_attacks.rs (fresh-job starter casts, unarmed basic refusal, per-row skill casts, shipped basic weapon_class rows) and tests/opening_abilities.rs (row/unlock content checks). I did not read opening_abilities.rs beyond its test names, so the per-slot weapon_class check in the last test was not compared against it. Three of the four tests are #[ignore]d and need external packages or a live gateway, so they do not run in the default suite. The one test that can cheaply be trimmed is the basic-row half of shipped_combat_rows_require_each_jobs_weapon_class. The whole file is not removable."}
```
