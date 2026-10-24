<!-- fleet job=guide-refresh id=Content-Dungeons-Vampire-Dance-Practice status=done turns=12 usd=0.0121 tokens(read,write,in,out)=[211076, 33545, 26, 11618] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Vampire Dance Practice.md

**Verdict:** minor drift. The note has no code citations and its status claims (seasonal special spawn, no bonus objective, crew groups, quest and level lines) hold at the tip. Two client-locale citations are imprecise.

**Corrections:**

1. `old:` Every item name below exists in the client locale exactly as written. [client, checked by exact name]
   `new:` Every item name below exists in the client locale exactly as written, except "150 Coins": the locale has no such string, only "Bonus: 150 Coins!" (`loc 2159027881`). [client, checked by exact name]
   `why:` locale/en_us_data.dat:56849 (`2159027881 ucdt Bonus: 150 Coins!`); no exact "150 Coins" entry in the client locale (locale lookup for "150 Coins" returns only 119985 "Bonus: 150 Coins!"). The other wheel names checked (Bat Pail 119249, Jack-O-Lantern Pail 119245, Skeleton Paper Bag Mask 119226, Werewolf Cake Slice 7336, and the Stand-Up and Mask names in the .dat) all exist.

2. `old:` **Ed Sullenfangs**, "the head vampire" (`loc 169485919`; game data `1778043178`)
   `new:` **Ed Sullenfangs** (name `loc 169485919`; game data `1778043178`); the "head vampire" wording is in the panel text `loc 3523083160`
   `why:` locale/en_us_data.dat:4444 and :46951/:1778043178 (`169485919` and `1778043178` are both just "Ed Sullenfangs"); locale/en_us_data.dat:93242 (`3523083160` is the panel text containing "the head vampire"). The note cites the name ID for a quoted phrase that is in a different ID.

**Checked and holding (no change):**
- Crew spawn groups: `411837368`, `161665061`, `1692806121` are "Vampire Dance Crew", "…Crew 2", "…Crew 3" (ucdt) in locale/en_us_data.dat.
- Level gate lines: "Requires a level 5/9/13 combat job" (`2145075890`, `1291047686`, `1323029355`) exist; no "Recommended levels" line exists in the client, as the note says. Dungeons.md:128 agrees with "3+ recommended".
- Panel, objective, and boss text IDs (`3523083160`, `687102900`, `3394593415`, `1963231226`, `2999318093`, `2077101154`, `2428213276`, `3896567252`, `3532653789`, `234157957`, `1973293418`, `1976011520`, `411443314`, `3005524025`, `1822449295`, `1889624620`, `1458878127`, `611651650`) all match the quoted text.
- Stand-Up versus Sticker: no "Sticker" item of these names; the mapping note in Werewolf Dance Practice.md:72 is consistent.

**Unsure:**
- The spawn gate ("only spawns during the Super Spooktacular"), the Sinking Graveyard entrance, the 96 Stars and wheel contents, and the event-gate claim come from the wiki. The repo has no server code, spawn table, or Build Ledger entry for this battle (searches of `repo` for vampire/dance-practice/spooktacular hit only data JSON and notes), so they cannot be checked against code. The note makes no routing or implementation claim, so nothing there is false by our evidence.
- The "Ed Sullenfangs" name ID `169485919` is also cited in notes/Autopilot/T034.md:65 as mapping to `432135`; not relevant to this note's claims, not checked further.
