<!-- fleet job=test-verify id=tests-piece-065-rs-L1-f1 status=done turns=6 usd=0.0068 tokens(read,write,in,out)=[55252, 22323, 14, 6941] model=claude-haiku-5-5 -->
# high: tests/piece_065.rs:447-450

**Verdict:** refuted (as stated). The named regression, a change that lets a preserved run satisfy the gates, is caught by tests that always run. The silent skip is still a real hygiene defect, and there is one narrower gap (aggregate `accepted`), but the claim's "only guard" premise is wrong.

**Evidence**

1. The skip is real. `prototype/osfr-tools/tests/piece_065.rs:447-450` returns early when `../../../lab/reports` cannot be read, and `:469-472` returns when no `piece-065-*/replay-transcripts` exists. The repo root listing has no `lab/` directory, so the test body never runs in this checkout.

2. Gate-level overclaims are caught unconditionally. The preserved-run test only grades by calling `evaluate()` and asserting `!report.accepted`. Each gate's outcome is pinned by always-running tests on mutated synthetic replays:
   - Combat: `GateOutcome::Failed(_)` at line 259, `detail(...).contains("stationary")` at line 261.
   - Boss: `GateOutcome::Failed(_)` at line 300, `NotEvidenced(_)` at line 311.
   - Rewards: `GateOutcome::Failed(_)` at line 326, `contains("loss")` at line 328, `contains("39/47")` at line 339.
   - Exit: `GateOutcome::Failed(_)` at lines 370 and 381.
   - Reconnect: `NotEvidenced(_)` at lines 391 and 412, `Failed(_)` at line 402.

   If a change flips a preserved run's gate outcomes to `Passed`, these fail. The claim's "this is the only guard in the file" is therefore false.

3. Narrow residual gap. `prototype/osfr-tools/src/restoration/piece_065.rs:943` computes `accepted = gates.iter().all(|r| r.outcome.passed())`. The only always-running assertion on `accepted` is line 112, which asserts `true` for the all-pass synthetic replay. Nothing always-running asserts `!accepted` when a gate fails. A change such as `let accepted = true;` or dropping a gate from the `all()` would pass every unconditional test. That is an aggregate-logic overclaim, not "a preserved run satisfies every gate," so it does not rescue the named claim. It is caught only by the vacuous test.

**Recommended follow-up (not a refutation of the named regression)**
- Add an always-running negative, e.g. `assert!(!evaluate(&single_session_replay()).accepted)`, so the aggregate is guarded regardless of `lab/reports`.
- Make the missing-fixture case explicit (`#[ignore = "requires lab/reports/piece-065-*"]`) so a green run does not imply preserved-run grading happened.
- Severity is closer to medium than high, since the unconditional gate tests carry most of the guard.
