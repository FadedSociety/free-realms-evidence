<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Sanctuary status=done turns=13 usd=0.0201 tokens(read,write,in,out)=[501991, 74965, 28, 11414] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md

**Verdict:** minor drift. Most client and wiki facts are outside what the code can check and were left alone. The two statements about our own notes (the Postman page and the Gaps list) are now false, and one vendor row is stale because the Bordon Cloo stock was added after the note was written.

**Corrections:**

1. Part F, "Notes on quest givers and trainers" (Postman bullet, line 201)
   - `old:` The Postman line has no content page yet.
   - `new:` The Postman job page exists: [[Postman]], and it holds the Felipe and Flitter quest lists.
   - `why:` repo:notes/Build Guides/Content/Jobs/Postman.md:1-30 (front matter and overview), with the Sanctuary trainer rows at Postman.md:33-34 (Felipe, Flitter) and the Sanctuary quest band at Postman.md:69-82.

2. Gaps, line 231
   - `old:` a Postman page and a Harvesting page do not exist yet, so Felipe's and Flitter's quest lists are not filled in.
   - `new:` a Harvesting page does not exist yet. Felipe's and Flitter's quest lists are on the Postman page ([[Postman]]).
   - `why:` repo:notes/Build Guides/Content/Jobs/Postman.md:33-34 and 69-82 fill those lists. The Jobs folder (repo:notes/Build Guides/Content/Jobs/) has no Harvesting page.

3. Part B/C table, Bordon Cloo row, Services column (line 46)
   - `old:` client store names "Chef Supplies & Recipes" (1311255679). Cooking table
   - `new:` client store names "Chef Supplies & Recipes" (1311255679). Cooking table. Sells 12 cooking-supply ingredients at 12 coins each: Spice, Bat Meat, Mystery Meat, Spider Meat, Bear Meat, Butter, Egg, Broth, Sugar, Chocolate Bar, Snowhill Ice Cream: Chocolate, Snowhill Ice Cream: Vanilla (Chef guide Vendors/Ingredients; video ukTXIyG6EKI/00006).
   - `why:` repo:prototype/osfr-tools/data/content/vendors.json:47113-47116 (npc_id 9000000028, "Bordon Cloo", twelve items); the change is recorded in repo:notes/Autopilot/T275.md:8-30.

4. Part C intro, row count (line 19)
   - `old:` Part C 19 (including three rows for enemy groups)
   - `new:` Part C 20 (including three rows for enemy groups)
   - `why:` the Part C table runs from line 105 to line 124 in this note, which is 20 data rows (the three enemy-group rows are at lines 122-124).

**Unsure:**

- Captain Sunspark's Sanctuary placement. The note keeps him as a Sanctuary row with no stand. repo:notes/Build Guides/Content/NPCs/NPCs - Shrouded Glade.md:123 and :262 agree with the warpstone reading in Conflicts 15. I did not check the Job Center line (3440602433) against the client.
- Client facts such as locale ids, NPC names, and the "21 frames tagged zone Sanctuary" in Gaps were not re-checked against the locale or video data.
- Row-level claims for the trainer levels (Gordon at 5, Clover at 10, Osgood at 10 and 15, Whittington at 15, Roscoe at 1 to 10) match repo:notes/Build Guides/Content/Jobs/Medic.md:36, Wizard.md:52, Warrior.md:36 and 52, and Pet Trainer.md:42. The Clover row is not confirmed in the Medic job page.
- The Sanctuary/Queensfields/Memorial Caverns zone placements match repo:notes/Build Guides/Content/Dungeons/Forgotten Caves.md:3 and :18, Darvon's Descent.md:3 and :18, and Bixie Hive.md:3. The Cursed Graveyard claim (Conflicts 10) matches repo:notes/Build Guides/Content/Dungeons/Cursed Graveyard.md:3 and :18 (Stillwater Crossing).
- The Greyli Dustywings reference (line 45) and the Pixiewood Hills reference (line 15) are cited by Autopilot reports, and their line numbers still match.
