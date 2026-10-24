<!-- fleet job=test-audit id=tests-vendor-sell-rs-L1 status=done turns=14 usd=0.0192 tokens(read,write,in,out)=[465154, 55630, 30, 15272] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/vendor_sell.rs lines 1-1054 of 1054

Window reviewed: `prototype/osfr-tools/tests/vendor_sell.rs` lines 1-1054. Most tests check real behaviour: the refusal helper compares state, the gateway snapshots are compared, and the fixture panics (not skips) when content is missing. The findings below are the ones I could confirm against the code.

- **[medium] prototype/osfr-tools/tests/vendor_sell.rs:292 sale_completion_id_drives_buy_back - the test never shows that the id selects the sale.**
  - Why it cannot catch a regression: `buy_back_with_context` (`src/coin_shop.rs:906-909`) finds the sale by `transaction_id == sale_transaction_id && remaining > 0`. If that predicate were weakened to `sale.remaining > 0` (or the id were ignored and the first sale taken), this test would still pass, because the test has only one sale and sends that sale's own id. The test also calls `counter.shop.handle` directly and skips `handle_coin_store`, so the route that carries the id is not covered.
  - Fix: after the sale, send a buy-back with a different id (for example `completion.transaction + 1`, or 0) and assert `result_code != RESULT_OK`, that coins and stacks are unchanged, and that the original id still restores once. Optionally add a second sale and check that the buy-back restores the one named by the id.

- **[low] prototype/osfr-tools/tests/vendor_sell.rs:272 native_sell_changes_exactly_one_stack_and_the_coin_balance - the completion asserts `timestamp == 0` (line 273) and `merchant == 0` (line 272), which the name does not claim.**
  - Why it cannot catch a regression: it doesn't need to. Any server change that stamps a real time or writes a different merchant field would break this test without changing the sale. That is churn, not a missed bug.
  - Fix: drop the `timestamp` assertion (and the `merchant` one if it is not part of the sell contract), and keep the assertions on result, kind, definition, quantity, price and remaining, which the name and comments cover.

- **[low] prototype/osfr-tools/tests/vendor_sell.rs:770 gateway_native_sell_pays_once_saves_and_survives_a_reconnect - the post-reconnect refusal is pinned only as `assert_ne!(done[0].result, RESULT_OK)`.**
  - Why it cannot catch a regression: the comment at line 766 says the sell is "refused", but any non-OK code passes. If the reconnected session returned, say, RESULT_FAILURE for a reason other than "no open shop", the test would still pass. The state check at line 771 does still catch a payment, so this is a weakened claim, not a hole.
  - Fix: assert the specific code that a closed shop produces (the same `coin_shop::RESULT_INVALID_MERCHANT` used by the service-layer "never opened" case), with a label.

- **[low] prototype/osfr-tools/tests/vendor_sell.rs:494 replay_and_reload_cannot_pay_twice - the "reload" is a fresh `Counter::new` seeded from the serde round-trip of `InventoryState`, not a reload of a saved shop.**
  - Why it cannot catch a regression: `Counter::new(0, ...)` sets the coins and then the closure overwrites the whole state, so the coins argument is dead. A change to how the shop or its session reloads would not be caught, because the new shop never saw the old session. The name overclaims a reload of the session.
  - Fix: either rename it to cover only the state round-trip, or reload through the gateway path (`Fixture::connect` with `snapshot().gameplay`, as the gateway test at line 764 does) and check the replay is refused there.
