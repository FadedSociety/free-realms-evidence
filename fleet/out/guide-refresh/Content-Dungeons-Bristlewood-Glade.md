<!-- fleet job=guide-refresh id=Content-Dungeons-Bristlewood-Glade status=nothing_found turns=21 usd=0.0252 tokens(read,write,in,out)=[881108, 74822, 44, 14038] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bristlewood Glade.md

**Verdict:** current. I found no claim in `Bristlewood Glade.md` that the tip contradicts. The note is almost entirely client-locale and wiki sourcing, and the few claims about our own code and data hold.

**Corrections:** none.

**Checked and holding:**
- **Level 5 gate (Requirements).** The note says "from the shared tier rule". `notes/Build Guides/Content/Dungeons/Dungeons.md:45` sets tier 3 to "combat job level 5+", and our data agrees: `prototype/osfr-tools/data/content/field_battles.json:406-407` has `difficulty: 3` with `required_combat_level: 5`. Our `data/content/dungeons/bristlewood_glade.json` (lines 114-127) carries `minimum_combat_job_level: 5`, derived from this note.
- **Difficulty 3 (Overview).** Matches `Dungeons.md:86` (`[[Bristlewood Glade]] | 3 | 5`) and the dungeon JSON `difficulty: 3`.
- **Client strings.** I spot-checked the locale ids in the dat file (`refs:FreeRealmsLocaleTools/.../en_us_data.dat`) and they match the note's wording. Examples: 1463044901, 1665042062, 2656147850, 3976251720, 2145075890, 3173661191, 1748407955, 2124037158, 2246705638, 2975337297, 3721764698, 3226033583, 897434791, 3133083628, 2622756725, 3833484049, 575707451, 3848230664, 1632086635, 3855134009, 2703640191, 3429949018, 2500181263, and the enemy names 3014580400, 3510328411, 1752935167, 3134977912. The 2190795178 "Group: Bristlewood Glade" line also matches `data/content/achievements.json:4215`.
- **Achievements.** `data/content/achievements.json:3351-3352` and `4215-4216` match the Rewards and Group-size rows.
- **Prize wheel item names.** Drifting Archer Quiver, Scholar Wizard Talisman, Nusumi Ninja Shoulderguard, Catchweight Brawler Shoulderpads and Emergency Medic Backpack all exist in the client locale (locale ids 132763, 133425, 133239, 132884, 133109).
- **Status.** No Autopilot report touches this dungeon. `notes/Design/Build Ledger.md:78` says dungeons beyond the cave are researched and none are playable, which the note does not contradict.

**Unsure:**
- **Frame citations.** The 74 m "Bristlewood Glade" marker on `piWfe7lXZ9I/00195` and the Blari markers on the same frame (`NPCs - Briarwood.md:100`, 25 to 59 m) cannot be checked from text alone. They are not contradicted.
- **Wiki coin figures** (128 and six 162s in the template fields) and the wiki-only Vine Wolf and Vine Bear names. These sit in refs or the wiki cache, which I did not check against the template fields.
- **Wiki-links.** `[[Amaranthus]]`, `[[Sergeant Cargug]]`, `[[Blari]]` and `[[Reginald]]` have no page of their own under `notes/`. NPCs are rows in `NPCs - Briarwood.md`, and other dungeon notes use the same links, so this is a vault convention, not a false claim.
- **Locale id scheme.** The `locale` tool does not resolve the note's numeric ids directly (`no such id`). I matched them against the dat file instead, and they hold.
