<!-- fleet job=testaudit-infer id=job_trainers-v1 status=done turns=3 usd=0.0042 tokens(read,write,in,out)=[28108, 20826, 8, 2690] model=claude-haiku-5-5 -->
# tests/job_trainers.rs

{"file": "tests/job_trainers.rs",
 "tests": [
  {"name": "trainer_rows_match_the_job_and_spawned_npc_content", "verdict": "keep", "covered_by": null, "reason": "Content-integrity check over every shipped trainer row against the job and NPC data; the only check of that cross-file consistency in this file. Not read in full."},
  {"name": "malformed_trainer_files_are_refused_at_load", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed input refusal at load; security-style check, kept by default."},
  {"name": "each_listed_trainer_offers_the_job_and_unlocks_it_once", "verdict": "keep", "covered_by": null, "reason": "Matrix over every listed trainer; per-job files (derby_chapter, fisherman_entry_chain, card_duelist_trainer) cover only single jobs, so this is not a duplicate."},
  {"name": "service_refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check (changes nothing); keep."},
  {"name": "an_ordinary_player_learns_each_trainers_job_once_and_only_switches_to_a_complete_outfit", "verdict": "keep", "covered_by": null, "reason": "Ordinary-player gateway path with outfit completeness; not found elsewhere in this exact form."},
  {"name": "learning_a_starter_grant_counts_each_item_once", "verdict": "keep", "covered_by": null, "reason": "Canary-like check that a starter grant raises a quest count once; unique to this file (synthetic collect quest)."},
  {"name": "an_outfit_grant_error_leaves_the_trainer_menu_usable", "verdict": "keep", "covered_by": null, "reason": "Error-path rollback check; keep."},
  {"name": "selecting_an_unlocked_job_without_an_outfit_is_refused_atomically", "verdict": "keep", "covered_by": null, "reason": "Atomic refusal check; keep."},
  {"name": "gateway_refusals_leave_the_save_untouched", "verdict": "keep", "covered_by": null, "reason": "Refusal/persistence check through the gateway; keep."},
  {"name": "without_the_content_file_nobody_offers_a_job", "verdict": "keep", "covered_by": null, "reason": "Absent-content refusal check; keep."},
  {"name": "selecting_a_bare_unlocked_job_emits_an_activation_from_the_repaired_outfit", "verdict": "keep", "covered_by": null, "reason": "F155 regression guard for the activation packet after starter repair; no other file asserts the 38/21 slot list after repair."},
  {"name": "learning_does_not_increase_owned_starter_quantities", "verdict": "keep", "covered_by": null, "reason": "F155 no-free-regrant check; unique."},
  {"name": "a_failed_bundle_keeps_the_trainer_menu_usable", "verdict": "keep", "covered_by": null, "reason": "F155 bundle rollback check; rollback of staged state is a refusal-type guarantee; keep."},
  {"name": "two_talk_choices_in_one_bundle_both_reach_the_open_menu", "verdict": "keep", "covered_by": null, "reason": "S15 regression for staging of multiple choices in one bundle; keep."},
  {"name": "all_six_combat_jobs_learn_activate_fight_and_gain_xp", "verdict": "keep", "covered_by": null, "reason": "Six-job end-to-end matrix (learn, activate, fight, XP); broader than any single-job test; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Partial review: read the bodies of the F155/S15 tests and the six-job matrix, plus the test list. Did not read every test body (e.g. the service-level matrix and refusal tests), so verdicts for those rest on names and doc lines. Similar files (derby_chapter.rs, fisherman_entry_chain.rs, card_duelist_trainer.rs) test single jobs' trainers and do not drive the same multi-job matrix, so no superseded or duplicate verdicts were supported. The file is a shared matrix over all trainer rows and should not be removed wholesale. A possible follow-up is to check whether the service-level tests in the first half duplicate each other row by row."}
