<!-- fleet job=testaudit-infer id=l052_staff_jobs-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[28143, 17754, 8, 1750] model=claude-haiku-5-5 -->
# tests/l052_staff_jobs.rs

{"file": "tests/l052_staff_jobs.rs",
 "tests": [
  {"name": "staff_jobs_come_from_the_login_role_and_go_with_a_demotion", "verdict": "keep", "covered_by": null, "reason": "Only check that staff jobs are granted from the login role, absent for players, and vanish after a demotion-and-reload; persistence and role-security behaviour. role_enforcement.rs covers role persistence generally but not the staff job list."},
  {"name": "a_spoofed_staff_job_select_is_refused_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Security refusal: a player (and a demoted moderator) selecting a staff job is refused and state is unchanged. No equivalent staff-job refusal found elsewhere."},
  {"name": "a_moderator_wears_a_staff_job_without_saving_owning_or_levelling_it", "verdict": "keep", "covered_by": null, "reason": "Unique check that a worn staff job is display-only: 38/21 names it, neighbours get the outfit, and the save is unchanged."},
  {"name": "a_staff_job_the_catalogue_cannot_dress_is_refused_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal path for missing outfit pieces and a missing Legs piece; changes nothing. Not found in other files."},
  {"name": "experience_paid_while_a_staff_job_is_worn_goes_to_the_real_job", "verdict": "keep", "covered_by": null, "reason": "Checks XP accrues to the real job while a staff job is worn and that staff jobs never enter unlocked or experience. Specific to L052; miner_first_ore.rs covers XP to profile after a job switch but not staff jobs."},
  {"name": "the_staff_record_has_the_captured_job_layout_in_38_21_and_the_self_data", "verdict": "keep", "covered_by": null, "reason": "Byte-layout canary against the captured 38/21 record and the self-data parser round trip for staff jobs. Not duplicated elsewhere in the similar files."},
  {"name": "staff_jobs_stay_out_of_trainers_and_survive_a_reward_reload", "verdict": "keep", "covered_by": null, "reason": "Refusal that a trainer row cannot name a staff job, plus staff jobs surviving a reward adopt and being absent for a fresh session. Unique to this file as far as the similar files show."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Every test covers a staff-job behaviour (role grant, refusal, display-only wear, wire layout, XP routing, trainer isolation) that the five similar files (vendor_sell, coin_store_siblings, warpstone_travel, npc_interaction, miner_first_ore) do not drive. A grep for REFERER/ENFORCER/staff job across tests/ found no other staff-job tests. role_enforcement.rs uses bind_account_role for role persistence, so there is some adjacency, but it does not assert staff job lists or the 38/21 wear. Confidence is moderate because I only skimmed the similar files and did not read the crate's Profiles or Gateway code."}
