<!-- fleet job=test-verify id=tests-piece-042-rs-L1-f1 status=done turns=7 usd=0.0078 tokens(read,write,in,out)=[91079, 29704, 16, 6386] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_042.rs:269-270

**Verdict:** `confirmed`

**Evidence:** I tried to refute this and could not. The two assertions cannot fail on any XP-related change, and nothing else in the suite catches an added XP field.

1. **The assertions are tautological.** `XpCurve` has exactly one variant, `Missing` (`src/restoration/piece_042.rs:61-64`). `tests/piece_042.rs:269-270` asserts `postman.xp_curve == XpCurve::Missing` and `soccer.xp_curve == XpCurve::Missing`. Both job rows are hard-coded to `XpCurve::Missing` (`src` lines 594 and 617). No runtime value of the field can differ from what the assertion expects.

2. **Adding XP data still passes the test.** Suppose someone adds `pub xp_thresholds: &'static [u32]` to `JobProgression` (src line 155) and fills in real numbers for POSTMAN/SOCCER_STAR. The test does not construct `JobProgression`, so it still compiles. Lines 269-270 still pass. The other assertions in `progression_does_not_invent_experience_or_unlock_quest_ids` (lines 271-275) cover `unlock_quest_ids_recovered`, two `*_RECOVERED` constants, `MAX_JOB_LEVEL` and `NON_MEMBER_JOB_LEVEL_CAP`. None of them looks at XP. `validate()` (src 666-727) has no XP check. The only other XP-related hits in `tests/piece_042.rs` are the imports and the two lines above.

3. **The Python gate does not close the gap.** `tests/pieces/test_piece_042.py:202-214` only flips the Rust boolean `XP_CURVE_RECOVERED` and checks that the checker rejects it. `scripts/pieces/piece_042.py:404` checks only that boolean. `scripts/pieces/piece_042.py:860` hard-codes `"numeric_curve_recovered": False`, so it never reads the Rust struct. Adding XP fields with the boolean left at `false` passes the Python suite too.

**Minimal fix:** Replace the two tautological lines with an exhaustive destructure of the struct, with no `..`, so that any new field breaks compilation of the test:
`let JobProgression { profile_id: _, name: _, name_id: _, description_id: _, profile_type: _, hint_id: _, icon_id: _, members_only: _, trial: _, classification: _, kit_class_id: _, kit_class_name_id: _, creation_kit: _, milestones: _, gates: _, questline: _, xp_curve: _, unlock_quest_ids_recovered: _ } = postman;`
Also assert that the `XpCurve` debug name is `"Missing"` in every row, or add a second variant and a numeric field so the row-level check has something to fail on.
