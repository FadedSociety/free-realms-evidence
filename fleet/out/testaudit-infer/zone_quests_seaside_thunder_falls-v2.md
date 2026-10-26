<!-- fleet job=testaudit-infer id=zone_quests_seaside_thunder_falls-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[11105, 11960, 6, 1201] model=claude-haiku-5-5 -->
# tests/zone_quests_seaside_thunder_falls.rs

{"file": "tests/zone_quests_seaside_thunder_falls.rs",
 "tests": [
  {"name": "a_postman_runs_the_level_ten_gate_and_is_paid_once", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end test of quest 3130017 (Enve LeStamp, Postman level 10): gate, single coin payment from the data, no job XP, and no duplicate 49/14. job_level_quest.rs covers the same objective mechanism for the Warrior quest W5, which is a different quest, actor and reward."},
  {"name": "short_of_the_gate_nothing_completes_or_pays", "verdict": "keep", "covered_by": null, "reason": "Refusal check: one rank short must not credit, offer or pay, and an early 49/14 must change nothing. No equivalent for this quest elsewhere."},
  {"name": "another_job_is_not_offered_the_postman_gate", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an Adventurer is not offered the Postman gate and a forged 49/2 changes nothing. Not covered for this quest elsewhere."},
  {"name": "the_gate_survives_a_reconnect", "verdict": "keep", "covered_by": null, "reason": "Persistence check, including a held turn-in across save and reload. job_level_quest.rs::the_progress_and_reward_survive_a_reload covers W5 only."},
  {"name": "accepting_at_the_gate_rank_completes_at_once", "verdict": "keep", "covered_by": null, "reason": "Checked job_level_quest.rs::accepting_at_level_five_completes_immediately (lines 401-415): it only asserts counts [1], unchanged profile XP and objective_complete on accept. It does not run the Talk, the 49/13 end screen, the coin payment, the 49/14 settle or the Completed status, which this test does. So it is not the same path and is not superseded. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Every test checks a distinct path for quest 3130017, which no other file drives end to end. The prior superseded verdict on accepting_at_the_gate_rank_completes_at_once was wrong because its cover stops before the turn-in and payment, as the critique said. The shared overlap with job_level_quest.rs is the job_level objective mechanism only, on a different quest and reward. No duplicates or obsolete tests found. Judged from the excerpt and the cited cover test, not from a full suite run."}
