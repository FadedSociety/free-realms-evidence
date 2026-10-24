<!-- fleet job=pin-audit id=tests-vendor-sell-worth-rs status=done turns=6 usd=0.0042 tokens(read,write,in,out)=[60763, 20375, 14, 2173] model=claude-haiku-5-5 -->
# tests/vendor_sell_worth.rs

**tests/vendor_sell_worth.rs:149 shop_open_shows_each_owned_item_at_what_165_5_pays - pins `750` from `data/content/stores.json` `purchase_price_coins` (item_id 75250, NECKLACE; row at line 17310).**

- The expected balance `10_000 - 750` equals the shipped non-member buy price for NECKLACE. Retuning that row would break the assertion while the server's purchase logic is still correct.
- Fix: read it through `purchase_price(NECKLACE)`. That helper already lives in `tests/common/resale.rs` and is imported at line 41 of this file. Assert `inventory_of(&gateway).coins == 10_000 - u64::from(purchase_price(NECKLACE))` (or the matching `u32` form). Use `purchase_price`, not `member_price_coins`, because the test takes the non-member buy path.
