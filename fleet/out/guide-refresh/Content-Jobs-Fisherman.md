<!-- fleet job=guide-refresh id=Content-Jobs-Fisherman status=done turns=30 usd=0.0343 tokens(read,write,in,out)=[1393904, 80359, 62, 20671] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Fisherman.md

**Verdict:** Minor drift. Almost every code-facing claim holds at the tip: the opcode and sub-type map, the six spots and their roster and gate tables, the 40-species count, the frontmatter, and the achievement and trophy data. One claim about job XP is false for our server.

**Corrections:**

- `old:` - Whether quests or the minigame give job XP, and how much, is unknown.
  `new:` - Whether quests give job XP, and how much, is unknown. Our server's minigame policy pays 10 Fisherman XP per paid catch while the Fisherman job is unlocked (reconstructed, not an original value). Per-grade rows are in `fishing_spots.json` under `payout.by_grade`.
  `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:959-971` (`job_xp` is set only when `FISHERMAN_PROFILE` is unlocked, from `payout.fisherman_xp`); `repo:prototype/osfr-tools/data/content/fishing_spots.json:5-25` (`fisherman_xp: 10` per grade); `repo:prototype/osfr-tools/src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs:380` (test asserts `fisherman_xp == 10` after a paid catch).

**Checked and holding (no change needed):**
- Opcode 0x8a = 138 and the sub-type numbers 2, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18 match `repo:prototype/osfr-tools/src/fishing.rs:24` and `:69-130`. The Result packet is sub 14 (`fishing_service.rs:1189`).
- Six spots (`fishing_spots.json:35-90`). The Shallows, Bayou, Rainbow Lake, Wintery Basin, Frostbitten Banks and Darklit rosters and the per-species `minimum_level` gates match the note's spot table (`fishing.json:67-230`, species from line 232).
- The species count is 40 (`type_id` 1001 to 1040, `fishing.json`), matching the note's "40 fish".
- Trainer and guide NPCs: Reed (`job_trainers.json:19-23`), Big J, Selvi, Lila, Gunther and Chip Numbwing (`fishing_spots.json`) match the trainer table.
- `jobs.json:709-714`: Fisherman, freestyle, max_level 20, members_only false.
- Achievements `achievements.json:1380-1500`: level 4, 8, 12, 16 and 20; trophy points 5, 5, 10, 10 and 15; "The Angler" on level 20.

**Unsure:**
- Brambleback's Bayou access (note: "via Reed with a crate for Gunther, or the boat by Brambleback's farm"). `fishing_spots.json:65-70` names Gunther (Briarwood) as the Bayou guide NPC, and the note does not say so. This is a client-text question, so I did not change it.
- Build Ledger line 107 marks Fishing as "Wired, never run natively". The note makes no native-playability claim, so I did not flag it, but readers should not take the minigame as proven in play.
- I did not check the 42-title and 9-unprefixed-title counts, or the Sanctuary/Snow Days/event claims. They are client-locale questions outside the repo.
