<!-- fleet job=test-audit id=tests-piece-054-rs-L1 status=done turns=5 usd=0.0053 tokens(read,write,in,out)=[36878, 15738, 12, 6002] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_054.rs lines 1-254 of 254

Window: `prototype/osfr-tools/tests/piece_054.rs` lines 1-254. I read the test window, `src/restoration/piece_054.rs` (the code under test, all 268 lines), and confirmed the production strings in `src/encounter.rs` (lines 301, 1873-1877, 2457, 2895-2903).

- **[medium] prototype/osfr-tools/tests/piece_054.rs:71 `production_melee_reach_is_still_the_reviewed_three_units` - the name says the production reach is pinned, but the body only greps `encounter.rs` for literal row text and then asserts constants that belong to the restoration module.**
  - Why it cannot catch a regression: the string `"2 => (3.0, 100)"` still matches if that row is no longer the value used for `range` (for example, the table is reordered, or `range` is taken from a different expression). The `"> range"` and `"saturating_sub(last) < 600"` substrings also match elsewhere in the file. Lines 113-115 (`PLAYER_MELEE_REACH == 3.0`, `ENEMY_MELEE_REACH == 2.5`, `MELEE_REPEAT_GATE_MS == 600`) check the restoration module's own constants, which production code does not read. Changing the production reach to 8.0 and leaving the row text intact passes this test.
  - Fix: call the production encounter's attack/range path (or a public helper that exposes its reach) and assert that an 8-unit player hit is refused and a 3.0-unit hit is accepted. If that is not possible, rename the test to say it only checks source text and add a comment that the behavioural gate is not covered here.

- **[medium] prototype/osfr-tools/tests/piece_054.rs:118 `far_hits_are_rejected_at_the_reviewed_boundary` - the name claims production far-hit rejection, but every call goes to `resolve_melee_attack` in the restoration module (`src/restoration/piece_054.rs:233`), which is a separate implementation from `encounter.rs`.**
  - Why it cannot catch a regression: if the production encounter's `distance > range` check were removed or widened, this test would still pass because it never reaches the production path.
  - Fix: add a test that drives the production encounter attack handler at 8.0 and 3.0+1ulp units and asserts that no damage or target-state change occurs. Or rename the test to say it tests the restoration rule.

- **[low] prototype/osfr-tools/tests/piece_054.rs:229 `animation_and_timing_evidence_matches_the_original_client_resources` - `assert_eq!(H2H_ATTACK_01_SLOT, COM_H2H_ATTACK_01_SLOT)` compares an alias with the constant it is defined as (`src/restoration/piece_054.rs:194`).**
  - Why it cannot catch a regression: the alias is a plain `const` copy, so this check only fails if someone changes the alias's right-hand side to a different row. Nothing else is tested by it, so the line adds no evidence about the original resources.
  - Fix: delete the line, or assert the alias's fields against the XML-derived values in the lines that follow, which already exist.

- **[low] prototype/osfr-tools/tests/piece_054.rs:139 `reviewed_capture_distances_are_accepted_and_the_old_reach_would_not_be` - the name says the old reach would refuse these hits, but the body never runs the old reach. It only checks that 2.434 is accepted and 8.0 is refused under the current rule.**
  - Why it cannot catch a regression: a change to the old reach value would not affect any assertion here, so the claim in the name is unverified. Line 154 repeats the 8.0 refusal already checked at line 121.
  - Fix: either rename it to `reviewed_capture_distances_are_accepted` and remove the "old reach" wording, or add a documented constant for the pre-fix reach and assert that `resolve_melee_attack` with that reach would accept 8.0.

- **[low] prototype/osfr-tools/tests/piece_054.rs:93-95 `production_melee_reach_is_still_the_reviewed_three_units` - the check on `"12 => (20.0, 130)"` pins a Wizard damage value that, per the comment, was changed for balance.**
  - Why it is churn, not a missed bug: a balance edit to the damage column breaks a test whose subject is melee reach and ranged-kit separation. The check it needs (that the Wizard row is not in the melee profile) can be made using the reach column only.
  - Fix: assert only the reach column for the ranged rows, for example `"12 => (20.0, "`, so the test stays focused on reach.

No `#[ignore]` or early-return skips were found in the window. The `#[path]` include target `src/restoration/piece_054.rs` exists. The far-boundary float check at lines 132-137 (`3.0` plus one ulp) is sound: I worked through the f32 arithmetic and `sqrt(x*x)` for that value rounds above 3.0, so the test is valid.
