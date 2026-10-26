<!-- fleet job=testaudit-infer id=vendor_coin_window-v1 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[9647, 13565, 6, 1138] model=claude-haiku-5-5 -->
# tests/vendor_coin_window.rs

{"file": "tests/vendor_coin_window.rs",
 "tests": [
  {"name": "roosey_coin_window_lists_her_stock_at_server_prices", "verdict": "keep", "covered_by": null, "reason": "Single test that is the only end-to-end check of Roosey's 165/10 coin list against the stores.json prices, the presentation fields, the 35/37 definition-price correction, a 165/4 buy at the server price, and a refused unknown-item buy that must leave the snapshot unchanged. Similar files (vendor_buy_sell_gateway.rs: a_client_supplied_price_field_cannot_change_the_server_price, buy_and_sell_refusals_change_nothing; priced_vendors_drawable.rs and starter_items.rs, which decode the 165/10 list) overlap in parts, but none is named as driving the same Roosey list-to-buy path with the same assertions. Refusal and price-authority checks are kept by policy."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Only one test, created and last changed by T362/T434. The 165/10 decoder is checked in several files, and buy/refusal behaviour is also covered in vendor_buy_sell_gateway.rs and vendor_sell.rs, so partial overlap is real. I did not read those bodies line by line, so the verdict rests on the names and search hits. If someone wants to trim, the list-shape assertions could be compared with priced_vendors_drawable.rs, but the Roosey-specific pins and the refusal snapshot should stay."}
