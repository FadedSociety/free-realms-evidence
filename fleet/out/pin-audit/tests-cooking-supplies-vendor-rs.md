<!-- fleet job=pin-audit id=tests-cooking-supplies-vendor-rs status=done turns=6 usd=0.0046 tokens(read,write,in,out)=[42805, 18701, 14, 3659] model=claude-haiku-5-5 -->
# tests/cooking_supplies_vendor.rs

Source of the numbers: `const PRICE: u32 = 12;` (tests/cooking_supplies_vendor.rs:49) is a hardcoded test constant. Its value matches the shipped `purchase_price_coins: 12` on every ingredient row this test uses (`data/content/stores.json`, e.g. items 2900, 2862, 2859, 2902, 2897, 2898, 2895, 2896 and others; the rows are also in `data/content/vendors.json`). Retuning that stores.json field would break these asserts while the server code is still correct. The member price 10 is the shipped `member_price_coins: 10` in the same stores.json rows (`member_discount_percent: 10`).

- **tests/cooking_supplies_vendor.rs:417 cooking_supplies_vendor test (the one that loops over INGREDIENTS and checks `store_rows`) - pins `10` from `data/content/stores.json` `member_price_coins`.**
  **Fix:** read it through the row already loaded at line 410 (`store_rows`), e.g. assert `store["member_price_coins"]` equals `store["purchase_price_coins"] * (100 - store["member_discount_percent"]) / 100` (integer floor), or bound it as `is_null()` or a value below `purchase_price_coins`. Do not compare it to a literal 10.

- **tests/cooking_supplies_vendor.rs:482 (server-price test around the forged 66/43 buy) - pins `PRICE` (12) from `data/content/stores.json` `purchase_price_coins`.**
  **Fix:** replace `PRICE` with the value read from the row of `item_id` (the store row in `stores.json`, the same way `common/vendor_fixture.rs::store_price(stores, item, "purchase_price_coins")` does). That helper is private to `vendor_fixture.rs` (fn `store_price` is not `pub`), so either make it `pub` and import it, or read the row inline in this test. `VendorFixture::price()` only covers `REPRESENTATIVE_ITEM`, so it does not fit `item_id` unless that is the item bought here.

- **tests/cooking_supplies_vendor.rs:603 (closed-shop / other-player test) - pins `PRICE` (12) from `data/content/stores.json` `purchase_price_coins`.**
  **Fix:** same as 482: read `purchase_price_coins` for `INGREDIENTS[1].1` (item bought on line 601) from `stores.json` and use `100 - that`.

- **tests/cooking_supplies_vendor.rs:613 selling_an_ingredient_back_uses_the_store_price_and_is_once - pins `PRICE` (12) from `data/content/stores.json` `purchase_price_coins`.**
  **Fix:** read `purchase_price_coins` for `INGREDIENTS[0].1` (the item bought on line 610) from `stores.json` and use `100 - that`.

Note: the other `PRICE` uses (lines 414, 450, 519, 542, 676, 700, 803, 813) hit the same constant. They were not on the screened list, but the same fix applies: change `const PRICE` to a value read from `stores.json` once, instead of a literal 12.
