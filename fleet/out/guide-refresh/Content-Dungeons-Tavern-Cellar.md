<!-- fleet job=guide-refresh id=Content-Dungeons-Tavern-Cellar status=nothing_found turns=17 usd=0.0200 tokens(read,write,in,out)=[602628, 59743, 36, 13085] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Tavern Cellar.md

**Verdict:** current. I found no claim about our code or our status that is now false, and no citation that moved.

**Corrections:** none.

What I checked, and what held:
- **Repo claims.** The note makes no build or status claim about the dungeon. Its only cites into our code are the achievements and the prize-wheel names. `repo:prototype/osfr-tools/data/content/achievements.json:3131-3142` has "Tavern Cellar" (bronze, 5 points, "Complete the Tavern Cellar encounter."). Lines 3996-4006 have "Group: Tavern Cellar" (silver, 10 points, full group). Both match the note. `repo:prototype/osfr-tools/data/content/dungeons_unresolved.json:24401-24412` and the cells around it cite the note's "Prize wheel by job" and "Boss" headings, and those headings still exist. The sibling notes' Tavern Cellar rows and the Build Ledger's "Dungeons beyond the cave" row (`repo:notes/Design/Build Ledger.md:78`, "None are playable") do not conflict with this note.
- **Client IDs and strings.** I matched these against the locale dumps under `refs` (the `opening-*` en_us_data.dat files): `loc 2276216439` and `4140767304` (Brawl Club Rule), `3097094835`, `3303574665`, `809940740`, `3598668745` (the four rules), `641623023`, `3110595084`, `1789685962`, `1642156473`, `2772865612`, `1035823821`, `1670271115`, `4257117921`, `369829490`, `4116518594`, `4125033743`, `2173819079`, `1941255956` (Wolf House), `2920003869`, `2734741738`, `3694236271`, `2806269795`, `2682021743`, `1360555798`, `988363789`, `1437399701`, `1835477181`, `976593727`, the ability IDs, `1466150632`, `1381486697`, `3324003218`, `1549957578`, `1008851474`, `746979375`, `174198601`, `2104536113`, `3505099100`, `2925961911`, `1919065011`, `181260335`, `3206726430`, `3449156659`. All exist with the quoted text.
- **Prize wheel.** All 26 item names in the wheel table are in the client locale, as the note says. I spot-checked 20 of them, including the ones that were hardest to find.
- **Limits.** The `locale` tool's lookup-by-number returned "no such id" for the hash IDs. Its numbers are line indices, so I checked IDs by grepping the dumps under `refs` instead.

**Unsure:**
- Boss dialogue row: the note says Cal says "Ha! Check you out" and that "the player name that followed was redacted." The client has locale `2612906883` = "Ha! Check you out Sergeant Quackers!" (`refs` en_us_data.dat). "Sergeant Quackers" looks like a fixed string, not a redacted player name. I could not tie that string to Cal (no label record or JSON hit), so I left the row alone. Someone with the client should confirm which NPC says it before the "redacted" wording is kept.
- Video and wiki claims (Wolf House spawn rules, Cal's wand behaviour, stars, the 49 and 88 coin values, the player levels in the recordings, the entrance direction) are outside this check. I could not verify them from the repo or the client.
