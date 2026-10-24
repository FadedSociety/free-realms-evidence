<!-- fleet job=guide-refresh id=Content-Dungeons-Mushroom-Cavern status=done turns=14 usd=0.0152 tokens(read,write,in,out)=[359589, 45081, 30, 11895] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Mushroom Cavern.md

**Verdict:** current. Almost every checkable claim holds at the tip. The one defect is a dangling wiki link in the NPC line, which implies pages that do not exist.

**Corrections:**

1. `old:` NPCs: Marasmius (boss, no NPC page yet), [[Sperry]], [[Chicory]], [[Johnny]]. Zone: [[NPCs - Briarwood]].
   `new:` NPCs: Marasmius (boss, no NPC page yet), Sperry, Chicory, Johnny (rows in [[NPCs - Briarwood]]; no separate NPC pages). Zone: [[NPCs - Briarwood]].
   `why:` No note has a `# Sperry`, `# Chicory` or `# Johnny` heading, and no alias matches. The NPCs folder holds only area pages (`notes/Build Guides/Content/NPCs/`). The rows are in `notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:157-160` (Sperry, Chicory, Johnny) and `:229` (Marasmius, "no NPC page" in this note is correct). The same dangling `[[Sperry]]` also appears in `Trail of Betrayal.md:108` and `Dark Spore Depths.md:93`, which are outside this note's scope.

**Checked and holding (no change needed):**
- Difficulty 3, zone Nettleseed/Briarwood, barrier entrance, members-only false: `prototype/osfr-tools/src/restoration/piece_059.rs:161`.
- Combat job level 5 entry requirement: `prototype/osfr-tools/data/content/dungeons/mushroom_cavern.json` (`minimum_combat_job_level` = 5).
- Achievements "Complete the Mushroom Cavern encounter." and "Group: Mushroom Cavern" (with the full-group wording): `prototype/osfr-tools/data/content/achievements.json:3492-3496, 4356-4360`.
- Client strings: "Defeat Marasmius!", "Defeat the mad mushroom Marasmius!", "Marasmius kicks the wall…", "You leave Marasmius home now!", "Marasmius walk around…", the panel description, "Collect all of the Sprouting Budlings!", "Mushroom Caverns Bonus Objective", "Speed Boost for Mushroom Caverns.", "Giant Man Eating Fungus", "Fungus Golem", "Fungal Soldier", "Man Eating Fungus", and "Find the entrance to the Mushroom Cavern" all resolve in the locale.
- "Vine Wolf" exists in the locale only in card-game and food text (no enemy name), as the note says.
- All 36 prize-wheel item names in the table resolve in the locale, including the Fez/Medium Cloak pair in Conflicts 2.
- `[[The Mushroom Gigas]]` exists (`notes/Build Guides/Content/Dungeons/The Mushroom Gigas.md`), and it says the same thing about the cave boss.

**Unsure:**
- The Goals section says "Three wiki spellings differ from the client and are listed in Conflicts." Conflicts lists only two item spellings (Fez, shard), plus the boss spelling in item 1. The count may be off, but I could not tell which third spelling was meant.
- The `loc <id>` numbers are hash-style IDs, and the locale tool does not accept them (for example `2145075890` returned "no such id"). I matched the text instead. The IDs themselves are unverified.
- Coin values on the wheels (80 vs 162), the 372-star payout, the Atlas video frame, the "Speed Boost" meaning, and the wiki's "Vine Wolves" and "(6)" count cannot be checked against code or client. Left as they are.
- `mushroom_cavern.json` has empty goals and rewards with a "(R) Page goals remain in dungeon_data" comment. The note does not claim otherwise, so no change, but it is a known gap.</result>
