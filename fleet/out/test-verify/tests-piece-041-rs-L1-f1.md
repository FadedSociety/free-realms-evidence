<!-- fleet job=test-verify id=tests-piece-041-rs-L1-f1 status=done turns=7 usd=0.0070 tokens(read,write,in,out)=[102233, 27118, 16, 5150] model=claude-haiku-5-5 -->
# high: tests/piece_041.rs:204

**Verdict:** `refuted` (as worded). The narrow fact is true: the Rust test never reads a catalogue. The claim that drift "would still pass every assertion here" is false, and the catalogue join does exist in the gate.

**Evidence**

1. **The stated drift is caught by the test.** The claim's example is a loadout's `model_index` or `name_id` drifting. For the first loadout, `tests/piece_041.rs:208` asserts `roadster.name_id == 141872`, and `:210` asserts `roadster.model_index == 6`. Changing `CAPTURED_VEHICLES[0]` to `model_index` 7 fails line 210. The zipper (`[4]`) is pinned the same way at `:215-217` (`item_id`, `model_index == 51`, `power_rating == 5`).

2. **The catalogue join is real, in the Python checker.** `scripts/pieces/piece_041.py:335-361` builds `by_id` from the item catalogue. For each of the six slots it requires the loadout's `Unknown3/4/5/2` to equal the expected tuple, and the catalogue row's `NameId`, `DescriptionId`, `Param1` (model index) and `PowerRating` to match too. That is exactly the four-key join the reviewer asks for, so it is not missing from the suite. It is outside the Rust test, and its own tests are `tests/pieces/test_piece_041.py`.

**Residual (real, but not the claimed defect)**

- The name `captured_vehicles_match_the_recovered_catalogue_rows` overclaims. The Rust test cannot detect catalogue drift at all, because the catalogue is not in the crate. That part of the claim is correct.
- Pinning is partial. Slot 0 is pinned on every field, and slot 4 on item, model, power and label. Slots 1, 2, 3 and 5 have no field pinned beyond the `> 0` check at `:220-225`, so a literal change there would pass the Rust test. The Python gate would still catch it.

**Minimal fix (optional):** rename the test to `captured_vehicle_literals_are_pinned`, or add a per-slot `assert_eq!` on `model_index` and `name_id` for slots 1–3 and 5. The catalogue check itself belongs in `scripts/pieces/piece_041.py`, which already does it.
