<!-- fleet job=bug-hunt id=src-housing-service-rs-L1 status=done turns=17 usd=0.0199 tokens(read,write,in,out)=[553410, 51969, 36, 15808] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/housing_service.rs lines 1-800 of 2033

## Findings (window `housing_service.rs` 1-800)

Most of the window is clean. I checked every client-reachable parse path in `decode_request` (bounds on the 127/14, 127/5, 127/2 and 127/23 bodies, the `inner[2..]` slice, and `text_len` arithmetic), the `FurnitureStock for Inventory` wrappers (`consume`, `return_instance`, `return_instances`, `owned_instance`), the content validators, and the denial mapping. I found no panic, unbounded growth or client-trusted authority in lines 1-800. The one defect below comes from a window function, `owned_instance`, that the place path depends on.

- **[medium] `housing_service.rs:586-596` - `owned_instance` (feeding `FurnitureStock::instances`, `:545-552`) does not exclude rental items, so a time-limited rental furniture unit can be placed and then returned to the backpack as a permanent item.**
  - **Failure scenario:**
    1. The backpack holds a furniture unit with `rental: Some(RentalState{..})` and `count == 1`, and its definition has a fixture row.
    2. The client sends `127/2` (or `127/1`) with that item's guid. `place` (`:1514-1520`) finds it through `stock.instances()`. Nothing checks `rental`, so it passes.
    3. `stock.consume(item_instance_id, 1)` at `:1555` removes the rental unit from the backpack, and the fixture is placed.
    4. The client sends `127/3` (or `127/4`). `pickup` calls `stock.return_instance(item_definition_id, tint)` at `:1591`, which calls `grant_with_tint(0, def, 1, tint)` (`inventory.rs:962-1042`). That builds a new `InventoryItem` with `rental: None`.
    5. Net effect: a rental unit (which expires) becomes a permanent furniture item in the backpack. The rental's expiration and bundle id are lost.
  - **Reach:** `decode_request` (`:444-456` for 127/2, `:485-496` for 127/1) → `HousingService::handle` → `place` (`:1514-1520`, `:1555`) → `pickup` (`:1587-1591`). No upstream check on `rental` exists: `grep rental` over `housing_service.rs` finds no match. The rest of the codebase refuses rental items for the same reason: `trade.rs:1224` (`item.rental.is_some()` blocks trade), `coin_shop.rs:770` (blocks sale), and `equip_eligibility` tests check rental expiry. Housing is the one path that skips the check. Rental items are real: `trade.rs:1583` and `startup_selfdata.rs:641` write `RentalState`.
  - **Caveat:** the exploit needs a rental unit whose definition has a fixture-configuration row. I did not confirm that any shipped rental item is furniture. The defect is in the rule, not in the data.
  - **Fix:** in `owned_instance` return `None` when `item.rental.is_some()`, so rental units never reach `instances()` and `place` reports `UnknownInstance`. (Optionally also refuse `stored_count > 0` and equipped items the same way.)
</result>
