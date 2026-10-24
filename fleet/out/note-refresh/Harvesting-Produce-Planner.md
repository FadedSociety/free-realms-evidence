<!-- fleet job=note-refresh id=Harvesting-Produce-Planner status=nothing_found turns=13 usd=0.0160 tokens(read,write,in,out)=[352553, 53699, 28, 11489] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Produce Planner.md

**Verdict:** current. Every claim I could check at the tip holds. Most of the note's evidence sits in the private `lab/` tree, which is absent from the repo, so those claims can only be cross-checked against other notes, not against code.

**Corrections:** none.

Checked and consistent:
- **Padded 11x11 shape** ("playable x1..10 / y1..9, dropzone row 10"): `prototype/osfr-tools/src/harvesting.rs:765-774` sets `RECONSTRUCTED_BOARD_WIDTH/HEIGHT = 11`, `RECONSTRUCTED_PLAYABLE_ROWS = 9`, `RECONSTRUCTED_BORDER = 1`. `padded_engine_shape` at `harvesting.rs:910-915` puts the 1s at x/y from the border up, with the dropzone row after them. `notes/Research/Harvesting Native Content v2.md:20-22` agrees.
- **Planner rank is the same as the Mining repair:** `notes/Reviews/Mining Ore Planner Repair Review.md:29` and `notes/Research/Mining Mouse Ore Strategy Repair.md:22-28` describe the same `collect_now, helped, cleared, -remaining, length, depth` order. The note's bottom row `geometry.top + geometry.rows - 1` = 1+9-1 = 9 matches the padded playable rows.
- **Mining driver pin:** `4c41fa64…` is recorded consistently in `notes/Reviews/Mining Ore Planner Repair Review.md:3-4,66` and `notes/Research/Mining Mouse Ore Strategy Repair.md:3-5,57-60`. The note's "pin unchanged" is relative to `df061eb8…`, which is correct.
- **Predecessor state:** `notes/Reviews/Mining Ore Planner Repair Review.md:64-73` says the `df061eb8` adapter's own `rank()` still had the old form. That matches the note's RED (`df061eb8`) column.
- No `lab/` directory exists in the repo, and no other note or code mentions `7d256a4f`. That is consistent with a private lab-only edit.

**Unsure:**
- **Dry-run "identical to the 1337Z baseline"** (`Harvesting Produce Planner.md:53`). The baseline in `notes/Research/Harvesting Native Mouse Driver.md:115` used the v1 content `280f5cd7…` (10x10, unpadded, playable 0..9 x 0..8). The current content is v2 `c08f264e…` (11x11 padded, per `notes/Research/Harvesting Native Content v2.md:15,20`). The note says only "real content shape" and does not name the file, so I cannot tell whether the identical plan `[[2,1],[2,2],[2,3]]` was produced on v1 or v2 geometry. If it was v1, the note should say so.
- **Private evidence** (the `lab/reports/harvesting-produce-planner-20261009T1448Z/` files, the 13/13 self-test, the RED/GREEN table, and the `7d256a4f` hash) cannot be verified from the repo. I found nothing that contradicts them.
- **Side note, not this note's claim:** `notes/Research/Harvesting Native Mouse Driver.md:33-35,115` still describes the 10x9 playable rectangle at 0..8 with no border. That is superseded by the padded v2 shape, so it is stale, but it is outside this note's scope.
