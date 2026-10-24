<!-- fleet job=guide-refresh id=Content-Dungeons-Snowy-Canyon status=done turns=16 usd=0.0185 tokens(read,write,in,out)=[489881, 54465, 34, 13633] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Snowy Canyon.md

**Verdict:** minor drift. Almost every checkable claim holds at the tip. One cross-note claim in Conflicts is now false because the Briarheart Caverns page was corrected.

**Corrections:**

1. `old:` The Briarheart Caverns page uses the unhyphenated form, so its "client spellings" note is slightly off for this set.
   `new:` The Briarheart Caverns page now uses the hyphenated form too ("Brawler Bare-Knuckle" in its bonus list, and its Conflicts item 4 keeps "Bare-Knuckle" as the client spelling), so the two pages agree.
   `why:` repo:notes/Build Guides/Content/Dungeons/Briarheart Caverns.md:93 (the bonus clothing line reads "Brawler Bare-Knuckle, Knockdown, Power Punch ... (client spellings)") and :115 (Conflicts item 4: "The client spelling is used"). Client confirms the hyphen: locale string "Bare-Knuckle Brawler Jacket" (loc 950110269, per the Briarheart note).

**Checked and holding (no change):**
- Dungeon row: `Snowy Canyon`, difficulty 5, entrance `barrier` in `Snowhill`, objective locale 30473 = "Complete the Snowy Canyon encounter." (repo:prototype/osfr-tools/src/restoration/piece_059.rs:178; locale 30473). Matches the Overview, Entrance row and Requirements row.
- No Snowy Canyon zone or stub zone is declared (piece_059.rs:178 has no zone; scripts/pieces/piece_059.py:91 and :126 are `None` / `[]`). The note makes no zone claim, so nothing to fix.
- Client strings cited in the note exist with matching text: "Snowy Canyon" (locale 4229), "Snowy Canyon Entrance Placeholder" (5070), "Find the gate to the Snowy Canyon" (6760), "Defeat the yeti boss in Snowy Canyon, north of Snowhill." (18622), "snowy canyon - elite ability" (24033), "Enter the Snowy Canyon with a battle group ... SERVER 1" (31308), "Battles in Snowy Canyon give bonus rewards!" (31323), "Snowy Canyon Bonus Objective" (140142), "Find the Elusive Tranquil Sasquatch!" and its description (130580, 130581), the four sasquatch states (37256 to 37258, 37540), the Clockwork Cowboy campaign text (39525), and "Requires a level 13 combat job" / "must have a combat job of at least level 13" (4201, 4191). The full-group encounter achievement exists (31124).
- Prize-wheel item names exist in the locale: "Archer's Raptor Bow of Blizzards" (131905), "Medic's Shockrod of Vitals" (131965), "Ninja's Shadow Blade of 1000 Storms" (131995), "Wizard's Ornate Wand of Glaciers" (132055), and every "Ring of Precision" (130946 onward). "Pin Hole Archer Shades" is at locale 132791, so Conflicts item 2 holds.
- Scoring arithmetic: 141,000 + 181,000 + 250,000 + 120,000 + 75,000 = 767,000. The Briarheart Caverns page has the same per-unit weights (3,000 per enemy, 50,000 per knockout, 120,000 for goals, 25,000 bonus), so "match Briarheart" holds.

**Unsure:**
- The `loc <id>` numbers in the note are hash-style keys. The locale tool does not resolve them (for example 1429180355 and 1644634710 return "no such id"), so I could only check the text, not the ids. The Overview cites 1644634710 for "Snowy Canyon, north of Snowhill", while Goals cites the same id for "Defeat the yeti boss in Snowy Canyon, north of Snowhill." Both strings exist as text, but the shared id may be a copy error.
- The wiki-links [[Unga Frostclaw]], [[Elusive Tranquil Sasquatch]], [[Milo]], [[Jeni Shortfuse]], [[Sampson Idlefist]], [[Farmer Cinn]], [[Jimmy]] and [[Chilly]] were not checked against note files. The NPCs folder has zone pages only, and none of these names appears as a file name there.
- The video-based claims (results screens, the Medic video title, the sasquatch chase) and the wiki-based claims (infobox, 304 coins, 186 stars) cannot be checked from the tip.
