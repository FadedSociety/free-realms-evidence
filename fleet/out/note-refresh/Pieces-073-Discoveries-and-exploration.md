<!-- fleet job=note-refresh id=Pieces-073-Discoveries-and-exploration status=done turns=17 usd=0.0255 tokens(read,write,in,out)=[715841, 81043, 36, 16370] model=claude-haiku-5-5 -->
# notes/Research/Pieces/073 Discoveries and exploration.md

**Verdict:** minor drift. The module, tests, Python checker, test counts, the evaluator's policy and the "not wired / not registered" gaps all hold at the tip. One factual claim is wrong (the Lua zone-handler range), and three source citations point at the wrong lines or files in the supplied server.

**Corrections:**

1. `old:` i.e. exactly the range the Lua handler reacts to.
   `new:` i.e. inside the range the Lua handler reacts to (`1 < poiId < 11`, so ids 2–10).
   `why:` repo:`ScriptsBase.lua:5051` (`if 1 < tonumber(poiId) and tonumber(poiId) < 11`) accepts ids 2 through 10. repo:`prototype/osfr-tools/src/restoration/piece_073.rs:80-81` has `ZONE_NOTIFICATION_MIN_POI_ID = 2` and `MAX = 10`. The note's "exactly" is false because the handler also accepts id 2.

2. `old:` `LibSOE/SOE/BasePackets.cs:32-33` spells the same two ids
   `new:` `Server/LibSOE/Core/PacketCodes.cs:35-36` (enum `BasePackets`, line 6) spells the same two ids
   `why:` refs:`OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/PacketCodes.cs:6,35-36`. No `BasePackets.cs` file exists in the supplied server tree. The ids 56/57 are at lines 35–36, not 32–33.

3. `old:` (`Gateway.Login/LoginManager.cs:65-68`)
   `new:` (`Gateway.Login/LoginManager.cs:60-63`)
   `why:` refs:`OpenSourceFreeRealms/ofrserver/Gateway/Login/LoginManager.cs:60-63`. `HandlePacketClientIsReady` starts at line 60 and calls `Map.SendPacketPointOfInterestDefinitionReply` at line 63. Lines 65–68 are NPC, warp-stone and stat calls.

4. `old:` (`Gateway.MapChat/Map.cs:15-32`)
   `new:` (`Gateway.MapChat/Map.cs:15-34`)
   `why:` refs:`OpenSourceFreeRealms/ofrserver/Gateway/MapChat/Map.cs:15-34`. The per-record loop runs from line 15 through the `Unknown15` write at line 34, and the terminator is at line 38.

**Checked and holding (no change):**
- `prototype/osfr-tools/src/restoration/piece_073.rs` exists. `DiscoveryTracker::evaluate` (lines 378–423) implements the planar X/Z distance, the nearest in-range candidate, the optional location filter, the finite-radius check, and `AlreadyDiscovered` on replay.
- Nothing in `src/` calls `DiscoveryTracker` (only `tests/piece_073.rs` and the module itself). The "wire into the position update path" gate is still open.
- `pub mod piece_073` is not registered anywhere (`src/lib.rs` has no piece entries). The `#[path]` include is still in `tests/piece_073.rs:34-37`. `tests/warpstone_travel.rs:27-29` also includes the file by `#[path]`, which the note does not mention.
- Rust tests: 11 `#[test]` functions plus one `#[ignore]` private gate (`tests/piece_073.rs:392-394`). This matches "11 passed; 1 ignored".
- Python tests: 16 `def test_` methods (`tests/pieces/test_piece_073.py`), including the changed-capture-byte and changed-Lua-column rejections.
- `scripts/pieces/piece_073.py` exists.
- Lua data-source columns at `ScriptsBase.lua:2966-2980`, `CurrentPOI_DS.POIName` at 3085, `LoadingZone` at 5052, and the map loop at 31133–31134 all match the note.
- Locale: `93636` = Exploration, `5133` = Treeleaf's Retreat, `5707` = Briarheart Caverns, `93710` = Rainbow Lake.
- `client` has `Resources/CollectionCategories.txt` containing `1^93636^9535`.
- Notification-type labels: Sanctuary `PointOfInterestNotificationType.cs:5-8` gives Dungeon=3, Local=6, ZoneHub=7, Ruins=10, as the note says.
- `Build Ledger.md:134` still lists "073 points of interest" as a piece worth integrating, with no built/verified status.

**Unsure:**
- The `lab/` paths (`pseudocode.c` line numbers, the capture `0009-ready.bin` and its sha256, the `lab/reports/piece-073-20261009T0449Z/` artefacts, the 149-row POI JSON, and the 253/257/48/220 collection counts) are not in the repo, so I could not check them.
- The "102 of 103 name ids resolve" and "six shared name ids" claims depend on the POI JSON and could not be checked.
- The `piece-073` gate note (`notes/Reviews/Delegated Task Readiness*.json`) matches the note's gate list, so I did not treat it as a separate claim.
