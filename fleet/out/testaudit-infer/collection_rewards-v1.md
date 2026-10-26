<!-- fleet job=testaudit-infer id=collection_rewards-v1 status=blocked turns=7 usd=0.0049 tokens(read,write,in,out)=[95108, 18012, 16, 3453] model=claude-haiku-5-5 -->
# tests/collection_rewards.rs

{"file": "tests/collection_rewards.rs",
 "tests": [
  {"name": "seaside_rare_pays_its_boots_once_after_the_38_10", "verdict": "keep", "covered_by": null, "reason": "Could not read the body. Pack says it is the only check of the Seaside Rare boots reward path; kept by default."},
  {"name": "a_saved_completion_pays_nothing_again_even_when_an_entry_comes_back", "verdict": "keep", "covered_by": null, "reason": "Persistence/replay guard (no double pay after save); kept by default."},
  {"name": "relog_after_completion_never_pays_again", "verdict": "keep", "covered_by": null, "reason": "Relog replay guard; kept. Possibly overlaps the saved-completion test above, unverified."},
  {"name": "coins_and_xp_go_to_the_named_profile_when_unlocked", "verdict": "keep", "covered_by": null, "reason": "Only visible check of profile routing of coins/XP; kept."},
  {"name": "a_locked_profile_skips_the_xp_and_still_pays_the_coins", "verdict": "keep", "covered_by": null, "reason": "Locked-profile branch; kept."},
  {"name": "a_girl_gets_the_girls_item_and_a_boy_the_captured_one", "verdict": "keep", "covered_by": null, "reason": "Gender-specific reward branch; kept."},
  {"name": "a_full_bag_refuses_the_completing_click_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; kept by rule. Overlaps the bag-full refusal tests in other files (e.g. miner_first_ore::a_full_bag_refuses_the_node_before_the_run_and_changes_nothing), but those are on different paths."},
  {"name": "an_xp_overflow_refuses_the_completing_click_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; kept."},
  {"name": "map_has_exactly_14_pairs", "verdict": "keep", "covered_by": null, "reason": "Load-time map canary; tests/collection_catalogue.rs covers set 284 -> 309 mapping, but the 14-pair count is not verified elsewhere; kept."},
  {"name": "completing_284_records_309s_entry_2170_after_its_own", "verdict": "keep", "covered_by": null, "reason": "Specific cross-entry record check; kept."},
  {"name": "completing_all_elite_sets_pays_the_backpack_once", "verdict": "keep", "covered_by": null, "reason": "Only check of the 309 backpack payout; kept."},
  {"name": "a_meta_reward_refusal_changes_nothing_and_the_retry_pays_once", "verdict": "keep", "covered_by": null, "reason": "Staged-change rollback refusal; kept by rule."},
  {"name": "a_full_bag_completing_elite_click_leaves_309_untouched", "verdict": "keep", "covered_by": null, "reason": "Refusal check; kept by rule."}
 ],
 "whole_file_removable": false,
 "confidence": 0.1,
 "notes": "BLOCKED: tests/collection_rewards.rs does not exist in the repository tip (rg reports the path missing; no fn in the tree matches any of the 14 test names, and no brief mentions T522 or this file). The verdicts above are placeholders from the pack's names and doc lines, not from the test bodies, so they are not a real audit. Nearby real coverage: tests/collection_coin_pickup.rs (completing_a_set_records_completion_once, the_three_added_coins_record_their_entries, relog_keeps_coin_hidden) and tests/piece_038.rs (a_collection_completes_once_when_its_last_entry_arrives). Those cover completion recording but not the reward payout, so no test here is shown removable. Re-run the audit against the branch that contains this file."}
