<!-- fleet job=guide-refresh id=Content-Dungeons-Prince-of-Low-Tide status=done turns=13 usd=0.0147 tokens(read,write,in,out)=[351046, 46783, 28, 10699] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Prince of Low Tide.md

**Verdict:** current, with minor drift in two quoted client strings. The note's status and code-facing claims hold at the tip. Most of the note is client-locale and wiki text, and the locale checks below mostly pass.

**Corrections:**

1. `old:` `"Which of you was followed! Idiots!"`
   `new:` `"Which of you was followed? Idiots!"`
   `why:` client locale 116201 reads "Which of you was followed? Idiots!" (question mark, not exclamation mark). The note's own `[client]` tag makes this the authoritative form.

2. `old:` `failsafe teleport ports "Prince of Low Tide Failsafe Port 1" and "Teleport 2"`
   `new:` `failsafe teleport ports "Prince of Low Tide Failsafe Port 1" and "Prince of Low Tide Failsafe Teleport 2"`
   `why:` client locale 117013 is "Prince of Low Tide Failsafe Port 1" and 117015 is "Prince of Low Tide Failsafe Teleport 2". The note's fragment "Teleport 2" is a truncated form of that string.

**Checked and holding:**
- Repo: `prototype/osfr-tools/data/content/dungeons/prince_of_low_tide.json` exists. Its `name_string_id` is 3994251663, and its difficulty (4), level 9 requirement and Seaside zone match the note. `Dungeons.md:139` lists the battle as difficulty 4, level 9, Seaside, Special Spawn, written, which agrees with the note.
- Repo: `enemies_unresolved.json` (around lines 13073–13130) and `dungeons_unresolved.json` (around line 18855 onward) cite this note's section headings ("Enemies and boss > Boss", "Enemies and boss > Minions", "Rewards > Prize wheel by job > Wizard"). All of those headings still exist.
- Client locale: the panel description, the lore text, "Knock out the Prince of Low Tide!", "Knock out some Cray Royal Servants!", "Defeat the Prince of Low Tide", "Win Wandering Combat Encounter Prince of Low Tide!", "Requires a level 9 combat job", the Cook-off Catastrophe description, "Cray Royal Servant", the tidal-wave system line, and the speech lines "They found us!", "Get them!", "I need smarter servants. I'll get you myself!", "The water will get you!", "Get them, or I'll make chowder out of you!" and "I command the tide! Wash away my foe!" all match. Of the prize-wheel items, the 16 I spot-checked (for example Hydrostatic Medic Gloves, Adherent Wizard Gloves, Medic's Megasaw of Alarm, Wizard's Jewel Wand of Firestorm, Hardwood Celestial Necklace) match exactly.

**Unsure:**
- The lead says "not an Atlas dungeon". The repo nonetheless stores the battle as a record under `data/content/dungeons/` (`prince_of_low_tide.json`), and `Dungeons.md` lists it. The note's wording is a classification choice, not a code fact, so I left it alone.
- Locale hash IDs (for example `loc 3166866536`, `1796529187`) could not be resolved in the locale tool, which uses row IDs. I checked the strings by text instead.
- Nothing in the server code (`prototype/`) routes or implements this battle, so the "not built" framing is not contradicted. Nor is it confirmed by any Autopilot or Build Ledger entry.
- The video frame claims, the coin and star figures, and the wiki infobox inference are outside what the tip can check.
