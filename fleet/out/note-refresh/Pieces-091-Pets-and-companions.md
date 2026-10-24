<!-- fleet job=note-refresh id=Pieces-091-Pets-and-companions status=done turns=11 usd=0.0131 tokens(read,write,in,out)=[235542, 43352, 24, 10687] model=claude-haiku-5-5 -->
# notes/Research/Pieces/091 Pets and companions.md

**Verdict:** minor-to-moderate drift. The status, artifact, path and test-count claims hold at the tip. Two rows in the "Client request bodies" table are now wrong because they predate the F114 review fixes (2026-10-17), and the Gaps section does not say that the codec in `piece_091.rs` is the stale one.

**Checked and holding:**
- `piece_091.rs` is not registered in `src/lib.rs`. `lib.rs` has `pub mod pets;` and no `restoration` module.
- The Rust suite has 15 `#[test]` functions (`tests/piece_091.rs`).
- The Python suite has 16 `def test_` functions (`tests/pieces/test_piece_091.py`).
- Sanctuary `PacketReaderExtensions.cs:499` is the `53 => reader.Read<byte>() switch` line.

**Corrections:**

1. `old:` `` `u8 action = 0` alone ``
   `new:` `` `u32 id` (uninitialised on the dismiss path) then `u8 action = 0`, 5 bytes on the wire; `FUN_00b60610` assigns only the action byte, but the shared writer `00b5a650` always emits the dword. ``
   `why:` `repo:prototype/osfr-tools/src/pets.rs:549-554` (the live route requires `body.len() == 5` and says the writer "always serializes a u32 id followed by the action byte"); `repo:notes/Autopilot/F114.md:42-46` (`00b5a650` writes the dword at +0xc and the byte at +0x10 for all subtype-4 senders, including `00b60610`).

2. `old:` `` `u32 pet_id`, `u32 item_id` ``
   `new:` `` `u32` ItemRecord definition id (`ItemRecord` +0x04), `u32` tint (+0x08); never a pet or instance id ``
   `why:` `repo:prototype/osfr-tools/src/bin/osfr_gateway/pet_wire.rs:4-6, 13-14`; `repo:notes/Autopilot/F114.md:24-28, 49-52`. The server resolves one owned instance by definition and tint (`repo:prototype/osfr-tools/src/pets.rs:590-600`).

3. `old:` `* Integration: the module is unregistered.`
   `new:` `* Stale codec: the module is unregistered, and its codec still models the one-byte forced-dismiss body (accepted at len 1) and reads subtype 32 as a pet id plus item id. The live route (\`src/pets.rs\`) takes the 5-byte form and the definition-id/tint pair. Correcting \`piece_091.rs\` and its round trips is a separate task. Integration: the module is unregistered.`
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_091.rs:206-218` (1-byte arm), `:142-144` (`SummonByItemId { pet_id, item_id }`); `repo:notes/Autopilot/F114.md:100-103`; `repo:prototype/osfr-tools/src/pets.rs:549-562`.

**Unsure:**
- The 28-record sample, "8,225 bytes total", "Captain Zeus 482 bytes" and "ten records with no trick list" were not re-measured. The first name matches `tests/piece_091.rs:82, 272`. The lab JSON is outside the refs roots, so I could not check the byte counts.
- The `ClientPcData.cs` line numbers (353 and 397) point into `lab/`, which I could not read. The refs copy is a different file (`OpenSourceFreeRealms/.../ClientPcData.cs:738`).
- The `FUN_00b5f720`/`FUN_00b5f8c0` flag at `+0x143` and the `DAT_*` follow-distance addresses were not checked against the client export.
- Same stale claim outside this note: `repo:notes/Build Guides/Gameplay/Pets.md:169` lists subtype 4 as "`u8 action` alone" for forced dismiss and `u32 pet id, u8 action` for the rest, and the subtype-32 row in the same table is not checked here. The fix for correction 1 applies there too.
