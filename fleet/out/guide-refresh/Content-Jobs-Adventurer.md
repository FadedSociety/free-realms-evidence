<!-- fleet job=guide-refresh id=Content-Jobs-Adventurer status=done turns=38 usd=0.0371 tokens(read,write,in,out)=[1792996, 77968, 80, 18928] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Adventurer.md

**Verdict:** minor drift. Most code-checkable claims hold at the tip. One count in the Overview is misleading, and a few gate facts are worth a look but are not clear errors.

**Corrections:**

1. `old:` lists 35 collections whose common reward is "Adventurer Exp."
   `new:` lists 35 collections, 22 of which give "Adventurer Exp." (the 19 common collections plus Briarwood, Sacred Grove and Wilds Explorer)
   `why:` repo:prototype/osfr-tools/data/content/collections.json has 35 collection records in total (19 common, 12 Rare Exploration, 4 Explorer). Exactly 22 carry "Adventurer Exp." (lines 223 through 2233). The Newbie Explorer collection gives an item, and the Rare ones give coins or items. The note's own table (lines 189 to 191) lists 19 common and 3 Explorer collections, so the Overview sentence contradicts it.

**Checked and holding:**
- Max level 20: repo:prototype/osfr-tools/data/content/jobs.json:9.
- No trainer and no abilities: jobs.json:11 (`trainer_npc_ids: []`) and jobs.json:76 (`abilities: []`).
- Quest count: jobs.json quest_ids hold 3000001 to 3000061 plus 3000200, which is 62 entries. That matches Parts A to G in the note (14+5+4+5+22+8+4 = 62).
- Level trophies at 4, 8, 12, 16 and 20: repo:prototype/osfr-tools/data/content/achievements.json:477 onward ("Adventurer: Level 4/8/12/16", with 20 presumably after).
- Rare reward example: collections.json:1459 gives "Seeker's Boots" for Blackspore Rare, matching the note's table.
- The vault note [[Starting Area Content Audit]] now lives at notes/Research/Starting Area Content Audit.md (repo:notes/Research/Starting Area Content Audit.md). The wikilink resolves by name, so it is not false, but a path citation would break.

**Unsure:**
- "Quests do not require the job" (line 32) holds for Adventurer itself. However, two quests in adventurer.json carry explicit job gates. 3000009 ("Fighting the Pack", the A9 row) has `"job": 43` (Brawler) at repo:prototype/osfr-tools/data/content/quests/adventurer.json:682, and enforcement is at src/quest_engine.rs:2126. 3000016 ("Cleetus' Copper Collection", B2) has `"job": 14` (Miner) at adventurer.json:1215. Neither gate appears in the note's prerequisite cells (A9 says only "After A8"). I did not edit these, because the note's statement is still true for the Adventurer job itself. Consider adding the gates to the A9 and B2 rows.
- The Gaps section says XP per quest is unknown. adventurer.json carries reconstructed `job_xp` values for some quests (for example the 20 XP test policy for 3000021 in w64_regional_quest_tests.rs:428). Those are test policy, not recovered rewards, so the note's "unknown" may still be right.
- Line 24 and line 215 ("all 35 above") both treat the 35 collections as the XP source. The correction above only fixes the Adventurer Exp. count.

I could not finish checking the quest-text and client-ID claims within the budget.
