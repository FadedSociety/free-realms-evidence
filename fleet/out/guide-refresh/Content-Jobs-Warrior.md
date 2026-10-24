<!-- fleet job=guide-refresh id=Content-Jobs-Warrior status=done turns=26 usd=0.0348 tokens(read,write,in,out)=[1498698, 93390, 56, 16224] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Warrior.md

**Verdict:** minor drift. Most code-checkable claims hold at the tip. One status claim about how the job is unlocked is out of date, and the members-only flag conflicts between two of our own files, so I left that as Unsure.

**Corrections:**

1. `old:` Start of line. **Unlocks the job.** Client: level 20 Brawler (79965512, 190929883 †).
   `new:` Start of line. Retail W1 unlocked the job. On this server the trainer menu (T201/W176) unlocks it, and W1 is offered only after Warrior is learned and activated. Client: level 20 Brawler (79965512, 190929883 †).
   `why:` repo:prototype/osfr-tools/data/content/quests/warrior.json:73 says "this server's T201/W176 trainer menu remains the unlock path, so the quest is offered only after learning Warrior and activating it". No code path in `src/` ties job unlock to W1.

**Checked and holding (no change needed):**
- Ability unlock levels and rank ladders (Kick 1: 133/150/167/183/200; Spinning Blade 5: 50–75; Quake 10: 83–125; Commanding Shout 15: 50–75) match repo:prototype/osfr-tools/src/restoration/piece_033.rs:359-384 and repo:prototype/osfr-tools/data/content/job_abilities.json:220-305 (min_level 1/5/10).
- Gate levels 5/10/15/20 match the level-test ladder in piece_033.rs:190-270 and the job-level quest objectives in warrior.json (for example W5 `"level": 5` at line 288).
- Title ids for W5, W10, W16 and W22 match warrior.json (for example W10 ucdt 2322652085 / ugdt 2233459052, W22 ucdt 3302139690 / ugdt 3592347326).
- Frontmatter `max_level: 20` matches repo:prototype/osfr-tools/data/content/jobs.json:1400.

**Unsure:**
- **Members-only.** The note's frontmatter (`members_only: true`) and its Overview and Free-tier gap say Warrior is members-only. repo:prototype/osfr-tools/data/content/jobs.json:1401 agrees (`"members_only": true`). But repo:prototype/osfr-tools/src/restoration/piece_033.rs:50 sets `WARRIOR_MEMBERS_ONLY = false` (recovered from the Legacy profile record) and piece_033.rs:52 sets `WARRIOR_TRIAL = true`. The note cannot be fixed without deciding which record is right. Someone should reconcile the two before the Free-tier gap is written.
- **Quest count.** The note says "26 client quest titles". repo:prototype/osfr-tools/data/content/jobs.json:1416-1440 lists 24 quest ids (3150001–3150024). I did not check whether the 26 count is about client titles only, so I left it.
- **Unlock-level sourcing.** Gaps says the unlock levels "come from the wiki only". piece_033.rs:21-23 says they are the wiki table, corroborated by the locale "Achieve Level 5/10/15" text. This is close enough that I did not correct it.
- **Stray test comment.** repo:prototype/osfr-tools/tests/job_trainers.rs:1280 calls Kick "62005" and says it unlocks at rank 5. The shipped data has Kick as 62004 at level 1 and 62005 as Spinning Blade at level 5 (job_abilities.json:220, 261). This is a test comment, not in the note, so it is not a correction here.
- **Not checked.** The Build Ledger (repo:notes/Design/Build Ledger.md:72) says Warrior has no basic attack in runtime content. The note does not make that claim, so I did not chase it.
