<!-- fleet job=test-audit id=tests-piece-041-rs-L1 status=done turns=4 usd=0.0049 tokens(read,write,in,out)=[22301, 16740, 10, 5175] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_041.rs lines 1-226 of 226

Window: `prototype/osfr-tools/tests/piece_041.rs` 1-226. I read the test file in full and the code under test in `prototype/osfr-tools/src/restoration/piece_041.rs` (1-420). The `#[path]` fixture exists, so no silent skip. The job identity, activity, progression, and once-only credit tests check real behaviour: the `WrongJob` branch and the `Duplicate` branch both leave state unchanged, and the test asserts that.

- **[high] tests/piece_041.rs:204 `captured_vehicles_match_the_recovered_catalogue_rows` - the name says the loadouts match the catalogue rows, but no catalogue is read or joined anywhere in the test.**
  - Why it cannot catch a regression: the test only compares the `CAPTURED_VEHICLES` literals with themselves and checks that ids are > 0. `src/restoration/piece_041.rs:206-213` defines no catalogue table, and nothing in the test joins on item id, name id, description id or model index (the join described at `src/restoration/piece_041.rs:194-195`). If a loadout's `model_index` or `name_id` drifted away from the catalogue row, every assertion here would still pass.
  - Fix: either rename the test to something like `captured_vehicle_literals_are_pinned` and drop the catalogue claim, or add a check against a catalogue fixture (for example the output of `scripts/pieces/piece_041.py`, or a committed catalogue slice) that asserts each `CAPTURED_VEHICLES` row matches exactly one catalogue row on all four keys.

- **[medium] tests/piece_041.rs:139 `max_rank_credits_but_does_not_advance` - "does not advance" is never checked.**
  - Why it cannot catch a regression: the ledger keeps no rank state (`src/restoration/piece_041.rs:289-293`), and the `AtMaxRank` result always reports `MAX_JOB_RANK` (line 336) rather than the caller's rank. The test asserts only the returned enum, the star total and the credited count. A change that bumps the caller's rank, or starts or stops awarding stars at the cap, would not be caught by the "does not advance" claim. The only thing actually asserted is that stars still accrue at the cap (`total_stars: 2`).
  - Fix: rename to `max_rank_credits_stars_and_reports_cap`, or add a check that the rank the caller holds at the cap is unchanged, for example by having `credit` take and return the rank, or by asserting the `AtMaxRank.rank` value equals the input rank when it is already 20.

- **[low] tests/piece_041.rs:197-199 `gear_class_and_part_class_constants_are_recovered` - the test pins catalogue row counts (450, 609, 586) that the test name does not mention.**
  - Why it cannot catch a regression: these counts are data-corpus facts. Re-exporting the catalogue with a different row count would fail this test even though the class constants and the job behaviour are unchanged. The test is about class ids, so this is churn, not a missed bug.
  - Fix: move the row-count checks into a catalogue test, or assert only the rank and label fields here.

- **[low] tests/piece_041.rs:124 `star_award_is_a_single_byte` - the name claims a single-byte wire format, but the test only compares the constant with `255` and then credits it.**
  - Why it cannot catch a regression: `MAX_STARS_PER_OUTCOME` is `u8::MAX` (`src/restoration/piece_041.rs:85`), so the literal check restates the definition. The byte-width fact is enforced by the type, not by this test. Nothing here checks the packet encoding of `MiniGameStarsEarnedPacket`, which the doc at `src/restoration/piece_041.rs:30` relies on.
  - Fix: rename to `max_star_award_is_u8_max`, or add an encode/decode round-trip for the stars field in the packet module, if one exists, and assert that 255 survives it.
