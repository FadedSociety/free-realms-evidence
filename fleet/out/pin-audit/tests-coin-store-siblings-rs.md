<!-- fleet job=pin-audit id=tests-coin-store-siblings-rs status=nothing_found turns=6 usd=0.0032 tokens(read,write,in,out)=[40094, 12584, 14, 2408] model=claude-haiku-5-5 -->
# tests/coin_store_siblings.rs

No findings in `prototype/osfr-tools/tests/coin_store_siblings.rs` for the three screened lines.

- **1654 / 1673 `gateway_sc_balance_and_ride_survive_reload` - not a finding.** The 50 is `150 - SC_RIDE_PRICE`. The 150 is the test's own wallet fixture (`state.sc_wallet = Some(Wallet { balance: 150 ... })`, line 1631). `SC_RIDE_PRICE = 100` is a test-file constant (line 630), not a shipped value. The shipped `stores.json` row for 14289 (line 17444) has `purchase_price_coins: null` and no SC price, so no data field feeds this number.
- **1752 `gateway_sell_then_buy_back_once_then_replays_pay_nothing` - not a finding.** The 750 is `2 × 375`. The sell price comes from the test's own `stores.json` fixture written at lines 401-413 (`store_row(75060, Some(750), Some(375), false)`, line 408), with the `STACK_MANY` note "sell 375 each" at line 240. That fixture is written to a temp content directory, so retuning the shipped `stores.json` does not affect it. The test is consistent with its own fixture and does not depend on shipped data.
