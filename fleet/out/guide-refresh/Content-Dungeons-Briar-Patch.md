<!-- fleet job=guide-refresh id=Content-Dungeons-Briar-Patch status=done turns=17 usd=0.0203 tokens(read,write,in,out)=[613316, 59291, 36, 13486] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Briar Patch.md

**Verdict:** minor drift. Nearly every checkable claim holds at the tip. Two claims about the "NOT LIVE" dev flags overstate what the client locale shows. The note makes no claim about our code's implementation status, so there is nothing there to check against the tip.

**Corrections:**

1. Related quests table, Lead Champs row.
   - `old:` The "Lost in the Briar Patch" titles are marked NOT LIVE (`loc 3154811741`, `3918781666`).
   - `new:` Only one of the two "Lost in the Briar Patch" titles is marked NOT LIVE ("NOT LIVE - Lost in the Briar Patch", `loc 3154811741` or `3918781666`). The other reads "Lost in the Briar Patch" with no flag.
   - `why:` The locale holds one "NOT LIVE - Lost in the Briar Patch" (text row 73678) and one unflagged "Lost in the Briar Patch" (row 73733). A search for "NOT LIVE" near "Briar" returns only the flagged one. Repo: `prototype/osfr-tools/data/content/dungeons/briar_patch.json` has no status for these titles.

2. Conflicts, item 4.
   - `old:` Two strings label a related quest "NOT LIVE".
   - `new:` One string labels a related quest "NOT LIVE" ("NOT LIVE - Lost in the Briar Patch"). Its unflagged twin "Lost in the Briar Patch" is not marked.
   - `why:` Same locale check as correction 1. The locale holds one NOT LIVE string for this quest, not two.

**Checked and holding (no change):**
- Dungeon difficulty 4: `scripts/pieces/piece_059.py:77,116` and `tests/pieces/test_piece_059.py:101` (`by_name["Briar Patch"]["difficulty"] == 4`).
- Achievement texts "Complete the Briar Patch encounter." and "...with a full group." and the names "Briar Patch" and "Group: Briar Patch": `prototype/osfr-tools/data/content/achievements.json:3567-3568, 4431-4432`.
- Client text for Azure's quest, Dewybloom's escort, Susy's bears, Chugilda's meat, the Nettalie barrier, the Mutated Shepard bonus, Briar Patch Bonus Objective, Barrier Knockback, Briar Patch Wolf and Bear, Forest Giant Boss, Wolf Vine Golem, and the quest-complete line: all found in the locale.
- Every prize-wheel item name in the table exists in the locale. Items with a `{n}` prefix, such as "Bodkin Archer Gloves", "Stick and Move Brawler Gloves", "Medic's Megasaw of Vitamins", "Ninja's Jagged Scythe of Shadow Armies", "Sensei Ninja Wristguards", "Threat Range Warrior Gauntlets", and "Pressure Wave Medic Gloves", are present in that form. "Warrior's Double Axe of Whirlwind" is at locale row 132020.
- Prize-wheel items also appear in `prototype/osfr-tools/data/content/dungeons_unresolved.json` (owner `briar_patch`, around lines 2813–3062), which matches the note.

**Unsure:**
- The `loc <id>` numbers (for example 429991411, 1367235519, 1291047686) do not resolve in the `locale` tool. Its numeric keys are row numbers, not the hashed ids the note uses. I could only confirm the text, not the ids.
- The NPC wiki links `[[Azure]]`, `[[Nettalie]]`, `[[Sven]]`, `[[Dewybloom]]`, `[[Susy]]`, `[[Chugilda]]` and `[[Zargoomi]]` have no matching files under `notes/Build Guides/Content/NPCs/`. The NPC rows live in `NPCs - Briarwood.md`. This is a broken-link question, not a status claim, so I did not propose an edit.
- The "Defeat the Briar Patch bears before they are mutated" line (`loc 2175577612`) and the wiki-only counts (10 Shepards, the 176 and 255 Coin payouts, and "182 Stars or less") could not be checked. They rest on the wiki.
