<!-- fleet job=guide-refresh id=Content-Dungeons-Vale-of-the-Ancients status=nothing_found turns=19 usd=0.0230 tokens(read,write,in,out)=[727421, 66142, 40, 14949] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Vale of the Ancients.md

**Verdict:** current. I found no false status, routing or path claims. The note is almost entirely client-locale and wiki content, and the repo copy of it agrees with the note.

**Corrections:** none.

**Checked and holding:**
- Prize wheel rows. All 30 item names in the "Prize wheel by job" table, the 202 and 238 coin figures, and "316 Stars or less" match `repo:prototype/osfr-tools/data/content/dungeons/vale_of_the_ancients.json` (coins 202 at line 742, 238 at line 772; item values at lines 814–2016).
- Difficulty 4 and the Briarwood zone. Matches the same JSON (`difficulty` at line 61, zone at line 72).
- Level 9 combat job requirement. The JSON `minimum_combat_job_level` is 9 (line 116). "Requires a level 9 combat job" is in the locale (line 4200).
- Achievement names. `repo:prototype/osfr-tools/data/content/achievements.json:3735-3736` ("Vale of the Ancients" / "Complete the Vale of the Ancients encounter.") and `:4599-4600` ("Group: Vale of the Ancients" / full-group text).
- Client strings, checked by text in the locale table:
  - "Find and remove the source of the disturbance." (line 18908)
  - "Destroy all of the Corrupted Artifacts!" (line 430443)
  - "Vale of the Ancients Bonus Objective" (line 140186)
  - "Corrupted Hound" (line 18877) and "Corrupted Hound Claw" (line 130289)
  - Dev strings for the boss and the lightning, fire column and dark aura effects (lines 20214–24770)
  - "Vulture proc effect" (line 35711)
  - "The second shard is said to be in the hands of a Mysterious Stranger in the Vale of Ancients in Briarwood." (line 419173)
  - "Sir Wellington's outside the Vale of the Ancients." (line 413876)
  - "Dark Essences from sinister hounds" (line 93615)
- Conflicts section. "Howling Fateeater" has no locale hit. "Savage" appears only inside longer names such as "Savage Howl" and "Savage Claws".
- Shard chain. The fourth shard is in the Mushroom Cavern (line 419197), which supports "other dungeons hold the fourth…".
- No code in `repo` (`src`, `tests`, `notes`) references the Vale. The note makes no build or routing claim, so there is nothing to check there.

**Unsure:**
- **Dangling NPC wikilinks** (line 97): `[[Mysterious Stranger]]`, `[[Docaloc]]`, `[[Sir Wellington]]`, `[[Clyra]]`, `[[Miss Artie]]` and `[[Smitty]]`. No file with those titles exists under `notes/` (a search for `^# <name>` found nothing). `notes/Build Guides/Content/NPCs/` holds only zone pages, so the links are likely unresolved in Obsidian. This is a link problem, not a fact about the game, so I did not propose a correction.
- **Locale ids in the note** (for example `loc 2997463613`, `loc 1291047686`, `loc 2778914998`). The `locale` tool does not resolve these numeric ids. I checked the strings by text instead, so the id-to-text pairing is unverified.
- **Video and wiki-only claims** (entrance marker at 62 m, Adventurer 20 frames, members bonus, bonus clothing sets, the Deer NPCs). Not checkable from the repo or client.
