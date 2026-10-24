<!-- fleet job=guide-refresh id=Content-NPCs-NPCs-Cobblestone-Village status=done turns=19 usd=0.0330 tokens(read,write,in,out)=[919969, 90847, 40, 24792] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/NPCs/NPCs - Cobblestone Village.md

**Verdict:** minor drift. Most checkable claims hold at the tip: the job-page row IDs (Adventurer A11 to A14, C2; Brawler C1 to C6; Chef C1, X2, X8; Pet Trainer rows 23 and 26), the Tavern Cellar placement at the Roadhouse, the Kibler/Mongo "No longer in-game" status, the locale strings for Samantha and Ricky, and the Quest index counts (38 rows; 5/7/7/6/9/4 by page). The drift is in the vendor prices. The note says prices are unknown, but the code now carries reconstructed reference prices for Roosey and Gloria.

**Corrections:**

1. old: `the other names match the client. Prices unknown.` (Part D, Roosey row)
   new: `the other names match the client. No captured retail price exists; vendors.json holds (R) stores.json reference prices for the stock (Brawler's Ring of Energy I 75 coins, member 67, sell 37; Brawler's Mallet of Sweeps 750 coins, member 675).`
   why: repo:prototype/osfr-tools/data/content/vendors.json:14649-14652 (Roosey, npc 9500000255); :14675-14676 (Mallet 750/675); :14759-14761 (Ring 75/67/37). Each price is labelled "(R) stores.json reference price; no captured retail NPC quote" (:14679, :14763).

2. old: `Client: pet outfits and accessories. Prices unknown.` (Part D, Gloria row)
   new: `Client: pet outfits and accessories. No captured price exists; vendors.json holds (R) stores.json reference prices (Crab 5000 coins, member 4500).`
   why: repo:prototype/osfr-tools/data/content/vendors.json:14503-14523 (Gloria, npc 9500000246; Crab at :14515-14521; price_basis "(R) stores.json reference price").

3. old: `Prices, and whether the Potions, Pet Collars and Pet Supplies shops had an NPC, are unknown`
   new: `Captured prices are unknown (vendors.json carries only (R) reference prices for Roosey and Gloria, see Part D), and whether the Potions, Pet Collars and Pet Supplies shops had an NPC is unknown`
   why: repo:prototype/osfr-tools/data/content/vendors.json:14652-14763 and :14503-14523 (both price_basis fields say "(R) stores.json reference price; no captured retail NPC quote").

**Unsure:**

- **Simone's zone in the code.** The note places her in Cobblestone Village (Part B, Conflicts 6: "Client Cobblestone placement used"). But the only Simone record is in `repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:54220-54232` (npc name_string 15820), with `"zone": "Sanctuary"`, `zone_id` 10, and `region_pages` "Cobblestone Village". The code and the note disagree. I did not change the note because the mismatch sits in the generated content file, not in the note's claim. Someone should check which zone the content loader uses for her.
- **Carlos Brazenfist does not spawn.** `repo:notes/Design/Build Ledger.md:88` says "Carlos Brazenfist doesn't spawn, which blocks the Brawler chain." The note says nothing about server spawns, only that he stands at the Ring "to the east" and is "Not seen in video", so I left it. A reader of the note should be warned.
- **Rewards.** The Quest index preamble and the Gaps bullet say no source gives XP for Cobblestone quests except the wiki's 5 coins. The code gives Introduce Yourself 5 coins plus 20 Adventurer job XP, labelled "(R)" (reconstructed), at `repo:prototype/osfr-tools/data/content/quests/adventurer.json:1650-1666`. The claim about sources still holds, but a builder may read the 20 XP as sourced. Call The Crew! also has a reconstructed 5-coin fallback (adventurer.json:4194).
- **Samantha's Mail** is not in the code at all (no hits for the title in the repo outside notes). The note's "Not on a job page" is accurate. `repo:notes/Reviews/Native Round5 050310.md:117` says "Samantha's follow-ups (Samantha's Mail and others) are not in the data yet", which the note does not mention.
