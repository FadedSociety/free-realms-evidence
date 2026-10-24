<!-- fleet job=guide-refresh id=Gameplay-Housing status=done turns=26 usd=0.0290 tokens(read,write,in,out)=[1094267, 80774, 54, 15855] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Housing.md

**Verdict:** minor drift. The client-side facts I could check hold. The one claim about our own code that is now false is the note's statement that the community lot table is excluded from the project. The server's `houses.json` takes its bounds, spawns and lot roster from that same community file.

**Corrections:**

1. `old:` Our own scene and terrain data supplies boxes; the community lot table is excluded from this project.
   `new:` Our `houses.json` takes provisional spawn points, six-float build-area bounds and the lot roster from the community Legacy `Houses.json` reference (AGPL-3.0, reference only, no code copied); the scene choices are our own matches (R), and the bounds are still provisional.
   `why:` repo:prototype/osfr-tools/data/content/houses.json:3 (provenance: "Legacy Houses.json ... supplies provisional spawn and six-float bounds"), :11 ("Legacy six-float bounds and spawn values remain provisional"), :23 (`build_areas` on each lot), :57 (`source_tag` "legacy-reference:FreeRealms-Legacy@AGPL-3.0:Houses.json:Id=1").

2. `old:` The vault holds a community lot table that this guide does not use; our server needs boxes derived from the client's own scenes.
   `new:` The vault holds a community lot table. Our server's `houses.json` already uses it for provisional spawn and build-area bounds (see the provenance and `source_tag` lines), so the boxes are not yet derived from the client's own scenes.
   `why:` repo:prototype/osfr-tools/data/content/houses.json:3, :11, :57.

3. `old:` the wiki list (about 30 lots) is the only roster.
   `new:` the wiki list (about 30 lots) is the only roster of lot names. Our `houses.json` lot rows carry their own `property_id` and `name_id` values taken from the Legacy `Houses.json` ids (for example `Id=1` to `Id=8` in the `source_tag` lines).
   `why:` repo:prototype/osfr-tools/data/content/houses.json:17-19, :57, :104.

**Checked and holding (no change):**
- Only the housing family is routed. The request decoder covers inner opcodes 1, 2, 3, 4, 5, 6, 10, 14, 19, 20 and 23. Reply constants cover 28, 39 to 45, 51 and 53. The rating service (174) is not implemented, so the note's "implement the rating service" item is still a to-do. (repo:prototype/osfr-tools/src/housing_service.rs:63-90, :394-511; :1249-1299.)
- The enter reply order is 45, 28, 44, 43, then the saved 40s, which matches the "127/28 before any 127/4x" requirement (repo:prototype/osfr-tools/src/housing_service.rs:1382-1393; repo:prototype/osfr-tools/src/gameplay/housing.rs:165-170).
- Housing is dormant unless `houses.json` exists (repo:prototype/osfr-tools/src/gameplay/housing.rs:1-7, :36-39).

**Unsure:** these sit in the "What the Rust server must do" section. They are written as requirements, so I did not change them. Our code does not yet match them:
- Step 4 (line 195) says refusals use the 127/46 codes. The server never emits 127/46 and sends a chat line plus 127/53 only for a few denials (repo:prototype/osfr-tools/src/housing_service.rs:81-90, :705-712; repo:prototype/osfr-tools/src/gameplay/housing.rs:99-109).
- Step 3 (line 194) says a grant sends 127/49. The code says 127/49 is not sent (repo:prototype/osfr-tools/src/housing_service.rs:1410-1413).
- Steps 8 and 9 (lines 199-200) list 127/7, 9, 11, 12, 13, 15, 16, 17, 21 and 22 as to-do. The decoder returns UnknownOpcode for them (repo:prototype/osfr-tools/src/restoration/piece_025.rs:274).
- Step 13 (line 204) asks for pet dismissal on house entry. I found no housing hook in `pets.rs`; the only dismiss code is generic (repo:prototype/osfr-tools/src/pets.rs:514-561).
- Client-side addresses and column lists were not checked against the shipped client, because that is outside this pass.
