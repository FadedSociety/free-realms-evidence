<!-- fleet job=guide-refresh id=Content-Dungeons-Dark-Spore-Depths status=done turns=14 usd=0.0149 tokens(read,write,in,out)=[384836, 48062, 30, 10064] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Dark Spore Depths.md

**Verdict:** minor drift. Almost every client string the note cites is in the locale and matches its quoted text. The one false claim is a count of "NOT LIVE" strings, and it appears twice. The note makes no claims about our code's build status, so there is little code to check.

**Corrections:**

1. `old:` Two "NOT LIVE - Dark Spore Depths" strings exist (`loc 65907624`, `1576939540`), which are dev leftovers.
   `new:` One "NOT LIVE - Dark Spore Depths" string exists (`loc 130869` in the locale table), which is a dev leftover.
   `why:` A locale search for "NOT LIVE - Dark" and for "Dark Spore Depths$" returns a single row, 130869 "NOT LIVE - Dark Spore Depths". No second row matches. The hash ids `65907624` and `1576939540` do not resolve as locale rows, so the note's second string has no evidence. (The note's ids are hashes; the locale tool takes row numbers. See Unsure.)

2. `old:` Two client strings label the dungeon "NOT LIVE".
   `new:` One client string labels the dungeon "NOT LIVE" (locale row 130869).
   `why:` Same search as correction 1 (locale: "NOT LIVE - Dark", "Dark Spore Depths$"). Only one row exists. Conflicts item 4 repeats the count.

**Checked and consistent (no change):**
- `loc 514666743` is the dungeon name ID in `repo:prototype/osfr-tools/data/content/dungeons/dark_spore_depths.json:7`. Locale rows "Dark Spore Depths" (4469, 30433) and "Group: Dark Spore Depths" (31083) match.
- Difficulty 5 maps to a combat level of 13 (`repo:prototype/osfr-tools/data/content/enemies_unresolved.json:4240`). The note's Level 13 row is consistent.
- Goal, boss, spore, quest and enemy strings quoted in the note all match locale rows: "Defeat Necrolaceous!" (92413), "Remove five Necro Spores…" (130721), "Defeat the knights…" (4656), "Necro spores are a poisonous fungus…" (130722), "The Nettleseed Pest begins to split!" (74051), "Dark Spore Knight" (4692), "Fungus Golem" (4477), "Necrowart Zombie3" (118947), "Ancient Necrowart Zombie" (442328), and the dev strings at 130600, 130728 and 130730.
- Achievement strings "Complete the Dark spore Depths encounter." (30470) and "…with a full group." (31121) match the note's lower-case "spore" note. `repo:prototype/osfr-tools/data/content/achievements.json:3804-3808` and `:4668-4672` agree.
- Prize-wheel item names checked in the locale all exist: Jonin/Soke Ninja Hakama, Wizard's Ornate Wand of Tsunami, Called Shot Warrior Breeches, Pin Hole Archer Leggings, Wound Ballistic Medic Fatigues, Archmagus Wizard Slacks, Battle Item Mystery Pack, Power Punch Brawler Pants, and "Energy Transfer" (the note's "Enery" spelling is a wiki error).
- Quest texts for Cargug (116025), Chaz (72993), Sperry (17951, "four mushrooms") and Akari (419277) match.

**Unsure:**
- The note's `loc <id>` numbers (e.g. 2155422622, 1323029355, 65907624) are hash-style IDs. The locale tool accepts only row numbers, and the repo does not map the hashes to rows. I confirmed texts by text search, not by ID, so the ID column is unverified. The same hashes appear in other repo files (e.g. `treasure_of_the_bone_shaman.json`), so they are used consistently, but I could not confirm them.
- The "Level 13 combat job" row cites `loc 1323029355`. That string is generic ("Requires a level 13 combat job") and is shared across many dungeons, which the note does not say. I did not treat this as false.
- Wiki-only claims (entrance, members bonus, 117/321 coin figures, stars, enemy list) cannot be checked against the tip. I left them unchanged.
