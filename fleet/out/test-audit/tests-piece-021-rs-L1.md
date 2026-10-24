<!-- fleet job=test-audit id=tests-piece-021-rs-L1 status=done turns=5 usd=0.0058 tokens(read,write,in,out)=[47260, 19671, 12, 5831] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_021.rs lines 1-488 of 488

Reviewed `prototype/osfr-tools/tests/piece_021.rs` lines 1-488 against `src/restoration/piece_021.rs` (`from_json`, `validate_property`, `acquire`). Most tests are sound: the member-price, schema, once-only ownership, starter-grant, membership, bonus and insufficient-balance tests all compare against recorded constants and would fail on the regressions they name. The ignored real-catalogue test has a reason and panics (not early-returns) when the env var is missing, so it is not a silent skip. Three findings:

- **[medium] tests/piece_021.rs:152 `catalogue_rejects_unknown_schema_and_duplicate_deed_items` - the duplicate-deed half asserts only `CorruptCatalogue { .. }`, so any corruption error passes, not the deed-collision rejection the name claims.**
  - Why it cannot catch a regression: if `validate_property` rejected the document for some other reason (for example a broken `name` or `station_cash` check that fires on the Seaside row), the test still passes even if the cross-property deed check at `src/restoration/piece_021.rs:401` is removed, since the removal would still leave... (in practice the removed check would make this test fail, but a second, unrelated rejection of the same document would mask the deed check entirely).
  - Fix: `assert!(matches!(error, AcquisitionError::CorruptCatalogue { ref reason } if reason.contains("deed item 2213")), "unexpected error: {error:?}");`

- **[low] tests/piece_021.rs:410 `an_ownerless_request_is_rejected_without_mutation` - the name says the request is rejected without mutation, but the post-state checks only `CHARACTER` (a different owner); nothing inspects owner `0`, the owner the request named.**
  - Why it cannot catch a regression: the only thing that fails this test is the `matches!` on `InvalidOwner`. A change that let guid 0 accrue ownership or a balance on a path that returns a different error would not be caught by the state assertions, because they never look at guid 0.
  - Fix: add `assert_eq!(engine.station_cash(0), 0); assert!(!engine.owns(0, SEASIDE_LOT));` alongside the existing assertions.

- **[low] tests/piece_021.rs:446 `real_recovered_catalogue_loads_and_charges_the_recorded_prices` - pins `properties().count() == 31`, a corpus row count that changes whenever the extractor or lab corpus changes, and it is not what the test body is about (price and membership behaviour).**
  - Why it cannot catch a regression that matters: a legitimate corpus update (new row) fails the test with no change to acquisition logic, which is churn, not a missed bug.
  - Fix: assert `count() >= 31`, or move the exact count into the extractor's own report check and keep this test on the Seaside and Small Wilds facts.
