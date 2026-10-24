<!-- fleet job=bug-hunt id=src-npc-interaction-rs-L1 status=nothing_found turns=12 usd=0.0178 tokens(read,write,in,out)=[338908, 49610, 26, 16421] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/npc_interaction.rs lines 1-800 of 1511

No reportable defects in `prototype/osfr-tools/src/npc_interaction.rs` lines 1-800. I read the whole window and the nearby code it depends on (`coin_shop.rs` 180-205, 385-480, 600-900, 1013-1030; `npc_interaction.rs` 801-1000; `gameplay/npc.rs` 790-840). Each candidate was dropped for the reason below.

Checked and rejected:
- **`select` (508-565):** the length is checked before any slice (515). The choice id must match a server-built option (533-537) and the NPC must match the active menu (530). Range is checked (525).
- **`handle_coin_store` (574-602):** subtypes 2, 8 and 14 skip the session check, but all three are non-mutating. Subtype 8 is a fixed empty reply (coin_shop.rs:421), subtype 2 is read-only (`item_definitions`), and subtype 14 is refused with no debit or grant (`refuse_gift`, coin_shop.rs:1013-1030). Buy and sell lengths are enforced before any fixed-offset read (636, 644, 658), and buy-back is length-checked at 12.
- **Sell atomicity:** `sell_with_merchant` (coin_shop.rs:707-895) stages the inventory and commits it only at line 888. The sales record is pushed after the last fallible step. So the `is_sell` refusal mapping at line 596 cannot run after a partial sell.
- **Buy quantity and price:** `buy_once` uses `checked_mul` and bounds quantity (coin_shop.rs:504, 533). The price comes from the server catalogue, not the packet.
- **66/43 buy (`validate_merchant_item_66_43`, 686-713):** the only caller, gameplay/npc.rs:812, runs it before `buy_vendor`. Stock, active shop and range are all enforced there.
- **`load` (277-386):** every count is capped before it is stored, and the duplicate checks reject before any insert takes effect. Byte totals use `saturating_add`.
- **`check_range` (946-977):** non-finite values are rejected, and the distance check is correct.
- **`interaction_list_packet` (979-1000):** the name length is capped at 1024 and option count at 128. The `as u32` and `as i32` casts are bounded.
- **Remaining helpers in the window** (`build_options`, `merchant_window`, `named_target_quest_for_talk`, `zero_starter_sell_prices`, the `set_*` gates): no panic path on client input, and no logic that contradicts its doc comment or caller.

The window contains no findings that meet the bar.
