<!-- fleet job=guide-refresh id=Content-Dungeons-Grexan-s-Camp status=done turns=23 usd=0.0264 tokens(read,write,in,out)=[903888, 65426, 48, 18416] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Grexan's Camp.md

**Verdict:** current, with minor citation drift. I checked about 35 client `loc` ids and quoted texts against the decompiled locale dump (`refs:opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat`) and the shipped text table. Nearly all match. Two citations are wrong. The dungeon record (`repo:prototype/osfr-tools/data/content/dungeons/grexan_s_camp.json`) and the Dungeons index row (`repo:notes/Build Guides/Content/Dungeons/Dungeons.md:99`, "Northern Wilds", difficulty 4, level 9) agree with the note. No Autopilot report touches this page.

**Corrections:**

1. Overview, Entrance row. The `3593632403` citation does not support "in Briarwood".
   - `old:` (`loc 1062088120`, `2364232962`, `3593632403`), which disagrees with the wiki zone
   - `new:` (`loc 1062088120`, `2364232962`), which disagrees with the wiki zone
   - `why:` `refs:opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat:95302` (id 3593632403) reads "...It's not surprising that they entered Grexan's Camp." It does not say Briarwood. The two other ids do: 1062088120 "enter Grexan's Camp in Briarwood" (line 28116) and 2364232962 "outside of Grexan's Camp in Briarwood?" (line 62156). The same wrong id appears in Conflicts 1 only indirectly, so the one cell above is the fix.

2. Enemies and boss table, Enemies row. `3555192058` is an objective line, not an enemy name.
   - `old:` Troll Spider Handler (`loc 3555192058`)
   - `new:` Troll Spider Handlers (objective text "Defeat 6 Troll Spider Handlers.", `loc 3555192058`; no singular enemy-name string in the locale)
   - `why:` `refs:opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat:94146` (id 3555192058 = "Defeat 6 Troll Spider Handlers."). A search for the singular name returns only quest text (locale search "Troll Spider Handler", ids 22739, 23117, 37688).

**Unsure:**

- **Missing Wallet quote** (Related quests table). The quote "lost my wallet traveling through the hedge maze" and "Can you search Grexan's Camp for my wallet?" are not in the client locale. The closest client text (id 72532, "I ran into a bunch of spiders deeper in Briarwood") and the Missing Wallet objectives (95083–95085, "Find Andrew's wallet amongst the Bristlewood Arachnids", "Return to Andrew in Briarwood") point to Bristlewood Arachnids, not Grexan's Camp. The note sources this row to video, so I cannot settle it. Brawler.md line 246 makes the same video claim.
- **NPC links.** The line "NPCs: [[General Grexan]], [[Spinnerette]], [[Buttercup Webbywand]], [[Bowman Bilter]], [[Ree Peatpants]]" points at pages that do not exist in `repo:notes/Build Guides/Content/NPCs/` (only zone pages and `NPCs.md`). The zone links resolve: `NPCs - Wilds.md` frontmatter aliases include "NPCs - Northern Wilds" (line 4).
- **Wiki-only figures** (162 and 176 Coins, 264 Stars, the prize-wheel lists, entrance "northeast of the Wilds", "Atlas icon"). No cached wiki page for Grexan's Camp is in `refs` (searches for "264 Stars", "162 Coins", "176 Coins" found nothing relevant), so I could not check them.
- **Prize-wheel item names.** The six boots and shoe names, the Necklace/Shard names and the Battle Item Mystery Pack all exist in the locale. The note's Ninja "Power Shard" capitalisation matches the client, so Conflict 3 is right.
- **Hash ids** (e.g. 610001547, 4161890033, 1291047686). The `locale` tool only takes row numbers, so I checked them through the `.dat` dump. All the ones I tried match their text (1291047686 = "Requires a level 9 combat job"; 4161890033 = "Defeat General Grexan."; 1499850166 and 2065138959 match the cocoon text).
