<!-- fleet job=bug-hunt id=src-restoration-piece-046-rs-L1 status=nothing_found turns=8 usd=0.0104 tokens(read,write,in,out)=[160391, 39625, 18, 7761] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_046.rs lines 1-784 of 784

## Window: `prototype/osfr-tools/src/restoration/piece_046.rs` lines 1-784 (whole file)

No reachable defect found. I read the full window and traced the callers.

### How the window is reached
- `src/item_bar.rs:44-45` mounts this file as `item_bar::use_wire`. That is the only production consumer. Client packets reach it through `ItemBar::handle` (`item_bar.rs:226-280`).
- Production code in `item_bar.rs` uses only these items from the window: `consumable()` (lines 97, 175, 260, 337), `decode_immediate_activation` (255), `decode_client_request_start_ability` (275), `ITEM_ACTION_BAR_ID` (273), `ImmediateActivation`, `ActivateRequest`, `Target` (393-404), and the `encode_*` helpers used by `bin/osfr_gateway/f261_pickup_reload.rs:15`.
- `ConsumableLedger` (lines 594-784), `UsePolicy`, `UseRequest`, `decode_slot_update`, `usable_now`, `recast_remaining_ms`, `decode_ability_failed` and `decode_item_action_bar_assign` have no caller in `src/` outside this file. They are used only by `tests/piece_046.rs` and by the piece's own checker. The 42/6 path is served by `piece_048` (`bar_wire::parse_assign`), not by this file's decoder.

### Checks on the reachable code
- `decode_client_request_start_ability` (316-346): the length is checked as 24 or 32 before any index. Mode 0 is accepted only with 24 bytes and mode 1 only with 32, so the `bytes[offset+3]` reads are in range.
- `decode_immediate_activation` (362-375) and `decode_item_action_bar_assign` (277-290): exact-length checks come before the indexing. Unknown subs return `None`.
- `item_bar.rs` checks the returned `bar`/`slot`/instance against server state (`bound(slot)`, the inventory lookup in `handle`, `usable`). Target mode 1 (position) and any guid other than the player's or 0 are refused (`item_bar.rs:403-408`).
- `decode_slot_update` (440-482) is server-to-client only. Its `payload` slice is 51 bytes after the 63-byte length check, so every index up to 50 is in bounds.
- The `consumable()` table has unique ids and is in id order, which matches its doc comments.

### Observations I did not report
These are real in the code but cannot be reached from a client packet, so they do not meet the defect bar:
- `ConsumableLedger::assign` (628-655) checks only `slot < 0`, with no upper bound, so `assignments` can grow with each new slot. Its only caller is in tests, and the live bar bounds slots through `bar_wire`.
- `ConsumableLedger::use_item` (746, 760) does `request.now_ms + cooldown/duration` with no `checked_add`. This would overflow only for an `i64` clock near `i64::MAX`, and no production code builds a `UseRequest`.
- `use_item` with `effect_duration_ms == 0` (759-773) leaves the instance's previous effect window in place, while the doc at 682-683 says an accepted use "replaces that instance's effect window". This is a doc mismatch in unreachable code.

No finding is submitted because none of these can be triggered by a remote player or a save.
