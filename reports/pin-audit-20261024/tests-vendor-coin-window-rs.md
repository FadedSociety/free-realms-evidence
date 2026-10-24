<!-- fleet job=pin-audit id=tests-vendor-coin-window-rs status=done turns=5 usd=0.0016 tokens(read,write,in,out)=[13860, 5377, 12, 1615] model=claude-haiku-5-5 -->
# tests/vendor_coin_window.rs

**prototype/osfr-tools/tests/vendor_coin_window.rs:182 roosey_coin_window_lists_her_stock_at_server_prices - pins `75` from `prototype/osfr-tools/data/content/stores.json` `items[].purchase_price_coins` (row `item_id` 75260, `purchase_price_coins`: 75).**

The expected value is the file-local constant `RING_PRICE: u32 = 75` (line 25), which is a hand-copied copy of that store row's price. Retuning the ring's price in `stores.json` would break this assertion while the server is still correct.

- **Fix:** read it through the existing helper `stock_prices()` (lines 29-43 of the same file), which already loads `purchase_price_coins` from `stores.json` for the `STOCK` ids. Use `stock_prices()[&RING]` in place of `RING_PRICE` here. Then delete the `RING_PRICE` constant, or derive it from the same helper.

Related, not screened: line 186 (`1_000 - RING_PRICE * bought`) uses the same constant and has the same problem. It should use the same helper value.
