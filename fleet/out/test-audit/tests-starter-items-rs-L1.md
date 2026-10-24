<!-- fleet job=test-audit id=tests-starter-items-rs-L1 status=done turns=8 usd=0.0081 tokens(read,write,in,out)=[122433, 26518, 18, 7050] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/starter_items.rs lines 1-468 of 468

Window `prototype/osfr-tools/tests/starter_items.rs` lines 1-468 reviewed. Most of the window holds up. Notes on the checks that passed are below the one finding.

- **[low] prototype/osfr-tools/tests/starter_items.rs:372 a_regranted_starter_weapon_sells_for_zero_and_a_normal_item_keeps_its_price - `assert_eq!(rows.len(), 2)` pins the total vendor row count, which the starter-price claim does not depend on.**
  - Why it cannot catch a regression: this check is not what guards the F228 rule, so it adds no detection. It fails for unrelated churn. Adding or removing any row in the synthetic `vendors.json` (lines 289-291) or `stores.json` (lines 300-303) breaks this test even when starter pricing is correct. That is the over-pinning in category 5.
  - Fix: drop the total count, or assert only the presence of the two rows that matter, which lines 373-380 already do. If a count is kept as a guard, make it a per-item check such as "the starter row appears exactly once".

Checks that passed:
- Line 386 `assert_eq!(gateway.snapshot(), before_refusal)` is a real no-mutation check. `Snapshot` derives `PartialEq` and includes the full `GameplayState` (`game_store.rs:20-25`, `gateway.rs:1249-1262`), so a refused sale that changed inventory, coins or shop state would fail it.
- The 0-coin expectations are not derived from the code under test. The store rows use literal values (`store_row(STARTER_BOW, 10, 375)`, line 301), and the zeroing happens in `coin_shop.rs:186-199` and `coin_shop.rs:245-250`. The test checks the sell price, the coin balance and the inventory count after each sale.
- The regrant path (lines 399-411) asserts the re-grant (count 1, equipped instance) before the sale, so it cannot pass vacuously.
- The second test (lines 448-468) has a doc that says it guards shop construction. That is accurate: `gameplay.rs:969-976` calls `CoinShop::load` with the session profiles whenever the fixture's `npcs/`, `stores.json` and `vendors.json` exist, and the fixture writes all three. The canary at lines 461-464 covers the `None` path.
- Fixture absence is not silently skipped. `Fixture::new` asserts that `profiles.json` and `inventory.json` exist (lines 251-255), and it panics rather than returning early. There is no `#[ignore]`.
