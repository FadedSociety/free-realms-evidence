<!-- fleet job=test-audit id=tests-piece-045-rs-L1 status=done turns=6 usd=0.0083 tokens(read,write,in,out)=[87980, 28789, 14, 7728] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_045.rs lines 1-779 of 779

Window reviewed: `prototype/osfr-tools/tests/piece_045.rs` lines 1-779 (read in full), with the code under test in `src/restoration/piece_045.rs` (COSMETIC_SLOTS at 55-105, cosmetic_slot at 120, validate_appearance at 245, inspect at 476, replay_equip at 555, capture/assert at 623-667) and `src/inventory.rs` 1190-1250. Most tests check real behaviour (the refusal messages in `replay_accepts_owned_cosmetics...` match `inventory.rs:1205/1227/1242`, and the private gate is correctly `#[ignore]`d with a reason). Four findings:

- **[high] tests/piece_045.rs:304 cosmetic_slots_are_the_recovered_appearance_pairs - the (slot, category_id) pairing is checked only against the table itself, so changing any `category_id` or `recovered_rows` value passes.**
  Why it cannot catch a regression: the loop at 304-311 computes the expected value as `cosmetic_slot(row.slot).category_id`, and `cosmetic_slot` (src/restoration/piece_045.rs:120-121) is just `COSMETIC_SLOTS.iter().find(...)` over the same table. The `> 0` checks at 305 accept any positive value. The only independent pins are the category strings at 312-317, which cover slots 1, 3, 4, 5, 6, 17. Slot 2 (Gloves), the `category_id` values (101-106, 201) and the `name_id`/`recovered_rows` evidence are never asserted. Editing `category_id: 101` to `111` for Hats, or `recovered_rows`, leaves the test green.
  Fix: assert the literal pairs, e.g. `assert_eq!((1, 101, "Hats"), ...)` for every row, including slot 2 `(2, 102, "Gloves")` and slot 17 `(17, 201, "Costumes")`, and pin the recovered row counts (7522, 3189, ...) with the evidence comment.

- **[medium] tests/piece_045.rs:735-747 private_snapshot_cosmetics_match_pinned_content - the wrong-slot refusal is checked only for byte-stability, not for why it was refused.**
  Why it cannot catch a regression: the arm at 742-744 accepts any `Refused` with unchanged equipment. If the handler started refusing every request for a different reason (for example "unowned inventory item", or a malformed-request error after a parser change), or if the slot check were removed and the request were refused by some other guard, this gate still passes. Only a successful wrong-slot equip would fail it. The same weakness is in the synthetic test at 524-549, which does pin the reason, so only this private gate loses the check.
  Fix: assert `error == CosmeticError::Inventory { kind: InvalidData, message: "equipment does not match profile or slot" }` in the `Refused` arm at 742, the same as the synthetic test at 541-548.

- **[low] tests/piece_045.rs:599 restart_round_trip_preserves_profile_bytes - an exact byte length (16) for profile 2's equipment is pinned, though the test is about restart stability.**
  Why it cannot catch a regression: it passes only while the saved layout is exactly one 4-byte count plus one 12-byte row. Unrelated changes to the equipment encoding, such as an added field or a different row layout that still round-trips, would fail it without any restart bug. This is incidental churn rather than a missed bug.
  Fix: assert that `before[1].equipment` equals `capture_profiles(&reloaded)` output (already done at 607), and compare the count against the encoded row count derived from `span_bytes`, or drop the literal 16.

- **[low] tests/piece_045.rs:298-299 cosmetic_slots_are_the_recovered_appearance_pairs - `assert_eq!(COSMETIC_SLOTS.len(), 7)` pins the table size as a magic number.**
  Why it cannot catch a regression: it is a constant compared with the array type's own length, which the compiler already enforces via `[CosmeticSlot; 7]` in src/restoration/piece_045.rs:55. It adds no evidence and fails only on a deliberate table edit, which is churn.
  Fix: remove it, or replace it with a check against the evidence count (the seven slot pairs recovered from ClientItemDefinitions.json) in a comment-backed literal list.

Not reported: line 749 `assert!(accepted >= rows.len() && refused == rows.len())` is weak, since the loop already panics on any non-accepted equip and so `accepted == rows.len()` by construction. It is redundant rather than a hole, so I left it out to stay within the cap.
