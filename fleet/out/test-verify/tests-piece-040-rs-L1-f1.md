<!-- fleet job=test-verify id=tests-piece-040-rs-L1-f1 status=done turns=6 usd=0.0060 tokens(read,write,in,out)=[63441, 22850, 14, 5104] model=claude-haiku-5-5 -->
# high: tests/piece_040.rs:413

**Verdict:** `confirmed` (as a statement about this Rust test). The severity is overstated, because the regression is caught elsewhere in the gate.

**Evidence:**

- The Rust test cannot refute the claim. Walking the claimed change (`src/cooking.rs:18` `PROFILE` 45 → 46, or `src/forging.rs:18` 16 → 17) through `tests/piece_040.rs:413-433`:
  - L414 `assert_eq!(ACCEPTED_COOKING_PROFILE, CHEF_PROFILE)` and L415 `assert_eq!(ACCEPTED_FORGING_PROFILE, BLACKSMITH_PROFILE)`. Both sides come from `src/restoration/piece_040.rs:39-51`, where `ACCEPTED_*` = `CHEF_PROFILE`/`BLACKSMITH_PROFILE`. The file never reads `src/cooking.rs` or `src/forging.rs`. The `#[path]` include at L29-31 only pulls in the restoration module.
  - L416-418 `(ACCEPTED_COOKING_PROFILE, ACCEPTED_FORGING_PROFILE) == (45, 16)` pins only the module's own copy.
  - L421-432 are match arms over `recipe_access`/`wiki_gate_access` and do not touch the services.
  - No other assertion in the test reads the service files. A grep for `cooking.rs|forging.rs|include_str|read_to_string` across `tests/piece_040.rs` finds nothing.
  - So the test passes under the claimed change. The claim holds.
- The test does still pin the module side. Editing `ACCEPTED_COOKING_PROFILE` alone, or `CHEF_PROFILE`/`BLACKSMITH_PROFILE`, fails L414/L415/L418.
- Mitigation exists outside this test. `scripts/pieces/piece_040.py:46-47` pins `const PROFILE: i32 = 45;` / `= 16;` in the real source. Line 619-627 check `needle in source` against `src/cooking.rs` and `src/forging.rs` and emit the `accepted_services_preserved` check. `tests/pieces/test_piece_040.py:276-284` (`test_service_profile_drift_fails`) writes `const PROFILE: i32 = 16;` into a fixture `cooking.rs` and asserts that check fails. So service drift is caught by the Python piece checker, not by the Rust test. I did not confirm that the Python checker runs in the merge gate.

**Minimal fix:** The Rust test's name and its "mirror the live services" wording overclaim. Either rename it to something like `accepted_crafting_profiles_equal_the_recovered_jobs`, or add the file-text canary the reviewer proposed, e.g. `assert!(include_str!("../../src/cooking.rs").contains("const PROFILE: i32 = 45;"));` and the same for `forging.rs` with `= 16;`. Note that the Python checker already covers this, so the canary would be redundant. The finding should be downgraded from high to low.
