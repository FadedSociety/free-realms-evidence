<!-- fleet job=note-refresh id=Mining-Starting-Round-Pacing status=done turns=8 usd=0.0091 tokens(read,write,in,out)=[82062, 27881, 18, 9523] model=claude-haiku-5-5 -->
# notes/Research/Mining Starting Round Pacing.md

**Verdict:** badly stale on the baseline. The study's probe results are historically accurate for the inputs it used (`collectable_percent` 10–50, goals 15+12), but the note's statements about the shipped baseline and the candidate's status are false at the current tip. The 40% / 6+6 candidate it proposes as a lab-only option has since been adopted as the shipped default.

**Corrections:**

1. `old:` this study provides. The original baseline stays `collectable_percent = 10`.
   `new:` this study provides. The shipped baseline is now `collectable_percent = 40` with 6+6 quotas, adopted from this lab candidate (see [[Mining Completion]]). The 10 and 15+12 inputs above are the pre-adoption values this probe ran against.
   `why:` `repo:prototype/osfr-tools/data/content/mining.json:16` (`"collectable_percent": 40`), lines 23 and 30 (quota 6 for 601 and 602). `repo:prototype/osfr-tools/src/mining.rs:1005-1018` (quota 6 and 6) and `:1037` (`collectable_percent: 40`). `repo:notes/Research/Mining Completion.md:13,20` (the 40% / 6+6 default is selected in code). `repo:notes/Tasks.md:240`. The "Candidate path" paragraph (lines 45–49) also reads as if deployment were still open. It is no longer: the 40 / 6+6 content is in the shipped package.

2. `old:` `038a135d64fe0c3be6a8e57eabbe002e7f8b651566b0ca260098175abf16959e` (zero-powerup baseline; the
   `new:` `038a135d…` (pin as frozen on 2026-10-09; superseded at tip, because `src/mining.rs` now selects the 40% / 6+6 default and no longer matches this hash) (zero-powerup baseline; the
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1005-1037` (the default-spec change). `repo:notes/Research/Mining Completion.md:20` ("`src/mining.rs` now selects the 40% and 6+6 default"). I could not recompute the sha256 with the tools I have, so this is inferred from the content change.

3. `old:` 10 (existing authored baseline)
   `new:` 10 (pre-adoption baseline; shipped default is now 40)
   `why:` `repo:prototype/osfr-tools/data/content/mining.json:16` and `repo:prototype/osfr-tools/src/mining.rs:1037` (both 40). The row is historically accurate for the study's inputs, but "existing authored baseline" now misleads.

**Unsure:**
- The lab artifacts (`lab/reports/mining-pacing-study-20261009T1716Z/…`, `run_pacing_study.py`, `--content` flag, `PLAYABLE_MAX = 10` harness setting) are not in the repo, so I could not confirm them. The `PLAYABLE_MAX` setting is only cited in other notes (`Mining Whole Round Feasibility.md:20`, `Mining Clickable Round Feasibility.md:17`).
- The 14x14 board / 8x8 playable rectangle is consistent with `mining.json` height 14 and with the Playable Candidate note. I did not check the width or the playable rectangle fields.
- The cross-links resolve (`notes/Design/MMO Worker Contract.md` exists; the Research notes were found by search).
- The headline finding (all five parameters miss the 5–10 minute window) describes the 15+12 quotas. It is not contradicted by the tip, but the tip's 40% / 6+6 candidate was separately measured at 85 chains and 340 modeled seconds (`repo:notes/Reviews/Mining Starting Round Candidate Review.md:39-40`). The note should probably say so.
