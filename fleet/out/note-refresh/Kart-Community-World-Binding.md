<!-- fleet job=note-refresh id=Kart-Community-World-Binding status=done turns=21 usd=0.0274 tokens(read,write,in,out)=[836604, 79372, 44, 18219] model=claude-haiku-5-5 -->
# notes/Research/Kart Community World Binding.md

**Verdict:** minor drift. Most checkable claims hold at the tip: the op31 field map and its 87-byte layout match `repo:prototype/osfr-tools/src/zone_transition.rs:190-250`; the `sg_kt_track` manifest rows match `refs:osfr-asset-manifest/Assets_manifest.txt:84051-84102`; the ForgeLightToolkit `.gzne` TODO is at `refs:ForgeLightToolkit/Editor/LoadWorldWindow.cs:124`; the `sanctuary.db` entity list matches `refs:FreeRealms-Legacy/src/Sanctuary.Database/Entities/`; the "no `917566` / `speedway` in OFR" negative holds in `refs:OpenSourceFreeRealms`.

**Corrections:**

1. `old:` `` `WorldZone.GetZoneAreaId(position)` over area definitions ``
   `new:` `` `StartingZone.GetZoneAreaId(position)` over area definitions (`FreeRealms-Legacy/src/Sanctuary.Game/Zones/StartingZone.cs:1302`); the public copy has no `WorldZone` class, and its spatial tests are `Vector4Extensions.IsInCircle` / `IsInRectangle` ``
   `why:` `refs:FreeRealms-Legacy/src/Sanctuary.Game/Zones/` lists only `BaseZone.cs`, `CollectionNodeStatus.cs`, `IZone.cs`, `StartingZone.cs`, `ZoneTile.cs`. `StartingZone.cs:1302-1318` holds `GetZoneAreaId`, and `refs:FreeRealms-Legacy/src/Sanctuary.Core/Extensions/Vector4Extensions.cs:15-20` holds the primitives. `WorldZone.GetZoneAreaId` exists only in the other forks (e.g. `refs:Sanctuary/src/Sanctuary.Game/Zones/WorldZone.cs:37`).

2. `old:` `2/3/4/5/6/62/102-133`
   `new:` `family-41 sub-opcodes 2/3/4/5/6 and a sparse subset of 102-133 (102-109, 114, 120-125, 129-130, 132-133), plus top-level family 62 (EncounterDataCommon)`
   `why:` `refs:FreeRealms-Legacy/src/Sanctuary.Packet.Common/Extensions/PacketReaderExtensions.cs:383-408` (family 41 switch; no sub-opcode 62 there). Top-level `62 => "EncounterDataCommon"` is at `:563`. The range 102-133 is not contiguous in the map.

**Unsure:**

- **Frame 15449 contents.** The note says it is `41/2` PlayerEnter. `notes/Research/Kart Entry Encounter Binding.md:106` and `notes/Research/Kart Native Race Entry Contract.md:57-58` describe it as a 41/114 + 41/2 bundle, which agrees with the note. But `notes/Autopilot/T392.md:81` says the server sent `39/23` at frame 15449. I could not settle this from the repo, because the capture files are in the lab.
- **"Public code search for `EncounterDetailsResponsePacket` returns only emulator name tables/forks."** `refs:Sanctuary-combat-pr-research/pr-76/src/Sanctuary.Packet/BaseEncounterPacket/EncounterDetailsResponsePacket.cs:34` is a full class with a body. That is a PR research checkout, not a server or name table, so the claim may be too strong. I did not change it.
- **Lab-only artifacts** (`lab/reports/...` probes, `proof*.json`, `final-hashes.txt`, the 24-pack catalogue offsets and hashes, the `FabledRealms.json` local/downloaded SHAs and sizes, and the `op43/12` Mining packet) are not in the repo or refs. I could not verify them.
- **`sg_demo_derby_encounter.gzne`** is listed as pack size 84; the manifest line `refs:osfr-asset-manifest/Assets_manifest.txt:82560` gives 58. The note's "both recorded, not reconciled" framing only covers the two `sg_kt_track` rows, so this is not clearly false. Recorded here for awareness.
