<!-- fleet job=guide-refresh id=Content-Jobs-Ninja status=done turns=27 usd=0.0372 tokens(read,write,in,out)=[1517786, 90835, 58, 21417] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Ninja.md

**Verdict:** minor drift. Most checkable claims hold at the tip. One sentence is now misleading because our shipped trainer data enforces a different Archer gate than the note describes. I stopped at the budget limit, so the checks below are a sample, not the whole note.

**Corrections:**

1. `old:` and records the Archer 20 gate as a client-only requirement.
   `new:` and records the Archer 20 gate as a client-only requirement. Our shipped trainer row is weaker: it requires Archer rank 5 (the recovered level 20 is reduced to 5 for playtesting, and restoring 20 is a data change, not a code change).
   `why:` repo:prototype/osfr-tools/data/content/job_trainers.json:65-70 (`requires` profile 35 Archer, rank 5, with the (R) playtest reduction note); repo:prototype/osfr-tools/src/gameplay/s15_npc_transactions.rs:40-41 and :55 (`LEARN_REFUSAL = "level 5 Archer"`); repo:prototype/osfr-tools/src/profiles.rs:62-64.

**Checked and holding (no change):**
- Frontmatter `max_level: 20` and `members_only: true`: repo:prototype/osfr-tools/data/content/jobs.json:1087-1088.
- Achievements "Ninja: Level 4/8/12/16/20" with bronze 5 (4, 8), silver 10 (12, 16), gold 15 (20): repo:prototype/osfr-tools/data/content/achievements.json:1867-1985.
- Dungeon difficulties: Deep Mines 3, Fleetfoot Ninja 2, Forest Troll Fort 5, Cursed Graveyard 1, Misty Mountain 3 (spot-checked): repo:prototype/osfr-tools/data/content/dungeons/*.json line 60-61 or 72-73.
- Entry gates 3/4/5 need level 5/9/13: repo:prototype/osfr-tools/src/encounter.rs:541.
- Giver for E2 "Stolen Away" is Grosh (9000000335) and for B5 "Return to the Mentor" is Frostpetal (9000000093): repo:prototype/osfr-tools/data/content/quests/ninja.json:94-97 and :742-744; repo:prototype/osfr-tools/data/content/npcs/snowhill.json:17028-17033.
- Server quest records for the Ninja line are ids 3110001 to 3110025 (25), matching rows E1 to G1 of the table. Quest ids 3110001 to 3110025: repo:prototype/osfr-tools/data/content/jobs.json:1100-1126.

**Unsure:**
- E1 "Ninja: The Ninja Path" reward is "unknown" in the note, but repo:prototype/osfr-tools/data/content/quests/ninja.json:23-33 assigns a reconstructed 0 coins and 15 Ninja job XP (labelled (R), not sourced). The note's "unknown" is about sourced rewards, so it may be fine, but a reader of the server data would see a value.
- Weapon tier gates: the note says the wiki's Blades are at level 4, while repo:prototype/osfr-tools/src/restoration/piece_034.rs:16 gates the named Ninja weapons on MinProfileRank 1/5/8/12/16. Different sources; not settled.
- The note's count of 31 titles versus 25 server records: the six extra titles (Restoring Honor, The End of the Path, Shadow Master, Walking the Path, Gathered Shadows, Stilling the Waters) have no server record. That fits the note's own "client-only" wording, so no correction.
- Title id for "Return to the Mentor": repo:notes/Research/Quest Audit.md:78 cites 78874 while ninja.json:743 has title_string_id 78873. Probably a different column; not settled.
- Not checked: the Ty/Chloe/Sakka trainer locations, the dungeon difficulties for Grexan's Camp, Howling Hills, Floren Forest, Hot Springs, Danger Peaks, Cray Caves and Bixie Hive, the trait and ability tables, and the job-ability unlock levels (repo:notes/Research/Job Skill Levels.md marks them (R) "exact level still unknown", consistent with the note).
