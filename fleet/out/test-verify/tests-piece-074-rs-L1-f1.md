<!-- fleet job=test-verify id=tests-piece-074-rs-L1-f1 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[12811, 12529, 8, 2823] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_074.rs:52-57,143-156

**Verdict:** `confirmed`

**Evidence:**
- `tests/piece_074.rs:52-57` defines `fn category_bucket(category_id: i32) -> Option<u32>` locally as `(category_id as u32) % COLLECTION_CATEGORY_HASH_BUCKETS`. It is not imported from the module. The only `use` is `use piece_074::{COLLECTION_CATEGORIES, COLLECTION_CATEGORY_COUNT, CollectOutcome, CollectionCatalogue, CollectionDefinition, CollectionError, CollectionLedger};`, and none of those names is a bucket function.
- `tests/piece_074.rs:143-156` (`category_bucket_is_the_recovered_modulo`) asserts only on `category_bucket(1|10|11|0)`. None of its four assertions touches `piece_074::` code. Replacing the module's category handling with anything, or deleting it, leaves this test green.
- Searching `src/restoration/piece_074.rs` for `bucket` or `% 10` finds only the doc comment at lines 14-15. There is no bucket function in code. `notes/Autopilot/T034.md:35-36` records that `category_bucket` was removed from `src/restoration/piece_074.rs` as "unused private code" and that "the test target now owns those test-only helpers". So the shipped module lost the function and the test kept a copy, which means the test checks its own arithmetic.
- The remaining category test, `category_table_is_the_ten_recovered_client_rows`, does check shipped data (`COLLECTION_CATEGORIES` ids, names and icons), but it does not cover bucketing. So the "% 10 / FUN_009fd050" claim has no shipped-code check.

**Caveat on severity:** the reviewer's "cannot catch a regression" is accurate for the test's name and message, which claim `FUN_009fd050` bucketing is verified. No shipped bucketing exists to regress. The defect is a misleading coverage claim (plus a dead helper), not a missed regression in live code. "High" is probably overstated.

**Minimal fix:** either rename the test and drop the `FUN_009fd050 hashes with % 10` message, or move the bucket into `src/restoration/piece_074.rs` as `pub fn category_bucket(id: i32) -> Option<u32>` and assert `piece_074::category_bucket` on 0, 1, 10 and 11, with the `None` for 0.
