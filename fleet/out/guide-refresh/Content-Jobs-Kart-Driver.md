<!-- fleet job=guide-refresh id=Content-Jobs-Kart-Driver status=done turns=16 usd=0.0182 tokens(read,write,in,out)=[471278, 53958, 34, 13456] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Kart Driver.md

**Verdict:** minor drift. Most checkable claims about our code and content hold: frontmatter, level achievements, title and achievement names, the trainer and quest data. One Gaps statement now misleads, because the build registers a reconstructed race payout.

**Corrections:**

1. `old:` Race prize wheels or per-race payouts were not seen.
   `new:` Race prize wheels were not seen, and per-race payouts were not seen in video. Our build registers one reconstructed payout, 50 coins and 25 job XP per finished Wildwood race (speedway 31). No other speedway has a live payout; the starter rows for the other four are used only by tests. Original amounts are unknown.
   `why:` repo:prototype/osfr-tools/data/content/kart_entry.json:7118-7124 (speedway 31, laps 3, reward coins 50, xp 25). repo:prototype/osfr-tools/src/kart_gateway.rs:355-370 (the registered price comes only from that content's `race.reward`). repo:prototype/osfr-tools/src/kart_rewards.rs:119-130 (`starter_defaults` covers 31-39, and its only callers are in `tests/kart_rewards.rs`). repo:notes/Design/Build Ledger.md:103 (Kart: "50 coins and 25 XP paid once", native-verified for the Wildwood race, solo only).

**Checked and holding (no change):**
- Frontmatter `max_level: 20`, `category: freestyle`, `members_only: true` match `prototype/osfr-tools/data/content/jobs.json:813-818`.
- Level achievements at 4, 8, 12, 16 and 20 match `achievements.json:1505-1604`.
- "Rageracer" with the title "Racer" matches `achievements.json:5880-5892` and `titles.json:713-716`.
- "The Speed Demon" for level 20 matches `titles.json:338-342`.
- The trainer NPC for Kart Driver (Cale Yardbird at Tangletrack) matches `job_trainers.json:25-31`.
- The job-quest count is consistent: `jobs.json` lists quest ids 3080001-3080049 (49). The note's 2 entry quests plus 47 table rows also give 49.

**Unsure:**
- The Wildwood row in the Tracks table says "Reward amounts unknown". This is true of the original game, but our build pays 50 coins and 25 XP there (see correction 1). I did not change it, since the note is written from original sources.
- I did not verify the client locale ids or the video frame citations. The `ucdt`/`ugdt` and "53 titles" counts are client-side and outside this repo check.
