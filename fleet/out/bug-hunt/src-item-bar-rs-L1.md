<!-- fleet job=bug-hunt id=src-item-bar-rs-L1 status=done turns=10 usd=0.0151 tokens(read,write,in,out)=[211837, 39849, 22, 16020] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/item_bar.rs lines 1-515 of 515

Reviewed `prototype/osfr-tools/src/item_bar.rs` lines 1-515 and the callees they rely on (`restoration/piece_048.rs` `ActionBarState::{validate,reconcile,assign,set,remove}`, `item_slot_update`, `restoration/piece_046.rs` decoders, `inventory.rs` `consume`, and the caller `gameplay.rs` `handle_item_bar`). I found no panic, unbounded growth, trust-the-client, or atomicity defect that a remote player can reach. Notes on what I checked:

- Slot indices from 42/6, 42/9 and 36/10 are range-checked (`piece_048.rs:608,665`) before any mutation. `word()` is only called after `inner.len() == 16`. `slot_update`'s `self.last_used[..]` index is guarded by the preceding `cooldown_left` `Some`.
- `activate` self-target check (`item_bar.rs:403-404`) and the per-definition cooldown hold. `consume` is atomic: `inventory.rs:1063-1101` stages the change and commits only after `validate_content_state`.
- `Effects::new` bounds `cooldown_ms` (so `as i32` at `item_bar.rs:492` is safe) and rejects non-catalogue definitions and duplicates. Map growth is bounded by 16 definitions and 4 slots.
- `assign`'s `?` paths after `set`/`remove` (`piece_048.rs:672,689,690`) cannot fail for in-range slots and validated bindings, so no half-applied bar state is reachable.

One low-severity logic inconsistency:

**[low] `prototype/osfr-tools/src/item_bar.rs:168-185` and `:490-499` - rental consumable stacks are shown as enabled on the bar but every use is refused.**
- Failure scenario: a stack of Small Health Potion (2173) with `rental: Some(..)` is assigned with 42/6. `View::owned_action` (168-185) does not exclude rentals, and `slot_update` only sets `enabled = false` when the definition has no effect row (499). The slot therefore renders enabled, with a 10 s recast, and looks usable. When the player clicks it, `activate` → `consume` → `usable` (460) hits `filter(|_| item.rental.is_none())` and returns `NotUsable`, so the player gets the 36/1 refusal. The slot never shows as disabled.
- Reach: 42/6 → `ItemBar::handle` (`item_bar.rs:233-239`) → `ActionBarState::assign` → `owned_action`; render path `refresh` (284-295) → `slot_update`. The `usable` rental filter at 460 is the only rental check on the path. I did not confirm that rental consumables can actually be created for these definitions, so treat this as conditional.
- Fix: in `View::owned_action` (or `slot_update`), return `None` / set `enabled = false` when `item.rental.is_some()`, so the display matches `usable`.

No other reportable defects in this window.
