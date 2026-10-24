<!-- fleet job=note-refresh id=Mining-Pending-Fall-Reshuffle status=done turns=12 usd=0.0108 tokens(read,write,in,out)=[184210, 32888, 26, 9589] model=claude-haiku-5-5 -->
# notes/Research/Mining Pending Fall Reshuffle.md

**Verdict:** minor drift to badly stale on citations and the pinned source. The probe's conclusions were measured against a pre-fix `mining.rs`, and the tip has moved past that. The `Type8Engine`, `OnLevelEventMsg 21/25/11` and reshuffle-on-no-move behaviour still exist as described.

**Corrections:**

1. `old:` `| src/mining.rs (reviewed) | 6c59ae0ce97a998c062e5cc25658c0c4c8accd150e8db0ac7550c756c1ed38ed |`
   `new:` `| src/mining.rs (reviewed, pre-fix; superseded) | 6c59ae0ce97a998c062e5cc25658c0c4c8accd150e8db0ac7550c756c1ed38ed |` and add below the table: "Tip moved on: the `has_move` wildcard fix is final at `da3b5b567bdcaf054d713297af9bae412a367453c8989dc157030f8946fe7a1d` (`bytes=59480`). This replay has not been re-run against that hash."
   `why:` `repo:notes/Reviews/Mining Move Detection Repair Review.md:3-4,19-29` (pre-edit `6c59ae0c` → final `da3b5b56`); `repo:notes/Research/Mining Wildcard Move Detection.md:70-71`. `has_move` now sits at `repo:prototype/osfr-tools/src/mining.rs:2087`, and the no-move reshuffle decision depends on it.

2. `old:` `reproduces the real post-state` and the following `bit-for-bit. The crafted pending-bottom case remains only a bounded private`
   `new:` `reproduces the real post-state bit-for-bit against the pre-fix \`has_move\` (\`6c59ae0c\`); the later wildcard \`has_move\` fix (\`da3b5b56\`) has not been replayed. The crafted pending-bottom case remains only a bounded private`
   `why:` `repo:notes/Reviews/Mining Move Detection Repair Review.md:11-15,42-50` (the fix changes `has_move` results on captured boards; `has_move` is at `repo:prototype/osfr-tools/src/mining.rs:2087`).

3. `old:` `` (`src/mining.rs:616-624`, ``
   `new:` `` (`src/mining.rs:1320-1334` definition, reshuffle branch at 1328-1334; call sites `src/mining.rs:1678` in `settle_after_collect` and `src/mining.rs:1810` in `apply_powerup_action`, ``
   `why:` `repo:prototype/osfr-tools/src/mining.rs:616-624` is the packet-dispatch `match` (`OnStartLevelMsg` → `initialize_board(..., false, ...)` at 653-660), not a reshuffle. `initialize_board` is at 1320-1327 and emits `OnLevelEventMsg\t11\t1` at 1333. Lines 1678 and 1810 are the two `initialize_board(..., true, ...)` reshuffle calls.

4. `old:` `` `1068-1081`). ``
   `new:` `` the reshuffle calls are inside `settle_after_collect` and `apply_powerup_action` (see 3). ``
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1068-1081` is `write_content` / `validate_powerup_definitions`, which has nothing to do with reshuffle.

**Unsure:**

- The note cites `src/mining.rs`, but the file lives at `prototype/osfr-tools/src/mining.rs`. Other notes use the same short form, so I left it alone.
- I could not recompute any sha256 with these tools. The tip hash is therefore unverified, and the `da3b5b56` value comes from the review note, not from the file.
- The probe at `lab/reports/mining-pending-fall-reshuffle-20261009T140740Z/` is private and not visible here, so the test counts (6 passed) and the capture/state hashes were not checked.
- The `core/ServerGrid.as` / `ServerTile.as` line anchors describe the original client, which I did not verify.
- I did not check whether the later `has_move` fix changes the crafted counterexample's outcome (no-move reshuffle erases a bottom-row 601). The fix only removes wildcard false positives, so the outcome may still hold; it needs a re-run.
