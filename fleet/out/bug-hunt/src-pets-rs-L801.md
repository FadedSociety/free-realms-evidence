<!-- fleet job=bug-hunt id=src-pets-rs-L801 status=nothing_found turns=14 usd=0.0241 tokens(read,write,in,out)=[465486, 54800, 30, 25282] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/pets.rs lines 801-1600 of 1819

## pets.rs lines 801-1600: no reachable defect found

I read the whole window and checked the live callers. The only path from a client packet into this window is `gameplay.rs:2251` (`handle_pets`) → `handle_with_inventory` (pets.rs:1098) → `handle` / `summon_by_item_owned`. `PetRequest::decode` (pets.rs:531-600) limits the inputs to Summon/Dismiss (subtype 4), Rename (6, 1-256 bytes, UTF-8, control-char check), UI mode (24, must be ≤2) and SummonByItem (32, 8-byte body). Each one is checked before it reaches this window.

Checked and found sound:
- **Atomicity.** `adopt_with_replies` (793-824), `handle` (1019-1093), `handle_with_inventory` (1098-1152) and `care` (1306-1379) all stage roster and inventory on clones. Errors return before any commit, and the `*self = next` / `*inventory = next_inventory` assignments come last. A failing `summon` after adoption rolls back the consume too, because the inventory is a clone.
- **Client-supplied ids.** `summon` (885) checks ownership via `self.pet`. `owned_item_for_record` (1569) requires `count > 0`, an exact definition and tint match, and a server-side `definition_for_item` lookup. `adopt_with_replies` checks that the owned item's definition equals the species' adoption id before consuming it.
- **Rename.** A client name must match the server's recovered first×second name lists (`rename_selected`, 871). Lookups use `.get`, so there is no indexing panic.
- **Clock.** `rebase_clock` runs before every live `advance_time` / `advance_roster` (summon, dismiss, summon-by-item, settle_pets), so the "clock moved backwards" error is not reached from the live path.
- **Panics.** `utilities[index]` is guarded by `index < 8` and the array is `[_; 8]`. `favorite_tricks[slot]` is guarded by the 1..=4 range check and the array is `[_; 4]`. `i32::try_from` covers the u32 wire values, and `insert_pet`'s `checked_add` covers the id counter.
- **Roster growth.** Pets are capped by `MAX_PETS` (50) in `insert_pet`, and `vendor_grants` only grows with new pets.

Not reported (no live caller, so no client or save input can reach them): `care` (1306), `play` (1229), `equip_item` (1257), `unequip_item` (1288), `learn_trick` (1397), `set_favorite` (1409), `follow_location` (1198), `set_in_water` (1219), `adopt_vendor_grant` (827) and `adopt_from_owned_item` (781). A grep of `src/` finds no non-test caller for any of them. Their checks look reasonable as far as I read them. They should be re-reviewed if the pet care/equip subtypes are wired to the gateway later.

Other observations, not defects: `rename_selected` (873-877) rebuilds up to 60×250 formatted strings on each rename request. That is a cost, not a failure.
