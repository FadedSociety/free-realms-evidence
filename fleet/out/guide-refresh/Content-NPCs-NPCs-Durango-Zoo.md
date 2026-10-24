<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Durango-Zoo status=nothing_found turns=13 usd=0.0179 tokens(read,write,in,out)=[407787, 61394, 28, 12253] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Durango Zoo.md

**Verdict:** current. I found no statement about our code or status that is now false, and no citation that has moved.

**Corrections:** none.

**What I checked (all held):**
- Row counts: Part A has 7 rows, Part B 1, Part C 3 (11 NPC rows, matching `repo:notes/Build Guides/Content/NPCs/NPCs.md:29` "Written (11 rows)"). The cross-reference table has 14 rows and the quest table 18, as the note says.
- Every internal link resolves to a file in the tip: `NPCs - Lakeshore`, `NPCs - Sanctuary`, `NPCs - Highroad Junction`, `NPCs - Shrouded Glade`, `NPCs - Snowhill`, `NPCs - Blackspore Swamp`, `NPCs - Briarwood`, `NPCs - Wugachug`, `Archer`, `Brawler`, `Pet Trainer`, `Grexan's Camp`, `Hewey's Escape` (`repo:notes/Build Guides/Content/Jobs/` and `.../Dungeons/`).
- Cross-page ties agree with the other pages. Archer rows 20 and 21 are Animal Investigation and Prevention First, with Mr. Miles at the zoo (`repo:notes/Build Guides/Content/Jobs/Archer.md:110-111`). Hewey's Escape is in Highroad Junction's Bear Cave (`repo:notes/Build Guides/Content/Dungeons/Hewey's Escape.md:21`, `repo:notes/Build Guides/Content/NPCs/NPCs - Highroad Junction.md:22`). Lorna, Preston Daly, Napoleon, Valinda, Smitty, Bowman Bilter and Sam Potts sit on the pages the note names (`repo:notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:35,52,70,113`; `NPCs - Snowhill.md:70`; `NPCs - Blackspore Swamp.md:163`).
- Quoted client strings and titles were checked with `locale` and match the text: "Durango Zoo, just southwest of Shrouded Glade" and the rabbit-release lines; "Mr. Miles at the Durango Zoo"; "Zanna Sugarzing runs the candy cart in Durango Zoo"; "Gram Tracker wants you to visit various animals within the zoo!"; "Sam insists" on "roam freely"; "Monno Monogram" / "Mono Monogram"; "Nugglewug has just done a headcount"; "Community Event: Stampede!"; "Scoring a Chess Table"; "Robgoblin Adept Trouble!"; "Bears on the Loose!" and its thanks line; "Zoo Keeper" (two entries); "Loose Bear"; "Glenn should be somewhere around the zoo."; "Wow, lots of goats here at the zoo."; and the Park Tour and Bixie Defense lines.
- The ten individual zoo names in the Overview match the Part A to C rows.

**Unsure:**
- The `ucdt`/`ugdt` numbers in the note are hash-style keys, not the locale table's small numeric ids (for example, "no such id" for 2842182503 and 3191433081). I could not confirm them, only the text they point to.
- "About 60 client strings mention the zoo (41 of them say 'Durango')" needs a full count. The locale search returns only 30 hits, so I could not check the count.
- Wiki claims (Sam and Mr. Miles pages, the 2013 and 2026 revision dates, the goat photo caption) and the video frame IDs are outside what I could read at the tip.
- Conflict 3 (25 vs 10 Robgoblin Boomers, and the "12 stars and 22 coins" reward) depends on video frames I did not open.
