<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Lakeshore status=done turns=19 usd=0.0205 tokens(read,write,in,out)=[681826, 61028, 40, 12125] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md

**Verdict:** minor drift. Most of the note is client-text and wiki sourcing that the code does not contradict. Two statements about the repo's state are now false, and both sit in places a builder would trust.

**Corrections:**

1. `old:` - **No positions.** No map coordinates for any NPC. Only text ("on the docks", "east, edge of lake", "south of the Robgoblin Camp") and two warpstone-distance markers (Mister Nooklings 35 m, Lan Spryleaf 70 m).
   `new:` - **No recovered positions.** No client or video source gives map coordinates for any NPC. Only text ("on the docks", "east, edge of lake", "south of the Robgoblin Camp") and two warpstone-distance markers (Mister Nooklings 35 m, Lan Spryleaf 70 m). The server's `data/content/npcs/lakeshore.json` does carry positions for Lakeshore NPCs (e.g. Alexander at `[84.92, 42.0, 1017.64]`), but they are reconstructed by POI-name match (`placement_source: reconstructed_poi_name_match`, `placement_confidence` low or medium, `placement: poi_anchor`), so they are not evidence of where an NPC stands.
   `why:` repo:prototype/osfr-tools/data/content/npcs/lakeshore.json:58-72 (Alexander position, placement_source, confidence) and :1224-1225, :552-553 (further records); the same POI-anchor method is recorded in repo:notes/Autopilot/F168.md:51.

2. `old:` The **Durango Zoo** has its own placeholder ([[NPCs - Durango Zoo]]) and is left out.
   `new:` The **Durango Zoo** has its own page ([[NPCs - Durango Zoo]]), which holds the zoo's NPC rows, and is left out here.
   `why:` repo:notes/Build Guides/Content/NPCs/NPCs - Durango Zoo.md:1-12 (a full 130-line NPC page with front matter, sub-areas and source tags, not a stub).

**Checked and holding (no change):**
- Conflict 12 (Mino Tendersole): Briarwood now ties him to Dori of Lakeshore. Confirmed at repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:36 and :344.
- Conflict 6 (Ty): listed under Part H of NPCs - Seaside. Confirmed at repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:166-174.
- Ty's Ninja level 10 gate: consistent with repo:notes/Build Guides/Content/Jobs/Ninja.md:41, :93.
- Natali's four repeatable Wizard contracts (Troll, Robgoblin, Secret, Life and Death Magic): consistent with repo:notes/Build Guides/Content/Jobs/Wizard.md:89, :101, :113, :119.
- Every `[[...]]` link target in the note exists as a page (Dungeons and Jobs folders, NPCs folder).

**Unsure:**
- `repo:notes/Design/Field Enemies.md:35-37` gives proposed field-actor coordinates for Troll Bone Shamans in the "Lakeshore / northeast Wilds" area, anchored on community NPC ids 3149 and 3150. These are enemy placements, not NPCs, so I did not treat them as contradicting the Gaps line. Correction 1 keeps the note's own "No recovered positions" wording and does not cover them.
- The note's wiki and video claims, quest-text wording matches, merchant dates and the Campaign 4 details were not checked. They are client or wiki sourcing, not code state.
