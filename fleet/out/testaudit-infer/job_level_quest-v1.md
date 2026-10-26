<!-- fleet job=testaudit-infer id=job_level_quest-v1 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[20196, 12929, 8, 2826] model=claude-haiku-5-5 -->
# tests/job_level_quest.rs

{"file": "tests/job_level_quest.rs",
 "tests": [
  {"name": "the_record_loads_and_offers_to_a_warrior", "verdict": "keep", "covered_by": null, "reason": "Loads the W5 record and checks the Steele offer for the new job_level objective; the only check of the W5 record offer path. Similar warrior_entry_chain tests cover W1/W4, not this gate."},
  {"name": "real_xp_to_level_five_completes_it_once", "verdict": "keep", "covered_by": null, "reason": "Drives real field-kill job XP to rank 5 and asserts single completion; the only end-to-end check of the job_level objective being credited from XP. Shared kill path is not tested for level gating elsewhere."},
  {"name": "the_developer_level_command_completes_it_too", "verdict": "keep", "covered_by": null, "reason": "Exercises the 'realm level' dev path to the same objective; distinct entry point from the XP path, not a duplicate of it."},
  {"name": "accepting_at_level_five_completes_immediately", "verdict": "keep", "covered_by": null, "reason": "Pins immediate completion on accept when the level is already met; unique to this objective kind."},
  {"name": "a_higher_rank_still_completes_it", "verdict": "keep", "covered_by": null, "reason": "Checks the at-least comparison for ranks above the target; unique boundary check for job_level."},
  {"name": "a_job_level_event_is_profile_exact_and_uses_at_least", "verdict": "keep", "covered_by": null, "reason": "Profile-exactness and at-least semantics of the event; unique to job_level events and a refusal-style check."},
  {"name": "a_reconnect_at_a_late_level_completes_it_on_load", "verdict": "keep", "covered_by": null, "reason": "Persistence/reload check that completion is applied on load; canary-like for the new objective, not covered by other files."},
  {"name": "another_profile_and_another_player_are_not_credited", "verdict": "keep", "covered_by": null, "reason": "Security/isolation check (other profile, other player must not be credited); keep per policy."},
  {"name": "a_live_change_before_the_turn_in_survives", "verdict": "keep", "covered_by": null, "reason": "Persistence check that a live level change before turn-in is kept. Same name exists in investigate_the_wolves.rs but drives a different objective and path; not the same assertions, so not a duplicate."},
  {"name": "a_near_cap_wallet_refuses_the_turn_in_atomically", "verdict": "keep", "covered_by": null, "reason": "Refusal check that a full wallet refuses atomically. Similar limit-refusal exists in quest_turnin_feedback.rs::a_near_cap_wallet_is_a_limit_refusal_that_keeps_the_end_screen but it asserts the end-screen feedback, not atomic non-payment; keep."},
  {"name": "the_progress_and_reward_survive_a_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence check for progress and reward across reload; keep per policy."},
  {"name": "refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; same name exists in sheep_watch_dungeon.rs and station_cash.rs but on other quests and paths. Not confirmed equivalent, so keep."},
  {"name": "a_quest_turn_in_job_xp_completes_it_too", "verdict": "keep", "covered_by": null, "reason": "Checks that the quest turn-in reward job XP also satisfies the objective; distinct route from the kill/dev-command paths."},
  {"name": "a_malformed_job_level_goal_is_a_load_error", "verdict": "keep", "covered_by": null, "reason": "Refusal/hostile-input load check (bad profile, level bounds, duplicate ids, missing provenance, ordering). Refusal check; warrior_entry_chain.rs::a_malformed_warrior_record_fails_at_load covers different malformations (ids, source, caps) and is not an equivalent test. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Partial review: I read the test names, the excerpt, the bodies of the load-error test and a few named tests only, plus search hits for same-named tests in chat_settings, sheep_watch_dungeon, station_cash and quest_turnin_feedback. The file is the sole coverage of the job_level objective and the W5 gate, so no test was found superseded or obsolete. Same-named tests elsewhere (refusals_change_nothing, a_live_change_before_the_turn_in_survives, a_near_cap_wallet...) test different quests or paths and were not confirmed equivalent. Verdicts are conservative; a deeper body-by-body comparison was not done."}
