<!-- fleet job=note-refresh id=Mining-Focused-Ore-Strategy status=done turns=6 usd=0.0059 tokens(read,write,in,out)=[57458, 20944, 14, 5425] model=claude-haiku-5-5 -->
# notes/Research/Mining Focused Ore Strategy.md

**Verdict:** minor drift. The code paths, constants and semantics the note relies on still exist as described; one path:line citation has moved.

**Corrections:**

- `old:` `(-500 = `COLLECTABLE_SCORE`, `mining.rs:99/1275`)`
  `new:` `(-500 = `COLLECTABLE_SCORE`, `mining.rs:117/1594`)`
  `why:` `prototype/osfr-tools/src/mining.rs:117` is now `const COLLECTABLE_SCORE: u32 = 500;`. The score add that the note's `collect_fall` discussion refers to is at `mining.rs:1594` (`.checked_add(COLLECTABLE_SCORE)`), and the `OnLevelEventMsg/21/500` emit is at `mining.rs:1610`. `mining.rs:1275` is now inside `dropzone` bounds code (`Ok(Bounds { left: min_x, ... })`) and has nothing to do with the score.

**Checked and still holding (no edit needed):**
- `validate_chain`, `gravity`, `collect_fall` exist in `prototype/osfr-tools/src/mining.rs` at 1722, 1502 and 1554. The note's "ported from mining.rs" holds. (`forging.rs` has its own `gravity`/`validate_chain`, which the note does not cite.)
- `TILE_BLOCKER = 800` at `mining.rs:66`. `gravity` skips `TILE_BLOCKER` cells (`mining.rs:1517`), which matches the "engine skips blockers in gravity" statement.
- Refill order: `gravity` pops from `tile_queue` first, then if `len < QUEUE_MIN` (50) adds `QUEUE_BATCH` (20) tiles (`mining.rs:1527-1548`, constants at `mining.rs:107-108`). Matches "pop, then `len<50` -> +20".
- `collect_fall` removes the bottom ore, adds the score, emits the quota update, then calls `gravity` a second time and `settle_after_collect` (`mining.rs:1587-1613`). Matches "second gravity/refill per reported fall".
- `Type8Engine` exists (used throughout `prototype/osfr-tools/tests/`).
- `[[Mining Mouse Ore Strategy Repair]]` link target exists at `notes/Research/Mining Mouse Ore Strategy Repair.md`.
- The rank tuple `(collect_now, helped, cleared, -remaining, length, depth)` appears in the Rust test helper `prototype/osfr-tools/tests/mining_lifecycle.rs:210-243`, which is the same shape the note describes.

**Unsure:**
- The driver `lab/tools/play-native-mining.py` (hash `4c41fa64…`) is not in the repo, so I could not check its rank, its `TILE_BLOCKER`-counts-as-remaining behaviour, or its `--self-test` fixture. The mining_lifecycle.rs rank counts any nonzero cell (`!= 0`) as remaining, which is consistent with the note's blocker claim, but that is a test helper, not the driver.
- The Python model code, the "Rust probe blocked, os error 4551" result, the run/report paths under `lab/`, and the shipped-shape blocker counts (0x124 / 1x64 / 4x8) are outside the repo or the tip code and could not be verified.
- The DFS parameters (3..12 tiles, 50 000 nodes in the note's first study; 10k nodes in the follow-up) are model settings; the 50 000 / 12 values match the test helper at `mining_lifecycle.rs:207-208`, but I did not confirm the 10k follow-up figure against anything in the repo.
