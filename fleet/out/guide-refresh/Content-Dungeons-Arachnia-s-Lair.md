<!-- fleet job=guide-refresh id=Content-Dungeons-Arachnia-s-Lair status=done turns=22 usd=0.0270 tokens(read,write,in,out)=[912581, 74918, 46, 17052] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Arachnia's Lair.md

**Verdict:** current, with minor drift. The note's game-text and reward claims match the tip. Its one checkable break is a set of wikilinks to NPC pages that do not exist in the vault.

**Corrections:**

- `old:` NPCs: [[Queen Arachnia]], [[Spinnerette]], [[Wuumba]], [[Sven]], [[Miffit]]. Zone: [[NPCs - Briarwood]].
  `new:` NPCs: Queen Arachnia, Spinnerette, Wuumba, Sven, Miffit (one row each in [[NPCs - Briarwood]], which has no per-NPC pages). Zone: [[NPCs - Briarwood]].
  `why:` `repo:notes/Build Guides/Content/NPCs/` holds only area pages (NPCs - Briarwood.md, NPCs - Wilds.md, and so on), and no note has an H1 for any of the five names. The rows that cover them are `repo:notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:64`, `:221-223` and `:314-315`. Sven's wand quests are at `:315`.

**Checked and holding (no change):**

- Prize wheel by job: all 6 jobs, 28 items. Every item name matches `repo:prototype/osfr-tools/data/content/dungeons_unresolved.json` (the `arachnia_s_lair` owner rows) and the wiki infobox `refs:freerealms-wiki/wikitext/4592-49334-2dbdc2a6ead2.wiki:29-75`.
- Difficulty 2, members-only false, zone "Briarwood (Bristlewood)" with a spider-web trigger: `repo:prototype/osfr-tools/src/restoration/piece_059.rs:146` and `repo:prototype/osfr-tools/data/content/dungeons/arachnia_s_lair.json:61, 162, 180, 209`.
- Mobs and boss, goals (including the 3 Webspinner Princesses bonus), 418 stars, 153 members coins and the bonus clothing sets: all match the wiki page at `refs:freerealms-wiki/wikitext/4592-49334-2dbdc2a6ead2.wiki:11-85`.
- Client strings checked against `refs:FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat` and the locale tool: "Defeat the Spider Queen!", "Defeat Arachnia", "Win Combat Encounter Arachnia's Lair", "Arachnia's Lair Entrance", "Locate Arachnia's Lair in central Bristlewood.", "Defeat the 3 Webspinner Princesses.", "Arachnia's Lair Bonus Objective", the Wuumba, Miffit, Morgan, silk and Sven quest texts, and the Black Widow, Spiderling Mother and Spider Web Spit names. The lookup tool does not take the note's hash ids, so I did not confirm those ids one by one.
- Achievements "Complete the Arachnia's Lair encounter." and the group version: `repo:prototype/osfr-tools/data/content/achievements.json:3156-3160, 4020-4024`.
- No code path or status claim is in the note. Nothing here says the dungeon is built or routed, so there is no status to correct.

**Unsure:**

- **Combat job level "None" (Requirements row).** The wiki quote supports "None", and `repo:prototype/osfr-tools/src/restoration/piece_059.rs:267-270` (`entry_rule(2)`) says `min_combat_level: Some(3)` with `recommended_only: true`. Because the rule is flagged recommended-only, the note's "None" is probably a fair reading, but a reader of the code could take it as a gate of level 3. I did not change it.
- **"No video frame names this dungeon."** `refs` has no video frame index, so I could not confirm this. A search of `refs` for "Arachnia" and "Webspinner" found no frame names.
- **Gap-list claim that the dungeon's goals and rewards are unseen.** The data file `repo:prototype/osfr-tools/data/content/dungeons/arachnia_s_lair.json:13-14` has empty `goals` and `rewards` lists. That matches "unseen" but does not prove it.
