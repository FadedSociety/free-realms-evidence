<!-- fleet job=testaudit-infer id=collection_coin_pickup-v1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[25200, 15536, 8, 1827] model=claude-haiku-5-5 -->
# tests/collection_coin_pickup.rs

{"file": "tests/collection_coin_pickup.rs",
 "tests": [
  {"name": "click_in_range_collects_and_hides", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 26/8 coin click producing the exact 38/10 AddEntry bytes, the ledger write, and the coin removal on the next visibility update."},
  {"name": "second_click_does_nothing", "verdict": "keep", "covered_by": null, "reason": "Idempotence/no-double-collect check on the coin route; no other file drives a repeat coin click through handle_in_world."},
  {"name": "out_of_range_and_busy_refuse_without_change", "verdict": "keep", "covered_by": null, "reason": "Refusal check (far, wrong zone, busy mining run) asserting exact refusal chat and unchanged state/revision; must be kept."},
  {"name": "relog_keeps_coin_hidden", "verdict": "keep", "covered_by": null, "reason": "Persistence check: collected coin stays hidden after reload from saved state. Similar relog tests exist (archer_entry_chain::relog_keeps_completed_history_and_no_duplicate_reward) but cover quest history, not coin visibility; not an equal check."},
  {"name": "content_reload_keeps_coin_hidden", "verdict": "keep", "covered_by": null, "reason": "Canary for content reload not resurrecting a collected coin; no equivalent found in the similar files (coin_authoring covers overlay moves, not collected-state reload)."},
  {"name": "other_player_still_sees_it", "verdict": "keep", "covered_by": null, "reason": "Per-character isolation check: one player's collection does not hide the coin for another session; not duplicated elsewhere."},
  {"name": "non_coin_click_falls_through", "verdict": "keep", "covered_by": null, "reason": "Negative check that a vendor click does not write a collection entry and still gets the 26/9 list; guards the router fall-through."},
  {"name": "completing_a_set_records_completion_once", "verdict": "keep", "covered_by": null, "reason": "Only test of set completion via all five Seaside Rare coins and the single completion record plus replay being inert."},
  {"name": "the_three_added_coins_record_their_entries", "verdict": "keep", "covered_by": null, "reason": "Covers the T479 added coins (2038, 2195, 2203) which no other file exercises through the click route; not a duplicate."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Searched for other click-to-collect coverage: none found in the similar files. coin_authoring.rs (T525/F717) covers placement, overlay and visibility after moves, not collecting coins, so it is not a superseding match. The only overlapping-looking relog test (archer_entry_chain.rs) is about quest history. No test is obsolete: no later task replaced this coin route in the pack. Low-risk candidate for future consolidation: the_three_added_coins_record_their_entries could be folded into a table test with completing_a_set, but it is not redundant as written."}
