<!-- fleet job=pin-audit id=tests-piece-046-rs status=nothing_found turns=5 usd=0.0029 tokens(read,write,in,out)=[27016, 14213, 12, 1705] model=claude-haiku-5-5 -->
# tests/piece_046.rs

No findings in `prototype/osfr-tools/tests/piece_046.rs` for the five screened lines.

- **247/248 `slot_input_gate_matches_the_recovered_client_checks`:** the 40 and 39 come from the test's own fixture (`costly.mana_cost = 40`, line 246). Not a data value.
- **298 `catalogue_is_the_recovered_consumable_rows`:** `stew.cost == 180` matches `CONSUMABLE_ITEMS` in `src/restoration/piece_046.rs:130`, a Rust constant recovered from the client catalogue, not a value in `data/content/*.json`. Not a tunable data field, so not a finding under the stated rule. If the team wants it read from data, that would be a separate change.
- **307 `catalogue_is_the_recovered_consumable_rows`:** `power_rating == 1` for item 11002 is the same kind of code constant (`piece_046.rs:184`). Not a data-file value.
- **388 `ledger_consumes_once_and_gates_on_the_caller_supplied_cooldown`:** 11_000 = second use at 6_000 plus the test's own `UsePolicy { cooldown_ms: 5_000 }` fixture (line 321). Test-built, not from data.

Note for the team: the consumable catalogue (`src/restoration/piece_046.rs`) is code, not in `data/content`. That is why the tests pin its values. Moving it to data would be the route to making 298 and 307 live-tunable.
