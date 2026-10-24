<!-- fleet job=bug-hunt id=src-gameplay-npc-rs-L801 status=nothing_found turns=19 usd=0.0204 tokens(read,write,in,out)=[598597, 54473, 40, 15160] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/npc.rs lines 801-1434 of 1434

No reportable defects in `gameplay/npc.rs` lines 801-1434 (non-test code). I read the whole window and checked the callers and helpers it depends on.

What I checked and why each is not a defect:

- **66/43 buy (801-858):** `request.initial_dwords` and `trailing_dwords` are fixed-size arrays (`[u32; 2]` / `[u32; 3]`, `npc_interaction.rs:1404-1407`), so `[0]` and `[2]` cannot go out of bounds. The client item id goes through `i32::try_from(..).unwrap_or(-1)`. `validate_merchant_item_66_43` (`npc_interaction.rs:686-713`) checks active shop, stock membership and range. `buy_vendor`/`buy_once` (`coin_shop.rs:335-604`) reject `item_id <= 0` and `quantity` outside `1..=i32::MAX`, use `checked_mul` for the price, and check coins before subtracting. `grant` enforces the stack limit. Nothing is mutated before the checks that can fail, and the `Err` path falls back to a refusal.
- **`begin_kart_race` (862-896):** the `kart_entry.unwrap()` at 889 is safe because `admit` returned `Ok` only when `kart_entry` was `Some`. Its state changes (unlock, activate, outfit) are staged through `commit_if_changed` (`npc.rs:58-68`, called at 577), so a later `?` discards them.
- **`begin_fishing` (900-942):** the `let _ = profiles.unlock(..)` only errs for a profile id missing from content, and 137 is a known job. Denials return `changed: false`, so staging discards the unlock.
- **`talk_to_npc` (947-1091):** the `expect` at 980 is safe because `pending_before` is `Some` only when `npc_quests` is `Some`. The `packet.get(14..18)` at 1020 with `try_into().unwrap()` is safe because `get` only returns 4-byte slices.
- **`patch_npc_actor` (1156-1166):** each branch checks `len` before slicing, and the 49/1 `len - 14` offset matches the 14-byte trailer that `encode_quest_offer_49_1` writes (`npc_interaction.rs:1255-1259`).
- **Dialogue, merchant and quest-offer builders (1168-1273):** no client-controlled indexing or unbounded growth. Encoder errors are mapped to `Err`.

No finding meets the bar of a defect that a remote client can trigger.
