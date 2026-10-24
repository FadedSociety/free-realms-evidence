<!-- fleet job=bug-hunt id=src-restoration-piece-048-rs-L1 status=done turns=6 usd=0.0102 tokens(read,write,in,out)=[99661, 35443, 14, 9499] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_048.rs lines 1-775 of 775

## Findings

**[low] prototype/osfr-tools/src/restoration/piece_048.rs:663-666 - `assign` prunes stale bindings via `reconcile` and then returns a rejection with `changed: false`, contradicting the `AssignOutcome.changed` doc at line 748 ("True when the persisted binding set changed").**

- **Failure scenario:** The persisted bar holds a binding in slot 0 whose stack has since been consumed (`count` reaches 0). A client sends 42/6 with slot `9` (out of range). Line 664 `self.reconcile(items)` drops the slot-0 binding, so the set has changed. Line 665-666 then returns `AssignOutcome::rejected(SlotOutOfRange)`, which hard-codes `changed: false`. The same happens for the `UnknownItem` and `Unavailable` rejections at lines 676-680.
- **Reach:** `item_bar.rs:234-238` (`handle`) → `ItemBar::assign` (`item_bar.rs:297-328`) → `ActionBarState::assign` (`piece_048.rs:658`). The only production caller computes `changed: before != self.bar` (`item_bar.rs:325`) over the whole bar, so the pruning is still reflected there. **No current player-visible effect**. The defect is in the public API contract of this module, which any future caller that trusts `outcome.changed` would get wrong.
- **Fix:** Compute `let pruned = self.reconcile(items) > 0;` at line 664, and set `changed: pruned` on the rejected returns at lines 666, 677 and 680. Alternatively, document that `changed` excludes pruning.

## Considered and dropped

- **`assign` lines 689-690 (`self.set(binding)` … `item_slot_update(...)?` … `self.validate()?`):** state is mutated before two fallible calls. `item_slot_update` cannot fail because the slot was range-checked at line 665. `validate` could only fail if an owned instance had `item_instance_id <= 0` or `definition_id <= 0`. Inventory ids come from `instance_ids::allocate_from_snapshot` and definitions are looked up by id (`inventory.rs:977-1036`), so this is not reachable from a client packet.
- **`parse_assign` / `read_i32` / `from_bytes` slicing:** all accesses are preceded by exact length checks (12 bytes for 42/6, 51 bytes for slots) or use constant offsets within those lengths. No panic reachable.
- **`item_slot_update` range and `SLOT_FIELDS` offsets/widths:** offsets sum to exactly 51 bytes and match `to_bytes`/`from_bytes`.
- **Client-supplied instance id and quantity:** `item_instance_id` is resolved through `ActionBarItems::owned_action`, and quantity and definition come from the server-side inventory projection, so the client cannot choose them.
- **`ActionBarState` deserialization:** `validate()` is called on load (`item_bar.rs:210`), in `assign`, and in `slot_updates`, so an invalid saved bar fails closed.
- **`CAPTURED_*` constants:** data only; offsets were spot-checked against the field layout.
