<!-- fleet job=pin-audit id=tests-coin-shop-rs status=done turns=7 usd=0.0047 tokens(read,write,in,out)=[74838, 19394, 16, 3133] model=claude-haiku-5-5 -->
# tests/coin_shop.rs

Four assertions in `tests/coin_shop.rs` pin the item 8 coin price. All four come from `data/content/stores.json`, item_id 8 row (`purchase_price_coins` 15, `member_price_coins` 13). The test fixtures set only the starting balance (100 or 5), so the expected balances change if the store row is retuned.

- **prototype/osfr-tools/tests/coin_shop.rs:96 buy_debits_exact_cost_and_retry_is_idempotent - pins `15` from `data/content/stores.json` `items[item_id=8].purchase_price_coins`.** (`100 - 15 * bought`)
  **Fix:** read it through `resale::purchase_price(8)` from `tests/common/resale.rs`, so the expression becomes `100 - purchase_price(8) * bought`.

- **prototype/osfr-tools/tests/coin_shop.rs:117 member_purchase_uses_catalogued_discounted_price - pins `87` (= 100 − `13`) from `data/content/stores.json` `items[item_id=8].member_price_coins`.** The member price is not covered by any helper in `tests/common/`.
  **Fix:** read the row's `member_price_coins` in the test (or add a `member_price(definition)` helper beside `purchase_price` in `tests/common/resale.rs`) and assert `100 - member_price`.

- **prototype/osfr-tools/tests/coin_shop.rs:366 purchase_uses_the_synced_live_inventory - pins `85` (= 100 − `15`) from `data/content/stores.json` `items[item_id=8].purchase_price_coins`.** The 5-coin starting balance is the fixture's, but the 15-coin debit is the store row's.
  **Fix:** read it through `resale::purchase_price(8)` and assert `100 - purchase_price(8)`.

- **prototype/osfr-tools/tests/coin_shop.rs:384 vendor_buy_debits_grants_and_retries_without_replaying - pins `85` (= 100 − `15`) from `data/content/stores.json` `items[item_id=8].purchase_price_coins`.** The vendor buy goes through the same catalogue price path (`buy_vendor` -> `buy_once`).
  **Fix:** read it through `resale::purchase_price(8)` and assert `100 - purchase_price(8)`.

Not findings: none of the other listed lines were screened in; the rest of the file's literals (5, 100, quantities, ids 71001–72001, result codes, packet lengths) are fixture or protocol values.
