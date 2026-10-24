<!-- fleet job=guide-refresh id=Content-Jobs-Archer status=done turns=27 usd=0.0339 tokens(read,write,in,out)=[1249970, 77554, 56, 23335] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Archer.md

**Verdict:** minor drift. The note is almost entirely client and wiki content, and its locale ids, title ids, quest order, dungeon level gates and entry-chain facts check out against `archer.json` and `tests/archer_entry_*`. Three statements about our server and data are now false or misleading.

**Corrections:**

1. `old:` Per-quest rewards likely live in server quest data not present in the locale or videos.
   `new:` Server quest data now carries fallback payouts that are not client values: Path of the Archer 5 coins and 15 Archer XP (`archer.json:158-172`), Oath of Honor 10 coins and 20 Archer XP (`archer.json:340-354`). The client gives no reward quantities, and these figures are labelled W110 fallback, not recovered rewards.
   `why:` `repo:prototype/osfr-tools/data/content/quests/archer.json:158-172`, `:340-354`, `:350`, `:382`. The Gaps line claims no reward is known. The rewards exist in our data, though unsourced.

2. `old:** Ability unlock levels.** Weapon-bound abilities have no unlock level in any source.`
   `new:** Ability unlock levels.** No client or video source gives an unlock level for Archer abilities. Our `job_abilities.json` (profile 35 block, lines 949-1170) carries `min_level` values for four Archer skills, sourced to a 2009 MMORPG.com article and applied as (R), not client tables (lines 978, 1021, 1057, 1104). Build Ledger line 73 describes the Archer ladder as 1/5/10/15 (R).`
   `why:` `repo:prototype/osfr-tools/data/content/job_abilities.json:949` and `:978`; `repo:notes/Design/Build Ledger.md:73`. "No unlock level in any source" is false for our repo.

   The `old` text above is a shortened version of the note's line 226 sentence. The script should match the exact text `Weapon-bound abilities have no unlock level in any source.` with the bold label kept as written.

3. `old:` (2334013303). [client] See [[Ninja]].
   `new:` (2334013303). [client] The shipped server gate is lower: the Ninja trainer row requires a level 5 Archer, with the client's level 20 kept as the recovered text (`repo:prototype/osfr-tools/src/profiles.rs:62-64`, `repo:prototype/osfr-tools/src/gameplay/s15_npc_transactions.rs:40,55`). See [[Ninja]].
   `why:` The bolded claim "Level 20 unlocks Ninja" is the client's text and stays. Our shipped row uses the rank-5 reduction, so an implementer reading only this page would get the wrong gate.

**Unsure:**

- **Locale ids in lines 36 and 27.** The `locale` tool returned "(no such id)" for 1592607723 and 2334013303, so I could not confirm those ids. A near-match exists at id 5100390 ("Requires: Level 20 Archer"), and 5100368 has the Ninja text.
- **Oath of Honor prerequisite (row 4, "After 3").** Server data has Oath requiring only Path of the Archer (3010003), not Taking Aim (`archer.json:320-322`, and the comment at `:370`). The note's "After 3" follows the wiki order, so it may be right as order but not as a prerequisite.
- **Server chapter scope (not a note claim, but relevant to Gaps).** `archer.json` holds 10 records (3010001–3010010). Only 3010003 (Path) and 3010006 (Oath) are `enabled: true`. Test of Agility and Taking Aim are disabled, and the Oath stump step is skipped (`archer.json:335`, `:370`, `:374`). The Level 10, 15 and 20 gates have no records in our data.
- **Lugabow grants the job.** Server data says trainer 9000000387 unlocks Archer before the chapter opens (`archer.json:188`). The note's "Lugabow then grants the job" describes the client, so I left it.
- **Amateur Archer Bow "now unobtainable"** (quest 6 reward cell). Our code calls it the starter weapon, definition 4266 (`archer.json:350`, `restoration/piece_035.rs:93`). I could not confirm whether a new Archer is actually given that item.
