<!-- fleet job=test-verify id=tests-piece-045-rs-L1-f1 status=done turns=7 usd=0.0075 tokens(read,write,in,out)=[83480, 31267, 16, 5497] model=claude-haiku-5-5 -->
# high: tests/piece_045.rs:304

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. Walking the test against the proposed mutations:

- **`category_id` 101 → 111 for Hats (`src/restoration/piece_045.rs:58`).** The only assertion that touches `category_id` is the loop at `tests/piece_045.rs:304-311`:
  ```rust
  assert_eq!(
      cosmetic_slot(row.slot).map(|found| found.category_id),
      Some(row.category_id)
  );
  ```
  Both sides read the same `COSMETIC_SLOTS` entry (`cosmetic_slot` is `COSMETIC_SLOTS.iter().find(...)`, line 120-121), so the mutated value compares equal to itself and passes. The category-string asserts at 312-317 check only `.category`, never `.category_id`. Nothing else in the repo tests references `category_id` for this module. `src/restoration/piece_045.rs` never reads `category_id` outside the struct and table, so no behavioural test would notice either.
- **`recovered_rows` change (e.g. Hats 7522 → 1).** The only check is `row.recovered_rows > 0` at line 305. No assertion pins 7522, 3189, 8254, 5873, 5867, 2301 or 93, so the mutation passes.
- **`name_id` change.** Only `> 0` is checked (line 305). Not pinned.
- **Slot 2 (Gloves).** There is no `cosmetic_slot(2)` assertion at all. Lines 312-317 cover slots 1, 3, 4, 5, 6 and 17 only. Its category string and pairing are checked only by the self-referential loop.
- **Ignored private gate (`tests/piece_045.rs:647-`).** It is `#[ignore]` with a stated reason, so it does not count. In any case it checks only `row.appearance.slot == row.slot` and `tint >= 0`, not the table's category or count fields.
- **Other test files.** A repo-wide search for `category_id|recovered_rows|COSMETIC_SLOTS|cosmetic_slot` finds no test that pins these values. The only `category_id` hits in tests are unrelated (`tests/account.rs` uses different identifiers).

Also, the claim's description of the `> 0` checks and the category-string coverage (slots 1, 3, 4, 5, 6, 17) matches the file exactly.

**Minimal fix:** replace the self-referential loop with literal pins, and add a canary on the counts:
`assert_eq!(COSMETIC_SLOTS.map(|r| (r.slot, r.category_id, r.category, r.name_id, r.recovered_rows)), [(1,101,"Hats",23319,7522),(2,102,"Gloves",23320,3189),(3,103,"Shirts & Dresses",23321,8254),(4,104,"Pants",23322,5873),(5,105,"Shoes",2482,5867),(6,106,"Miscellaneous",23324,2301),(17,201,"Costumes",5273,93)]);`
A tighter option is to derive these tuples from the pinned `ClientItemDefinitions.json` in the private-gate test, but the literal above already closes the gap the first-pass reviewer named.
