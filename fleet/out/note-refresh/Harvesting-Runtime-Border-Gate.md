<!-- fleet job=note-refresh id=Harvesting-Runtime-Border-Gate status=done turns=10 usd=0.0109 tokens(read,write,in,out)=[190538, 36516, 22, 8764] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Runtime Border Gate.md

**Verdict:** minor drift. The gate itself is current: the helper, its two call sites, and the two-test runtime file all match the tip. Only the "(current)" label on the test-count snapshot is stale.

**Corrections:**

- `old:` `## Focused family (current)`
  `new:` `## Focused family (snapshot at the 2026-10-09 receipt; not re-run at the tip)`
  `why:` `prototype/osfr-tools/tests/type8_harvesting_gateway.rs` now defines 14 `#[test]` functions (lines 438 through 1135, none `#[ignore]`), not the 11 the note lists. `tests/harvesting_border.rs` (3 `#[test]`, lines 135/179/207) is also missing from the family list. The note's counts for the other seven files still match the tip (harvesting 17, job_binding 3, review 4, reward_catalogue 4, runtime_border 2, runtime_tiles 3, tile_registration 9). `notes/Autopilot/` and `MODLOG.md` both describe a later 56-test focused run, which fits 53 + harvesting_border 3 and does not include the newer gateway count. Only the label needs changing; the numbers are a dated snapshot.

**Checked and holding (no change):**

- `harvesting::validate_border(shape, width, height)` exists at `prototype/osfr-tools/src/harvesting.rs:1300`. It refuses any code other than `0` or `SHAPE_DROPZONE` (`4`, defined at `harvesting.rs:776`) on x==0 or y==0, with a message naming the index-0 border (lines 1310–1317). It is `pub(crate)`, which matches "no public engine API was added".
- `validate_content` calls it at `harvesting.rs:1104`, before the rectangle and dropzone checks.
- `Gameplay::load` calls it at `src/gameplay.rs:1013–1014`, after the Chef and farming-asset checks and the tile-registration gate (`:1009`), before the reward-definition loop (`:1015`) and `Some(engine)` (`:1023`). The error is built with `invalid()` (`gameplay.rs:346–347`), which is `io::ErrorKind::InvalidData`.
- `tests/harvesting_runtime_border.rs` has 2 tests (`:134`, `:183`). They cover the unpadded eight-kind export, a row-0 rectangle and a column-0 rectangle (all refused with a tree-fingerprint check), and padded writer output, the Mining-only campaign and the no-content legacy campaign (all loaded).
- The `harvesting.rs` source hash `a977c466…` matches the one in `MODLOG.md`. The `Mining` file hash `6c59ae0c…` matches `notes/Reviews/Harvesting Runtime and Border Review.md`.
- `notes/Autopilot/F165.md:137` cites `validate_border` at `src/gameplay.rs:949-954`. That is F165's own old citation and does not appear in this note, so it is not a correction here.

**Unsure:**

- The receipt directory `lab/reports/harvesting-runtime-border-20261009-1428Z/` (with `red-tests.log`, `green-tests.log`, `family.log`) is not in the repo. `lab/reports` is not a directory here, so the RED 1-passed/1-failed and GREEN 2-passed results cannot be confirmed from the tip.
- The sha256 values for `src/gameplay.rs` (`d65f89a8…`) and `tests/harvesting_runtime_border.rs` (`3ce83c9f…`) were not recomputed. The `harvesting.rs` hash matches MODLOG, and the `Mining` and test-file hashes are consistent with the review note.
- The note's `Gameplay::load` location is not cited by line number, so there is no line citation to go stale.
