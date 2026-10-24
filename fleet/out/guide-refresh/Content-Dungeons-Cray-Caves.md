<!-- fleet job=guide-refresh id=Content-Dungeons-Cray-Caves status=nothing_found turns=12 usd=0.0138 tokens(read,write,in,out)=[344087, 54324, 26, 7185] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Cray Caves.md

**Verdict:** current. The note makes almost no claims about our code. Its checkable claims are about client locale text, the wiki, and our data files, and the ones I could test hold at the tip.

**Corrections:** none.

**Checked and holding:**
- Locale strings quoted in the note exist with the quoted wording: "Cray Caves" (807812371 is the id in `data/content/dungeons/cray_caves.json:7`), "Cray Caves Teleporter", "cray caves facade 01", "Cray Caves Bonus Objective", "Cray Caves - Boss Healing", "Defeat Kelp Knight Oseidon!", "Defeat Tideweaver Oceana!", "Descend into the lower caves.", "All enemies are defeated", "Complete the Cray Caves encounter with a full group.", "Group: Cray Caves", "Mayor Gilly ... explore the Cray Caves ...", "Alonzo ... help clean up", "Diggy ... clams", "Escort Acade Vulgari through the Cray Caves.", the Acade Vulgari completion line, and the Oseidon/Oceana quest line. The "to the north" wording is in the Diggy text. (Locale tool: `repo`-independent `client` strings, e.g. Cray Caves rows 30432, 30469, 31082, 31120, 74843, 75974, 76281, 140194; boss strings 76369, 76366, 417227, 431704.)
- Prize wheel items all exist in the locale: Archmagus Wizard Robe, Soke Ninja Gi, Jonin Ninja Tabi Boots, Brawler's Atlas Hammer of Sweeps, Wizard's Ornate Wand of Shock, Ninja's Shadow Blade of Dragonstrike, Medic's Shockrod of Triage, Called Shot Warrior Tunic, Warrior's Warlord Axe of Spinning, Archer's Raptor Bow of Volleys, Battle Item Mystery Pack. "Pin Hole Archer Hoodie" and "Energy Transfer" (the Conflicts section) are also present.
- The Seaside exploration collection has 8 entries, including "Cray Caves" (`data/content/collections.json:985-1032`), which matches "one of eight components".
- Our data agrees with the note's requirement (`cray_caves.json`: `minimum_combat_job_level` 13, difficulty 5, `members_only` false, Seaside entrance). Its `dungeons_unresolved.json` rows owned by `cray_caves` cite headings that still exist in this note (Rewards > Prize wheel by job, Overview > Client name, Requirements > Combat job level, Goals > 1 to 4).

**Unsure:**
- Numeric locale ids (e.g. 1323029355, 2197579535, 1921154870) could not be looked up. The `locale` tool does not accept these ids and reports "no such id", so I could only match the text, not the id. The ids are therefore unverified, not wrong.
- "Rewards 275 stars" (collection panel) did not match any locale string on a direct search. It is video-only, so I left it alone.
- Video-, wiki- and HUD-based claims (underwater setting, 24 m red marker, Goals (4) panel, Ocean Crab text, 214/473 coin figures, the 274-star wording) are outside the repo and could not be checked.
- The note's `cray_caves.json` carries no goals or rewards (`encounters[0].goals: []`, `rewards: []`), and the Build Ledger lists dungeons beyond the cave as "None are playable". The note does not claim otherwise, so this is not a correction. A reader could still assume the dungeon is runnable.
