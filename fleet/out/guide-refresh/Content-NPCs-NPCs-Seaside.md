<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Seaside status=done turns=17 usd=0.0186 tokens(read,write,in,out)=[462491, 59198, 36, 13077] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Seaside.md

**Verdict:** current, with one minor drift. The note cites no code paths, routes or build status, so there was no code claim to falsify. Its checkable claims are client strings, quest titles, and its own row counts, and the ones I sampled hold.

**Corrections:**

- `old:` 3. **Troubled Waters / Troubling Waters.** The wiki Captain Sunspark page lists "Troubling Waters" while the Mayor Gilly page and the Heroes Journal page say "Troubled Waters". The client has only "Troubled Waters" (2309051198). Client used.
  `new:` 3. **Troubled Waters / Troubling Waters.** The wiki Captain Sunspark page lists "Troubling Waters" while the Mayor Gilly page and the Heroes Journal page say "Troubled Waters". The client has "Troubled Waters" (2309051198) as the Seaside quest title; it also holds a separate Ninja-job entry "Ninja: Troubled Waters" (locale text 78869), which is not this quest. Client used.
  `why:` The locale holds "Troubled Waters" (5101823) and "Ninja: Troubled Waters" (78869), so "only" overstates the match. The Seaside quest and the Ninja entry are two strings.

Checked and holding:
- Row counts in the Counts section match the tables: Part A 13, Part C 37, Part D 5, Part E 13, Part F 8, Part G 9, Part H 13 rows with 17 names (Cakeling has no name entry), Part I 2. The Quest index has 71 rows, and 10 `[inferred]` marks.
- Link targets exist: every `[[...]]` dungeon, job and NPC page the note names is in `notes/Build Guides/Content/Dungeons/`, `Jobs/` or `NPCs/`.
- Client text and titles: "Welcome to Seaside where vacation is an adventure!", "the first building ever built in Seaside", "has a green roof", "follow the beach North", "lives under the boardwalk", "Give Crabcake the Treat", "Crabcake believes…", "Master Kai" as founder, "Beach Ball Wear?", "Cleansing the Pearls", and the titles Horrible Hiccups, Smoothie Operator, Hungry Hungry Troll, Cakey Clue, Diggy's Shopping List, Half a Dozen, No Prey No Pay, Open House Clean-Up, Scaredy Pants, Having a Ball, Seaside Report, Sandstorm's Grand Opening and Legendary Seaside Coin.

**Unsure:**
- The note's numeric citation ids (for example 2194642825, 3042670347, 2309051198) do not resolve in the `locale` tool, which keys strings by different numbers. I checked those claims by text search, not by id, so the id column is unverified.
- "Shadeside Island" (Overview sub-area list) returned no locale hit. I did not check whether it appears elsewhere in the client, so I left it alone.
- The Ty row and Conflict 10 say the client has no Seaside tie for Ty. I did not run a full client search for Ty's location, so I left it alone. Our `scripts/quest_audit.py` (lines 301-304) uses a Ty-in-Seaside fixture, but that is test data, not evidence about the client.
