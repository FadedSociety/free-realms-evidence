<!-- fleet job=bug-verify id=src-restoration-piece-010-rs-L1-f1 status=done turns=5 usd=0.0042 tokens(read,write,in,out)=[47657, 19485, 12, 2556] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_010.rs:461-468`

**Verdict:** refuted

**Severity if confirmed:** n/a. The defect is real as a code-reading observation, but it is test-only. It is not in the shipped server, and nothing in the server reaches it.

**Evidence:**

1. **Not in the module tree.** `src/lib.rs` contains no `restoration` module. `grep restoration` on `src/lib.rs` returns no matches. There is no `src/restoration/mod.rs`. The only inclusion of `piece_010.rs` is `prototype/osfr-tools/tests/piece_010.rs:13-14`: `#[path = "../src/restoration/piece_010.rs"] mod piece_010;`. The `piece_010` hits in `src/` are only doc comments.

2. **No reachable caller.** A repo-wide search of `prototype/osfr-tools` for `TcgMatch`, `from_snapshot` and `MatchSnapshot` finds the definitions in `piece_010.rs` and their uses only in `tests/piece_010.rs`. `piece_043.rs` has its own unrelated `from_snapshot` and a `TcgMatch` enum variant, not this type. No gateway, login, or gameplay dispatch path, and no save load, constructs or restores a `TcgMatch`. The claimed "public reconnect entry point" has no caller in the server.

3. **Claimed mechanics are accurate, but only inside test code.** `piece_010.rs:461-468` does map `(finished=false, winner=None)` to `Phase::Playing`. `snapshot()` at lines 588-595 does write the same fields for a `WaitingToStart` match. `apply_points` at lines 534-538 does refuse only `WaitingToStart`. So the design wart exists, but it is not in a live path.

4. **Existing test coverage.** `tests/piece_010.rs:152-169` checks the start gate on a fresh match, not the restore path. `tests/piece_010.rs:343-352` and `354-383` cover finished and out-of-range snapshots. None of them touch the unstarted-snapshot case.

**Corrected fix:** not needed for this claim. If the module is later registered in `lib.rs` and wired to a reconnect path, the proposed fix (a `started` flag on `MatchSnapshot`) would be the right way to close the gap. Until then it is a hardening note, not a defect in the running server.
