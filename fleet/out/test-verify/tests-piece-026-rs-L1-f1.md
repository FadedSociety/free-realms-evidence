<!-- fleet job=test-verify id=tests-piece-026-rs-L1-f1 status=done turns=9 usd=0.0073 tokens(read,write,in,out)=[103606, 22680, 20, 6934] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_026.rs:762

**Verdict:** `refuted` as stated. The skip is real, but the claim overstates what it hides. The placement, move and conservation logic the claim names is exercised unconditionally by other tests in the same file. One narrow gap remains (see below).

**Evidence:**

1. **The skip is real.** `tests/piece_026.rs:763-765`: `let Some(directory) = std::env::var_os("OSFR_PIECE_026_EVIDENCE_DIR")... else { return; };`. With the variable unset, the test passes without running its body. The claim is right about that.

2. **The gated body's sequence is duplicated unconditionally.** Lines 766-789 do: place CHAIR instance 1 at (400,4,410); move it to (402,4,411) with `tint_id: 7`; place TABLE instance 1; assert `balance(CHAIR)==(4,1,3)` and `balance(TABLE)==(2,1,1)`.
   - `a_repainted_move_commits_and_the_pickup_keeps_the_new_tint` (lines 407-474, no env gate) runs the same chair place and repaint move. It asserts `moved.tint_id == 7` (428), `balance(CHAIR)==(4,1,3)` (432), and reloads the pair to check the new tint (441-450). A move or repaint regression fails it.
   - `placement_and_pickup_conserve_the_owned_pool` (lines 214-280, no env gate) asserts the placement balance `(4,1,3)` (228), the owned/placed totals `(6,1)` and `available==5` (230-231), and the table balance `(2,1,1)` after pickup (272). Conservation regressions on a single definition fail it.
   - `failed_persistence_rolls_the_placement_back` (lines 154-211) covers rollback and conservation, and `placing_a_unit_the_pool_does_not_own_is_rejected` (379-404) covers rejection.

3. **The residual gap.** The only test that has CHAIR and TABLE placed at the same time is the gated one. Line 262 places the table only after the chair is picked up, and line 394 is a rejected placement. So the per-definition balance check `(4,1,3)` and `(2,1,1)` with both definitions placed together runs only when the variable is set. A regression that breaks cross-definition accounting in that concurrent state would pass the default gate. That is a real but narrow gap, and it is not the blanket blindness the claim describes.

4. **The export itself is not a placement check.** The file copies (791-801) and the report only write evidence for the independent checker. Their absence does not hide a placement, move or conservation regression.

**Suggested follow-up (not a confirmed defect):** the claim's fix of `#[ignore]` would not add coverage and would change the skip's visibility only. The narrower fix is to move the 766-789 sequence, with its `(4,1,3)`/`(2,1,1)` asserts, into an unconditional test, and keep only the file writes behind the env var. The silent early return on line 764 is still a hygiene issue worth a visible skip, but it is not a missed regression for the named classes.
