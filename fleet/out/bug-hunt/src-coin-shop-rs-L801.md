<!-- fleet job=bug-hunt id=src-coin-shop-rs-L801 status=nothing_found turns=7 usd=0.0112 tokens(read,write,in,out)=[107907, 34412, 16, 11721] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/coin_shop.rs lines 801-1390 of 1390

Window `prototype/osfr-tools/src/coin_shop.rs` 801-1390 read in full (plus 385-435, 700-800 and the callee paths `station_cash::place_order`, `Inventory::grant_coins` / `grant_with_tint`, `spend_coins`). No defect I could tie to a line and show reachable from a client packet or save.

Checked and ruled out:

- **Sell completion (801-895):** every fallible step (`consume`, `grant_coins`, `checked_mul`) runs before any mutation. `self.sales` and `self.inventory` change only after the last `?`/early return, so no half-applied sale. `consumed_count.min(quantity)` cannot underflow.
- **Buy back (897-978):** `client_context` is bounded by `quantity <= sale.remaining` (or 0 = all), so `wanted >= 1` and `remaining -= wanted` cannot underflow. Coins are checked (`coins < total_price`) before `next_state.coins -= total_price`. `Inventory::load(...)?` fails before any state change. Bag capacity is checked on the staged copy before `self.sales[index].remaining` and `self.inventory` are written. Restored quantity equals the quantity that was charged, so no duplication or free coins.
- **Buy-back refusal paths and `allocate_transaction_id` (980-984):** no panic, and the wrapping arithmetic is safe.
- **`refuse_gift` (1013-1034):** the length check precedes `read_i32(inner, 20)`. `count` is range-checked before `as usize`, and the exact-length check is consistent. No state is changed.
- **`handle_marketplace` (1056-1150):** the `read_u16` calls are length-guarded and `decode_order` errors propagate before any mutation. `place_order` is passed `busy`, and its own staged commit (`station_cash.rs:458-468`) changes wallet and inventory together only after all checks. The 66/38 and 27 arms are ordered correctly.
- **`marketplace_request_is_well_formed` (1269-1282):** `inner.get(4..8)` always yields exactly 4 bytes, so the `try_into().unwrap()` cannot panic. Negative lengths fail `usize::try_from`, and the length is capped at 32 before `8 + n`.
- **Serialisers and readers (1153-1390):** `put_text` casts only config-sourced strings. `known.len() as i32` and `balance as i32` are safe because coins are capped at `i32::MAX` by `can_grant_coins`. `read_*` helpers use `get(offset..offset+N)`, which cannot panic.

No findings.
