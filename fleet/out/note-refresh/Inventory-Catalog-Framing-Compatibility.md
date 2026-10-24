<!-- fleet job=note-refresh id=Inventory-Catalog-Framing-Compatibility status=done turns=9 usd=0.0083 tokens(read,write,in,out)=[124214, 29021, 20, 6872] model=claude-haiku-5-5 -->
# notes/Research/Inventory Catalog Framing Compatibility.md

**Verdict:** Stale on status, not on code. The framing fix is in the tree as described, but the note still says native acceptance is pending, and a native run has since accepted it (173814).

**Corrections:**

1. `old:` Native acceptance of the repair below remains pending.
   `new:` Native acceptance of the repair below passed in run `client-baseline-20261008T173814Z`: the startup catalogue was 311622 bytes with payload length 311614 and count 1647, matched the compiled community writer, and All Items, hats and Chef Head gear were populated.
   `why:` `repo:notes/Reviews/Native Inventory Repair 173814.md:3,9` (screenshots and the 311622/311614/1647 frame-665 catalogue); `repo:notes/Design/Build Ledger.md:91` ("Inventory, categories, equip | Native-verified"); `repo:notes/Tasks.md:86`.

2. `old:` Next native gate: fresh launch with the reviewed framing repair, browse All Items, Supplies/Food & Drink, Clothes & Armor/Hats and Chef Head gear; confirm existing food35 and hat14794 display with the same16 items and120 coins. A new grant is unnecessary.
   `new:` Native gate passed in run 173814 (fresh launch with the framing repair): All Items, Clothes & Armor/Hats and Chef Head gear showed the existing items with wallet 120, and no new grant was needed.
   `why:` `repo:notes/Reviews/Native Inventory Repair 173814.md:3,7` (populated All Items, both hats in Hats, Chef Head choices, wallet 120; initial checkpoint is the finalized 172324 checkpoint). `repo:notes/Tasks.md:86`.

3. `old:` Only `Inventory::definitions_packet` now wraps the same count/definition bytes with their original required length.
   `new:` `Inventory::definitions_packet` now wraps the same count/definition bytes with their original required length, by delegating to `v2_fixes::encode_definition_batch_v2`, which writes the 35/37 header and the payload length.
   `why:` `repo:prototype/osfr-tools/src/inventory.rs:625` (definitions_packet calls `v2_fixes::encode_definition_batch_v2`); `repo:prototype/osfr-tools/src/inventory_v2_fixes.rs:74-85` (payload_len computed and written after the 35/37 header, then count). The wrap lives in the helper, not in `definitions_packet` itself, so the old wording points at the wrong place.

**Checked and holding:**
- `Inventory::definitions_packet` exists at `repo:prototype/osfr-tools/src/inventory.rs:607`.
- The synthetic complete-packet regression exists: `repo:prototype/osfr-tools/tests/inventory.rs:211` (`definitions_catalog_matches_original_community_payload_framing`), which asserts `[35,0,37,0]`, length = len-8 and count 3 against the community vector fixture.
- The private compiled-writer comparison exists, ignored unless content is provided: `repo:prototype/osfr-tools/tests/inventory.rs:579-604`. It checks count against unique manifest IDs.
- The older 1386-item captured-self regression: `repo:prototype/osfr-tools/tests/inventory.rs:617` (`assert_eq!(inventory.state().items.len(), 1386)`).
- Client side: `FUN_0092f460` (dispatcher), `FUN_008f81f0`, `FUN_00a6d9b0` (inventory row predicate, calls `FUN_00b0d810` for definition lookup) and `FUN_00a6dd70` (category predicate) exist in the client DB and match the described roles.

**Unsure:**
- "Twelve ordinary inventory checks" pass: I did not count or run the suite, so I could not confirm the number.
- "All1701 disk rows reduce to1647 unique definitions through54 byte-identical duplicates": the 1647 figure matches the 173814 review and the test logic, and the private `inventory.json` is not in the repo to recount. `repo:notes/Research/Item Catalogue.md:79` gives a different figure (1,649 IDs from 54 duplicates), which is a conflict in that note, not evidence against this one.
- The lab paths and SHA256 values in Evidence are private and could not be checked from the repo.
