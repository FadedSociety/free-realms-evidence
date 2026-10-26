<!-- fleet job=testaudit-infer id=job_ability_bars-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[18775, 12722, 8, 1718] model=claude-haiku-5-5 -->
# tests/job_ability_bars.rs

{"file": "tests/job_ability_bars.rs",
 "tests": [
  {"name": "switching_jobs_keeps_each_jobs_level_and_unlocked_bar", "verdict": "keep", "covered_by": null, "reason": "Only test that drives Profiles::select through a long mixed switch sequence (including Adventurer 1 and back) while asserting that experience is unchanged after every switch and that each job's activation bar is identical afterwards. Related checks exist but none combine them: opening_abilities.rs::every_job_bar_has_exactly_the_unlocked_ladder_at_every_level checks bars by level without switching; opening_abilities.rs::noncombat_class_clears_all_eight_slots_and_invalid_profile_fails checks only the Adventurer activation against a vector, not a switch from a combat bar; tests/profiles.rs (select around line 310-320) selects jobs but I did not confirm it asserts experience invariance over the full cycle. Brawler row layout at level 5 (T421) overlaps opening_abilities.rs brawler_level_boundaries, but it is a small part of this test."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Single test, classified keep because it is the only switching/persistence check across all seven jobs. Overlap is partial: the level-ladder and Adventurer-clears-slots assertions are largely duplicated in tests/opening_abilities.rs (every_job_bar_has_exactly_the_unlocked_ladder_at_every_level, noncombat_class_clears_all_eight_slots_and_invalid_profile_fails, brawler_level_boundaries). If the team wants to trim, the Brawler and Adventurer blocks are the removable parts, but the test as a whole should stay. Did not read tests/profiles.rs in full, so the experience-invariance overlap there is unverified."}
