<!-- fleet job=pin-audit id=tests-player-trade-rs status=nothing_found turns=3 usd=0.0013 tokens(read,write,in,out)=[7037, 5760, 8, 1041] model=claude-haiku-5-5 -->
# tests/player_trade.rs

No findings in `prototype/osfr-tools/tests/player_trade.rs` for the screened lines 505, 544, 545, 547, 549, 558, 559.

All of these numbers come from the test's own fixture, not from a shipped data file:
- Items are built by the local `item(id, definition_id, count)` helper (lines 35-48), and the definition ids 100, 200, 400 and the counts are literals passed into it in the test (for example lines 527-528 and 532-535).
- The trade inventory's item definitions are built in the local `inventory(...)` helper (lines 60-70) with `max_stack` 99 and `no_trade` flags written inline. No test here reads `data/content` or a price field.
- The expected `ItemMove` and row tuples in lines 505-559 are derived from those fixture inputs through the trade logic. They do not depend on any price or item-value field.

So retuning a data value would not change these assertions. Nothing needs to move to a helper or a bound.
