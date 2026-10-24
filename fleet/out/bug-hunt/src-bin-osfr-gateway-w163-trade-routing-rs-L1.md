<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-w163-trade-routing-rs-L1 status=nothing_found turns=4 usd=0.0026 tokens(read,write,in,out)=[25158, 12388, 10, 1513] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/w163_trade_routing.rs lines 1-463 of 463

No reportable defects in `prototype/osfr-tools/src/bin/osfr_gateway/w163_trade_routing.rs` lines 1-463.

Why nothing qualifies:

- The whole file is test-only code. It is included from `prototype/osfr-tools/src/bin/osfr-gateway.rs:4634-4636` as `#[cfg(test)] #[path = "osfr_gateway/w163_trade_routing.rs"] mod w163_trade_routing;`.
- Every item in the window is either a test helper (`row`, `inventory`, `rig`, `inner`, `select`, `choice`, `pkt`, `subs`, which exist only to build fixtures) or a `#[test]` function (lines 189, 229, 318, 390, 430).
- The task's rules exclude code in `#[cfg(test)]`. Test-side `unwrap`s, the hard-coded fixture ids (`A`, `B`, `TRADE_ENTRY_ID` use), and the expected-value assertions are therefore not in scope.
- No production function is defined in this window. The production trade logic it exercises (`route_application`, `settle_trades`, `refresh_trade_player`, `trades.maintain`, `leave_player`) lives elsewhere and is outside my window.

I did not hunt further in other files because the instructions limit me to this window.
