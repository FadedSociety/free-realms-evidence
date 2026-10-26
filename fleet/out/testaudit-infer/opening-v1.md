<!-- fleet job=testaudit-infer id=opening-v1 status=done turns=3 usd=0.0041 tokens(read,write,in,out)=[30010, 21859, 8, 2219] model=claude-haiku-5-5 -->
# tests/opening.rs

{"file": "tests/opening.rs",
 "tests": [
  {"name": "ordered_progress_survives_reload_and_turnin_rewards_only_once", "verdict": "keep", "covered_by": null, "reason": "Persistence across reload plus reward-once on turn-in and ordered-stage gating. Only test in the pack covering this sequence; the reward-once and reload checks are security-relevant."},
  {"name": "gathering_requires_correct_job_zone_and_proximity", "verdict": "keep", "covered_by": null, "reason": "Refusal test: wrong job, wrong zone and out-of-range gathering must change nothing. Refusal checks are kept by policy."},
  {"name": "discoveries_have_zone_identity_and_persistent_reward_once", "verdict": "keep", "covered_by": null, "reason": "Zone-identity refusal and persisted reward-once across reload. Not clearly covered elsewhere."},
  {"name": "chat_cannot_complete_skip_or_accept_a_remote_step", "verdict": "keep", "covered_by": null, "reason": "Hostile chat-command refusal; state must be unchanged. Security check."},
  {"name": "invalid_events_reject_before_mutating_persisted_state", "verdict": "keep", "covered_by": null, "reason": "Hostile input (zero/overflow quantity, NaN position, negative profile) must error without mutation. Refusal check."},
  {"name": "corrupted_future_progress_reward_flags_and_content_change_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Load-time rejection of tampered save state and changed content. Security and persistence canary."},
  {"name": "journal_exposes_only_saved_counters_and_session_reset_removes_remote_authority", "verdict": "keep", "covered_by": null, "reason": "Journal exposes saved counters only and session reset revokes authority. Likely overlaps with tests/opening_journal.rs, which I did not read, so this is not confirmed as a duplicate; kept conservatively."},
  {"name": "private_opening_content_loads_with_all_objectives_and_verified_actor_references", "verdict": "keep", "covered_by": null, "reason": "Ignored content canary tied to private recovered reference data (counts, rewards, wolf encounters). Cannot be replaced by synthetic tests."},
  {"name": "private_opening_every_stage_is_completable_through_typed_events_and_reward_once_after_reload", "verdict": "keep", "covered_by": null, "reason": "Ignored full-traversal canary over private content with reward-once after reload. Its own doc notes that synthetic traversal is not native proof, so it stays."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The pack's five similar files (kart_service, housing_service, kart_racing, app_fuzz, soccer_match) share no opening-engine surface, so no test-level superseded or duplicate match could be established from them. The only opening-related file I found is tests/opening_journal.rs, which I did not read; it is the place to check the journal test. Other opening use appears in chess_route, cooking_gameplay, forging_gameplay, dev_teleport and the src unit tests in gameplay/t013_objective_events.rs and gameplay/w104_quest_tests.rs, but I did not compare those assertions. Nothing was classed obsolete: the pack gives no later task that replaced opening behaviour. Confidence is low because the comparison set was unrelated and the candidate overlaps were not read."}
