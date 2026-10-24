<!-- fleet job=guide-refresh id=Content-Dungeons-Bone-Bog-Cemetery status=nothing_found turns=22 usd=0.0223 tokens(read,write,in,out)=[796773, 63511, 46, 12809] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md

**Verdict:** current. I found no claim about our code or its status that is now false, and no citation that has moved.

**Checked and holding:**
- **Dungeon record exists and matches:** `prototype/osfr-tools/data/content/dungeons/bone_bog_cemetery.json:6` (id `bone_bog_cemetery`, `name_string_id` 51703131, difficulty 3 at line 61, `instance_scene_name` `bs_bone_bog_cemetery` at line 313, zone Blackspore Swamp, entrance target "gate").
- **Difficulty 3 gives a level 5 requirement:** `prototype/osfr-tools/src/encounter.rs:541-542` ("3/4/5 show 'Requires a level 5/9/13 combat job'"). This supports the Requirements row.
- **Restoration row:** `prototype/osfr-tools/src/restoration/piece_059.rs:154` has "Bone Bog Cemetery", difficulty 3, gate entrance, Blackspore Swamp.
- **Trophies:** `prototype/osfr-tools/data/content/achievements.json:3327-3339` (bronze, 5 points, client trophy 5) and `:4191-4200` (group, silver, 10 points). Both match the Trophy row and the "Group" achievement.
- **Bonus-skeleton goal text:** locale 430433 "Find and defeat the 3 Bone Bog Skeletons!" (the same string as `loc 3694930972` in the note; the number-to-text lookup returns it).
- **Skeleton enemy:** `prototype/osfr-tools/data/content/enemies.json:1549-1573` (`bone_bog_skeleton`, name 430428 "Bone Bog Skeleton", game data 1223040688 in the client locale).
- **Prize wheels:** every item named in the Prize wheel table appears in the dungeon JSON (`bone_bog_cemetery.json` lines 1105-2761 and the `target_name` entries at 2488-2761). These include the Cross Wind Archer Boots conflict resolution.
- **Client strings:** about 45 `loc` IDs were checked against `client/locale/en_us_data.dat` and `en_us_data.dir`, and all match the quoted text. Examples: 407646356, 2145075890, 3325099950, 3691261868, 2691222384, 420065248, 202086571, 3506549451, 3549407549, 2369094282, 3248953191, 3750868535, 3843472766.

**Unsure:**
- **Event level (Conflicts 1 and the Pumpkin Prince row).** The wiki's "level 13+" for the Pumpkin Prince fight is not contradicted by our code. Our `enemies.json:770-777` has a prototype record `w58_the_pumpkin_prince_l5_boss` with `level: 5`. Those are prototype stats (the file says so), not evidence for or against the wiki. I left the note's "not confirmed" wording as is.
- **Lucinda and Pumpkin Prince wiki-only claims** (Ghost Hunter in Pixiewood Hills, the 13+ gate, "Five wraiths"). The code has no record of these, so I could not check them.
- **Gaps and Conflicts 3.** These are wiki or video matters, not code. Not checked.
