<!-- fleet job=note-refresh id=Self-Data-Layout status=done turns=21 usd=0.0250 tokens(read,write,in,out)=[728053, 69093, 44, 18065] model=claude-haiku-5-5 -->
# notes/Research/Self Data Layout.md

**Verdict:** minor drift. The architecture, file and symbol citations, native addresses, and the wire-layout facts I could check all hold at the tip. Two statements are off: the test count and one "named byte array" description.

**Corrections:**

1. `old:` The required Cargo target passed nine synthetic tests, with the private oracle ignored by default.
   `new:` The required Cargo target (`tests/startup_selfdata.rs`) has two synthetic tests (`synthetic_typed_sections_round_trip`, `built_self_message_contains_another_characters_inventory_equipment_and_pose`), with the private oracle (`private_self_capture_rebuilds_identically`) ignored by default.
   `why:` repo:prototype/osfr-tools/tests/startup_selfdata.rs:310-312 (ignored oracle), :334-335 and :343-344 (the two synthetic tests). That file holds only three `#[test]` functions, so nine is not what the target runs at the tip.

2. `old:` 51-byte action-slot payloads, and 81-byte effect payloads.
   `new:` 51-byte action-slot payloads (`[u8; 51]`), and 81-byte effect payloads (a `Vec<u8>` whose length is asserted at build time, not a fixed array).
   `why:` repo:prototype/osfr-tools/src/startup_selfdata.rs:310 (`fields: [u8; ACTION_SLOT_BYTES]`), :318 (`payload: Vec<u8>`), :1294 (`assert_eq!(effect.payload.len(), EFFECT_PAYLOAD_BYTES)`).

**Checked and holding:**
- `src/startup_selfdata.rs` exists. `parse_self`, `parse_self_with_quest_bindings` and `build_self` are at lines 1018, 1024 and 1161. Gateway uses it at `gateway.rs:853-854`.
- `inventory::InventoryState`, `InventoryItem`, `EquippedItem` (`inventory.rs:79`, `:53`, `:70`) and `quests::QuestState` (`quests.rs:60`) exist and are used as described.
- The item wire shape matches `inventory.rs:1432-1456` and `startup_selfdata.rs:665-682`: 30 bytes without rental, 46 with it. `stored_count` is set to 0 on parse (`startup_selfdata.rs:655-657`).
- Quest binding: quest 1617, objective 0, offset 4112 (`startup_selfdata.rs:19-23`). The body-offset arithmetic (157819 + 4112 = 161931) is consistent.
- The item reader is bounded at 30 bytes per row (`startup_selfdata.rs:1098`). The 1,962-byte `post_effect_tail` is kept opaque (`:1126`), and the test asserts 253 collections, 1386 items, 16 profiles and the 1962-byte tail (`tests/startup_selfdata.rs:317-322`).
- Native addresses in the note exist in the client `fn` table, including `009471a0`, `0089b240`, `00944fe0`, `00a19da0`, `00a18990`, `00911d60`, `008fa5c0`, `008ca050`, `00913850`, `008e9c10`, `008fc8c0`, `008fc960`, `00ae1f70`, `008e8230`, and `00c8df70`.

**Unsure:**
- Line 53: "nine synthetic checks pass in the isolated W18 harness". That harness and the `lab/reports/selfdata2-*` files are outside this repo, so I could not check them. It is probably the same stale count as correction 1.
- Native row 12 calls `0092b050` an "objective helper". The client's record for it reads `ClearTemporaryQuestObjectiveRecords` (game.quest, destroys temporary records). It is not a reader. I did not verify whether the reader path calls it.
- The `lab/` directory (oracle outputs, `probe_sections_corrected.py`, the 253/1386/1962 capture counts beyond the test assertions) is not in the repo, so those capture-derived offsets are unverified here.
- The capture-derived byte offsets in the table (for example the profile-1 span at 298/697) could not be checked without the reference capture.
