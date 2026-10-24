<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Wugachug status=nothing_found turns=23 usd=0.0317 tokens(read,write,in,out)=[984872, 90032, 48, 21202] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Wugachug.md

**Verdict:** current. I found no claim about our code or build status that is now false. The note is mostly client-locale and wiki evidence, and the few checkable repo claims hold at the tip.

**Corrections:** none.

**What I checked (all hold):**
- Postman level 15 gate, Postchug Runalug: the note says he is the Postman level 15 gate (row 57, Part B). `repo:prototype/osfr-tools/src/restoration/piece_042.rs:423` lists `gate(15, 387939, 387940, 387938, 387941, "Postchug Runalug")` in `POSTMAN_LEVEL_GATES`. The gate dialog text matches `piece_042.rs:343` and `tests/piece_042.rs:85`.
- Part row counts: Part A rows at lines 36–49 = 14; Part B rows at lines 57–69 = 13; Part C rows at lines 77–81 = 5; Part D rows at lines 89–96 = 8. These match the note's "14, 13, 5, 8" and "40 NPC rows" (also `NPCs.md:19`, "Written (40 rows)").
- Linked pages exist: all job pages cited (Chef, Postman, Card Duelist, Kart Driver, Adventurer, Medic, Ninja, Archer, Brawler) are in `notes/Build Guides/Content/Jobs/`. Dungeon pages Sweetwater Climb, Feisty Floren, Floren Forest and Tavern Cellar are in `notes/Build Guides/Content/Dungeons/`. NPCs - Merry Vale, Greenwood Forest, Highroad Junction, Wilds and Cobblestone Village exist.
- Cross-page deferrals: Merry Vale defers Cook Yumtumlot and Postchug Runalug to Wugachug (`NPCs - Merry Vale.md:155–156`). Greenwood defers Wugawump and the letter (`NPCs - Greenwood Forest.md:132`). Highroad Junction has the Bugawug Queen (`NPCs - Highroad Junction.md:77`).
- Sweetwater Climb gate: "gate in Wugachug" and "north of Wugachug" (`58657603`) agree with `Dungeons/Sweetwater Climb.md:18`. Medic.md:180 agrees.
- Card Duelist giver claims (Wugawump gives Squash the Shuffler; Runalug starts Parcel Recovery in the video) match `Jobs/Card Duelist.md:36–37, 95–96, 261`.
- Collections and achievements: "Wugachug Rare Exploration" and the Ledge of Relaxation (`collections.json:2141, 2154`); "Defeat 5/50/500 Bixies near Wugachug" (`achievements.json:5080–5128`).
- Client text spot checks: "The party tent is located at the west end of the Thoroughfare in Wugachug" (locale 70137); "heart of Wugachug" (5101334); "Chugawug Village" in the Woomplot lines (45771–45772); "Guard Thoomlug is our only guard" (42239); "Cakenstein has risen in Wugachug!" (6712); "Find all Rare Exploration coins in Wugachug" (119099); "A Missing Postchug" (46549).

**Unsure:**
- Overview, shops line: "Chef Clothing & Tools (level 9 tools, level 20 clothing)" is wiki-tagged. `Jobs/Chef.md:269` gives tool levels 1, 9 and 17 and clothing level 20, so the note's "level 9 tools" is a subset rather than false.
- Burnetta id cites differ between notes. Wugachug Conflicts 3 cites 1320192863 and 1472974034. `NPCs - Greenwood Forest.md:208` cites 1320192863, 3170182997 and 4206732159. I could not resolve the ids, so I left both alone.
- Parcel Recovery video frame: the note's Conflicts 10 cites `6mmERh2D8yc/00446`, while `Jobs/Card Duelist.md:37` cites `6mmERh2D8yc/00012`. Both may be valid frames. I could not confirm either from the tip.
- Video-only claims (nameplate frame counts, marker distances, "no recording shows…") cannot be checked from the repo and were not verified.
- The client locale id numbers in the note (e.g. 1426312283, 3004553622, 58657603) did not resolve through the locale tool's numeric lookup. The same text was found by search, so I checked the text rather than the ids.
