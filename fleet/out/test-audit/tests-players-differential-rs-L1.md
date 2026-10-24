<!-- fleet job=test-audit id=tests-players-differential-rs-L1 status=nothing_found turns=5 usd=0.0077 tokens(read,write,in,out)=[37499, 21487, 12, 9194] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/players_differential.rs lines 1-300 of 300

Reviewed `prototype/osfr-tools/tests/players_differential.rs` lines 1-300 in full, plus `tests/players_reference.rs` (the frozen oracle, lines 1-170) for the join/leave/update_pose semantics the tests depend on. No finding meets the five categories.

What I checked:
- **Oracle independence (cannot-fail, category 1):** `old::PlayerRegistry` is a separate frozen file (`players_reference.rs`, included via `#[path]`), not a call back into `osfr_tools::players`. Expected values are not derived from the code under test, so the differential comparisons can fail when the grid diverges.
- **Randomized test (lines 30-111):** exercises join, leave, pose, and flags-only updates over radius {0, min subnormal, 25, 100, f32::MAX} and cap {0, 1, 4, 64}, comparing full `Result<Vec<OutboundMessage>>` values in order plus session state every step. Non-finite headings are injected (step % 17), so the rejection path is compared too. No `#[ignore]`, no early returns.
- **Neighbourhood canary (lines 113-161):** the `len() == 2` check at 155-160 does fail if the grid only searches its own cell (cells 0 and 1 for x=99 and x=101 with cell size 100), so it is a real canary, not a tautology.
- **Rejected poses (lines 163-207):** the post-rejection joins and `get` comparisons against the oracle (which never saw the rejected calls) would catch partial GUID-index or session insertion before pose validation. Covered.
- **Dense test (lines 209-263):** seed 0 degenerates to an all-zero stream (xorshift fixed point), which the comment states accurately. Seeds 106 and the 0x106 seed still exercise varied ids and positions. Not a skip or cannot-fail.
- **Cutoff test (lines 265-300):** it asserts grid-vs-oracle equality on every `update_pose` in the listed sequence, so a cutoff or tie-break divergence fails. The "Viewer 0 starts with ids 1..=64" comment is an unasserted assumption, but it does not make the test pass vacuously.

Minor notes, not reported as findings (they fall outside the five categories): the comment at line 122 calls `-f32::from_bits(1)` "negative-zero-adjacent" (it is the smallest negative subnormal, not a negative zero), and line 131 duplicates `[f32::MAX; 3]` from line 129.
