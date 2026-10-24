<!-- fleet job=guide-refresh id=Content-Dungeons-Sweetwater-Climb status=done turns=16 usd=0.0176 tokens(read,write,in,out)=[440390, 50723, 34, 13676] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Sweetwater Climb.md

**Verdict:** minor drift. The note is almost entirely about client strings, video and wiki facts, and it makes almost no claims about our server code. Its only code-side facts (no level requirement, difficulty 2, Wugachug, name id) match `data/content/dungeons/sweetwater_climb.json`. I found two small text errors and nothing that changes build status.

**Corrections:**

1. `old:` `"Who are you? What have you done!"`
   `new:` `"Who are you? What have you done?"`
   `why:` The client string ends with "?" (locale text row 74525: "Who are you? What have you done?"). The note's "!" is a transcription error. Ability and name-bar claims check out (row 74486 "Sweetwater - Pollentine's Sonic Blast").

2. `old:` `No level-3 string exists in the client.`
   `new:` `No dungeon-entry level-3 string exists in the client. Level-3 text appears only on gear tooltips (e.g. "Wearable by a level 3 or higher Archer"), and "recommended level" has no client hit.`
   `why:` The client does contain "level 3" text, all on gear tooltips (locale search "level 3": "Wearable by a level 3 or higher Archer/Brawler/Medic/Ninja/Warrior/Wizard"). The claim is true only for dungeon entry. The same claim is repeated in `prototype/osfr-tools/data/content/dungeons/sweetwater_climb.json:117`, so that record would need the same wording.

**Checked and holding** (no change needed):
- Locale text matches the note: "Sweetwater Climb" (30411), "A Sweetwater Climb" (442624, 5101364), "Save the Sasparilla!" (74258), "Defeat the Big Hungry Bear!" (130633), "Win Combat Encounter Sweetwater Climb" (119166), "Sweetwater Climb Bonus Objective" (140196), the Pollentine panel text (74322), "Enter Sweetwater Climb and defeat Rebel Mage Pollentine." (389217), "Battles at Sweetwater Climb will give bonus rewards." (424986), and the Big Hungry Bear description (130634).
- Quest texts in the table match: Tugaboom's bixie plans, the dominant bear, Terrence's supplies, Kazuo's drink, the guards' "top of Sweetwater Climb" line, and "Complete Sweetwater Climb" (5101439).
- All 18 item names in the prize-wheel table exist in the locale. "Archer's Treasure Shard of Vitality II" does not, which matches the Conflicts entry. "Archer's Power Shard of Vitality II" exists.
- The Dungeons.md row (Sweetwater Climb, difficulty 2, "none (3+ recommended)", Wugachug) agrees with the note and with the JSON.
- The Bixie Hive names cited for cross-reference ("Rebel Bixie Elite", "Bixie Battlemage") are in the locale and in Bixie Hive.md:48.

**Unsure:**
- The note's `loc` ids (for example `loc 2099088689`, `loc 63281229`) do not resolve in the locale tool, which uses its own row numbers. I could only check the texts, not the ids.
- "Bonus: Defeat the Big Hungry Bear!" has no exact hit in the locale. The "Bonus:" prefix is used on other client objectives, so this may be a UI prefix. I left it unchanged.
- Video-only claims (OCR readings, result-screen numbers such as "Stars x119" and "Coins x82", frame numbers, and "Archer 13/14") cannot be checked from the repo or the client.
- The note's wiki-based claims (242 stars, 135 members coins, the rabbit and Bixie Workers NPCs) are outside what the client can settle; I did not check them.
- The repo has no Sweetwater code path. Build Ledger line 78 says none of the dungeons is playable. The note does not claim otherwise, so no correction is needed.
