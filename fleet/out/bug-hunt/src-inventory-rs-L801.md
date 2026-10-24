<!-- fleet job=bug-hunt id=src-inventory-rs-L801 status=nothing_found turns=17 usd=0.0287 tokens(read,write,in,out)=[730682, 66986, 36, 25970] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/inventory.rs lines 801-1513 of 1513

No reportable defect in `inventory.rs` lines 801-1513 after reading the whole window and the callers that matter.

Checked and ruled out:
- **Panics on client input:** `route` (1150-1154) rejects `inner.len() < 4` or `> 4096` before slicing. Opcodes 2, 3 and 8 check the exact length before `read(inner, n)`. `read` uses `get`, so it cannot panic. `definition_replies` (1110) requires length 12 before reading, and `initialization_patch` (1306) checks `len >= 13` before its envelope slices. `patch_gender` (1292-1300) runs `read(template, end)?` before `result[end..end+4]`. `decode_hex` (1413-1430) uses `chunks_exact(2)`.
- **Unbounded growth:** replies are bounded by the 65,536-byte definition cap (`Definition::decode`, line 200) plus the 4096-byte request cap. Item count is capped by `MAX_ITEMS` at 1009. `initialization_patch` checks `MAX_CONTENT` after each splice.
- **Atomicity:** `grant_with_tint`, `consume`, `adopt_state`, `grant_bundle` and `equip` all mutate a clone and assign `*self` only after the last fallible step. `equip` mutates `entry` only after every `?`. `grant_bundle` builds on a staged clone, so a failure in any item leaves the caller's state untouched.
- **Overflow:** `grant_coins` is guarded by `can_grant_coins` (checked_add plus the i32::MAX bound). `grant_with_tint` uses `checked_add` before `item.count += quantity` and bounds `quantity` by `i32::MAX`. `spend_coins` uses `checked_sub`. `write_item` uses `try_from` for `last_cast_time`.
- **Trusting the client:** `equip` checks ownership, `definition.slot == slot`, `profile.slots`, `allowed_classes`, and the `ineligible` rules (members, gender, rank) when `player` is present. Opcode 2 requires a profile the player has unlocked. Opcode 8 resolves the instance server-side from the owned list.
- **Callers:** the live `handle_inventory` (gameplay.rs:5230-5235) uses `handle_with` whenever progression exists. Consume callers pass server-computed ids or `1` from a checked bar binding. `grant_bundle` takes reward tables from content.

Near-miss, not reported (known and marked (R) by the author):
- `ineligible`'s expired-rental branch (inventory.rs:1380-1385) never fires live, because `equip_context` sets `rental_now: None` (gameplay.rs:5226, "rental expiry unit unproven"). Rentals do exist in saves (startup_selfdata.rs:641, trade.rs:1583). So expired rental gear stays equippable, which contradicts the `handle_with` doc at 1133-1135. This is a deliberate gap pending the time unit, not a crash or a grant, so I did not report it.
- `adopt_state` (914) sends only an item-update for any in-place change to an existing id, so a changed definition, tint or rental would not reach the client. I could not find a live path that produces such a change, so I did not report it.
