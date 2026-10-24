<!-- fleet job=pin-audit id=tests-piece-086-rs status=nothing_found turns=2 usd=0.0009 tokens(read,write,in,out)=[1868, 3773, 6, 808] model=claude-haiku-5-5 -->
# tests/piece_086.rs

No findings in `prototype/osfr-tools/tests/piece_086.rs` for the three screened lines. Each expected number is the sum or direct echo of amounts that the test's own fixture passes in as literals through `source(Producer::..., instance, amount)`, so none of them reads a shipped data file value.

- **piece_086.rs:166 `audit_accepts_the_local_producers_once_each` - not a finding.** `237` is the sum of the eight literal fixture amounts on lines 155-162 (25+10+40+15+5+30+100+12). The test builds these amounts itself; none is read from `data/content`.
- **piece_086.rs:224 `account_wallet_funding_is_the_only_station_cash_source` - not a finding.** `499` is the literal amount on line 220, passed straight into the audit. The test checks that the accounting echoes its own input and keeps currencies apart.
- **piece_086.rs:225 `account_wallet_funding_is_the_only_station_cash_source` - not a finding.** `100` is the literal amount on line 221, the fixture's own `CoinShopPurchase` input, not a shop price.

The screen's "reward" and "price" labels came from the variable names; the values do not come from data.
