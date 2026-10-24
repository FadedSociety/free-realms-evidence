<!-- fleet job=pin-audit id=tests-vendor-sell-rs status=done turns=5 usd=0.0035 tokens(read,write,in,out)=[32141, 15522, 12, 2416] model=claude-haiku-5-5 -->
# tests/vendor_sell.rs

**prototype/osfr-tools/tests/vendor_sell.rs:249 native_sell_changes_exactly_one_stack_and_the_coin_balance - pins `15` from `data/content/stores.json` `purchase_price_coins` (item_id 8).**
- The `Counter` fixture (lines 158-179) loads the shipped catalogue from `content_dir()` (`data/content/stores.json`, line 167), so the buy of definition 8 costs the shipped row's 15 coins. Retuning that row would break this assertion while the code is still right.
- **Fix:** read it through the existing helper `purchase_price(8)` from `tests/common/resale.rs` (already imported as `resale`; add `purchase_price` to that `use`), i.e. `assert_eq!(after_buy.coins, 100 - purchase_price(8));`.

Not findings (for the record): 755, 757, 834, 847, 864, 879, 893, 923, 968 and 1027 run on `Fixture::new()`, which writes its own `stores.json` into a temp dir with item 8 at 15/7, 75060 at 750/375 and the equipped item at 10/5. Those literals belong to the test's own fixture, not to shipped data. Lines 268/283/293 already use `resale()`.
