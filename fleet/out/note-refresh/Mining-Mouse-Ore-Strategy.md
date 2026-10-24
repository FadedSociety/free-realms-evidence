<!-- fleet job=note-refresh id=Mining-Mouse-Ore-Strategy status=done turns=8 usd=0.0089 tokens(read,write,in,out)=[113772, 35311, 18, 6671] model=claude-haiku-5-5 -->
# notes/Research/Mining Mouse Ore Strategy.md

**Verdict:** Badly stale on status, minor drift on citations. The 2026-10-09 diagnosis itself is a dated snapshot whose private numbers (41 chains, 9 down-moves, 44/166 boards, 32/12 split) I could not check: the `lab/reports/` proof is not in the repo. Its "no driver change made" framing, however, was overtaken the same day by a repair that changed the planner's rank.

**Corrections:**

1. `old:` row: `prototype/osfr-tools/src/mining.rs:1198-1247`, `:1249-1268`).
   `new:` row: `prototype/osfr-tools/src/mining.rs:1722-1764` (chain rules: >=3 tiles, orthogonal, idle, one colour), `:1502-1552` (gravity compaction), `:1554-1614` (collection only on the bottom playable row).
   `why:` repo:prototype/osfr-tools/src/mining.rs:1198-1268 is board-shape and bounds validation (the "shape code" grammar and dropzone checks), not chain or gravity rules. `validate_chain` is at 1722, `gravity` at 1502, and `collect_fall` (which requires `y == bottom`) at 1554.

2. `old:` ## Candidate (model only - no driver change made)
   `new:` ## Candidate (implemented later: driver `4c41fa64…`, see [[Mining Mouse Ore Strategy Repair]])
   `why:` notes/Research/Mining Mouse Ore Strategy Repair.md:3-5, 17-28 (driver `735f8ece…` → `4c41fa64…`, rank changed inside `find_path`'s `rank()`); notes/Reviews/Mining Ore Planner Repair Review.md:19-29 (one hunk, rank only); notes/Research/Mining Focused Ore Strategy.md:134 (root keeps `4c41fa64`).

3. `old:` Driver reviewed at `735f8eceb1f14e4decbf95d3ae88c9ff55d389799cb8b0a06c6c47cf3f3db594`.
   `new:` Driver reviewed at `735f8eceb1f14e4decbf95d3ae88c9ff55d389799cb8b0a06c6c47cf3f3db594` (pre-repair; the current driver is `4c41fa64a972bb17ea9b390f029d19e9eab618f9568b1b0f285d8e3d6157b742`, see the repair note).
   `why:` notes/Research/Mining Mouse Ore Strategy Repair.md:5; notes/Reviews/Mining Ore Planner Repair Review.md:21-22.

4. `old:` The driver's key `(clears_boolean, length, max_row)` treats every "clears" equally
   `new:` The pre-repair driver key `(clears_boolean, length, max_row)` treated every "clears" equally
   `why:` The current `rank()` is `(collect_now, helped, cleared_total, -remaining_min, len(path), max row)`: notes/Reviews/Mining Ore Planner Repair Review.md:28-29. The old form is only the `735f8ece…` version.

5. `old:` ## Candidate (model only - no driver change made)
   (see item 2: the "Candidate ... On the captured boards this priority had a strictly better ore-progress choice on 44 boards" paragraph is now superseded; add after it:)
   `new:` Superseded: the repaired driver reproduces this on 44/44 captured boards and passes the synthetic immediate-ore fixture (notes/Research/Mining Mouse Ore Strategy Repair.md:33-39). No live native win is proven (same file, Limits).
   `why:` notes/Research/Mining Mouse Ore Strategy Repair.md:33-44, 64-67; notes/Reviews/Mining Ore Planner Repair Review.md:89-90.

**Unsure:**
- The run counts (41 chains, 25,400 score, 3 reshuffles, 171 saves, 162 pairs, 9 ore moves, 44/166 and 32/12 boards, 40 one-blocker states) rest on `lab/reports/mining-mouse-ore-strategy-20261009T1419Z/`, which is not in the repo. I could not check them.
- The driver file `lab/tools/play-native-mining.py` is outside the repo, so the ranking was checked only through the repair and review notes, not the source.
- The "No driver/source/save/UI/process edit" statement is true as of the 1419Z run. I did not check whether `src/mining.rs` changed during the run (the review notes give its hash as `6c59ae0c…`, unchanged by the repair).
- The `save ordinal 79` reshuffle and the note's engine-order statements are not verifiable from the tip.
