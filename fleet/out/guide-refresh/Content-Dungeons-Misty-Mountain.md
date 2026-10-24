<!-- fleet job=guide-refresh id=Content-Dungeons-Misty-Mountain status=done turns=12 usd=0.0109 tokens(read,write,in,out)=[225333, 34815, 26, 8681] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Misty Mountain.md

**Verdict:** Current, with one minor factual drift in the Conflicts section. The note's claims are about client locale text, not our Rust code, and the repo has no Misty Mountain code to contradict it. Nearly every locale string and prize-wheel item I checked matches.

**Corrections:**

1. `old:` but wristguards only for Soke, Kanja and Chunin.
   `new:` but Ninja wristguards exist only for the Kanja, Sensei, Chunin, Soke and Jonin ranks (the client also has All-Star and Pro Ninja Wristguards, which are not Shinobi).
   `why:` locale lines 133248 (Kanja), 133254 (Sensei), 133260 (Chunin), 133266 (Soke), 133272 (Jonin) "Ninja Wristguards"; 33209 and 33236 are All-Star and Pro. The note leaves out Sensei and Jonin. (Conflict 1 is the one that matters here, and it stays "Unconfirmed".)

**Checked and holding (no change needed):**
- Panel description (locale 140757), "Battle the evil at Misty Mountains" promo (424984), "Misty Mountain - Primary/Bonus Objective" (140748, 140752), "Investigate the Shrine of Knowledge!" (140758), Tablet Fragment (140756), bonus tablet text (140754).
- Snowface lines: "Snowface" (103637), "Snowface... s-s-s-snow f-f-f-face!" (140366), "Defeat Snowface!" (140750), "Find and defeat the Elemental Lord, Snowface!" (140751).
- Requirement line "Requires a level 5 combat job" (4199).
- Prize-wheel items: all listed Archer, Brawler, Medic, Ninja, Warrior and Wizard names are in the locale (for example 131894, 131924, 131954, 131984, 132014, 132044, 132766, 132887, 133112, 133352, 133429, and the Regeneration III / Bark Skin III shards and necklaces). "Shinobi Ninja Gloves" is at 133242.
- Bonus clothing sets: Nusumi (133234–133239), Shinobi, Catchweight, Drifting, Emergency Medic, Combat Bonus Warrior (133344–133349), and Scholar Wizard (133418–133425) all exist.
- Dev strings "Misty Mountains 159: Wind Elemental Aura" (140643) and "Boss Confusion" (140684), plus "misty_mountains 159: Misty mountains base pop ability" (104300), "Misty Mountain - NOT USED" (74092), and "Misty Mountain Hermit" (140363) are present.
- Quest text for Lavender's Locker (385556), Scroll of Six Moons (418715, 418732), Elemental Samples (390180), Ancient Evils (78894, 91333), and Misty Mountain Fizz (103874) matches the note's quotes.

**Unsure:**
- The note cites hashed `loc` ids (for example `loc 440183008`, `loc 2145075890`). The locale tool only resolves its own row numbers, so I could not confirm any id. I matched the text instead.
- The enemy quote "snow cray" (`loc 2755439790`) is lowercase in the note. The locale has "Snow Cray" (103605). This is a capitalisation difference only, so I left it alone.
- Video frame claims, wiki-only facts (stars, coins, members bonus, Ninja-20 sighting), and companion-id lists could not be checked with these tools.
- No code, Build Ledger or Autopilot entry mentions Misty Mountain. The only dungeon status line is Build Ledger line 78 ("None are playable"), which this note does not contradict.
