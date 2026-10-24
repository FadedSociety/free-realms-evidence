<!-- fleet job=test-audit id=tests-coin-store-siblings-rs-L1201 status=done turns=7 usd=0.0099 tokens(read,write,in,out)=[111857, 33625, 16, 9108] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/coin_store_siblings.rs lines 1201-2074 of 2074

Window `coin_store_siblings.rs` 1201-2074 read in full, plus the helpers it relies on (`inner_packets`/`send` at 546-556, `tests/common/gateway_vendor.rs` 30-53). No `#[ignore]` or fixture-missing early returns in the window. Four findings:

- **[medium] prototype/osfr-tools/tests/coin_store_siblings.rs:2014 definition_reply_over_budget_is_refused_before_records_are_copied - the name promises the refusal happens before any record is copied, but the body only checks the reply shape (one 165/3 with an empty list) and that the snapshot is unchanged.**
  - Why it cannot catch a regression: an implementation that first copies all 65 records into a buffer, then discards them when the total exceeds 4 MiB, returns the same single empty 165/3 reply and leaves state unchanged, so every assertion still passes.
  - Fix: either rename the test to describe what it checks (over-budget definition reads return an empty 165/3 and change nothing), or add an assertion that observes ordering, e.g. the 4 MiB check is done from the summed record lengths before any copy (a size-based or allocation-counting canary), or the refusal is shown to occur before any 35/37 payload is produced.

- **[medium] prototype/osfr-tools/tests/coin_store_siblings.rs:1704 unanswered_marketplace_rows_are_known_traffic_and_malformed_ones_are_rejected - "known traffic" is only checked as `assert_ne!(reason, Some("unknown application message"))` for 66/27 and 66/38; the trace outcome is never checked.**
  - Why it cannot catch a regression: if a change starts rejecting 66/27 or 66/38 with some other reason (for example a merchant refusal) and still sends no reply, the test passes, even though the rows are no longer accepted as known traffic.
  - Fix: for the known rows, assert `outcome.trace.last().unwrap().outcome` is the accepted value (not `"rejected"`) and that `reason` is `None`, mirroring the `reason == None` check in `the_login_time_marketplace_requests_each_get_one_reply_through_the_gateway` (line 1333).

- **[medium] prototype/osfr-tools/tests/coin_store_siblings.rs:1960 a_refused_bundle_leaves_the_npc_menu_closed - the bundle refusal is asserted only with `is_err()`, not as the budget refusal, although the test's claim depends on it being the budget.**
  - Why it cannot catch a regression: the bundle could be refused for an unrelated reason (for example a malformed `npc_request(8, None)` child, or a parse change), and the follow-up "menu stays closed" check would still pass. The test would then not prove that a budget refusal discards the staged NPC menu.
  - Fix: assert the error text contains "outbound budget", as the sibling test at line 2058 does, and keep the positive control that proves the same `npc_request(8)` opens the shop when sent outside the refused bundle.

- **[low] prototype/osfr-tools/tests/coin_store_siblings.rs:1667 gateway_sc_full_bag_is_refused_atomically - the test is named for the full-bag refusal, but `ORDER_FAILURE` is the generic refusal code, and there is no control showing that the same order succeeds when the bag has room.**
  - Why it cannot catch a regression: any other refusal path that returns `ORDER_FAILURE` (for example a bad listing lookup) would pass, so the test would not show that the bag cap is what refuses the order.
  - Fix: add a positive control on the same fixture with one slot freed (items below 100), asserting `ORDER_SUCCESS` and the ride count +1, so the refusal is shown to depend on the bag size.
