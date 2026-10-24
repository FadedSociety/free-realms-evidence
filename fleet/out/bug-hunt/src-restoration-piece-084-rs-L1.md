<!-- fleet job=bug-hunt id=src-restoration-piece-084-rs-L1 status=nothing_found turns=5 usd=0.0089 tokens(read,write,in,out)=[52036, 27014, 12, 9996] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_084.rs lines 1-526 of 526

No defects in `repo:prototype/osfr-tools/src/restoration/piece_084.rs` lines 1-526 that I could tie to a client-reachable input or a real state error.

What I checked:

- **Client-controlled inputs to `sell` / `buy_back`:** `quantity < 1` (sell, `piece_084.rs:364`) and `quantity < 0` (buy_back, `:422`) are rejected before any lookup. `item_guid` and `transaction_id` are only used in `position` searches, and an unknown id returns an error. `wanted > quantity_remaining` is rejected (`:443`). Quantity 0 in buy_back is the documented "all outstanding" meaning, and it is capped by `quantity_remaining`.
- **Atomicity:** in `sell` (`:380-384`), `buy_back` (`:447-450`) and `adjust_coins` (`:349-352`), every fallible step (`sell_payout`, `checked_add`, `buyback_cost`, the coin-sufficiency check) runs before the first mutation. The later mutations (`:399-406`, `:457-473`) cannot fail.
- **Overflow:** coin math is `i64` with `checked_add` / `checked_mul`. `buy_back`'s `self.coins -= cost` cannot underflow because `cost <= coins` is checked. `item.quantity += wanted` (`:463`) and `items[index].quantity -= quantity` (`:402`) stay within the granted total, because units are conserved between held stacks and outstanding sale records. I walked through partial sale, partial buyback, and re-sale of a rebuilt stack, and the sums stay balanced.
- **Panics:** the only `assert!` (`grant`, `:333`) and the `expect` in `snapshot` (`:519`) are fed by server code, not packets. `restore` returns errors rather than panicking. Nothing indexes on client-sized data without a prior bounds check.
- **Reach:** the module is not registered in `src/lib.rs` and is compiled only by `tests/piece_084.rs` through `#[path]`. Its `VendorLedger` is not called from any live packet handler. The live coin-shop path in `src/coin_shop.rs` is a separate implementation. So the window has no current client-reachable defect.

Not reported, as noise or design choices rather than defects: `sell` does not check `merchant_guid` (the ledger keeps no merchant state, and the live `coin_shop.rs` `sell` does not take a merchant at all); `restore` does not revalidate the snapshot (it is server-written); `VendorError` doc/variant mismatches (`InvalidQuantity` vs `InsufficientQuantity`) are cosmetic.
