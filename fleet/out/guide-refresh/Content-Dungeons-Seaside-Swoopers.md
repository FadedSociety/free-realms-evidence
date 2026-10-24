<!-- fleet job=guide-refresh id=Content-Dungeons-Seaside-Swoopers status=done turns=16 usd=0.0138 tokens(read,write,in,out)=[353994, 43377, 34, 9631] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Seaside Swoopers.md

**Verdict:** current, with one minor drift. Every `loc` ID I could check resolves to the text the note gives (checked against `client:locale/en_us_data.dir` and `en_us_data.dat`). The one exception is the label text quoted for `loc 1925651180`. The note has no status claims about server code beyond the data record, which agrees with it.

**Corrections:**

- `old:` Members get "Members Only Bonus: 34 Coins" (client label `loc 1925651180`); a string "Bonus: 34 Coins!" exists (`loc 2268039290`), one of many "Bonus: N Coins!" strings, so the match is weak evidence.
  `new:` Members get a "Members Only Bonus" banner (client label `loc 1925651180` reads "Members Only Bonus!"); the amount is not in that string. A string "Bonus: 34 Coins!" exists (`loc 2268039290`), one of many "Bonus: N Coins!" strings, so the match is weak evidence.
  `why:` client:locale/en_us_data.dat:50746 (`1925651180 ucdt Members Only Bonus!`) and en_us_data.dat:59715 (`2268039290 ucdt Bonus: 34 Coins!`). The "34 Coins" text is in a separate string.

**Checked and holding:**

- Client name `loc 3802808002` = "Seaside Swoopers" and `loc 514782450` = "Seaside Swoopers" (en_us_data.dat:100588, :13711). No "!" variant found.
- Panel text `loc 416948446`, zone `loc 588304693` = "Luxurious Oceanfront Homes", and the goal strings `loc 1401192091` ("Shoo the swoopers!") and `loc 1601110213` ("Defeat all the Seaside Swoopers.") match.
- Enemy names: Lazy Swooper (`1912902840`, `2070462287`, game data `2435133780`) and Scavenger Swooper (`231668844`, `1421543497`, game data `1417640120`) match.
- Requirement strings `loc 2145075890`, `loc 66524078`, `loc 3173661191` match. Achievement strings `loc 1294437773`, `952418071`, `2358807378`, `3708924672`, `197501470` and `Caged Swooper` `682644336` match.
- Negative claim: no "Seaside Swoopers Bonus" or "Win Combat Encounter Seaside Swoopers" string exists in en_us_data.dat.
- All prize-wheel item names in the table exist in the locale as written (checked Archer, Brawler, Medic, Ninja, Warrior, Wizard items; Catchweight Brawler Boots, Nusumi Ninja Tabi Boots, Scholar Wizard Shoes and Drifting Archer Boots included).
- Server side: `prototype/osfr-tools/data/content/dungeons/seaside_swoopers.json` has difficulty 3 and `minimum_combat_job_level` 5. Dungeons.md:134 lists it as 3 / 5 / Seaside / written. Both agree with the note's Requirements and Overview.

**Unsure:**

- Video-only claims (`wA9BqwA5lr4/00066`, `/00196`: Medic 18 frame, 17 enemies defeated, results-screen scores and timer). I could not verify these from the repo or the client.
- Wiki-only figures ("127 Stars", "Levels 5 and higher", the 2-Coin prize-wheel slot, and the "Flying Dragon Dojo" / "Abandoned Dojo" naming). No cached wiki page for Seaside Swoopers turned up in `refs`.
- The JSON record has `encounters[0].goals: []` and `rewards: []`, with a note that page goals were left in `dungeon_data` because the objective keys are not mapped. The note does not claim otherwise, so I did not treat this as a correction.
