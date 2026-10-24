<!-- fleet job=guide-refresh id=Content-Jobs-Wizard status=done turns=20 usd=0.0240 tokens(read,write,in,out)=[691687, 72076, 42, 16221] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Wizard.md

**Verdict:** minor drift. The page's code-facing claims are small in number. Two statements in **Gaps** still describe the server data as absent or unknown, and the server now holds both answers. The ability levels, the level-4/8/12/16/20 goals and the quest-line citations still hold.

**Corrections:**

1. Gaps, Rewards bullet
   - `old:` Per-quest rewards likely live in server quest data not present in the locale or videos.
   - `new:` Server quest data (`data/content/quests/wizard.json`) now carries reconstructed rewards for the three enabled Band 1 rows (quests 1 to 3: records 3160003, 3160004, 3160005): 5 coins and 25 Wizard job XP each, no items. The values are marked (R), not taken from the guide, and every other Wizard record is still `enabled: false`.
   - `why:` repo:prototype/osfr-tools/data/content/quests/wizard.json:97-100 and :193-197 (rows 1 and 2, `coins: 5`, `job_xp {"12": 25}`); row 3 per repo:notes/Autopilot/T303.md:8-14; enabled flags at wizard.json:143, :239, :329 (only those three are `true`).

2. Gaps, "Which quest grants the job" bullet
   - `old:` Also unknown: whether a free player can start the line or is stopped by a membership prompt, and whether the Level 20 Medic gate was enforced.
   - `new:` Also unknown: whether a free player can start the line or is stopped by a membership prompt. The Level 20 Medic gate is not enforced at 20 in our build: the server's Wizard trainer row requires Medic rank 5, a playtesting reduction from the client's level 20 (the note's Conflicts 1 still stands as the client-side claim).
   - `why:` repo:prototype/osfr-tools/data/content/job_trainers.json:72-83 (`"requires": {"profile": 11, "job": "Medic", "rank": 5}`, with the source note that the recovered level-20 gate "is reduced to rank 5 for playtesting").

**Unsure:**

- **Which quest grants the job** (Gaps). The server does not grant it through a quest. It treats the Fizzlesticks trainer menu choice as the grant after the Medic prerequisite (`job_trainers.json:82`, a reconstructed source). The note's "unproven (quest 1, quest 5 or the entry quest)" is still accurate as client evidence, but the server's answer is a trainer menu, not a quest.
- **Weapon-bound abilities** (Conflicts 15, "the rule that applies in a rebuild is unknown"). Our `job_abilities.json` lists the four Wizard skills (Zap 1, Fireball 5, Ice Nova 10, Chaos 15; the levels match the note) all with `weapon_class: 10` (lines 444, 493, 549, 591). That is a wand-class gate, not the tier table the note describes (Burn, Firestorm, Chill, Splash, Tsunami). I left the note's wording alone because the server's rule is a rebuild choice, not client evidence.
- **Citation lines.** The note's `Wizard.md:148-151` references in `job_abilities.json` (Zap, Fireball, Ice Nova, Chaos) still point at the right rows of this page.
- **Not checked.** Most of the page is client locale text, wiki data and video, which the repo cannot settle. I did not check the video or locale claims.
