<!-- fleet job=test-audit id=tests-station-cash-rs-L1 status=done turns=4 usd=0.0062 tokens(read,write,in,out)=[44006, 24818, 10, 5277] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/station_cash.rs lines 1-853 of 853

Window reviewed: `prototype/osfr-tools/tests/station_cash.rs` lines 1-853 (read in full), plus `src/station_cash.rs` `Wallet::restore` (285-305) and `replay` (311+) to check the restore and replay tests. Most tests are sound: the packet walkers check trailing bytes, the refusal tests snapshot and compare state, the replay test compares state, and the restore tests check clamp, pruning and the disabled-package case against real behaviour. Two findings:

- **[medium] prototype/osfr-tools/tests/station_cash.rs:419 catalogue_packets_carry_the_scaled_price_and_skip_earn_only - the name says the packets carry the scaled price, but the body never reads a price.**
  - Why it cannot catch a regression: the body only checks that the earn-only item id is absent (`contains_u32`) and that opcodes 7, 6, 9 and 24 are present. A change that writes the unscaled `sc_price`, or zero, into every 66/5 row would still pass. The comment defers the price to `store_packet_matches_the_client_reader_field_for_field`, so the name overclaims for this test.
  - Fix: rename it to drop "carry_the_scaled_price", or add a price check here, e.g. walk the 66/5 rows and assert that the listed price for `RIDE_ITEM` equals `RIDE_PRICE` (137).

- **[low] prototype/osfr-tools/tests/station_cash.rs:404 bought_ride_catalogue_row_is_no_trade - the hard-coded `items.len() == 54` is an exact count of shipped catalogue rows that the test does not need (it is about the NO_TRADE flag).** The same pattern appears at line 549 (`decoded.len() == 52`).
  - Why it matters: adding or removing one shipped ride row fails these tests even though the no-trade or price logic is unchanged. This is churn, not a missed bug.
  - Fix: assert that the set is non-empty and that it equals the set of listings plus earn-only rows (as the other test does), or compare the count against `shop.sc_catalogue().listings().len() + earn_only().len()` instead of a literal.

No `#[ignore]` or silent early returns were found. The fixtures are loaded with `expect`, so a missing fixture fails the test rather than passing it.
