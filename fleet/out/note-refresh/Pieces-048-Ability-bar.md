<!-- fleet job=note-refresh id=Pieces-048-Ability-bar status=done turns=13 usd=0.0190 tokens(read,write,in,out)=[408392, 56179, 28, 15859] model=claude-haiku-5-5 -->
# notes/Research/Pieces/048 Ability bar.md

**Verdict:** Minor drift. The module facts hold: the 12-byte 42/6 request, the 63-byte 38/25 update, the 51-byte slot, four slots, the 42/9 refusal inside `piece_048.rs`, pruning, the 16 Rust tests and the 11 Python tests all match the tip. The integration section and the status line are stale: the wiring this note asks the lead to do has already landed in W146.

**Corrections:**

1. old: `Wire `piece_048::apply_parse` into the existing inventory dispatch in `src/gameplay.rs` where family 42 is currently handed to `inventory.handle` (which intentionally leaves the toolbar outside its layer), keep the `ActionBarState` in the version-2 snapshot behind `#[serde(default)]`, implement `ActionBarItems` over the live inventory, and forward the returned reply bytes through the existing `Outcome.replies`.` (wrapped across lines 138-142 of the note; copy it joined with single spaces)
   new: `Integrated by W146 (`86b1b0e`, Build Ledger line 92). `item_bar.rs` pulls this module in as `bar_wire` (`prototype/osfr-tools/src/item_bar.rs:42-43`) and routes 42/6 through `bar_wire::parse_assign` and `ItemBar::assign` (`item_bar.rs:233-239`, `297-311`), with 42/9 handled at `item_bar.rs:241-253`. `ItemBar` implements the live-inventory view as `View` (`item_bar.rs:167`) and holds `bar_wire::ActionBarState` (`item_bar.rs:154`). The snapshot field is `item_bar` with `#[serde(default, skip_serializing_if = "Option::is_none")]` (`prototype/osfr-tools/src/gameplay.rs:129-131`). `gameplay.rs:4439-4443` calls `handle_item_bar` before the family-42 branch (`gameplay.rs:4447-4449`, `handle_inventory`), and `gameplay.rs:5100-5101` returns the replies through `Outcome.replies`. `piece_048::apply_parse` (`restoration/piece_048.rs:643`) has no live caller; the live path calls `parse_assign` and `assign` directly.`
   why: `prototype/osfr-tools/src/item_bar.rs:42-43, 167, 233-253, 297-311`; `prototype/osfr-tools/src/gameplay.rs:129-131, 4439-4449, 5081-5101`; `notes/Design/Build Ledger.md:92`; `grep apply_parse` finds only its definition in `piece_048.rs:643`.

2. old: `Status: code plus tests returned for lead review, 2026-10-09 04:42 UTC.`
   new: `Status: integrated into the live item bar by W146 (`86b1b0e`); the module and its tests are current, and the path has never been run against the native client.`
   why: `notes/Design/Build Ledger.md:92` ("Built and wired (W146, `86b1b0e`) ... Never run natively."); `prototype/osfr-tools/src/item_bar.rs:42-43`.

**Unsure:**

- **42/9 record order.** The note says it is "not recovered" and the module refuses it. The module statement is true (`piece_048.rs:324-326`). But `item_bar.rs:7-10` says the 42/9 layout (slot, then definition and tint, 16 bytes) was "read from the bytes in W146", and `item_bar.rs:241-253` parses it. I could not check that against the native serializer `00a1c080`, so I left the note's "unrecovered" wording alone.
- **Fresh-bind template.** Reconstructed policy item 3 describes the module's `for_owned_action` (`piece_048.rs:394-412`), which is accurate. The live `ItemBar::slot_update` (`item_bar.rs:482-502`) then sets `total_refresh_time` and `cast_age` for consumables with a cooldown and disables bar items with no effect. The note does not mention this.
- **Owned-paths claim.** "No shared `lib.rs`, gameplay ... was touched" was true for this piece's work. The current tree wires it through `item_bar.rs` and `gameplay.rs`, so the claim is history only; I did not change it.
- **Lab evidence.** `lab/reports/piece-048-20261009T0442Z/` and the captured `PacketSendSelfToClient.json` are not in this repo. I could not confirm the quantities 59/28/33, the sentinel slot, or the report's "30 checks, 0 failing" count.
- **Community fields.** `Unknown7/10/12`, the `Unknown6 = 4` contradiction and the pinned Sanctuary facts are in `refs` or community code I did not open, so I did not check them.
