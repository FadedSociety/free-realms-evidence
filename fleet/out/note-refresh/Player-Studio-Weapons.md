<!-- fleet job=note-refresh id=Player-Studio-Weapons status=nothing_found turns=28 usd=0.0306 tokens(read,write,in,out)=[1313856, 75202, 58, 16077] model=claude-haiku-5-5 -->
# notes/Research/Player Studio Weapons.md

**Verdict:** current. I found no false claim and no moved citation. The note is a client-data research note and cites no repo code paths, so I checked its facts against the client resources, the Legacy item dump, the locale table, and the repo's curated `item_abilities.json`.

**Corrections:** none.

**What I checked and confirmed:**
- **Count and item ids:** 11 weapons. Item ids 78711–78718 and 79020–79022 match `refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1258730–1258981` and `repo:prototype/osfr-tools/data/reference/item_abilities.json:6–168`.
- **Item classes and models:** classes 17, 71, 6, 28, 5 and 10 and the `.adr` names match the same Legacy dump entries.
- **Swing trails and frost effect:** Ice Axe 5485 (gray), Gleam 5686 (blue), Gloam 5691 (purple), Lightning 5694 (yellow), Lunar 5485, Wing 5485, Bellringer 5694. Snowflake, Golf, Kingmaker and Precursor have no trail. All match `Legacy ClientItemDefinitions.json:1258730–1258981`. The four `WFX_trail_default_*` names resolve in `client:Resources/ActorCompositeEffectDefinitions.xml:4810, 6160, 6180, 6190`.
- **Effect 15449 (frost):** one particle and four sounds, as the note says (`client:Resources/ActorCompositeEffectDefinitions.xml:10928`). Effect 5728 has one particle and three sounds. The Elitist's Sword (68112) is the only non-Player-Studio item with 15449 (`Legacy ClientItemDefinitions.json:1158452–1158473`).
- **Animations:** `client:Resources/AnimationGroups.xml:635–700` shows `com_swing` (1099) with 1hs/2hs slots for wield types 9, 12, 13 and 14, and `com_cast_special_03`–`05` for wand wield type 10. `WieldTypeAnimationMappings.txt` maps 9, 10, 12, 13 and 14 to 1099.
- **Special attacks:** all the quoted front and area texts I looked up match the locale table (for example 5103185, 5103187, 5103199, 5103209, 5103211, 5103214, 5102643, 5102646, 5102650). Power Drive (5102644) has no description, as the note says.
- **Text id ranges:** 5103184–5103215 and 5102642–5102652 match `item_abilities.json`.
- **Creators:** the "Created by" credits match the locale strings at 5103169–5103183 and 5102637–5102641.
- **Asset-graph command:** `--who item:78711` is consistent with `repo:scripts/build_asset_graph.py:8–11`.

**Unsure:**
- "There are 41 more Player Studio items" (last line of the note). I did not count these, so I could not confirm the number.
- The item-class-to-wield-type link (for example, class 17 to Warrior 12, class 71 to Brawler). `ItemClasses.txt` is not in the client `Resources` tree, so I could not confirm this mapping. The item classes themselves match the Legacy dump.
- "Each weapon's model file (`.adr`) holds only its mesh, its textures and a right-hand attach point (`R_WEAPON`)." I did not open a `.adr` file to check this.
- The creator and job labels in the table (for example, "Brawler" for Gleam). I checked the creator names only, not the job column.
