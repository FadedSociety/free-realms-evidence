<!-- fleet job=testaudit-infer id=job_basic_attacks-v1 status=no_submit turns=3 usd=0.0034 tokens(read,write,in,out)=[22487, 15036, 8, 2524] model=claude-haiku-5-5 -->
# tests/job_basic_attacks.rs

```json
{"file": "tests/job_basic_attacks.rs",
 "tests": [
  {"name": "shipped_rows_name_each_jobs_starter_weapon", "verdict": "keep", "covered_by": null,
   "reason": "Pure data check of the shipped opening-abilities basic rows (weapon_definition_id and weapon_class per job). weapon_requirements::shipped_combat_rows_require_each_jobs_weapon_class and opening_abilities::frozen_basic_rows_inherit_the_canonical_starter_weapon look similar, but I did not confirm they assert the exact definition ids, so it is kept as the conservative choice."},
  {"name": "clothed_warrior_without_a_weapon_gets_the_starter_cudgel", "verdict": "keep", "covered_by": null,
   "reason": "Unique check of the reconstructed (R) fallback: a clothed warrior with no weapon receives the starter cudgel. The file header ties it to this fallback, and no similar test was seen to cover it."},
  {"name": "each_job_row_casts_its_skill_from_its_unlock_level", "verdict": "keep", "covered_by": null,
   "reason": "Drives the real 36/10 bar-1 request for every available skill at its unlock level, checks the cast packet and the composite effect id, and checks that rows 4-7 are refused with no state change. opening_abilities::job_rows_past_the_fourth_button_or_doubled_are_refused only tests loader rejection, not the request path. The refusal and canary aspects make it unsafe to remove."},
  {"name": "unequipped_basic_is_refused_without_combat_change", "verdict": "keep", "covered_by": null,
   "reason": "Refusal test: a basic attack with the weapon unequipped produces no hit and leaves combat state unchanged. weapon_requirements::private_fresh_outfits_cast_wrong_or_missing_weapons_refuse_every_route is the closest equivalent, but I did not confirm it asserts state equality on the same path, so this is kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The file is a T010 starter-weapon kill test, extended by T421 with a ladder cast test and an unequipped refusal. Its job-kill tests (the starter_test! macro) and its helper fixture are not in the listed test names, so the pack may be truncated. The strongest overlap is with tests/weapon_requirements.rs (missing or wrong weapon refused on every route, and shipped combat rows requiring each job's weapon class), and with tests/opening_abilities.rs (ladder and rows past the fourth button). I did not read those tests' bodies in full, so the verdicts stay keep. Re-check the two refusal tests against weapon_requirements before removing anything. Not removable as a whole."}
```
