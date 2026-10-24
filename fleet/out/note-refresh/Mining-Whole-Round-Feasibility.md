<!-- fleet job=note-refresh id=Mining-Whole-Round-Feasibility status=done turns=11 usd=0.0115 tokens(read,write,in,out)=[202612, 34142, 24, 10471] model=claude-haiku-5-5 -->
# notes/Research/Mining Whole Round Feasibility.md

**Verdict:** minor drift. The engine-side claims (state names, wall cap, board derivation) still hold. The build-failure paragraph and the headline status are stale. The lab artifacts and pin hashes are outside the repo and could not be checked.

**Corrections:**

1. `old:` at `src/mining.rs:1736` and `:1741` — the live module is mid-edit.
   `new:` at `src/mining.rs:1736` and `:1741` in the pinned copy at that time. The live module has since moved on: those lines are now the chain validator's `invalid(...)` returns, the `power` field is a powerup definition (`pub power: u32`), and no `power` identifier is used at those lines.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1734-1741 (the `invalid("mining chain outside board or repeated tile")` and `invalid("mining chain is not orthogonal")` returns); repo:prototype/osfr-tools/src/mining.rs:249-274 (powerup definitions, `pub power: u32` at :274); `grep power` finds no use at :1736/:1741.

2. `old:` Status: **frozen source compiled and driven; the whole-round attempt stops at a dead board —
   `new:` Status: **frozen source compiled and driven; the whole-round attempt completes the quota at the true 250 ms tick (`LevelComplete`) and stops at the 30-minute wall cap under the reconstructed 4 s model —
   `why:` The note's own run table (lines 14-15) and result paragraph (lines 32-37) report `[15, 14]` / `LevelComplete` at 250 ms and the wall cap at 4 s, not a dead-board stop. repo:Tasks.md:204 records the corrected 1127-chain quota completion and says the prior zero-ore reports are superseded. The phase exists at repo:prototype/osfr-tools/src/mining.rs:174 and the wall cap at :98 (`MAX_WALL_MS = 1_800_000`).

**Checked and holding (no change):**
- `Type8Engine::load`, `begin`, `tick`, `handle`, `state` exist (repo:prototype/osfr-tools/src/mining.rs:296, 476, 535, 572, 350).
- Phases `LevelComplete`, `Won`, `Lost` exist (repo:prototype/osfr-tools/src/mining.rs:174-176).
- `OnIdleMsg` and `OnLevelEventMsg 50 x y` are handled (repo:prototype/osfr-tools/src/mining.rs:801, 830).
- Fall row is the bottom of the derived playable rect, with the dropzone one row below it (repo:prototype/osfr-tools/src/mining.rs:1247-1279, 1564). This is consistent with the note's fall-row rule.

**Unsure:**
- Pin hashes (`153d55ca…`, `cba24bbf…`, `25370f04…`) and the `038a135d…` freeze: no hashing tool here. Only the `038a135d…` value appears elsewhere in the repo (`notes/Reviews/Mining Clickable Powerups Review.md:83`, `notes/Reviews/Lead MMO Dispatch Snapshot.json:484`). `153d55ca…` and `cba24bbf…` appear only in this note. The `mining.rs` at tip has changed since the cited copy, so the live hash in the table is historical.
- `lab/reports/mining-whole-round-20261009T1645Z/…`, `drive_mining_feasibility.py`, `test_settle_model.py`, and `lab/tools/play-native-mining.py` (planner `PLAYABLE_MAX = 10`) are not in the repo tree, so the artifact paths and planner constants could not be verified.
- Harness build success ("the actual Rust engine compiled and ran") and the 1500-chain / 60 s defaults rest on lab files I could not read.
