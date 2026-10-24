<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Wilds status=done turns=17 usd=0.0248 tokens(read,write,in,out)=[725908, 93668, 38, 11639] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Wilds.md

**Verdict:** minor drift. Most checkable claims hold. One sentence misstates where the Return to Sender battle lives, and the matching row in Part E repeats the error.

**Corrections:**

- `old:` - **PCA Camp** ends the Postman line (Emahl) and houses the Return to Sender boss.
  `new:` - **PCA Camp** ends the Postman line (Emahl). The Return to Sender node battle is started by clicking an Evil Postman in the Wilds (wiki: "northeast Wilds"); the page does not place a boss at the camp.
  `why:` repo:notes/Build Guides/Content/Dungeons/Return to Sender.md:11 (node battle, not an Atlas dungeon, "started by clicking on an Evil Postman in the northeast Wilds") and :20 (Entrance: "Click an Evil Postman in the Wilds"). That same page's :81 says only that the Postman line culminates at the PCA Camp. Note line 288 is in the Notes section.

- `old:` (Part E row, Mailbit) "Boss of [[Return to Sender]], which the wiki files at the PCA Camp."
  `new:` "Boss of [[Return to Sender]], a node battle started from an Evil Postman in the Wilds; the wiki's location for it is the PCA Camp."
  `why:` repo:notes/Build Guides/Content/Dungeons/Return to Sender.md:11, :20. I did not quote this cell in full because the tool cut the line. Please check the exact text before applying.

**Unsure:**

- The Part G statement "The [[Kart Racing]] engine page" is a link target. Build Guides.md:16 lists a Kart Racing page, so I did not treat it as broken, but I did not open that page.
- The row counts in the intro (109 NPC rows, 27 cross-reference rows, 19 town-quest rows, 139 linked titles) were not counted, so they are unverified.
- Locale numbers in the note are client hash ids, which the locale tool cannot look up. I checked the quoted sentences by text (for example the Roadhouse location lines, the Frost Ridge and Sacred Grove Raceway lines, the Wildwood "south of Cobblestone Village" lines, and the Forest Troll Village "northeast of the lake" line), and they match.
- Cross-note claims checked and consistent: Pear Jam in the Snowhill and Wugachug notes, Derp Axemaker's level-10 gate in the Blacksmith and Miner pages, Sakka at level 15 and the Wugachug wiki location in the Ninja page, Glerga's level-20 gate in the Chef page, Fizzlesticks in the Wizard page, Emahl in the Postman page, and Shooblemoot at Thunder Falls in the Kart Driver page.
- The Autopilot reports I searched contained nothing that changed the Wilds NPC content.
- I did not finish checking the Part B, F and H rows or the Conflicts 9 to 16 detail, because the budget ran out.
