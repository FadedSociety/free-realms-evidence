<!-- fleet job=testaudit-infer id=vendor_sell_worth-v1 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[11127, 17928, 6, 1705] model=claude-haiku-5-5 -->
# tests/vendor_sell_worth.rs

{"file": "tests/vendor_sell_worth.rs",
 "tests": [
  {"name": "shop_open_shows_each_owned_item_at_what_165_5_pays", "verdict": "keep", "covered_by": null, "reason": "Only end-to-end check that the 35/37 Worth rows pushed at shop open match what 165/5 actually pays, including the stores.json price patch for the mallet and the 'changes nothing else' row check. Not repeated in the similar files, which cover vendor buy/sell and wallet packets rather than the Sell-tab Worth rows."},
  {"name": "weapon_clothing_and_consumable_sell_for_a_tenth_of_their_price", "verdict": "keep", "covered_by": null, "reason": "T633 canary: the file's own doc says it is one of only two places the tenth rule is written down. Its rule is checked against the live sell result through the gateway. Not a duplicate of cooking_supplies_vendor.rs:616 or starter_items.rs, which only assert a single store-row price for other items."},
  {"name": "shipped_sell_prices_follow_the_tenth_rule_with_room_to_retune", "verdict": "keep", "covered_by": null, "reason": "Whole-catalogue regression guard for the T633 rule with a deliberate 1% tolerance set by T640 for hand retunes. It is the only check over all shipped rows; removing it would lose the guard."},
  {"name": "granted_ore_sells_for_its_worth_and_survives_a_relog", "verdict": "keep", "covered_by": null, "reason": "Covers the no-store-row Worth fallback and persistence of coins and remaining stock across a save/reload. Persistence check with no equal test elsewhere in the pack."},
  {"name": "rides_no_sale_rows_and_worn_items_are_refused_without_change", "verdict": "keep", "covered_by": null, "reason": "Refusal check: rides with NoSale and a worn item that the Sell tab would otherwise list must answer 165/6 with a non-success and leave state unchanged. Security/refusal test, kept."},
  {"name": "no_priced_item_sells_above_its_lowest_buy_price", "verdict": "keep", "covered_by": null, "reason": "Invariant over every shipped store row (no sell above lowest buy, rides refused, Worth fallback count). Whole-catalogue check not reproduced in the similar files, which test specific items."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "I read the full file and checked the similar-file overlap by searching for the tenth-rule and Worth terms. The only other hits were cooking_supplies_vendor.rs:616 and starter_items.rs, which check single-item prices, not the rule. I did not read those files' bodies or the similar files' test bodies in full, so the keep verdicts rest on names and the doc lines rather than a line-by-line assertion comparison. No test is clearly redundant, so all six are kept."}
