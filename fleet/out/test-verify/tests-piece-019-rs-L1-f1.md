<!-- fleet job=test-verify id=tests-piece-019-rs-L1-f1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[18243, 11323, 10, 2381] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_019.rs:153

**Verdict:** `refuted`

**Evidence:** The claim's walk-through is wrong. It assumes that if `commit` wrote the record before the finished-check, the later `commit(session, 10)` at line 186 would return `Ok(Recorded)`. It would not.

Mutation: `commit` inserts `(guid "A", value)` into the board before the `if !active.finished` check (`src/restoration/piece_019.rs:224`), and does not set `committed`.

- Line 170 (`commit(7, 999)`): `UnknownSession` is returned before any write. Passes.
- Line 176 (`commit(session, 10)` while unfinished): the mutation writes A=10, then returns `SessionNotFinished`. Passes.
- Lines 181 and 183: `InvalidValue` is returned at line 213, before any write. Passes.
- Line 186 (`commit(session, 10)` after finish): the board already holds A=10. In `commit`, the match at lines 229–233 gives `Some(record) if !active.kind.is_better(10, 10)`. For `ScoreKind::Points`, `is_better` is `10 > 10`, which is false, so the outcome is `CommitOutcome::KeptBest`. The test asserts `assert_eq!(store.commit(session, 10), Ok(CommitOutcome::Recorded));` (line 186). `KeptBest` ≠ `Recorded`, so the test fails.

A variant that also sets `committed` early fails at line 186 with `SessionAlreadyCommitted`. A variant that writes before the range check (lines 213–215) fails at line 186 too, because the line 183 write leaves the stored value at 10,000,000,000, so `is_better(10, …)` is false again and the outcome is `KeptBest`.

So the test's own line-186 assertion is state-sensitive: it fails whenever the board already holds the same value from a refused commit. The reviewer's "every assertion still passes" is false. The extra `rows(BOARD)` checks in the proposed fix would be a stronger and clearer canary, but the existing test already catches the regression described.</result>
