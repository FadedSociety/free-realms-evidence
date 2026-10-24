<!-- fleet job=bug-verify id=src-restoration-piece-043-rs-L1-f1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[10799, 11708, 8, 1754] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_043.rs:528-530,532-533,542-552,538`

**Verdict:** refuted

**Severity if confirmed:** n/a. The code is not in the server build, and no remote input reaches it.

**Evidence:**

1. **Module tree (refutes at step 1).** `piece_043.rs` is not declared in the server module tree. The only include is `prototype/osfr-tools/tests/piece_043.rs:33-35`, which uses `#[path = "../src/restoration/piece_043.rs"] mod piece_043;`. A repo-wide search for `piece_043|ProgressionLedger|LevelCurve` finds the file, its test, `scripts/pieces/piece_043.py`, and notes only. Nothing in `src/` declares it. The note `notes/Research/Pieces/043 Pet trainer and card progression.md:14` says it is "Not registered in `src/lib.rs` (lead-owned)", and line 15 says the test "`#[path]`-includes the module so it compiles before registration". The `src/` search matched `#[path]` declarations only for other pieces (piece_056, piece_025, piece_081, piece_093, etc.), never for 043.

2. **Reachability (would also refute).** `ProgressionLedger::apply` and `LevelCurve::new` have no callers outside the test file. No gateway or gameplay dispatch path reaches them, so a client packet cannot supply the caller-chosen curve or drive `apply`.

3. **The code matches the report.** The mutation order at `piece_043.rs:528-552` is as described: `credited.insert` (528) happens before `curve.required_for(self.level)?` (538), which returns `Err(CurveTooShort)` (`piece_043.rs:322-328`). So the non-atomicity is real in isolation. It is test-only, though, and the issue is a latent hazard in unregistered code, not a live defect.

**Corrected fix:** not needed for this finding. If the module is later registered by the lead, the fix suggested in the report (compute the whole level-up sequence on local copies, or pre-fetch `required_for` before mutating) would be appropriate at that point.
