<!-- fleet job=note-refresh id=Pieces-045-Cosmetic-equipment status=done turns=21 usd=0.0162 tokens(read,write,in,out)=[565197, 40735, 44, 10975] model=claude-haiku-5-5 -->
# notes/Research/Pieces/045 Cosmetic equipment.md

**Verdict:** minor drift. Nearly all checkable claims hold at the tip. One claim about field order is false.

**Corrections:**

- `old:` That order is exactly what `src/inventory.rs::write_attachment` serializes, so the attachment bytes the piece parses are the client's own appearance fields.
  `new:` The client's log lists the same fields that `src/inventory.rs::write_attachment` serializes, but not in the same order. The write order is ModelName, TextureAlias, TintAlias, TintIdOverride (the wire tint, `default_tint` when zero), Effect, then Slot last. The piece's `Appearance` reader follows the write order, so the attachment bytes are the client's appearance fields in that order.
  `why:` The client string `"EquipItem: Slot=%d, ModelName=%s, TextureAlias=%s, TintAlias=%s, TintIdOverride=%d, Effect=%d."` is at client fn 009392c0 (strings column). `repo:prototype/osfr-tools/src/inventory.rs:1494-1510` writes model, texture, tint_alias, then tint, effect, slot. `repo:prototype/osfr-tools/src/restoration/piece_045.rs:450-459` (`read_appearance`) reads in that write order. The same false "exact order" wording also appears in the module header at `repo:prototype/osfr-tools/src/restoration/piece_045.rs:124` ("in the client's own `EquipItem` log order") and should get the same fix.

**Checked and holding:**

- `src/restoration/piece_045.rs` exists. `COSMETIC_SLOTS` has 7 rows (1, 2, 3, 4, 5, 6, 17) with the category ids, names and row counts in the note's table (lines 55-105).
- The module is not yet registered in `src/lib.rs`. It is included by `#[path]` (line 34), matching the "lead registration" wording.
- The `write_attachment` tint rule (`tint == 0 ? default_tint : tint`) matches the note.
- `equip` in `src/inventory.rs:1215-1243` refuses an unowned item, a definition slot that differs from the requested slot, and a class the profile does not allow.
- `replay_equip` only accepts family 42 with opcode 3 or 8; anything else returns `NotEquipRequest` (`piece_045.rs:555-567`). The 3 and 8 shapes match `inventory.rs:1189-1208`.
- The validation rules match `validate_appearance` (`piece_045.rs:245-287`): `.adr` mesh, `<race>`/`<gender>` placeholders only, non-empty texture with no `<>`, non-empty tint alias, non-negative tint, 4,096-byte bound.
- Test counts: `tests/piece_045.rs` has 8 `#[test]` plus 1 `#[ignore]`. `tests/pieces/test_piece_045.py` has 10 `def test_`.
- Locale ids 23319 Hats, 23320 Gloves, 23321 Shirts & Dresses, 23322 Pants, 2482 Shoes, 23324 Miscellaneous, 5273 Costumes and 958 Clothing all match.
- `ScriptsBase.lua:9005` is `EquipmentSlotLabels`, as cited.
- The community handler `InventoryPacketEquipByGuidHandler.cs:128` has the `Tint == 0 ? Icon.TintId : Tint` rule and takes the slot from the definition, not the request (as the note says).
- `scripts/pieces/piece_045.py` exists and reads the Rust slot table (`rust_cosmetic_slots`, `DEFAULT_RUST_MODULE`).
- Native equip and restart are still unproved. Nothing in the Build Ledger or Autopilot reports closes them, so the boundary section stands.

**Unsure:**

- The catalogue row counts (7522, 8254, etc.), the 541/55 slot-17 overrides, the 32 creator ids, the 316 tint deltas and the lab report numbers (21 equipped rows, 686 attachment rows, 851 checked definitions) rest on `lab/` artifacts that are not in the repo or in the searchable roots. I could not check them.
- The client pseudocode line 1099052 cited in the note could not be confirmed. The log string is in the client database at function 009392c0, but its line number is not visible.
- The note says the community handler "fills the attachment from the definition". Its visible `PlayerUpdatePacketEquipItemChange` (`InventoryPacketEquipByGuidHandler.cs:210`) uses `clientItem.Tint` directly. The claim is about the client-update packet, so I left it.
