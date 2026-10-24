<!-- fleet job=guide-refresh id=Content-Dungeons-The-Bat-Cave status=done turns=23 usd=0.0232 tokens(read,write,in,out)=[843843, 58096, 48, 14908] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/The Bat Cave.md

**Verdict:** current, with one minor misquote. The note's code-facing claims agree with the tip, and nearly all of its client strings and ids check out against the locale.

**Corrections:**

- `old:` If you be headin' in the cave, be wary! It is chock full of bats.
  `new:` If you be headin' in the cave, be wary! It is chock full o' bats.
  `why:` The client string reads "chock full o' bats" (locale text, "If you be headin' in the cave, be wary! It is chock full o' bats.", id 18491). The note's quote, which is attributed to video FamA1qX7C38/00002, has "of" in place of "o'". Quote the client text as shipped.

**Checked and consistent (no change needed):**

- Entrance is a `barrier` in Singing Crystal Mines, Snowhill, difficulty 2: `repo:prototype/osfr-tools/src/restoration/piece_059.rs:152`. The objective locale 30449 matches `repo:prototype/osfr-tools/data/content/achievements.json:3319` and the locale text "Complete the The Bat Cave! encounter." (30449).
- The dungeon record exists as `repo:prototype/osfr-tools/data/content/dungeons/the_bat_cave.json`. Its name id 4019064620, difficulty 2, `recommended_player_level` 3, and `members_only` false match the note. Its goals and rewards are empty and marked reconstructed, which is consistent with "not playable" in `repo:notes/Design/Build Ledger.md:78`.
- `repo:notes/Build Guides/Content/Dungeons/Dungeons.md:84` ("none (3+ recommended)", written) agrees with the Requirements table.
- Client strings verified in the locale: "Remove the Bat King!" (6467), "Defeat the Elder Bats!" (6611), "Find the entrance to the Bat Cave." (6607), "Bat King Summons" (6661), "Bat Cave - Savage Claws" (45204), "Calren, the Lost Miner" (45981), "Defeat 15 bats within the Bat Cave!" (24486), "Group: The Bat Cave!" (31062), "Complete the The Bat Cave! encounter with a full group." (31100), "Battles in the Bat Caves give bonus rewards!" (31349), "Win Combat Encounter The Bat Cave!" (119153), "Bat Cave Bonus Objective" (140154), "Defeat Elder Deep Bats" (388305), the Elder Bats description, and the quest texts for Trixi, Robin, the Rowdy Rumbler hammers and the bat-complaint quest.
- Prize wheel items are all in the locale except the Medic necklace. The Medic Ring of Regeneration II and Ring of Energy II exist (131055, 131070). No "Necklace of Regeneration" string exists, so Conflict 1 holds.
- Locale ids in the note use a different (hash-style) id scheme from the locale tool's small integer ids. I did not treat that as an error.

**Unsure:**

- The NPC wikilinks `[[Echolyss]]`, `[[Calren]]`, `[[Brody Sparfist]]`, `[[Buren]]`, `[[Trixi]]`, `[[Spruce Waynehammer]]` and `[[Sorin]]` have no matching page under `notes/Build Guides/Content/NPCs/` (only zone pages exist) or anywhere in the repo as a `# Name` heading. They may be dangling links, but this is a link-target issue, not a factual claim.
- Wiki-only claims (49-coin slot, 100-coin members bonus, 124-star cap, the "(3)" Elder Bat count, the wheel contents by job, bonus clothing sets) and video-only claims (map markers, Adventurer 20, the 911 m marker) could not be checked from the repo or client.
- The locale tool does not resolve the note's hash-style ids (for example 1871453085 and 2258849547), so those ids are unverified. The text they point to was matched by content.
