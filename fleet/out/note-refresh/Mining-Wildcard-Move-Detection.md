<!-- fleet job=note-refresh id=Mining-Wildcard-Move-Detection status=done turns=9 usd=0.0075 tokens(read,write,in,out)=[102955, 23042, 20, 7210] model=claude-haiku-5-5 -->
# notes/Research/Mining Wildcard Move Detection.md

**Verdict:** minor drift. The fix, the helpers, the test file and its vector count (4: one ignored, three default) all match the tip. One statement about `has_move` is incomplete because a later change added a rule the note does not mention.

**Corrections:**

- `old:` `` `has_move` now answers "does a legal three-tile path exist", exactly what `validate_chain` accepts: ``
  `new:` `` `has_move` now answers "does a legal three-tile path exist", which is what `validate_chain` accepts plus one extra rule: any powerup `950..=953` on the board returns `true` at once (the first check in the scan). ``
  `why:` `repo:prototype/osfr-tools/src/mining.rs:2092-2098` (the `TILE_POWERUP_PRESSME..=TILE_POWERUP_SHUFFLE` early return, recovered from `ServerGrid.HasMove()` 203-207). The note's "exactly" is now false. The rule was added by the later clickable-powerup work (`notes/Research/Mining Clickable Powerups Implementation.md:42,81`; `prototype/osfr-tools/tests/mining_powerups.rs:877`).

**Checked and holding:**
- `has_move` is at `mining.rs:2087`. The helpers `neighbour` (`:2121`) and `chain_values_match` (`:2133`) exist. Both are narrow and sit next to it, as the note says.
- The six pairs (`PAIRS`, `:2089`) and the selectable range `400..=499` (`TILE_SELECTABLE_START = 400`, `:64`) match the note. Idle flags are ignored in `has_move`.
- `tests/mining_move_detection.rs` has four vectors: `chain21_snapshot_with_no_legal_path_must_reshuffle` (`#[ignore = "requires private native Mining snapshot"]`, `:166-167`), `wildcard_star_between_two_colours_has_no_move` (`:198`), `wildcard_next_to_a_goal_has_no_move` (`:211`) and `valid_three_tile_paths_keep_the_board_and_ignore_idle` (`:224`). That gives 3 default and 1 ignored, as the note says. The snapshot vector asserts the sha256, all idle flags and `reshuffles == 1`.
- The status "implemented" holds. The call sites are at `mining.rs:441`, `:1677` and `:1809`.

**Unsure:**
- The note says the snapshot vector "reads the live instance id (`18000004`)". The test does not hard-code that value. It reads `instance_id` from the loaded state (`tests/mining_move_detection.rs:149-155`). `FIRST_MINING_INSTANCE` is `18_000_001` (`mining.rs:94`), so the `18000004` figure can only come from the private snapshot, which I could not read.
- The lab paths (`lab/reports/mining-move-detection-20261009-1450Z/`, `lab/runs/client-baseline-20261009T143211Z/`) and the sha256 values (`da3b5b56…`, `6c59ae0c…`) could not be checked from the repo view. The `lab/` listings returned "not a directory", and I had no hashing tool. The Review note (`notes/Reviews/Mining Move Detection Repair Review.md`) also cites the `6c59…` hash, which supports it but is not independent verification.
- The per-command pass counts (`mining` 21, `harvest` family, etc.) are logs I could not open. The only count I cross-checked is the 3+1 for `mining_move_detection`, which matches other notes.
