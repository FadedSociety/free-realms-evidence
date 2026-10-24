<!-- fleet job=bug-verify id=src-restoration-piece-052-rs-L1-f1 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[31201, 21133, 10, 2515] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_052.rs:395-400

**Verdict:** refuted (step 1: the code is not in the real server build)

**Severity if confirmed:** n/a. The defect is test-only, so it cannot reach a player.

**Evidence:**

1. **Module tree.** `prototype/osfr-tools/src/lib.rs` declares modules such as `abilities`, `activity_portal`, `enemies` and `encounter`, but has no `mod restoration;`. A search of `prototype/osfr-tools` for `mod restoration|#\[path|piece_052|PatrolController|PatrolRoute` finds no `mod` declaration for `piece_052` anywhere in `src/`. Other restoration files are pulled in only through `#[path]` in `src/abilities.rs:15` (piece_056), `src/gameplay.rs:59` (piece_077) and `src/bin/osfr-terrain.rs:8` (piece_098). `piece_052.rs` is included only by `prototype/osfr-tools/tests/piece_052.rs:34-36` (`#[path = "../src/restoration/piece_052.rs"] mod piece_052;`).
2. **Reachability.** Nothing in the server calls `PatrolController`, `PatrolRoute` or `tick` from a packet handler, a save load or `src/`. The only hits are the file itself and its test. The reviewer's own note agrees: `notes/Reviews/Delegated Task Readiness.json` and `notes/Research/Pieces/052 Enemy patrol and idle.md:99` list "register `mod piece_052;` (and the `restoration` module) in `src/lib.rs`" as a missing gate that the lead has not yet done.
3. **Failure mechanism (not needed for the verdict).** The arithmetic in `piece_052.rs:395-415` looks plausible: the step scale is applied to all three axes, and the arrival snap at line 396 moves the position to the target. But this only matters once the module is wired in, and it is not wired in today.

**Corrected fix:** not applicable to the shipped server. If `piece_052` is registered later, apply the reviewer's fix (snap only when `full <= max_step`, or reject steep legs at validation) and add a regression test that does not depend on the `#[path]` include.
