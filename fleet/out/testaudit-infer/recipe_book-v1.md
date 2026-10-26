<!-- fleet job=testaudit-infer id=recipe_book-v1 status=done turns=3 usd=0.0042 tokens(read,write,in,out)=[32560, 20202, 8, 2600] model=claude-haiku-5-5 -->
# tests/recipe_book.rs

{"file": "tests/recipe_book.rs",
 "tests": [
  {"name": "decode_reads_the_recovered_eight_byte_body", "verdict": "keep", "covered_by": null, "reason": "Only test of recipe_book::decode's happy path; no other tests/ file calls recipe_book::decode."},
  {"name": "decode_ignores_other_messages_and_rejects_bad_lengths", "verdict": "keep", "covered_by": null, "reason": "Hostile/malformed-length input check for the decoder; no equivalent elsewhere in tests/."},
  {"name": "chef_recipe_starts_at_a_station_with_exact_inputs", "verdict": "keep", "covered_by": null, "reason": "Only test asserting the Cooking start path through recipe_book::start with exact requirements and cross-service inactivity."},
  {"name": "blacksmith_recipe_starts_at_the_anvil", "verdict": "keep", "covered_by": null, "reason": "Only test of the Forging arm of recipe_book::start."},
  {"name": "miner_recipe_with_an_id_starts_through_smelting", "verdict": "keep", "covered_by": null, "reason": "Only test of the Smelting arm selecting by recipe id rather than key."},
  {"name": "rank_and_inputs_at_the_limit_are_accepted", "verdict": "keep", "covered_by": null, "reason": "Boundary acceptance (rank 20, exact inputs) paired with rank_too_low_is_refused; not duplicated elsewhere."},
  {"name": "split_stacks_of_one_ingredient_add_up", "verdict": "keep", "covered_by": null, "reason": "Distinct behaviour: ingredient counts summed across stacks; no other test covers it."},
  {"name": "station_edge_is_inclusive", "verdict": "keep", "covered_by": null, "reason": "Boundary check at exactly the interaction radius, complementing distant_recipe_is_refused."},
  {"name": "unknown_recipe_ids_are_refused_without_panic", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal with no-mutation canary; security-type check."},
  {"name": "unlearned_recipe_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check with no-mutation canary; no other test drives NotLearned."},
  {"name": "wrong_active_job_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for WrongJob in both directions with no-mutation canary."},
  {"name": "distant_recipe_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for proximity (just outside radius and origin) with no-mutation canary."},
  {"name": "other_zone_station_does_not_count", "verdict": "keep", "covered_by": null, "reason": "Refusal check for zone isolation; unique to this file."},
  {"name": "only_a_station_of_the_recipes_own_job_counts", "verdict": "keep", "covered_by": null, "reason": "Refusal check that stations must match the recipe's job."},
  {"name": "non_finite_positions_never_reach_a_station", "verdict": "keep", "covered_by": null, "reason": "Hostile NaN/inf input refusal; security-type check."},
  {"name": "rank_too_low_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for RankTooLow; unique to this file."},
  {"name": "one_missing_ingredient_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for a short-by-one ingredient set with no-mutation canary."},
  {"name": "any_live_activity_blocks_the_start", "verdict": "keep", "covered_by": null, "reason": "Refusal check for Busy when in an activity."},
  {"name": "an_active_run_cannot_be_replaced_or_doubled", "verdict": "keep", "covered_by": null, "reason": "Replay/doubling refusal with state canary; persistence-style guard."},
  {"name": "missing_service_is_unavailable_not_a_panic", "verdict": "keep", "covered_by": null, "reason": "Refusal check for absent services; unique to this file."},
  {"name": "stations_come_only_from_craft_actors", "verdict": "keep", "covered_by": null, "reason": "Checks recipe_book::stations filtering; no other test covers it."},
  {"name": "every_refusal_has_a_system_chat_line", "verdict": "keep", "covered_by": null, "reason": "Feedback contract check over all Refusal variants; no equivalent found in tests/."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Grep of tests/ found no other file calling recipe_book::start or recipe_book::decode, so the file is the only direct test of this module. The similar-file packs (npc_interaction, kart_service, player_trade, housing_service, fishing_entry) list no recipe or crafting tests, so no superseded or duplicate matches were found. The pack's excerpt was truncated but the full file was read (lines 250-484). Caveat: I did not inspect cooking/forging/smelting service-level test files for overlapping start-path assertions, so the duplicate check is limited to recipe_book-facing calls. No obsolescence evidence (the file was last changed by T033, and nothing in it cites a replaced behaviour)."}
