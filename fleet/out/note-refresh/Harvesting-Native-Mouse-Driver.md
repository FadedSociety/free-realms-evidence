<!-- fleet job=note-refresh id=Harvesting-Native-Mouse-Driver status=done turns=11 usd=0.0155 tokens(read,write,in,out)=[211655, 42675, 24, 16146] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Native Mouse Driver.md

**Verdict:** badly stale. The border/geometry story was fixed at the tip after this note was written, and the adapter's pins and planner changed later. The file-existence and namespace claims still hold (`FIRST_INSTANCE_ID` = 58_000_001 at `src/harvesting.rs:49`; `validate_chain` at `src/mining.rs:1722`). The `lab/` files cited throughout are not in the repo snapshot, so those claims are checked only against other notes.

**Corrections** (most misleading first)

1. `old:` and a spec of width **10**, height **10**, shape `[1 x 90, 4 x 10]`
   `new:` and a spec of width **11**, height **11**, shape `0` border row/column with 90 playable `1`s at x1..10 / y1..9 and the dropzone row `4` at y10 (the v1 10x10 export is refused)
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:765-767` (11x11), `:774` (`RECONSTRUCTED_BORDER = 1`), `:910-921` (`padded_engine_shape`), `:989-997` (`board_spec` emits it); the pre-border 10x10 export is refused at `:1300-1318`.

2. `old:` playable columns **0..=9**, rows **0..=8**, i.e. a **10x9**
   `new:` the v1 shape gave playable columns 0..=9, rows 0..=8; the tip pads it to playable columns **1..=10**, rows **1..=9** (still a **10x9** rectangle)
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:770`, `:774`, `:910-921`; `notes/Research/Harvesting Border Fix.md:19-23`.

3. `old:` with the dropzone row at index **9** inside the 10x10 grid.
   `new:` with the dropzone row at index **10** inside the 11x11 padded grid.
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:767`, `:769` ("the tenth row of the padded grid (index 10) is the dropzone row"), `:918`.

4. `old:` **Potential native border-compatibility issue (flagged, not patched).**
   `new:` **Border-compatibility issue (resolved at tip by padding; native acceptance still open).** The v1 package's playable area started at column 0 and row 0; the tip's writer keeps row 0 and column 0 empty.
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:762-774` (comment cites the `while (... > 0)` loops); `:1294-1318` (`validate_border` refuses playable codes on index 0). Gate is wired at `repo:prototype/osfr-tools/src/gameplay.rs:1011-1013`.

5. `old:` 2. **Zero-edge border compatibility.** Flagged above with the exact `Grid.as` loops; a spec padding or
   `new:` 2. **Zero-edge border compatibility.** Resolved at tip: the spec is padded (see the two lines below), so the open item is only the native check. Padding was originally a root decision; it is now in `src/harvesting.rs`.
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:774`, `:910-921`, `:1300-1318`; `repo:prototype/osfr-tools/tests/harvesting_border.rs` (border vectors).

6. `old:` `735f8eceb1f14e4decbf95d3ae88c9ff55d389799cb8b0a06c6c47cf3f3db594`, and it is what this adapter binds.
   `new:` `735f8eceb1f14e4decbf95d3ae88c9ff55d389799cb8b0a06c6c47cf3f3db594` was the frozen successor when this note was written. The adapter was later re-pinned to the mining driver `4c41fa64…` (native-active), and the adapter itself became `7d256a4f…` after a planner change.
   `why:` `notes/Reviews/Mining Ore Planner Repair Review.md:3-7`, `:60-68` (`MINING_DRIVER_SHA256 = 4c41fa64…`, `MINING_DRIVER_PREVIOUS_SHA256 = 735f8ece…`); `notes/Research/Harvesting Produce Planner.md:3-8` (adapter now `7d256a4f…`, mining driver `4c41fa64…`).

7. `old:` the current run reports `matches_frozen: true`.
   `new:` the current self-test reports `frozen_sha256=4c41…` with `previous_task_pinned_sha256=735f…` and `previous_copy_matches=true` (13/13 ok).
   `why:` `notes/Reviews/Mining Ore Planner Repair Review.md:60-62`.

8. `old:` and prefers the mining driver's heuristic (a chain directly below an unmet collectable).
   `new:` and ranks chains by `collect_now` (a path that clears every blocker below an unmet produce so it reaches the bottom row), then measured progress for unmet goals, then length and depth. The below-collectable rule is no longer the rank.
   `why:` `notes/Research/Harvesting Produce Planner.md:15-27`.

9. `old:` `geometry 10x10 / playable 0..9 x 0..8 / dropzone 9`
   `new:` `geometry 10x10 / playable 0..9 x 0..8 / dropzone 9` (v1 content, historical log; the current v2 content gives 11x11 / playable 1..10 x 1..9 / dropzone 10)
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:765-770`; `notes/Research/Harvesting Border Fix.md:79`.

   (Also the content path at line 24 is superseded: `opening-harvesting-native-20261009T142624Z/content/` is the current immutable package. Evidence: `notes/Reviews/Delegated Task Readiness.json:117`, `notes/Reviews/Lead MMO Dispatch Snapshot.json:355`. No v2 hash was found in the notes, so I did not supply one.)

**Unsure:**
- `board_bounds` (cited as `src/mining.rs::board_bounds`): no function by that name exists in `src/mining.rs`. `harvesting.rs:1107` mirrors "the shared engine's `board_bounds`", and the bounds logic sits near `mining.rs:1212-1260`. I could not confirm the name.
- Client citations (`Grid.as` lines 248/249, 1103, 1119, 1235, 1386..1433; `GameData.as` `nTILE_SIZE = 40`): the client decompile did not return `checkFalls`/`addColumnFall` or `nTILE_SIZE`, so I could not check them.
- `lab/tools/play-native-harvesting.py`, the self-test's "13 checks", the content and movie hashes, and the reports under `lab/`: `lab/` is absent from the repo snapshot. I only have other notes' reports of these (13/13 ok in the Review).
- The "Owned paths" note that `src/harvesting.rs` is untouched was true only when the note was written; the later Border Fix edited it (see correction 5).
