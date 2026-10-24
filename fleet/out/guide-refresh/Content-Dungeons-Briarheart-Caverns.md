<!-- fleet job=guide-refresh id=Content-Dungeons-Briarheart-Caverns status=nothing_found turns=12 usd=0.0114 tokens(read,write,in,out)=[222926, 33023, 26, 10163] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Briarheart Caverns.md

**Verdict:** current. The note is a client-content page with no claims about server code or build status. Every quoted client string I could check matches the locale table. I found no false statement and no moved citation.

**Corrections:** none.

**What I checked (all match):**
- Client name "Briarheart Caverns" (locale 5707), journal description (16045), panel description "Geomancer Hailstorm is ruling his changelings through fear!..." (92504), main goal "Defeat Geomancer Hailstorm!" (16044), and boss name "Geomancer Hailstorm" (16000).
- Campaign blurb (39523) with Clockwork Cowboy Boots and "Campaign 2: Haunted Mines". "Campaign 3: Change of Heart" is a separate string (39511), so the note's "text never says its own number" holds. The TW campaign image strings (`FUN_01329630`, "TW 1.01 Cruisin' for a Bruisin'") support the Treasure War reading.
- Level-13 lines: "Requires a level 13 combat job" (4201) and "You must have a combat job of at least level 13 to play this battle" (4191).
- Achievements: "Complete the Briarheart Caverns encounter." (30468), "...with a full group." (31119), "Group: Briarheart Caverns" (31081), "Win Combat Encounter Briarheart Caverns" (119174).
- Bonus group "Briarheart Caverns Bonus Objective" (client fn table, row 140178). "Defeat all enemies" has no locale match, as the note says.
- Enemy and ability strings: "Changeling Berserker" (15997), "briarheart_caverns 41: Ninja Claw" (92391), "42: Ninja Stars" (92397), "42: Berserker Attack" (92404). The story-flavour order (rock warrior, changeling wizard, ninja, elder, then Hailstorm) matches 432913–432922.
- Quest texts: rescue Sven (76440, 117078), "Defeat the aggressive Changelings within Briarheart Caverns." (92249), "Defeat ten opponents in Briarheart Caverns and Howling Hills." (100768), elemental-core quest (18018, 16667), the summoning-crystal text (22315), and the archer ruthenium text (130873).
- Rewards and names: "Bonus: 281 Coins!" exists as a generic string (119992). "Bare-Knuckle Brawler Jacket" (132903), "Pin Hole Archer Boots" (132789), and "Energy Transfer Medic Jacket" (133128) match the note's spellings. Prize-wheel items spot-checked (Raptor Bow of Flame, Jonin Wristguards, Soke Tabi, Ornate Wand of Lightning, Archmagus Shoes, Shockrod, Warlord Axe, Atlas Hammer, Shadow Blade, Called Shot Hightops, Critical Hit Gauntlets, Stopping Power Gloves, Wound Ballistic Boots, Bull's-Eye Wristguards, Power Punch Boots, Knockdown Arm Pads) all exist.
- Scoring labels "Opponents Defeated" (117298), "Time Bonus" (9005), "Knock outs Remaining" (117309), and "Bonus Goals Complete:" (4463) exist.
- Repo: no code, ledger or Autopilot file mentions Briarheart, Hailstorm or dungeon/Atlas instancing (grep of `repo`). The note makes no server-status claim to check.

**Unsure:**
- The `loc NNNN` numbers in the note (e.g. `loc 632311160`, `loc 98909869`, `loc 697034942`) do not resolve in the locale tool. Querying `632311160` and `697034942` returned "no such id". The tool's ids look like row numbers, so the note's ids may use a different scheme. I matched the texts by content instead.
- Achievement point values (5 bronze, 10 silver) and the score totals in the wiki-derived results screen are not in the client and were not checked.
- The "Atlas icon exists" and "Briarheart (Press to Teleport...)" claims: the text "Press to Teleport..." exists (382845), but the composite Atlas label was not found as one string.
- The Briarheart Palace panel (`0mJBW1a0EIc/01260`) is outside this note's claims and was not examined.
