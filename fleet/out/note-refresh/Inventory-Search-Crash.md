<!-- fleet job=note-refresh id=Inventory-Search-Crash status=done turns=20 usd=0.0255 tokens(read,write,in,out)=[624381, 59503, 42, 23694] model=claude-haiku-5-5 -->
# notes/Research/Inventory Search Crash.md

**Verdict:** badly stale. The native-search diagnosis (client side) still matches the decompiled code, but the Rust checklist and the Integration steps describe the tree before the W09 and W146 changes. Several "Not implemented / Mismatch / still open" statements are now false, and a number of `inventory.rs` line citations have moved.

**Corrections:**

1. `old:` Not implemented. activate_enabled exists on an item but assignments and activations are not handled.
   `new:` Built (W146). `item_bar.rs` persists four bar slots, handles 42/6 and 42/9, sends 38/25 and bar casts. The Small Health Potion is the only usable consumable. Never run natively.
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:1-30 and :153; repo:prototype/osfr-tools/src/gameplay.rs:131, :5081-5095; repo:prototype/osfr-tools/src/gateway.rs:529, :2097-2098; repo:notes/Design/Build Ledger.md:92 ("Item bar and potion | Built and wired (W146)").

2. `old:` There is no stored-count field, item-bar assignment state, or storage usage/capacity.
   `new:` `stored_count` and item-bar assignment state are persisted. Storage usage and capacity are still absent.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:61-62 (`stored_count`, `last_cast_time: i64`); repo:prototype/osfr-tools/src/item_bar.rs:153; repo:prototype/osfr-tools/src/gameplay.rs:131.

3. `old:` under that mapping the current field five is ability_count instead of stored_count, and the final 64 bits are rental expiry instead of last-cast time.
   `new:` under that mapping the encoder now writes stored_count in field five and last-cast time in the final 64 bits.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:1484-1492 (`item_update` passes `stored_count` and `last_cast_time`); repo:prototype/osfr-tools/src/inventory_v2_fixes.rs:108-121.

4. `old:` Under the guide's reconstructed 38/3 field mapping (R), the current encoder also sends expiry in the last-cast field.
   `new:` The 38/3 encoder sends last-cast time, not rental expiry, in its final 64-bit field.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:1485-1491; repo:prototype/osfr-tools/src/inventory_v2_fixes.rs:119.

5. `old:` Not implemented in this inventory layer.
   `new:` Partial. `item_bar.rs` implements the 42/16 confirmation and 42/15 consumption for the Small Health Potion only, one item per use. Rewards and other consumables are not implemented.
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:15-30; repo:prototype/osfr-tools/src/gateway.rs:2099-2100.

6. `old:` The 35/37 encoder in Inventory::definitions_packet (inventory.rs:294) correctly writes a byte-length prefix and the catalogue count, but simply writes the available map; it does not require every id in the self-body item list to be present.
   `new:` The 35/37 encoder is now `Inventory::definitions_packet` (inventory.rs:607-627). It filters owned instances to those with a definition (inventory.rs:612) and delegates to `encode_definition_batch_v2`, which checks coverage and panics via `.expect` on failure (inventory.rs:625-626). The three unavailable instances are therefore withheld before the check, not sent.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:607-627; repo:prototype/osfr-tools/src/inventory_v2_fixes.rs:35-72.

7. `old:` New, currently unregistered helpers are in prototype/osfr-tools/src/inventory_v2_fixes.rs:
   `new:` New helpers, now registered in lib.rs:35 and also included by `inventory.rs` via `#[path]`, are in prototype/osfr-tools/src/inventory_v2_fixes.rs:
   `why:` repo:prototype/osfr-tools/src/lib.rs:35 (`pub mod inventory_v2_fixes;`); repo:prototype/osfr-tools/src/inventory.rs:23-24.

8. `old:` The current InventoryItem has no stored_count, and its last-cast field is only i32; wire integration therefore needs a state/snapshot change to preserve the 38/3 layout using the guide's semantic field interpretation (R).
   `new:` InventoryItem now has `stored_count: u32` (legacy default zero) and an `i64` `last_cast_time`, so the 38/3 layout needs no further state change.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:59-62.

9. `old:` Replace the free item_update encoder (inventory.rs:918-936) and its grant/consume call sites with encode_item_update_v2.
   `new:` The free `item_update` encoder (inventory.rs:1484) already calls encode_item_update_v2; this step is done.
   `why:` repo:prototype/osfr-tools/src/inventory.rs:1484-1493.

10. `old:` Game snapshot schema advances from 3 to 4; schema 3 snapshots remain readable and migrate on their next save.
    `new:` Game snapshot schema advanced from 3 to 4 in this change. The current gameplay save schema is 7 (`SCHEMA_VERSION`), and saves with gameplay write it.
    `why:` repo:prototype/osfr-tools/src/game_store.rs:15-18 and :86-94.

11. `old:` Replace the body/signature of Inventory::definitions_packet (inventory.rs:294-306) with encode_definition_batch_v2, passing the definition byte records and every definition_id in the active InventoryState.
    `new:` The body of Inventory::definitions_packet (inventory.rs:607-627) already calls encode_definition_batch_v2 (inventory.rs:625). Still open: it returns `Vec<u8>` and panics on failure via `.expect`, so the error is not propagated.
    `why:` repo:prototype/osfr-tools/src/inventory.rs:607, :625-626.

12. `old:` Propagate that error through Gameplay::definitions_packet (gameplay.rs:534-538) and the index-5 template replacement in Gateway::templates (gateway.rs:817-820).
    `new:` Propagate that error through Gameplay::definitions_packet (gameplay.rs:1581-1585, still `Option`-returning) and the index-5 template replacement in Gateway::templates (gateway.rs:1913-1916).
    `why:` repo:prototype/osfr-tools/src/gameplay.rs:1581-1585; repo:prototype/osfr-tools/src/gateway.rs:1913-1916.

Checked and holding: the `inventory_v2_fixes` test file exists with 3 tests (repo:prototype/osfr-tools/tests/inventory_v2_fixes.rs); the `character_store` schema is still 2; `validate_content_state` permits the three missing definitions only when they match the default state (repo:prototype/osfr-tools/src/inventory.rs:775-783); `activate_enabled` exists (inventory.rs:65); the native chain `00990d80` → `00b0d810` (reads +0x04, manager +0x20c, match at +0xb4, returns 0 on no match) matches the client pseudocode in the fn table; `0098faf0` tail-calls `00a6e7b0`.

**Unsure:**
- The `validate_content_state` citation (inventory.rs:404-433) has moved to inventory.rs:755-783. I did not change it, but it is stale.
- Row 9 (35/34 gets no reply for a missing id) and the native 00990e17 bare dereference (`mov eax,[eax+4]`) were not checked; the fn table pseudocode for 00990d80 is truncated before that point.
- The category figures (71 rows, 74 group associations, absent ids 0/127/148/149 and 58/60/401-407) were not verified against the category data.
- "Schema 3 snapshots remain readable" was not verified; I did not read the `read_document` version handling.
- `tests/game_store.rs:38` (cited in the verification section) now sits at tests/game_store.rs:42 and asserts `BASE_SCHEMA_VERSION` (5), so the cited failure has changed. Not corrected because it describes a past run.</result>
</invoke>
