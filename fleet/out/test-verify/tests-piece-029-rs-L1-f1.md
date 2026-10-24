<!-- fleet job=test-verify id=tests-piece-029-rs-L1-f1 status=done turns=8 usd=0.0068 tokens(read,write,in,out)=[102165, 24172, 18, 5525] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_029.rs:257

**Verdict:** `confirmed`

**Evidence:**

- The test body selects `Selection::FixtureGuid(0x0f00_0000_0000_00ff)` at `tests/piece_029.rs:266`. That guid appears nowhere in the fixtures. The only other use is the unasserted vector export at line 732. The foreign-lot row `fixture(CHAIR_A, LOT_B, ...)` pushed at line 259 is never addressed.
- The asserted outcome is `assert_eq!(outcome, Err(Refusal::UnknownFixture))` at line 269. The resolver at `src/restoration/piece_029.rs:286` is `row.lot_guid == lot_guid && row.fixture_guid == guid`. Deleting `row.lot_guid == lot_guid &&` from that arm still returns `UnknownFixture` for 0xff, so this test passes under that mutation.
- No other assertion in the file catches the mutation:
  - `guid_selection_resolves_the_addressed_instance` (209–223) selects CHAIR_B, which exists only in LOT_A, so it is unchanged.
  - `duplicate_guid_in_the_same_lot_is_refused` (273–285) adds a second CHAIR_A in LOT_A. The mutation still yields `AmbiguousSelection`, so it passes.
  - `LOT_B` appears only at lines 46, 259 and 656–660. The 656–660 fixtures feed the vector export at 640–914, which asserts only the table contents (907–908), not outcomes.
  - `0x0f00_0000_0000_00ff` appears only at 266 and 732.
- Result: the lot-scoping clause in the `FixtureGuid` arm can be deleted, and the change that would make a foreign-lot instance selectable, without any assertion in `piece_029.rs` failing.

**Minimal fix:** in the test, push `fixture(CHAIR_B, LOT_B, CHAIR_DEFINITION, CHAIR_ITEM)` and select `FixtureGuid(CHAIR_B)` from `LOT_A`, expecting `Err(Refusal::UnknownFixture)`. Add a positive case selecting `CHAIR_A` with the LOT_B duplicate present, expecting `plan.fixture_guid == CHAIR_A` and no `AmbiguousSelection`. The positive case is what catches dropping the lot filter. Without it, the mutation is caught only indirectly, and only if the foreign guid is the same as an addressed one.
