<!-- fleet job=pin-audit id=tests-station-cash-rs status=done turns=4 usd=0.0022 tokens(read,write,in,out)=[16912, 10629, 10, 1495] model=claude-haiku-5-5 -->
# tests/station_cash.rs

**prototype/osfr-tools/tests/station_cash.rs:666 a_station_cash_only_item_lists_at_a_quarter_and_no_longer_sells_for_coins - pins `12` from `data/content/stores.json` `station_cash.sc_price_scale` (0.25) applied to the Dog Tail wiki price of 49 SC (`round(49 * 0.25) = 12`).**
- The literal 12 is the value of the live-tunable scale. If Bryce retunes `sc_price_scale`, the test fails even though `StationCashCatalogue` (`src/station_cash.rs:152-154`) is still correct. The same test already derives `price` on line 665 from `shop.sc_catalogue().config().sc_price_scale`, so line 666 is the only place the number is hard-coded.
- **Fix:** read the scale from the config (already done on line 665) and drop the literal; or, if the check must stay, read the 49 base from the row in `stores.json` (the `item_id` 79511 entry, `sc_price`) and assert `price == (base as f64 * scale).round() as u32` (as `ride_sources.rs:79` and `station_cash.rs:955` already do with `policy["sc_price_scale"]`). The 1/4 ratio can be stated as a bound (`scale > 0.0 && scale <= 10.0`, the `src` validation range) instead of a pinned value.

Lines 669, 684 and 689 use the computed `price` and are not findings.
