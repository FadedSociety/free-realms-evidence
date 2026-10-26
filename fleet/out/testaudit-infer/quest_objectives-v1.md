<!-- fleet job=testaudit-infer id=quest_objectives-v1 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[27016, 17652, 8, 2431] model=claude-haiku-5-5 -->
# tests/quest_objectives.rs

{"file": "tests/quest_objectives.rs",
 "tests": [
  {"name": "collect", "verdict": "keep", "covered_by": null, "reason": "Per-kind check that a wrong CollectItem event is ignored and the right one advances and completes. Partly overlaps quest_engine.rs::all_six_requested_objective_kinds_increment_counters, but that test does not cover the wrong-event refusal or the stop-after-complete check, so it is not a strict superset."},
  {"name": "equip", "verdict": "keep", "covered_by": null, "reason": "EquipItem kind is not exercised by any other named test in the similar files; the wrong-definition refusal is unique to this file."},
  {"name": "gather", "verdict": "keep", "covered_by": null, "reason": "GatherResource advance and refusal checked only here among the similar files."},
  {"name": "craft", "verdict": "keep", "covered_by": null, "reason": "CraftRecipe advance and refusal checked only here among the similar files."},
  {"name": "minigame", "verdict": "keep", "covered_by": null, "reason": "FinishMinigame advance and wrong-id refusal; quest_engine.rs::all_six covers the increment but not the wrong-event refusal or overshoot-stop, so keep."},
  {"name": "area", "verdict": "keep", "covered_by": null, "reason": "EnterArea wrong/right event check with overshoot stop; closest is quest_engine.rs::all_six which lacks the refusal assertion."},
  {"name": "reach", "verdict": "keep", "covered_by": null, "reason": "ReachPoi advance and refusal, not covered elsewhere in the similar files."},
  {"name": "position_radius_and_zone", "verdict": "keep", "covered_by": null, "reason": "Checks radius boundary (1.01 refused), zone mismatch, and NaN position rejection with no state change. Hostile-input and boundary check; unique here."},
  {"name": "no_offered_content_quest_has_zero_objectives", "verdict": "keep", "covered_by": null, "reason": "Content-wide canary scanning every shipped quest JSON for hollow enabled quests. quest_engine.rs::empty_objective_quest_cannot_be_offered_or_turned_in uses only a synthetic definition, so it does not cover the shipped data. Keep as canary."},
  {"name": "split_json_kinds_reach_active_engine_and_disabled_flag_blocks_offers", "verdict": "keep", "covered_by": null, "reason": "Parses every split-JSON goal kind into the live engine, checks persistence round-trip via restored state, and checks the disabled flag blocks offers. Overlaps quest_engine.rs::split_quest_locale_ids and enabled_split_quests tests only at the loader level, not the per-kind JSON mapping. Keep."},
  {"name": "invalid_runtime_json_is_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile/invalid goal JSON refusal (zero quantity, zero recipe, overflow count, negative id, zero radius, oversized radius). Refusal check; no equivalent named test found."},
  {"name": "former_hollow_save_preserves_completion_and_resets_only_unearned_progress", "verdict": "keep", "covered_by": null, "reason": "Save migration/persistence check: resets bogus progress, clears pending turn-in, preserves completion and repairs over-counts. Persistence check; keep."},
  {"name": "disabling_a_pending_offer_clears_it_before_reload_acceptance", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a pending offer is cleared on reload when content is disabled and cannot then be accepted. Security/refusal style; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Every test here drives the split-content loader or per-kind objective paths that the similar files only partly cover. The closest overlap is quest_engine.rs::all_six_requested_objective_kinds_increment_counters (collect, area, minigame increments) and quest_engine.rs::empty_objective_quest_cannot_be_offered_or_turned_in (synthetic version of the no_offered canary). Those overlaps are partial: this file adds wrong-event refusals, overshoot stops, boundary and NaN checks, and shipped-data scans. I did not read the other similar files in full, so no superseded verdicts were given. Nothing is removable with confidence."}
