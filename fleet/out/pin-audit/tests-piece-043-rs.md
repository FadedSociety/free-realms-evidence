<!-- fleet job=pin-audit id=tests-piece-043-rs status=nothing_found turns=3 usd=0.0019 tokens(read,write,in,out)=[9627, 9822, 8, 1192] model=claude-haiku-5-5 -->
# tests/piece_043.rs

No findings in `prototype/osfr-tools/tests/piece_043.rs` for the screened lines (150, 155, 156, 167, 168, 200).

- **150, 155, 156 (`ledger_rejects_a_replayed_instance`):** the 60 is the test's own input, `ValidatedOutcome::tcg_match(77, OutcomeResult::Completed { xp: 60 })`. The XP curve is `fixture_curve()`, which the test defines itself as 100 XP per level (line 48, labelled "synthetic fixture, not recovered data"). No data file is read.
- **167, 168 (`ledger_is_job_scoped_and_rejects_cross_job_outcomes`):** the 20 is the test's own `Completed { xp: 20 }` input on lines 164-165. Not from data.
- **200 (`ledger_unlocks_each_milestone_once_and_respects_the_cap`):** `100 * 25` is 25 instances, each granting the test's own `xp: 100`, summed. Not from data. The `MAX_JOB_LEVEL` cap used on line 198 is a code constant, and line 202 hard-codes 20 which is a level-cap constant, not a data-file tunable.

None of these values equals a shipped data-file field. They are fixtures the test sets up, so they are not pinned tunables.
