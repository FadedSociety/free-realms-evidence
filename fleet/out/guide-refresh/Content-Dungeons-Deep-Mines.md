<!-- fleet job=guide-refresh id=Content-Dungeons-Deep-Mines status=done turns=23 usd=0.0232 tokens(read,write,in,out)=[746273, 55496, 48, 17637] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Deep Mines.md

**Verdict:** minor drift. The note is almost entirely client-locale and wiki sourcing, and it makes almost no claims about our code. Nearly every `loc` id and quoted string I checked matches the shipped locale. Two quotes are not verbatim.

**Corrections:**

1. `old:` `**"Bonus: Find and defeat the Robgoblin Pyromancer!"** (`loc 925498345`)`
   `new:` `**"Find and defeat the Robgoblin Pyromancer!"** (`loc 925498345`; the "Bonus:" label is not part of the string)`
   `why:` client/en_us_data.dat:24486 reads `925498345	ucdt	Find and defeat the Robgoblin Pyromancer!`. A search for "Bonus: Find and defeat" in the locale returns nothing.

2. `old:` `right after a "bruiser" boss falls`
   `new:` `right after "The boss takes a dive!" (the line does not name the boss)`
   `why:` client/en_us_data.dat:103186 (`loc 3902306687`) reads "The boss takes a dive! Now another Robgoblin wizard steps into the cavern..." The word "bruiser" is not in the cited line.

**Checked and holding (no change):**
- Locale ids and quotes: 2582793152, 871089970, 2145075890, 2333131853, 845659240, 4143159045, 2945778241, 1529480620, 1034205554, 1040761379, 2065943012, 2835023286, 430872612 and 2376467695 (whose text matches the note's paraphrase), 2926552261, 3121919529, 3144586265, 3726742448, 2199945195, 357101710, 350341811, 2749704609, 3089090172, 4152001137 (present in the .dat as ugdt "Deep Mines", although the locale tool's id lookup does not index it), 1943695917, 981677512, 3858944633, 3304566763, 3960897981, 1408180796, 2893458983, 1672961846, 2318379248, 1416343814, 2406676062, 3021989716, 1968595844, 3513295665, 4222962258, 3665649177, 2943023409 and the Tuga/Pyromancer ability names.
- Prize wheel: every item name in the table is present in the locale (checked through the locale tool, including Archer's Composite Bow of Explosions, Archer's Necklace of Vitality III, Charge Attack Warrior Pauldrons and Wizard's Bone Wand of Firestorm).
- Our code: `repo:prototype/osfr-tools/data/content/dungeons/deep_mines.json` exists. Its `name_string_id` (4152001137), difficulty 3 and `minimum_combat_job_level` 5 agree with the note. Its goals and rewards are empty, which the note does not claim otherwise. No Autopilot report mentions Deep Mines, and the Build Ledger has no per-dungeon status line for it.

**Unsure:**
- The "NPCs:" line links [[Tuga the Bruiser]], [[Taraz]], [[Buren]], [[Brock]], [[Burlen]], [[Tavil]], [[Trixi]] and [[Spruce Waynehammer]]. Searching `repo:notes` for matching `# <name>` headings found no pages, so these links may be dangling. I did not confirm this against a file list.
- The wiki-only claims (160 Stars cap, members-only 131 coins, 80-coin wheel slot, the "(2)" counter, bonus clothing sets, the red markers at 34/50/65 m) are outside what I can check against the repo or client.
- `deep_mines.json` carries its own zone and quest-id fields, which the note does not describe. I did not check whether those fields are themselves stale.
