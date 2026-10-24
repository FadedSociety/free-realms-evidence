<!-- fleet job=test-audit id=tests-coin-shop-rs-L1 status=done turns=7 usd=0.0093 tokens(read,write,in,out)=[104391, 31974, 16, 8472] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/coin_shop.rs lines 1-419 of 419

Window reviewed: `prototype/osfr-tools/tests/coin_shop.rs` lines 1-419. Most tests are sound. The coin prices (15/13/7 for item 8, member discount), the insufficient-coins, full-bag, sync, and vendor-retry assertions all check real state, and the code paths I read in `src/coin_shop.rs` (lines 130-170, 330-400, 483-580) would fail on the regressions they target. Three findings:

- **[medium] tests/coin_shop.rs:216 marketplace_purchase_is_disabled_and_does_not_change_inventory - the name says marketplace purchase is disabled, but the main assertions only show that an unlisted item (8) is refused with ORDER_FAILURE.**
  - Why it cannot catch a regression: the comment at 218-219 says T230 enables Station Cash orders, so the order refusal comes from the missing SC row, not from a disabled marketplace. If orders were switched on for every item, lines 233-242 would still pass. Only the final 66/43 check at 244-246 tests the disabled state, and that is a separate request that does not involve the order path.
  - Fix: rename the test to something like `unlisted_station_cash_order_is_refused_without_mutation`, and keep the 66/43 `MARKETPLACE_RESULT_DISABLED` check in its own test. Or, if the disabled state is what matters, first assert `catalogue.marketplace.orders_enabled == false` (or the handshake packet at line 309 showing the orders-off state) so the test fails when orders are enabled.

- **[low] tests/coin_shop.rs:379 vendor_refusals_report_low_balance_unknown_item_and_full_stack - the full-stack case relies on item 8 having `max_stack` 1, which the comment at 411 asserts but the test never checks.**
  - Why it cannot catch a regression: the fixture is `rust-gameplay/inventory.json` (outside `repo`, not checked in here). If that `max_stack` changed, the test would fail, but for an unclear reason. It would not show whether the refusal comes from the stack limit or from another grant error, because line 414 accepts any `RESULT_SERVICE_UNAVAILABLE`. The same code path also returns that code for bag-capacity overflow (`coin_shop.rs:572-580`).
  - Fix: before buying, assert the stack state (e.g. `count_definition(state, 8) == 1` and `grant` of 1 more fails with the expected error), and check the refusal code reason, or add a separate bag-capacity case so the stack-limit refusal is pinned on its own.

- **[low] tests/coin_shop.rs:49-54 merchant_status - the helper pins the whole 66/44 reply to exactly 56 bytes.**
  - Why it cannot catch a regression: the vendor tests (352-418) are about the status word and the state, not the packet size. An unrelated field added to the reply would fail every vendor test even though the status is still correct. This is churn, not a missed bug.
  - Fix: assert only the header (`packet[..4]`) and the status word at 48..52, and require `packet.len() >= 52`.
