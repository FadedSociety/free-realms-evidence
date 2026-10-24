<!-- fleet job=test-verify id=tests-mining-powerups-rs-L1-f2 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[7550, 7018, 8, 2521] model=claude-haiku-5-5 -->
# high: tests/mining_powerups.rs:607

**Verdict:** `refuted`

**Evidence:**

The claim is that the test cannot catch a regression where `shuffle_placements` returns wrong destinations. The coordinate assertions catch that, and I checked them against the real function in `src/mining.rs:2034-2073`.

- **Line 617 (distinct fixture):** `assert_eq!(distinct, vec![positions[0], positions[1], positions[2]]);`. Walking `[401,402,403]` through the code: each index's value is `drawn[(i+2)%3]`, and each destination's grid value differs from it, so no fold happens and every mover stays on its own slot. The assertion matches the code.
- **Line 626 (equal fixture):** `assert_eq!(equal, vec![positions[0], positions[2], positions[1]]);`. Walking `[401,401,402]`: index 1 folds onto slot 2 (`slots[2] = slots[1]`), and index 2 hits the `index+look >= n` branch and reverts to `slots[2]`, which is `p1`. The result is `[p0, p2, p1]`, which matches the assertion.

So a regression that returns the wrong destinations on these fixtures fails the test. Examples: an identity return fails line 626, and dropping the fold fails line 626.

The `*_result` blocks (618-621, 627-632) are indeed tautological. That is a real quality issue, but it does not make the test unable to catch the named regression. The claim's own description concedes the coordinate asserts exercise the function.

The strongest form of the claim is that some wrong-destination regressions survive. That is possible, for example one confined to the all-equal wrap path, but it is a coverage gap rather than the claimed "cannot catch" defect. The end-to-end test `runtime_shuffle_folds_equal_neighbours_the_as2_way` (lines 572-604) also replays through `engine.handle` and checks board values after the fold, so it adds further coverage.

**Note:** the `*_result` blocks should still be cleaned up (or derived from `shuffle_placements`), and a third all-equal fixture would close the gap. Those are hardening suggestions, not a refutation-proof defect.
