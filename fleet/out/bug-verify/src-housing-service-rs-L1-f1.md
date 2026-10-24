<!-- fleet job=bug-verify id=src-housing-service-rs-L1-f1 status=done turns=12 usd=0.0095 tokens(read,write,in,out)=[189416, 29319, 26, 7921] model=claude-haiku-5-5 -->
# medium: `housing_service.rs:586-596`

**Verdict:** `unsure`

**Severity if confirmed:** low (latent). The code gap is real, but I could not show that a rental furniture unit can exist on this server, and rental expiry is not enforced anywhere, so the stated harm is currently theoretical.

**Evidence:**

1. **Module tree (passes).** The live file is `src/housing_service.rs`, declared by `pub mod housing_service;` in `src/lib.rs:32`. It is used by `src/gameplay/housing.rs` (`handle_housing`, which dispatches family 127 and calls `session.service.handle(...)` with a clone of the live `Inventory`, lines 81-96). It is not test-only. The reviewer's `housing_service.rs:586-596` line numbers match the real file.

2. **The mechanism is real.**
   - `owned_instance` (`housing_service.rs:586-596`) filters only `count == 0` and `tint < 0`. It never checks `item.rental`. `grep rental` over `housing_service.rs` returns no match, as the reviewer said.
   - `place` (`:1514-1520`) finds the instance through `stock.instances()`, then `stock.consume(item_instance_id, 1)` runs at `:1555`.
   - `Inventory::consume` (`inventory.rs:1062-1093`) removes the item when `count == quantity`. It does not check `rental`.
   - `pickup` (`:1587-1591`) calls `return_instance`, which calls `grant_with_tint(0, def, 1, tint)` (`inventory.rs:962-1042`). That builds a new item with `rental: None` (`:1025`), so the rental is not restored.

3. **Upstream checks (none block it).** The request path is `decode_request` (`:444-456`, `:485-496`) → `HousingService::handle` → `place`/`pickup`. None of these checks rental state. The only gates are house access, edit mode and the fixture row lookup. The reviewer's comparison with trade and coin shop is also plausible.

4. **Precondition not shown (the reason for `unsure`).**
   - Only one place constructs a `RentalState` from data: `startup_selfdata.rs:641`, inside `parse_inventory_item`. That is a save-load parser.
   - `trade.rs:1583` is an encoder (`match &item.rental` → writes bytes). It does not create rentals, so the reviewer's claim that it "writes RentalState" is a misreading. The save writer is `inventory.rs:1447-1449`.
   - No grant, reward or purchase path sets `rental: Some(...)`. A rental unit can therefore arrive only through a save that already contains one.
   - The client-data search found no rental item whose definition is a furniture or fixture item. The `capture_defaults` fixture rows (`housing_service.rs:858-864`, item ids 7466, 14300, 77259, 7462, 16039, 18110, 16040) are not shown to be rental. The refs search for rental furniture returned nothing.

5. **Expiry is not enforced.** `gameplay.rs:5226` sets `rental_now: None // (R) rental expiry unit unproven`, so the server never expires rentals. The harm "a rental that expires becomes permanent" has no current effect on expiry. The worst case is that a save-carried rental loses its metadata.

**Corrected fix (if the defect is taken forward):** The fix proposed is right for the rule. Return `None` from `owned_instance` when `item.rental.is_some()`, so `place` returns `UnknownInstance`. Also consider refusing `stored_count > 0` and equipped items. Consider a regression test that a rental unit cannot be placed. Drop the "trade.rs:1583 writes RentalState" citation, since it is an encoder.
