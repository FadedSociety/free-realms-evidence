<!-- fleet job=pin-audit id=tests-piece-083-rs status=nothing_found turns=3 usd=0.0032 tokens(read,write,in,out)=[13288, 18399, 8, 1482] model=claude-haiku-5-5 -->
# tests/piece_083.rs

No findings in `prototype/osfr-tools/tests/piece_083.rs` for the screened lines.

- The merchant catalogue these tests use is an inline JSON fixture built in the test itself (`fn catalogue()`, lines 65-111). Its costs (5, 320, 206, 12) and discounts (10) are the test's own fixture values, not reads from a shipped data file. The header says they are "copied from" the pinned community `ClientItemDefinitions.json`, but that is a provenance note, not a live dependency. Retuning `data/content/*.json` does not change them.
- No shipped data file under `prototype/osfr-tools/data/content` holds merchant or coin-store item prices. A search for merchant, coin_store and ClientItemDefinition in `data` found only provenance references, so there is no data value for these lines to pin.
- `member_unit_price` (`src/restoration/piece_083.rs:240`) is a pure function of its arguments. Lines 189-196 pass literal cost and discount inputs, so the expected outputs follow the formula, not a tunable value.
- Lines 207, 248-249, 258, 276-277 and 433 come from the inline fixture: 320 is the row-2 cost, and 995 is 1000 credited minus the row-1 cost of 5. These are fixture-set numbers, not data-file values.
