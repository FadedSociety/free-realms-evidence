<!-- fleet job=testaudit-infer id=medic_entry_chain-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[11777, 13025, 6, 1783] model=claude-haiku-5-5 -->
# tests/medic_entry_chain.rs

{"file": "tests/medic_entry_chain.rs",
 "tests": [
  {"name": "naia_offers_the_medic_exam_only_to_medics", "verdict": "keep", "covered_by": null, "reason": "Job-11 gate refusal for the Exam offer. No equivalent found in the chapter files reviewed; security/refusal-style check, so keep."},
  {"name": "exam_and_house_call_complete_in_order", "verdict": "keep", "covered_by": null, "reason": "Asserts ordering, no reward before turn-in, and that a duplicate 49/14 pays nothing across Exam then House Call. medic_level_five_chapter.rs starts from complete_exam and does not assert this ordering."},
  {"name": "take_your_vitamins_requires_house_call", "verdict": "keep", "covered_by": null, "reason": "Prerequisite refusal (no Vitamins offer before House Call), wrong-giver refusal, and single payment. Not covered by the level-five file, which starts after the Vitamins step."},
  {"name": "medic_xp_goes_to_medic_not_the_active_job", "verdict": "keep", "covered_by": null, "reason": "Profile-routing canary: reward XP follows the Medic profile after a job switch. No equivalent found."},
  {"name": "refusals_and_replay_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal and replay coverage (wrong NPC, forged accepts, out-of-range interact/select, replayed end reply and accept). Security/refusal test; the similarly named level-five test covers a different step."},
  {"name": "relog_preserves_completed_history", "verdict": "keep", "covered_by": null, "reason": "Persistence through the game_store envelope with held 49/13 and pending turn-in speaker (verified in the body near line 700-730). Persistence test; keep."},
  {"name": "two_medics_progress_independently", "verdict": "keep", "covered_by": null, "reason": "Previously marked superseded by medic_level_five_chapter.rs::a_second_medic_does_not_share_progress, but that test drives the Palatable Pills chapter (Gordon, sunflower visit), not the Medic Exam. This test is the only check that two Medics each complete the Exam once, pay EXAM_COINS, and route EXAM_XP to the Medic profile. Not removable on the evidence available."},
  {"name": "enabled_medic_chapter_records_are_complete_and_others_stay_disabled", "verdict": "duplicate", "covered_by": "tests/medic_entry_content.rs::enabled_medic_chapter_records_are_complete_and_others_stay_disabled", "reason": "Both call medic_entry::assert_enabled_medic_chapter_records() under the same name; the content file is the intended home for this check. Removing the chain copy loses no assertion."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Only one removal is backed: the content-check duplicate at medic_entry_chain.rs:892. The earlier superseded verdict for two_medics_progress_independently is withdrawn because its named cover exercises a different quest chain (Palatable Pills, not the Exam). The seven remaining tests are keeps. The superseded replacement was not re-verified against the full body of a_second_medic_does_not_share_progress beyond the chain-vs-pills distinction."}
