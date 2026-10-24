<!-- fleet job=test-audit id=tests-job-outfits-rs-L1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[15318, 10418, 10, 2823] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/job_outfits.rs lines 1-64 of 64

Window: `prototype/osfr-tools/tests/job_outfits.rs` lines 1-64. Two of the three test-level concerns below are real gaps in the assertions; the `#[ignore]` on line 32 carries a reason and the private fixture is correctly absent from `repo`, so it is not reported as a silent skip. The code path is `gameplay.rs:4835` (`give_starter_outfit` on unlock), which I read.

- **[medium] prototype/osfr-tools/tests/job_outfits.rs:56-63 private_switching_to_a_bare_job_dresses_it - the "no duplicates" check passes if the re-activation of job 48 does nothing.**
  - Why it cannot catch a regression: the test never asserts that the active profile is 48 after the switch at line 58, nor that `dressed(&g, 48)` is still 3 or more afterward. If the switch-back packet (line 58) is dropped or ignored, the item count stays at `items` and the assertion on lines 59-63 still passes. A regression that makes the job-switch packet a no-op on the second switch would also pass.
  - Fix: after line 58, assert `job(&g) == 48`, then assert `dressed(&g, 48) >= 3` and that the equipped count is unchanged from its value after line 54. Keep the item-count comparison as well.

- **[medium] prototype/osfr-tools/tests/job_outfits.rs:54-55 private_switching_to_a_bare_job_dresses_it - the switch to job 48 is never asserted to take effect.**
  - Why it cannot catch a regression: line 52 checks only that the starting job is not 48, and line 55 checks a lower bound on dressed items. The test never asserts `job(&g) == 48` after the packet on line 54. Any packet that dresses profile 48 without making it the active job would pass the dressing check.
  - Fix: add `assert_eq!(job(&g), 48, "switch to Kart Driver took effect")` immediately after line 54.

- **[low] prototype/osfr-tools/tests/job_outfits.rs:55 private_switching_to_a_bare_job_dresses_it - `>= 3` is a weak, unexplained bound on the starter outfit.**
  - Why it cannot catch a regression: a grant of any three non-zero equipment rows for profile 48, including the wrong items or a partial outfit, would pass. The doc comment says "its starter outfit", which is a specific item set, but the body never compares against it.
  - Fix: derive the expected starter item ids from the content table for job 48 and assert that each one is equipped in profile 48 (or assert equality of the set of equipped item ids with that starter set).

I found no "cannot fail" (self-referential expected value) or name-overclaim issues in lines 1-64. The helper `enter_world` and `wrap` are fine as written.
