<!-- fleet job=testaudit-infer id=collection_rewards-v2 status=blocked turns=4 usd=0.0036 tokens(read,write,in,out)=[41705, 16731, 10, 2242] model=claude-haiku-5-5 -->
# tests/collection_rewards.rs

{"file": "tests/collection_rewards.rs",
 "tests": [
  {"name": "seaside_rare_pays_its_boots_once_after_the_38_10", "verdict": "keep", "covered_by": null, "reason": "Unverified: file body not readable at repo tip. Kept by the conservative default."},
  {"name": "a_saved_completion_pays_nothing_again_even_when_an_entry_comes_back", "verdict": "keep", "covered_by": null, "reason": "Unverified persistence/replay guard. Kept by rule."},
  {"name": "relog_after_completion_never_pays_again", "verdict": "keep", "covered_by": null, "reason": "Unverified relog replay guard; may overlap the saved-completion test. Kept by rule."},
  {"name": "coins_and_xp_go_to_the_named_profile_when_unlocked", "verdict": "keep", "covered_by": null, "reason": "Unverified profile routing check. Kept."},
  {"name": "a_locked_profile_skips_the_xp_and_still_pays_the_coins", "verdict": "keep", "covered_by": null, "reason": "Unverified locked-profile branch. Kept."},
  {"name": "a_girl_gets_the_girls_item_and_a_boy_the_captured_one", "verdict": "keep", "covered_by": null, "reason": "Unverified gender branch. Kept."},
  {"name": "a_full_bag_refuses_the_completing_click_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check. Kept by rule."},
  {"name": "an_xp_overflow_refuses_the_completing_click_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check. Kept by rule."},
  {"name": "map_has_exactly_14_pairs", "verdict": "keep", "covered_by": null, "reason": "Load-time map canary. tests/collection_catalogue.rs line 181 asserts set 284 -> [309] but not the 14-pair count. Kept."},
  {"name": "completing_284_records_309s_entry_2170_after_its_own", "verdict": "keep", "covered_by": null, "reason": "Cross-entry record check. Kept."},
  {"name": "completing_all_elite_sets_pays_the_backpack_once", "verdict": "keep", "covered_by": null, "reason": "Only payout check for 309 backpack 70349 in the pack. Kept."},
  {"name": "a_meta_reward_refusal_changes_nothing_and_the_retry_pays_once", "verdict": "keep", "covered_by": null, "reason": "Staged-change rollback refusal. Kept by rule."},
  {"name": "a_full_bag_completing_elite_click_leaves_309_untouched", "verdict": "keep", "covered_by": null, "reason": "Refusal check. Kept by rule."}
 ],
 "whole_file_removable": false,
 "confidence": 0.05,
 "notes": "BLOCKED. tests/collection_rewards.rs does not exist at the repository tip: `read` on prototype/osfr-tools/tests/collection_rewards.rs returns 'not a file', and no fn matching any of the test names exists in the repo. Briefs have no T480/T522 entry. The file appears only in the test-audit pack (quest-lines/testaudit-packs.json) and the prior answer. Every verdict above is a conservative keep from the pack's names and doc lines, not an audit of bodies, so none should be acted on for removal. Real neighbouring coverage: prototype/osfr-tools/tests/collection_catalogue.rs (set 284 -> collection_add [309], line 181; 14-not-captured accounting, line 598) and tests/collection_coin_pickup.rs (per the prior answer). Re-run against the branch that contains this file."}
