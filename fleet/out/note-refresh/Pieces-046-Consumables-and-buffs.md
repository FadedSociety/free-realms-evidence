<!-- fleet job=note-refresh id=Pieces-046-Consumables-and-buffs status=done turns=11 usd=0.0142 tokens(read,write,in,out)=[249717, 44867, 24, 12245] model=claude-haiku-5-5 -->
# notes/Research/Pieces/046 Consumables and buffs.md

**Verdict:** badly stale on integration status. The core ledger, constants, catalogue rows and expiry rule still match the code, but the "not routed / no-op / lead integration" statements at the end of the note are now false, because the wire codec was wired into the item-bar route after the note was written.

**Corrections:**

1. `old:` registration of 42/6 or 36/10; no native slot refresh;
   `new:` registration of 42/6 (sub 6 is routed) or bar-2 36/10 (the item-bar route serves them); no native slot refresh;
   `why:` repo:prototype/osfr-tools/src/gateway.rs:2097 (`(42, 6, "item_bar")`); repo:prototype/osfr-tools/src/item_bar.rs:233-240 (`ItemBar::handle` routes `42/0/6/0` to `assign`) and :272-278 (`36/10` with bar 2 goes to `activate`); repo:prototype/osfr-tools/src/gameplay.rs:4439-4441 (`handle_item_bar` runs before the shared branch).

2. `old:` note that `42/6` is currently a no-op and `36/10` ignores bar 2 in
   `new:` note that `42/6` is now handled by `ItemBar::handle` (`item_bar.rs:233-240`) and bar-2 `36/10` is intercepted by gameplay before the shared branch (`gameplay.rs:4441`, `item_bar.rs:272-278`), while `encounter.rs:1698` still returns no-op for non-bar-1 requests in
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:233-278; repo:prototype/osfr-tools/src/gameplay.rs:4441; repo:prototype/osfr-tools/src/encounter.rs:1698-1699 (the shared session encounter path still ignores bar != 1).

3. `old:` Integration gates for the lead: register `pub mod piece_046;` under `src/restoration/mod.rs` and
   `new:` Integration gates for the lead: the wire codec is already registered through `#[path = "restoration/piece_046.rs"] pub mod use_wire;` in `item_bar.rs` (there is no `src/restoration/mod.rs`); the `ConsumableLedger` still needs wiring through `item_bar.rs`, and `src/lib.rs` (which already declares `pub mod item_bar;`) before wiring it;
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:42-45; repo:prototype/osfr-tools/src/lib.rs:38; `src/restoration/mod.rs` does not exist (repo:prototype/osfr-tools/src/restoration/ listing).

4. `old:` integration of the wire codec, then a native assignment/activation capture to replace the
   `new:` wiring of `ConsumableLedger` into the route that `item_bar.rs` already serves (the wire codec is integrated there, `item_bar.rs:233-278`), then a native assignment/activation capture to replace the
   `why:` repo:prototype/osfr-tools/src/item_bar.rs:233-278 (decode/assign/check/confirm/activate all call the piece_046 codec); `ConsumableLedger` / `use_item` has no caller outside `piece_046.rs` (repo search for `ConsumableLedger` and `use_item(`).

**Checked and holding (no change):**
- Module path `src/restoration/piece_046.rs` and test `tests/piece_046.rs` exist; the test file has 16 `#[test]` functions, matching "16 passed".
- Status mask `0x0015_42C6`, string id 3079, ids 3264/232/267/4697 in the catalogue rows, and seven rows in `CONSUMABLE_ITEMS` (`piece_046.rs:80-84`, `119-169`).
- Ledger order and rules 1-8 (`piece_046.rs:684-783`): bar 2 only, `<=` replay guard, `now_ms < ready_at_ms` cooldown, Depleted and status-mask checks, one decrement per accepted use.
- Expiry at the exact boundary: `piece_046.rs:520-522` (`now_ms >= expires_at_ms`).

**Unsure:**
- The lab-only citations (`lab/reports/*/proof.json` SHA-256s, the Lua line numbers 8824/30493/30496, the 337-row class-9 count, and the wiki revision hashes) sit outside the searchable roots, so I did not verify them.
- The cached-wiki effect numbers and the 5-second tooltip were not re-checked.
