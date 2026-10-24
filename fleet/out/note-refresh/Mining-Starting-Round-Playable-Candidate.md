<!-- fleet job=note-refresh id=Mining-Starting-Round-Playable-Candidate status=done turns=5 usd=0.0034 tokens(read,write,in,out)=[26203, 11867, 12, 3307] model=claude-haiku-5-5 -->
# notes/Research/Mining Starting Round Playable Candidate.md

**Verdict:** minor drift. The core conclusion holds (an odd second quota is refused, and the baseline per_reward values are 1 for 601 and 2 for 602). The source anchor has moved and the validation expression is slightly misquoted.

**Corrections:**

- `old:` `` `src/mining.rs:1115`–`:1120` validates goals as ``
  `new:` `` `src/mining.rs:1159`–`:1167` validates goals as ``
  `why:` repo:prototype/osfr-tools/src/mining.rs:1159-1167. The goal check now sits at 1159–1167 (error returned at 1166, `invalid mining goals`). Lines 1115–1120 are now the duplicate-powerup-value and powerup-spawn-chance checks in the same file, so the old citation points at unrelated code.

- `old:` `` `!collectable.contains(value) || per_reward == 0 || quota % per_reward != 0`. ``
  `new:` `` `!(spec.selectable.contains(&g.value) || spec.collectable.contains(&g.value)) || g.per_reward == 0 || g.quota % g.per_reward != 0`. ``
  `why:` repo:prototype/osfr-tools/src/mining.rs:1160-1163. The membership test is against selectable or collectable, not collectable alone, and the code is written with `g.` rather than `value`/`per_reward`. The modulo rule (`quota % per_reward != 0`) is unchanged, so the conclusion that an odd second quota is refused still holds.

**Checked and holding:**
- Baseline `per_reward` 1 for 601 and 2 for 602, with quotas of 6 in the baseline spec: repo:prototype/osfr-tools/data/content/mining.json:19-32.
- Board is 14×14: repo:prototype/osfr-tools/data/content/mining.json:34 and :294.
- Duration 180 in the baseline: mining.json:17.

**Unsure:**
- The lab paths (`lab/reports/mining-playable-candidate-20261009T1755Z/…`), the `candidate-study.json` / `.log` receipts, and the run counts and durations (48/192 s, 46/184 s, 85/340 s) are not in the repo tip, so I could not verify them. The only related mention is in `notes/Reviews/Mining Starting Round Candidate Review.md`, which cites the same `percent40_quotas6_6` artifact and transcript hashes. I did not re-derive the 5.7-minute figure.
- The baseline hash `25370f04…` and the harness hash `3cc6652b…` cannot be checked from the repo.
- The "8×8 playable interior" was not checked against the code.
- The claim that the host "panicked at content load" for the odd-quota presets is not checkable from the tip.
