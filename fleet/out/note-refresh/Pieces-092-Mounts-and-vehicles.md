<!-- fleet job=note-refresh id=Pieces-092-Mounts-and-vehicles status=done turns=17 usd=0.0231 tokens(read,write,in,out)=[593439, 69688, 36, 16840] model=claude-haiku-5-5 -->
# notes/Research/Pieces/092 Mounts and vehicles.md

**Verdict:** minor drift. The artifact counts, the 34-row capture census, the item-11038 tie, the stat values, the Lua gates, the sub-opcode table and the 168/2 and 168/4 field orders all match the tip. Three statements are now wrong or incomplete: the pinned-server dismount claim, the routing picture behind gate 1, and the OSFR read description.

**Corrections:**

1. `old:` Both pinned servers dismount before spawning; what the original server sent for a duplicate
   `new:` Sanctuary dismounts before spawning (`Sanctuary/src/Sanctuary.Gateway/Handlers/MountBasePacket/PacketMountSpawnHandler.cs:53`). The supplied OSFR spawn path does not: `HandleMountBasePacket` sends the spawn straight to `SendPacketMountResponse` with no dismount (`OpenSourceFreeRealms/ofrserver/Gateway/NPC/MountSystem.cs:19-22`). What the original server sent for a duplicate
   `why:` `refs:OpenSourceFreeRealms/ofrserver/Gateway/NPC/MountSystem.cs:19-22` (no dismount) versus `refs:Sanctuary/src/Sanctuary.Gateway/Handlers/MountBasePacket/PacketMountSpawnHandler.cs:53`. The same false "both" claim is repeated in the `piece_092.rs` header at lines 35-37, which is worth fixing in the same pass.

2. `old:` 1. Dispatch tunneled inner opcode 168 to the decoder and answer `168/2` + `168/4` from a server
   `new:` 1. Route tunneled inner opcode 168 to the `piece_092` decoder. Today the gateway sends family 168 to the separate `mounts.rs` path (`repo:prototype/osfr-tools/src/gateway.rs:519-520`; W162 summon/board/put-away in `repo:prototype/osfr-tools/src/gameplay.rs:2028`), which already answers `168/2` and `168/4` with ownership read from inventory (`repo:prototype/osfr-tools/src/mounts.rs:209-221`). `piece_092` is still unrouted, so this gate means joining or replacing that path. Answer `168/2` + `168/4` from a server
   `why:` `repo:prototype/osfr-tools/src/gateway.rs:519-520`; `repo:prototype/osfr-tools/src/gameplay.rs:2028`; `repo:prototype/osfr-tools/src/mounts.rs:209-221`. `grep piece_092` finds no caller outside its own module and tests.

3. `old:` The supplied OSFR server reads the sub-opcode byte and then an `i32` for
   `new:` The supplied OSFR server reads the sub-opcode byte and then an `i32` (read before the switch for every sub-opcode, `MountSystem.cs:14-15`) for
   `why:` `refs:OpenSourceFreeRealms/ofrserver/Gateway/NPC/MountSystem.cs:14-15` reads the `i32` before the switch, so it is not spawn-only at the read. It is only used on the spawn path (`MountSystem.cs:19-21`).

**Checked and holding (no change):** 13 sub-opcode constants and the `0xa8` vtable pattern (`client_sql` on `FUN_0089f9c0`); 34 `CAPTURED_MOUNTS` rows, the members-only census (1017), fly-training rows (1019, 1017, 1001) and able-to-fly rows (1030, 1025, 1024, 1002) (`piece_092.rs:182-296`); item 11038 shared by 1002 and 1017 (`piece_092.rs:226`, `:265`); `item_bound_mount` taking the last match (`piece_092.rs:307-312`); Fire Hawk, able-to-fly, 1023 and default stat blocks and the dismount block (`piece_092.rs:512-551`, matching `MountSystem.cs:165-265`); the 168/2 and 168/4 field orders (`piece_092.rs:571-602`, matching `MountSystem.cs:156-164` and `:291-292`); test counts 11 Rust (`tests/piece_092.rs`) and 20 Python (`tests/pieces/test_piece_092.py`); the module is still not registered in `lib.rs` or `restoration/mod.rs`; the Lua gate at `ScriptsBase.lua:30411`, `Mount.Spawn` at `:30516`/`:34997` and `Mount.Dismount` at `:30509`.

**Unsure:**
- The four "not in either pinned item table" claims (81256176, 163632473, 35463452, 6346231). My search of `refs` did not settle them; the hits were inventory files, not item tables.
- The Fire Hawk "verbatim" match to `Mounts.json` row 13459, and the "byte-identical" `Mounts.json` in FreeRealms-Legacy. Not checked.
- The `67/64/68`-style CharacterStatId names. The constants match OSFR, but I did not check them against the recovered enum.
- Gate 2 (add the `38/7` stat block on spawn and dismount). I found no stat-block code in `mounts.rs`, so the gate looks open, but I did not search all of `gameplay.rs`.
- `encode_mount_response` writes the last field as `f32`, while OSFR writes `AddHostInt32(0)` (`MountSystem.cs:162`). The bytes match for 0, but the note's "field for field" wording hides the type difference.
- Sanctuary's `LastOrDefault` tie-break (named in the note and in `piece_092.rs:38-40`) was not checked.
