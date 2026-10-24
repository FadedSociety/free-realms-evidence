<!-- fleet job=guide-refresh id=Content-Jobs-Card-Duelist status=nothing_found turns=32 usd=0.0344 tokens(read,write,in,out)=[1528991, 78719, 66, 18563] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Card Duelist.md

**Verdict:** current. The note's checkable claims about our code and data hold at the tip. I found no false status claims and no moved citations that need a correction.

**Corrections:** none.

What I checked (all match):
- **Level achievements (Level 4/8/12/16/20).** Trophy values and the Level 20 title match. Bronze 5 for Levels 4 and 8, Silver 10 for 12 and 16, Gold 15 plus "The Card Strategist" for 20. `repo:prototype/osfr-tools/data/content/achievements.json:1017-1122`. `repo:prototype/osfr-tools/data/content/titles.json:239-241`.
- **Questline achievement "Duelist".** Gold 15 points, Title "Card Commander". `repo:prototype/osfr-tools/data/content/achievements.json:5806-5814`. `repo:prototype/osfr-tools/data/content/titles.json:641-642`.
- **Members only.** Not members only, category freestyle, max level 20. `repo:prototype/osfr-tools/data/content/jobs.json:393-398`.
- **Row citations used by other records.** The Part headings and row numbers the code cites still match the note. Row 27 is Best of the Best (`notes/Build Guides/Content/Jobs/Card Duelist.md:113`). Rows 36 and 37 are the Greenwood rows (lines 127-130). Rows 52-56 and 57 are the Zelda and Rumbledome rows (lines 159-171). Row 62 is Return from the Rumbledome (line 176). Line 67 names Jili and line 68 cites 635925311, as `repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:34293` says.
- **Wiki links.** `[[Trading Card Game]]` resolves to `notes/Build Guides/Gameplay/Trading Card Game.md`. `[[FRTW Game]]` and the NPC notes also exist.
- **Count of "71 Card Duelist: titles".** The table is consistent with it: 66 prefixed quest rows, 5 level titles, and Practice Makes Perfect and Pick a Card as the two bare titles.

**Unsure:**
- **Base-line quest count.** Overview line 23 says the base line is "28 quests". Part 1 (lines 58-113) has numbered rows 1-27 plus the bare entry row E1, so 28 counts E1. The count is defensible but ambiguous, so I left it alone.
- **Derived quest data is shorter than the note.** `repo:prototype/osfr-tools/data/content/jobs.json:415-478` lists 63 quest ids (3040001-3040063, with E1 as 3040001). The note has 68 quest rows. Rows 63-67 (Birth of a Cardshark, Gifted Cards, Four Round Challenge, Access Granted, Keeping Quiet) are missing from the job's `quest_ids`. The note itself is internally consistent; this is a data-side gap, not a note error.
- **TCG implementation status is outside this note.** `notes/Design/Build Ledger.md:110` lists "card game" as Researched with no code. `scripts/audit-minigame-coverage.py:481` says "no Rust module". Both are stale against `prototype/osfr-tools/src/restoration/piece_010.rs`, which now exists. This note does not make a status claim about the TCG, so I did not change it, but the Trading Card Game guide may need that check.
