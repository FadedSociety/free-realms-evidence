<!-- fleet job=guide-refresh id=Content-Dungeons-The-Snarling-Hedges status=nothing_found turns=16 usd=0.0161 tokens(read,write,in,out)=[465654, 51708, 34, 10037] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/The Snarling Hedges.md

**Verdict:** current. I found no claim in the note about our code or build status that is now false. The note is almost entirely client-locale, wiki and video facts, and it makes no playability or implementation claim, so the status-type checks had little to bite on.

**Corrections:** none.

**What I checked (all consistent with the tip):**
- Dungeon data: `prototype/osfr-tools/data/content/dungeons/the_snarling_hedges.json` exists. It has `difficulty: 3` (line 61), `minimum_combat_job_level: 5` (line 116), `members_only: false` (line 174), zone "Briarwood (Thistlerow)" with no numeric zone id (lines 72, 90), and quest "None found" (line 155). These match the note's Overview and Requirements tables.
- Rewards: the data file grants 162 coins on the prize-wheel slot (line 781) and 203 coins as the members-only bonus (line 811). The Stars line reads "270 Stars or less" (line 689). All match the note.
- Prize wheel: all six job wheels are in the data file's unresolved-item list (`dungeons_unresolved.json` ~25755 onward), so the item names are carried as named-but-unresolved, as the note says. Locale spot checks confirmed Ninja's Scythe of 1000 Storms (131981), Drifting Archer Hoodie (132758), Catchweight Brawler Jacket (132879), Emergency Medic Shirt (133104), Nusumi Ninja Gi (133234) and Scholar Wizard Medium Cloak (133418).
- Achievements: `prototype/osfr-tools/data/content/achievements.json` lines 3516–3520 ("Complete the The Snarling Hedges encounter.") and 4380–4384 ("Group: The Snarling Hedges", full-group text) match the note's Rewards table.
- Enemies: the data file lists Vine Bears, Ghost Snakes, Snake Statues, Hedge Guardians and Hedge Knights as wiki-sourced entries (lines 481–485, 2220–2289). The client-name entries (Hedge Guardian, Maze Viper, Snake Statue, Ghost Snake Form, Hedge Knight, Hedge Knight Statue, Hedge Knight Chest) are all in the locale. "Vine Bear" is absent from the locale, which matches Conflicts item 2.
- Quest and goal text: "Defeat Nogg the Cruel." (locale 4788), "Win Combat Encounter The Snarling Hedges" (119149), "Snarling Hedges Bonus Objective" (140144), "Complete the The Snarling Hedges encounter with a full group." (31109), "Group: The Snarling Hedges" (31071), "vine golem" (17161), "cursed bears" (18088), "Snarling Hedges Nature Resource card" (13341), and the Gorglemain mirror text (115951) all exist.
- Entrance and guard text: "The Snarling Hedges are located South, in the Hedge Maze..." (390042) and Hurplelump's "Halt! By Darkthorne's decree, this section of the maze is off limits." (3896) match the note.

**Unsure:**
- Locale ids cited as numbers (for example `loc 725470992`, `3814524718`, `2145075890`, `4036011684`) return "no such id" from the `locale` tool when queried by number. The text matches exist, so the note's ids probably use a different id scheme (the `cq.py loc` convention) that I could not reproduce here. I did not correct the ids.
- The Bonus Goal "Defeat the 3 Hedge Knights!" (`loc 2676374441`) did not appear in my locale search. The alternation query returned only the first 30 hits, so I could not confirm or refute it.
- The note's "Level 5 combat job" requirement is a content claim. Build Ledger line 69 says `required_combat_level` is not enforced by our server. The note does not claim enforcement, so I left it alone, but a reader might assume it is enforced.
- The NPC wikilinks `[[Nogg the Cruel]]`, `[[Private Gorglemain]]`, `[[Private Hurplelump]]`, `[[Cuttensnip]]`, `[[Chugilda]]` and `[[Tiny Tina]]` have no standalone notes in `Content/NPCs/`. NPC facts sit in `NPCs - Briarwood.md`. This may be an unresolved link rather than a false claim, so I did not change it.
