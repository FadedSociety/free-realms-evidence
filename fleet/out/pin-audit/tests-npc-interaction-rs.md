<!-- fleet job=pin-audit id=tests-npc-interaction-rs status=no_submit turns=6 usd=0.0024 tokens(read,write,in,out)=[28896, 9347, 14, 1816] model=claude-haiku-5-5 -->
# tests/npc_interaction.rs

**Findings: lines 160 and 176 pin the store price of item 8.** Line 657 does not.

- **prototype/osfr-tools/tests/npc_interaction.rs:160 test_name (the buy test that asserts `coins` after the first purchase) - pins `15` from `prototype/osfr-tools/data/content/stores.json` `items[item_id=8].purchase_price_coins`.** The fixture sets the balance to 100 (`coin_shop()` at line 47), so 85 = 100 − 15. The 100 is the test's own fixture and is fine. Only the 15 is the shipped price.
  - **Fix:** read it through `resale::purchase_price(8)` from `tests/common/resale.rs` (already imported as `mod resale` at line 1), then assert `100 - resale::purchase_price(8)`.

- **prototype/osfr-tools/tests/npc_interaction.rs:176 test_name (the same test, second buy) - pins `70` from the same `stores.json` `items[item_id=8].purchase_price_coins`.** 70 = 100 − 2×15, computed from the shipped price.
  - **Fix:** assert `100 - 2 * resale::purchase_price(8)`, using the same helper.

Not a finding:
- **Line 657 (`window.items[0].purchase_price_coins`, `Some(15)`):** this test writes its own `stores.json` fixture at line 622 with `purchase_price_coins: 15`. The value comes from the test's own fixture, not from `data/content`, so retuning the shipped data does not affect it.
