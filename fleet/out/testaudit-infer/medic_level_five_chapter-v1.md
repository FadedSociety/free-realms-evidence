<!-- fleet job=testaudit-infer id=medic_level_five_chapter-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[23468, 18360, 8, 2152] model=claude-haiku-5-5 -->
# tests/medic_level_five_chapter.rs

{"file": "tests/medic_level_five_chapter.rs",
 "tests": [
  {"name": "gordon_offers_palatable_pills_after_house_call_only_to_medics", "verdict": "keep", "covered_by": null, "reason": "Job-gate and prerequisite refusal for the Palatable Pills offer, plus authored record shape (visit_position + talk, no gather goal). Medic-specific content; no equivalent test for 3090004 elsewhere in the sampled files."},
  {"name": "the_queensfields_visit_and_naia_talk_pay_once", "verdict": "keep", "covered_by": null, "reason": "Full Palatable Pills chain: outside-radius refusal, in-radius visit, save/reconnect round trip, job switch not receiving Medic XP, and replay paying nothing. Asserts reconnect and persistence, so it must be kept."},
  {"name": "gordon_offers_achieve_level_five_only_at_rank_five", "verdict": "keep", "covered_by": null, "reason": "Pins the min_level 5 gate (rank 4 refused with state and save unchanged, rank 5 offers 3090006) and the one-time payout. Only check of the 3090006 level gate."},
  {"name": "refusals_and_reconnect_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal and reconnect canary for the Medic chain (missing prerequisite, wrong NPC, replayed packet). Same name as tests in blacksmith_first_order, missing_sisters_quest and scavenger_hunt_quest, but drives different quests and content; no equally strong duplicate found."},
  {"name": "surgical_precision_stays_disabled", "verdict": "keep", "covered_by": null, "reason": "Guard that 3090007 and every later Medic record stay disabled and are not offered. Content-closure check with no equivalent elsewhere."},
  {"name": "a_second_medic_does_not_share_progress", "verdict": "keep", "covered_by": null, "reason": "Per-character isolation: second Medic does not inherit chapter progress or pay. Security-style isolation check; keep."},
  {"name": "a_failing_quest_event_for_one_player_does_not_stop_the_other", "verdict": "keep", "covered_by": null, "reason": "Per-player failure isolation (near-cap wallet refusal for one player must not stop the other). Same name as tests in blacksmith_first_order, local_hero_quest and others, but uses Medic quests and the wallet/profile cap path; not duplicated."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Excerpt was truncated, and I read only the bodies of the Queensfields, Level Five, refusals, Surgical Precision, second-Medic and failing-event tests (lines ~430-1130), so the first two tests and the tail of the file were not inspected in detail. Every test in this file exercises Medic-specific content (3090004/3090006 and the disabled 3090007 gate) and asserts persistence, refusal or isolation, so none is marked removable. The same-named tests in other files target different quests. I did not compare the cross-file helper duplicates line by line, so a shared-helper overlap is possible but unverified."}
