<!-- fleet job=test-audit id=tests-piece-083-rs-L1 status=done turns=5 usd=0.0087 tokens(read,write,in,out)=[52692, 25708, 12, 9879] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_083.rs lines 1-505 of 505

Window reviewed: `prototype/osfr-tools/tests/piece_083.rs` lines 1-505 (read in full, plus the module under test `src/restoration/piece_083.rs` lines 130-549). No `#[ignore]`, no early-return skips, and no fixture is missing: the catalogue is inline. The price vectors are hand-derived, not computed from the code, so they can fail. Most tests are sound. The findings below are where the test name promises more than the body delivers, or where a plausible mutation of the module passes.

- **[medium] tests/piece_083.rs:350 stock_is_consumed_once_and_then_exhausts - the name says stock "exhausts", but no test drives stock to zero, and the exact-boundary case is never exercised.**
  - Why it cannot catch a regression: the only purchase that touches stock takes 2 of 3 (leaving 1). The second attempt asks for 2 of 1, which is refused whether the check is `quantity > available` or `quantity >= available`. So a change to `>=` (which would refuse buying the last unit) still passes, and so does a change that never lets stock reach 0.
  - Fix: add a purchase of exactly the remaining stock (`quantity == available`, e.g. buy 1 of the remaining 1) that must succeed, assert `ledger.stock(MERCHANT, 34) == Some(0)`, and then assert that a further order of 1 is refused with `OutOfStock { available: 0 }`.

- **[medium] tests/piece_083.rs:200 catalogue_document_is_validated_row_by_row - the name claims row-by-row validation, but four of the rules enforced in `ShopCatalogue::from_json` (src/restoration/piece_083.rs:211-225) are never checked.**
  - Why it cannot catch a regression: the untested rules are `icon_tint < 0`, `definition_id <= 0`, `cost > i32::MAX`, and the `MAX_CATALOGUE_ITEMS` / `MAX_CATALOGUE_MERCHANTS` / `TooLarge` limits. Deleting any one of those checks still passes every assertion in this test.
  - Fix: add one malformed-row case per rule, each asserting `Err(CatalogueError::Corrupt(_))` (or `TooLarge` for the size limit): `icon_tint: -1`, `definition_id: 0`, `cost: 2147483648`, and a document over the item/merchant cap.

- **[low] tests/piece_083.rs:237 purchase_debits_coins_and_grants_the_definition_once - the name says "once", but only a single purchase is made.**
  - Why it cannot catch a regression: nothing checks that a second grant of the same definition does not double-count or re-debit. A mutation that grants the stack twice on one purchase would still see `owned == 1` only if it also halved the count, so the "once" claim is not tested. The one-purchase case only shows the debit and grant happen once in the normal path.
  - Fix: either rename the test to `purchase_debits_coins_and_grants_the_definition` or add a second identical purchase and assert `coins`, `owned`, and `stacks` each moved by exactly one more unit's worth.

- **[low] tests/piece_083.rs:322 quantity_is_bounded_by_the_request_order_and_stock - the zero/negative loop compares only the result code, not the refusal reason.**
  - Why it cannot catch a regression: `refusal(...).0` passes if `quantity < 1` is refused for an unrelated reason that maps to the same code, for example via the `checked_mul` overflow path in `purchase` (`src/restoration/piece_083.rs:475-477`), which also returns `InvalidQuantity`. The wrong reason would be accepted.
  - Fix: assert the full tuple, `(COIN_STORE_RESULT_INVALID_QUANTITY, Refusal::InvalidQuantity)`, for both 0 and -1 (the `Refusal::InvalidQuantity` value is the same one used on line 439).
