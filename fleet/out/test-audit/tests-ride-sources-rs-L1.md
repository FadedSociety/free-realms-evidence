<!-- fleet job=test-audit id=tests-ride-sources-rs-L1 status=done turns=4 usd=0.0048 tokens(read,write,in,out)=[19611, 13898, 10, 5681] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/ride_sources.rs lines 1-210 of 210

Window: `prototype/osfr-tools/tests/ride_sources.rs` lines 1-210. Read in full, plus `src/station_cash.rs` 140-240 (`scaled_price`, `Catalogue::build`) and `src/coin_shop.rs` 150-170 (store-row validation). Checked that `lab/reports/round70-native-20261016T061000Z/content` is not present in the repo checkout; that path is external, so this is a fixture dependency, not a silent skip (a missing fixture makes `Inventory::load(...).expect` fail, and no early return exists).

- **[medium] ride_sources.rs:97-102 every_ride_is_sold_by_a_vendor_inside_the_price_bounds - the "not coin vendor stock" check only tests the store row's own `item_id`, not every candidate item id a ride can be granted under.**
  - Why it cannot catch a regression: the ride loop at 130-136 resolves a ride through `item_definition_id_candidates` (`find_map`), so a ride can have several candidate ids. If a vendor's `item_ids` contains a candidate id other than the one whose row has `sc_price`, the loop at 96-114 never looks at that id. Line 100 would not fire, and the ride loop checks only the price and listing, not vendor stock. Coin vendor stock for a ride can therefore return unnoticed.
  - Fix: in the ride loop (after line 137), assert that none of `ride.item_definition_id_candidates` appears in `stocked`, with a message naming the ride. Optionally also assert that the candidate ids have no coin price on any row.

- **[medium] ride_sources.rs:172-210 buying_each_ride_with_coins_grants_it - the comment at 174 says every listed ride is "granted once", but the body only checks `owned.iter().any(...)` (202-207) and never counts grants.**
  - Why it cannot catch a regression: `find` at 184-190 maps each listing to the first ride whose candidates contain its item id. If a ride has two listed candidate ids, or a grant is duplicated, the owned check for the second order is already satisfied by the earlier grant. An order that grants nothing, or grants the wrong item for a ride already owned, still passes once the earlier listing has run. The balance check (201) does not catch this either, since it only tracks coins.
  - Fix: before each order, assert `!owned` for the target ride (or record the owned count), then after the order assert the count rose by exactly one. This makes "granted once" true.

- **[low] ride_sources.rs:167 every_ride_is_sold_by_a_vendor_inside_the_price_bounds - `assert_eq!(rides, 54, ...)` pins the catalogue size, which is unrelated to the sourcing and price rules the test name claims.**
  - Why it cannot catch a regression: it does not check sourcing. Adding or removing a ride with correct data fails the test for an unrelated reason, which causes churn without catching a sourcing bug.
  - Fix: drop the exact count, or assert `rides > 0` and that every ride in `mounts.json` has a store row (already done at 136). Keep the earn-only pin at 168 if it is intentional.

- **[low] ride_sources.rs:209 buying_each_ride_with_coins_grants_it - `assert!(listings.iter().all(|listing| listing.price > 0))` is a trivial end-of-test check.**
  - Why it cannot catch a regression: `Catalogue::build` (src/station_cash.rs:199-216) and `scaled_price` (147-156) already reject a zero price, and this assertion runs after all orders, so it adds no grant or debit coverage.
  - Fix: delete it, or move it before the loop and assert it against the expected scaled price for each listing.
