<!-- fleet job=guide-refresh id=Gameplay-Pets status=done turns=29 usd=0.0285 tokens(read,write,in,out)=[1130944, 66289, 60, 17701] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Pets.md

**Verdict:** minor drift. The client-side readings and the server-side claims I could check mostly hold. One wire-body row is wrong, and one generated count is off by one per bucket.

**Corrections:**

1. `old:` `| 32 | PetSummonByItemId | u32 pet id, u32 item id | `00b60110` |`
   `new:` `| 32 | PetSummonByItemId | u32 ItemRecord definition id, u32 tint | `00b60110` (caller `00a1ec00` pushes ItemRecord +4, then +8) |`
   `why:` The two words are the item definition id and the tint, not a pet id and an item id. `repo:notes/Autopilot/F114.md:24-26` ("subtype 32 fields are the client `ItemRecord` definition id and tint"). `repo:notes/Autopilot/F161.md:86-90`. `repo:prototype/osfr-tools/src/pets.rs:517-522` (`SummonByItem { definition_id, tint }`, "neither word is a pet or instance id") and `pets.rs:590-605`. Client: in `00a1ec00` the call to `FUN_00b60110` takes `piStack_1a0+8` (tint) and `+4` (definition), per the decompiled pseudocode. This is the wire body that matters most to a builder.

2. `old:` `341 accepted functions: 150 confirmed, 95 likely, 29 speculative, 67 unknown.`
   `new:` `341 accepted functions: 149 confirmed, 96 likely, 29 speculative, 67 unknown.`
   `why:` Client label table, subsystems `net.pet`, `ui.pets` and `game.pet` (341 rows): `confidence` = confirmed 149, likely 96, speculative 29, unknown 67. The total of 341, the subsystem split (160 / 101 / 80) and the wire-linked count (47) all match. Minor, and this section is generated.

**Checked and holding (no change):**
- `HandlePetPacket` `00b5ce60`: 22 numeric switch cases (1, 3, 5, 9, 10, 0xb-0xf, 0x10, 0x14, 0x15, 0x17, 0x19, 0x1a, 0x1d, 0x1f, 0x21, 0x22, 0x24, 0x26). Other "case" hits are nested switches.
- Function roles in the Key functions table: `00b549f0` summon gate, `00b60080` SendPetSummon, `00b58bd0` PetIsActive, `00b54080` SetActivePet, `00b5fcf0` SendPetFollowLocation, `00b5f670` SendPetFavoriteTrick, `00b60770` PetTileTargetHandler::OnMessage, `00cce850` PetTactile ctor, `00cc8890` ScorePetTrickGesture, `00c066a0` Lua Summon, `00c07420` Lua Dismiss.
- Lua `Pet` module: the 24 names listed match the count.
- Subtype 4 body (u32 id + action byte) and PetList/PetActive layouts match `repo:prototype/osfr-tools/src/pets.rs:547-561` and `pets.rs:1643-1650`.
- The "35 classes, subtypes 0/27/30/37 missing" statement is consistent with the subtype table.
- Server: "Keep the active pet in session state" matches `repo:prototype/osfr-tools/src/gameplay.rs:254-256` (`PetService`, actor reset on reconnect).

**Unsure:**
- **"What the Rust server must do" (lines 190-208)** reads as a to-do list, so I made no correction. The current decoder accepts only client subtypes 4, 6, 24 and 32 (`repo:prototype/osfr-tools/src/pets.rs:547-607`; everything else returns `None`). It does not handle PerformTrick (7), TrickGestureResult (8), feed (19), groom (18), utility (16), equip (11), favourite (14), PetCanGoLocation (26), PetInWater (28), buy (25), delete (17) or preview (38). Dismiss on house entry is also not present: `settle_pets` (`repo:prototype/osfr-tools/src/gameplay.rs:2138-2148`) dismisses only on zoning. A reader could take item 5 to 13 as built, so this may be worth an explicit status line.
- **Subtype 6 layout:** the note says "name parts as strings" (line 170). The server decodes one length-prefixed UTF-8 name (`pets.rs:565-579`). The note's own Open questions (line 224) leave it unconfirmed, so I did not change it.
- **Build Ledger** (`repo:notes/Design/Build Ledger.md:109`) says pets are "Built (registered, not routed)". The gateway does route the pet family (`repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:16, 479, 948`, and `notes/Autopilot/F114.md`, `F161.md` with pet_routing tests). That line is outside this note, but it is probably stale.
- The client table row for `HandlePetPacket` says 9177 bytes. I could not verify the byte count from the client DB fields I had.
