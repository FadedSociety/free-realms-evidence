<!-- fleet job=note-refresh id=World-Object-Catalogue status=done turns=14 usd=0.0141 tokens(read,write,in,out)=[290256, 42666, 30, 11663] model=claude-haiku-5-5 -->
# notes/Research/World Object Catalogue.md

**Verdict:** minor drift. The parser description and the catalogue's shape hold, but the script path is wrong and the "server sends 47/9" trigger conclusion is contradicted by client Lua that the note does not cite.

**Corrections:**

1. `old:` `project/scripts/world_objects.py` parses the client's terrain chunks
   `new:` `scripts/world_objects.py` parses the client's terrain chunks
   `why:` repo:scripts/world_objects.py:1-9 is the parser. There is no `project/` directory at the repo root (root listing). notes/Project Map.md:81 lists it as `world_objects.py` under Content.

2. `old:` So the server sends **47/9** with the region id when the player crosses into a region.
   `new:` The banner also has a Lua caller that the dispatcher note omits. `BaseClient_CurrentPOI_OnDataUpdate` calls `NotificationHandler:LoadingZone(poiId)` when the `BaseClient.CurrentPOI` row has `1 < poiId < 11`, so the banner follows the POI data source. That data source is fed by POI definitions (packet 57, `PacketPointOfInterestDefinitionReply`). Whether the server also sends 47/9 for it is unproven.
   `why:` ui:ScriptsBase.lua:5049-5053 (the caller and the range); ui:ScriptsBase.lua:11642-11645 (`LoadingZone` wrapper); repo:scripts/pieces/piece_073.py:11-13 (same range, cited from ScriptsBase.lua); repo:prototype/osfr-tools/src/restoration/piece_073.rs:4-10 (opcodes 56/57 and the `BaseClient.CurrentPOI` columns `POIName, POIId, AreaId`).

3. `old:` Candidates: client region data (Adventurer's Journal `RegionData`), zone areas, or POI/area tables.
   `new:` Candidates: the POI definition rows (`Id, Name, ZoneID, X, y, z, ...` from opcode 57) that feed `BaseClient.CurrentPOI`, which the Lua banner caller already keys on; client region data (Adventurer's Journal `RegionData`); or zone areas. POI rows are points, not boundaries, so a boundary source is still needed.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_073.rs:8-10; ui:ScriptsBase.lua:5049-5053.

**Unsure:**

- **Native jump table claim** ("jump table at `00a92480` sends subtype 9 ... push `0x1818230` at `00a921a9`"). The client decompile of `00a91bf0` (client_sql) has no `01818230` hit, and I found no `0x1818230` string anywhere in the fn pseudocode. Repo searches for `47/9`, `(47, 9)` or `(47, 0, 9` found no sender in src. I could not confirm or refute the subtype-9 mapping; it may be right but is not demonstrated.
- **Run numbers** (2,130 chunks, 80,198 objects, 1,992 distinct models, 52 failed). `lab/reports/world-objects-20261015.json` is not in the tree. The script prints chunk, object and error counts (scripts/world_objects.py:123-125) but never counts distinct models, so "1,992 distinct models" has no code path here. I could not verify the figures.
- **"The failures are probably older versions."** The parser accepts versions 0–6 (scripts/world_objects.py:98) and reads material/tint only for version ≥ 6 (:63-67). Its real failure modes are the version >6 check, the length mismatch (:101-102), and layout or zlib errors. Older-version files would therefore not fail on version. I could not tell from the code which failure occurred for the 52 chunks.
- **Output source.** The note says "from every `.gcnk` under `lab/extracted`". The script takes both the input directory and the output path as CLI arguments (scripts/world_objects.py:107-110) and hard-codes neither, so this is a usage choice, not a code fact. Left as is.
- **Placement table** (NPC ids, coordinates, object ids, warpstone ×22). Not checked against data. The Troll Summoner string 42056 is confirmed in the locale table.
