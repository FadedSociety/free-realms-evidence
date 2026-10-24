<!-- fleet job=note-refresh id=Mining-Mouse-Ore-Strategy-Repair status=done turns=5 usd=0.0075 tokens(read,write,in,out)=[41865, 27748, 12, 7300] model=claude-haiku-5-5 -->
# notes/Research/Mining Mouse Ore Strategy Repair.md

**Verdict:** minor drift. The core repair claim holds: the mining planner is the `rank()` change described, and the driver is still at `4c41fa64…` (no later edit in the notes). Two details are now wrong: the diff size, and the harvesting adapter hash, which has since moved.

**Corrections:**

1. `old:` **+32/-2, entirely inside `find_path`'s nested `rank`** (lines 297-299).
   `new:` **+34/-2, entirely inside `find_path`'s nested `rank`** (lines 297-299).
   `why:` repo:notes/Reviews/Mining Ore Planner Repair Review.md:21-22 measured the preserved 735f vs current 4c41 copies with `git diff --no-index` as "1 hunk, 34 insertions, 2 deletions", inside `find_path`'s local `rank()`. The same review cites the same `driver-planner.diff`, so the note's "+32" is the miscount.

2. `old:` (`lab/tools/play-native-harvesting.py` `df061eb8…`). Private proof:
   `new:` (`lab/tools/play-native-harvesting.py` `df061eb8…` at this repair; superseded by `7d256a4f…`, see [[Harvesting Produce Planner]]). Private proof:
   `why:` repo:notes/Research/Harvesting Produce Planner.md:3-4 records the adapter moving `df061eb8…` -> `7d256a4f…` in a later repair, and line 7-8 says the adapter's `MINING_DRIVER_SHA256` pin is still `4c41fa64…`. So the mining-side claims in this note still hold, but the adapter hash it names is no longer current.

**Unsure:**
- The `find_path` line numbers "297-299" cannot be checked: the driver `lab/tools/play-native-mining.py` is not in the repo (no `lab/` directory at the tip), so the file, the hashes and the DFS constants could not be read directly. The only in-repo mirror is the Rust test model `prototype/osfr-tools/tests/mining_lifecycle.rs:207-244`, which has `MAX_PATH_LEN = 12`, `NODE_BUDGET = 50_000` and the same tuple-shaped `rank` (`collect_now` first, then helped, cleared, remaining, length, depth). That agrees with the note's description of the ranking, but it does not confirm the Python line numbers.
- The 44/44 board counts, the self-test counts (14/14, 13/13) and the probe results come from private logs. The review note agrees with them (Ore Planner Repair Review.md:41-62), so I have not flagged them.
- The note's "Implemented repair, 2026-10-09" and timestamps are historical and were not contradicted.
