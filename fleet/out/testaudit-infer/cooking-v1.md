<!-- fleet job=testaudit-infer id=cooking-v1 status=done turns=2 usd=0.0038 tokens(read,write,in,out)=[10876, 20305, 6, 2349] model=claude-haiku-5-5 -->
# tests/cooking.rs

{"file": "tests/cooking.rs",
 "tests": [
  {"name": "captured_native_go_sentinel_starts_only_the_matching_offered_instance", "verdict": "keep", "covered_by": null, "reason": "Pins a captured native frame (cooking_start vector) and refusal of wrong instance/sentinel values; sibling smelting.rs::shared_native_go_sentinel_is_bound_to_offered_smelting_instance is the same shape but for a different module (smelting), so it does not drive the cooking path."},
  {"name": "actual_native_stat_suffix_is_numeric_only_and_preserves_order_and_economy", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal set over StatUpdate/StopLevel/ScoreSet/GameWon with state-unchanged checks; only cooking-module coverage of captured native stat suffixes. Analogous smelting test is shared_original_stat_suffix_is_narrow_and_never_completes_a_recipe but is a different module."},
  {"name": "native_protocol_matches_compiled_community_vectors", "verdict": "keep", "covered_by": null, "reason": "Byte-level oracle against compiled community vectors (canary for wire format); not duplicated within the suite as a cooking-specific check."},
  {"name": "six_ordered_rounds_create_fixed_recipe_intent_once_and_restore", "verdict": "keep", "covered_by": null, "reason": "Full happy path with exactly-once transaction and restore persistence; only check of cooking's fixed recipe intent and restart."},
  {"name": "malformed_unordered_early_or_forged_reports_do_not_commit", "verdict": "keep", "covered_by": null, "reason": "Security/refusal check on forged and out-of-order reports; state-unchanged assertions."},
  {"name": "final_totals_and_all_six_rounds_are_required_for_reward", "verdict": "keep", "covered_by": null, "reason": "Refusal check that reward needs all rounds and totals; distinct assertions from the malformed test."},
  {"name": "loss_close_and_stale_attempt_never_grant", "verdict": "keep", "covered_by": null, "reason": "Refusal/no-grant check for loss and stale instance; unique to cooking."},
  {"name": "native_results_wait_for_actual_close_ack_and_replays_preserve_recipe", "verdict": "keep", "covered_by": null, "reason": "Replay/ack-ordering persistence check on terminal state; security-relevant replay refusal."},
  {"name": "content_and_saved_state_reject_unlabelled_or_inconsistent_recipe", "verdict": "keep", "covered_by": null, "reason": "Fail-closed content and saved-state validation; never removable without an equivalent elsewhere."},
  {"name": "private_original_movie_phase_configuration_loads", "verdict": "keep", "covered_by": null, "reason": "Ignored canary that needs private reference content; cannot run in the normal suite, so not redundant in practice. Keep as canary."},
  {"name": "every_cooking_catalog_recipe_uses_exact_transaction_once", "verdict": "keep", "covered_by": null, "reason": "Catalog-wide exact-transaction check over all 26 chef recipes; broader than any single-recipe test and the only one of its kind for cooking."},
  {"name": "cooking_recipe_rejections_leave_state_unchanged", "verdict": "keep", "covered_by": null, "reason": "Refusal check on begin_recipe with missing ingredients, zero count, unlabelled recipe and unknown key; state-unchanged assertions."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "No test is clearly a duplicate, superseded or obsolete. The file was created and last changed by T033 and no later task replaces any behaviour it pins. The main overlap is structural: tests/smelting.rs (and tests/forging.rs) carry near-identical mirrors of the native go-sentinel, stat-suffix, ack/replay and recipe-rejection tests. Those mirrors drive different modules (smelting, forging) and so do not meet the 'same path' bar. A possible consolidation is a shared generic harness for the three crafting modules, but that is a refactor, not a removal, and it would have to keep each module's own assertions. Only the most similar-file pack was read (smelting.rs lines 1-200); the remaining smelting tests were not compared line by line."}
]}
