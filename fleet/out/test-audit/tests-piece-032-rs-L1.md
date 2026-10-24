<!-- fleet job=test-audit id=tests-piece-032-rs-L1 status=done turns=6 usd=0.0086 tokens(read,write,in,out)=[78760, 31864, 14, 7645] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_032.rs lines 1-537 of 537

Window `prototype/osfr-tools/tests/piece_032.rs` lines 1-537 reviewed against `src/restoration/piece_032.rs` (RankWindow::for_sets 296-376, JobProgression::build 629-731, cross_check 774-786). Most vectors are sound: I hand-checked the unlock curve, `unlocked_at(15)`, the cross-check sets, the combat window bounds and the ceiling violation against the code, and they hold. The findings below are the real gaps.

- **[medium] tests/piece_032.rs:298 gate_rows_for_a_different_profile_type_do_not_form_a_window - the name says a different-profile gate forms no window, but the body only checks that a group mixing profile types is refused.**
  - Why it cannot catch a regression: the body (299-309) passes `groups = [(3,3),(3,13)]` and expects `MixedGateTypes { group_id: 3 }`. In `for_sets` (src 327-331) that error fires before the `if !found { continue; }` skip (src 357-359) or the `gate.profile_type != profile_type` filter (src 339-341) is reached. Removing the `continue` on a set with no matching-type gate, or making a single-type foreign-profile set produce a window, still passes this test.
  - Fix: add a case with one set whose only gate has profile type 10 (e.g. `requirements = [requirement(13, 6, 10, 9)]`, `groups = [(3,13)]`, `sets = [(3,3)]`) and assert `for_sets(..., COMBAT_PROFILE_TYPE)` returns `Ok(vec![])`. Keep the mixed-group assertion as a second case.

- **[medium] tests/piece_032.rs:534-536 recovered_constants / shipped-catalogue block - the final assertions cannot fail and do not reference the code under test.**
  - Line 536 `assert!(BTreeMap::from([(1, 1)]).contains_key(&1));` tests the standard library, not the module. Line 535 `items.len() < 65_536` hard-codes the literal instead of comparing against `MAX_ROWS` (src line 58), so a change to the cap in the module is never caught.
  - Why it cannot catch a regression: changing `MAX_ROWS` or the `TooManyRows` check in `JobProgression::build` (src 634-639) still leaves these lines passing.
  - Fix: delete line 536. For 535, assert that `JobProgression::build` rejects an over-cap input (e.g. `MAX_ROWS + 1` copies of one row) with `TooManyRows { table: "ClientItemDefinitions", rows: MAX_ROWS + 1 }`, and that `MAX_ROWS` equals the documented 65_536.

- **[low] tests/piece_032.rs:339 id_pair_tables_parse_and_reject_unknown_headers - `bad.is_err()` accepts any failure.**
  - Why it cannot catch a regression: if `parse_id_pairs` starts rejecting valid rows with `MalformedRow`, or returns a different header error, the assertion still passes. The name claims it rejects an unknown header, and the body does not check which error.
  - Fix: `assert!(matches!(bad, Err(ProgressionError::HeaderMismatch { table: "RequirementGroups" })));`, matching the form used at line 126-129.

- **[low] tests/piece_032.rs:343 recovered_constants_keep_original_and_community_labels_apart - the name claims a separation that the body never checks.**
  - The body only pins literal values (lines 344-351). Nothing checks that `BRAWLER_TRAIT_RANKS` (community, src line 54-56) is not presented as recovered, so the comment at line 350 is the only enforcement. Moving the community ranks into a recovered-labelled constant would still pass.
  - Fix: either rename it to `recovered_constants_match_their_pinned_values`, or add a check on the provenance API the module exposes (for example, that the community ranks are only reachable through the cross-check input and not through `observed_ranks()`).

- **[low] tests/piece_032.rs:467-485 private_brawler_tables_match_the_preserved_lab_inputs - exact counts (447 rank-1 rows, 907 total weapon rows, 17 development items, 11 rank-20 rows, 6 unrestricted rows) are pinned to the shipped snapshot, and several restate each other.**
  - Why it matters: unrelated catalogue edits or re-exports change these numbers and fail the test for reasons unrelated to the progression boundaries it is about. Line 485's 907 is the sum of the per-rank buckets at 470 and 469 plus the other buckets, so it adds churn without new coverage.
  - Fix: keep the boundary-level assertions (the observed rank set at 468, the cross-check at 464-467, the violation list at 436-439) and drop or relax the raw row counts, or assert the sum against `equipment.values().sum() + unrestricted.len() + development_items.len()` rather than a literal.

Not reported: the ignored test at 372-373 has a reason string and its env-var fixtures are documented in `notes/Research/Pieces/032 Brawler progression.md`, so it is not a silent skip.
