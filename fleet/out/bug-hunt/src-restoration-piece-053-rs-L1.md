<!-- fleet job=bug-hunt id=src-restoration-piece-053-rs-L1 status=nothing_found turns=4 usd=0.0052 tokens(read,write,in,out)=[19769, 17994, 10, 5524] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_053.rs lines 1-344 of 344

## Window: `prototype/osfr-tools/src/restoration/piece_053.rs` lines 1-344 (read in full)

No defects I can tie to a line with a client-reachable path.

**Reach:** `piece_053.rs` is not wired into production. `search` finds no `mod piece_053` registration and no caller of `AggroActor`, `rejection_for`, `disengage_reason` or `TargetCandidate` outside the module itself. The only includes are `tests/piece_053.rs` (via `#[path]`) and the Python checker. No client packet can reach these functions, so even a real arithmetic fault here would not be remotely exploitable today.

**Checked and cleared (in case a later window or the lead wants them):**
- **Division by zero:** `step_toward` (271-276) divides by `delta`, and `horizontal_heading` (342-343) divides by `delta`. Both are guarded. `close_in` returns early at `delta <= AGGRO_MELEE_REACH` (239-241), and `return_home` only steps when `delta > AGGRO_HOME_EPSILON` (258).
- **Stop-margin underflow:** in `close_in`, `delta - AGGRO_STOP_MARGIN` (246) is always above 0.1, because `delta > 2.5` at that point.
- **Non-finite input:** NaN/inf candidate or actor positions are rejected before any division or sort (`valid_position` at 170, 289, 317). The `partial_cmp(...).unwrap_or(Equal)` sort (196-199) therefore never sees NaN.
- **Huge finite coordinates:** squared distances overflow to inf, which fails the range test (301, 326). No panic.
- **Time:** `now_ms.saturating_sub` (175) and the clamp `elapsed_ms.min(AGGRO_STEP_CLAMP_MS)` (245, 257) prevent underflow and runaway steps.
- **Atomicity:** `tick` writes `last_tick_ms` (179) before the phase handler, but no handler has a fallible step after mutation, so there is no partial-state path.
- **Doc vs. behaviour:** the tick-interval, first-tick, disposition, dead-before-zone and TargetGone-for-non-finite claims match the code.

**Not reported (not a defect I can defend):** `horizontal_heading` (342-343) divides X/Z by the full 3D `delta`, so the emitted heading is not unit length when Y differs. The doc calls it "the horizontal direction", and the recovered opcode 125 consumer uses `atan2(X, Z)`, which is scale-invariant. No effect on behaviour.
