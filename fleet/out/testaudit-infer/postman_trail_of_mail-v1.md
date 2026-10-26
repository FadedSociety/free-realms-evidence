<!-- fleet job=testaudit-infer id=postman_trail_of_mail-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[32114, 15359, 10, 1977] model=claude-haiku-5-5 -->
# tests/postman_trail_of_mail.rs

{"file": "tests/postman_trail_of_mail.rs",
 "tests": [
  {"name": "postmaster_lane_pays_trail_of_mail_once", "verdict": "keep", "covered_by": null,
   "reason": "Overlaps postman_trainer.rs::a_new_player_learns_postman_at_flitter_and_is_paid_for_trail_of_mail (same quest 3130032, same offer/accept/Talk/49/13/finish, 5 coin/5 XP, replayed 49/14 changes nothing, relog keeps paid state). But this test uniquely pins the pending-turn-in persistence across reload before 49/14, the production relog re-send of 49/13 after the speaker's 35/2 (spawn-before-end ordering, speaker id, debrief text, 99-byte no-display-row bundle), and the completed-ledger reload. Those are not checked elsewhere, so keep."},
  {"name": "a_locked_postman_profile_is_paid_nothing", "verdict": "superseded", "covered_by": "tests/quest_job_xp.rs::locked_profile_turnin_is_refused_cleanly",
   "reason": "Same refusal mechanism: a reward naming a profile the character has not unlocked is refused at turn-in by the job gate, the end screen is released with no completion packet, no coins or profile XP are paid, and the quest stays Active with the Talk counted. quest_job_xp drives it on Ranger Requisition with a Chef profile and a legacy-profile rewrite, so it asserts the same or more. Residual difference: this test uses the opening save (Postman locked from the start) on 3130032. Moderate confidence because the locked-profile setup differs."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The file's value is mainly the relog re-send of the held 49/13 end screen (production gateway path) and pending turn-in persistence, which nothing else checks. Only the locked-profile test is substantially covered elsewhere. The content-level Postman learn path is in postman_trainer.rs (T407), which also records that the Trail of Mail reward was previously unpayable without a trainer row; the locked-profile test's doc comment says the gate has no job requirement on 3130032 and points to notes/Autopilot/F365.md, which I did not read. Other similar files (derby_route, zone_quests_seaside_thunder_falls, wizard_sticky_spell_book, miner_first_ore) cover other quests and were not compared line-by-line."}
