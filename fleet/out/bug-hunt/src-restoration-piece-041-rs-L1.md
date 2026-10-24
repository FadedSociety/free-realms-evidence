<!-- fleet job=bug-hunt id=src-restoration-piece-041-rs-L1 status=done turns=6 usd=0.0059 tokens(read,write,in,out)=[61049, 24139, 14, 4518] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_041.rs lines 1-420 of 420

Window `piece_041.rs` 1-420 read in full. No client-reachable defect found. The module is not registered in the server: the only non-test reference to it is the `#[path]`-less doc mention in `scripts/pieces`, and `src/` contains no caller of `DriverProgression`, `ValidatedOutcome` or `credit` (only `tests/piece_041.rs` includes it). So no packet path reaches `credit`, and the panic/overflow/unbounded-growth candidates are unreachable in practice. I checked them and dropped them:
- `credit` (321-344): `saturating_add` on `u32`, `BTreeMap` growth only per validated outcome, and the mutation before `AtMaxRank` is intended and tested (`max_rank_credits_but_does_not_advance`).
- `unlocked`/`unlocks_at`/`unlock_table`: no indexing, no arithmetic on client values.
- Table sizes (20 and 19 rows, rank 9 absent) match the doc comments and tests.

**[low] prototype/osfr-tools/src/restoration/piece_041.rs:408-417 - `validate()` is documented as "Structure checks over the recovered tables" but only checks that each `DRIVER_JOBS` entry's activity maps back to its own job id; it never inspects `KART_DRIVER_GEAR`, `DEMO_DERBY_DRIVER_GEAR`, or `CAPTURED_VEHICLES`.**
- Failure scenario: someone edits a gear row (duplicate rank, rank 0 or 21, or a row count change) and `validate()` still returns `Ok(())`. The in-tree tests in `tests/piece_041.rs:157-183` catch this, so only the doc-to-code contract is wrong.
- Reach: none. `validate()` has no non-test caller in `src/`, and no client input is involved.
- Fix: either narrow the doc comment to "checks the job-to-activity mapping", or add loops that check each gear table's ranks are strictly increasing and within 1..=MAX_JOB_RANK.

Also noted but not a defect: the module doc (lines 37-38) says the ledger "refuses to advance once the profile rank is at the cap", but `credit` still adds stars to `total_stars` at the cap (the tested behaviour). "Advance" is read here as the rank, which `credit` never changes, so I did not report it.
