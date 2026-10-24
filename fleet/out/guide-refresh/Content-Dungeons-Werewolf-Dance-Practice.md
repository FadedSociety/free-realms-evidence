<!-- fleet job=guide-refresh id=Content-Dungeons-Werewolf-Dance-Practice status=nothing_found turns=14 usd=0.0150 tokens(read,write,in,out)=[345950, 45452, 30, 11675] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Werewolf Dance Practice.md

**Verdict:** current. Every checkable client-side claim I tested holds at the tip, and the wiki citations match the cached wiki text. The note makes no claim about our server code, so there is no code path to check.

**Corrections:** none.

What I checked (all matched):
- Locale IDs for the client name, UI name, panel text, spawn groups (181480046, 1304241569, 3217598598), goals (1728337405, 4267283608, 333853165), boss (1273485489; game data 873209899), enemies (374121832, 675364171), cake (2077101154), quest titles (2428213276, 1776941631, 754696091, 1162972343) and quest descriptions (1050186681, 4055055841, 3005524025). The `loc` numbers in the note are the hash keys in `locale/en_us_data.dat` and resolve to the stated text (client:locale/en_us_data.dat).
- "No Bonus Objective string for this battle": the only generic "Bonus Objective" strings are for other dungeons (client:locale/en_us_data.dat, id 140066 and the per-zone entries).
- Sticker vs Stand-Up: no "Spider Web Sticker", "Jack-O-Lantern Sticker" or "Ghost Sticker" in the client. "Spider Web Stand-Up" (1889624620), "Jack-O-Lantern Stand-Up" (1551788738) and "Ghost Stand-Up" (2079854231) exist. The wiki Werewolf page uses "Sticker" and the wiki Vampire page uses "Stand-Up" (refs:freerealms-wiki/wikitext/4637-49157-943a5187ff30.wiki:31, 4636-49156-bb5a246f9010.wiki:41).
- "Break Dancer": the client has "Werewolf Slam Dancer" and "Werewolf Dancer" but no "Werewolf Break Dancer". The wiki writes "Werewolf Break Dancers" (refs:freerealms-wiki/wikitext/4637-49157-943a5187ff30.wiki:16).
- Prize wheels, 94 Stars, 150 Coins and the six-job item lists match the wiki Werewolf page (refs:freerealms-wiki/wikitext/4637-49157-943a5187ff30.wiki:25-85).
- Quest order (Being Prepared, First Bite, Pre-Emptive Bite, Another One Bites the Muck) matches the wiki Super Spooktacular list (refs:freerealms-wiki/wikitext/3113-48700-6d070a6b2cf5.wiki:43-47).
- Difficulty 2 "Recommended levels 3 and higher, but can be entered by anyone" is on the wiki Battles page (refs:freerealms-wiki/wikitext/16394-49285-9066384514a1.wiki:6). No such client string exists, as the note says.
- The repo has no werewolf dance code. The only hits are the note itself, the Vampire note and `prototype/osfr-tools/data/content/vendors_unresolved.json:215-216`, which list it as an unresolved vendor/source name. That matches the note's "not an Atlas dungeon" framing.

**Unsure:**
- Which team "Being Prepared" belongs to. The note says Team Vampire, and the Vampire note says Team Werewolf. The wiki lists both teams under the same title, and the client has one "Being Prepared" title with no team marker (client:locale/en_us_data.dat, 2428213276). Left as is; this belongs to the cross-note conflict, not to this note's own evidence.
- Video-only claims (S8hbCvXj8Kg frames, Pre-Emptive Bite objective order, Archer 20 seen playing) and wiki-only claims (spawn rules, "Members only" not tagged, 94 Stars) cannot be checked against the repo or client.
