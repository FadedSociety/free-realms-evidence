<!-- fleet job=pin-audit id=tests-piece-021-rs status=nothing_found turns=4 usd=0.0032 tokens(read,write,in,out)=[25759, 17981, 10, 1342] model=claude-haiku-5-5 -->
# tests/piece_021.rs

No findings in `prototype/osfr-tools/tests/piece_021.rs`. None of the six screened lines pins a number from a shipped data file under `data/content/`.

- **Line 103 (`catalogue_accepts_recovered_rows_and_pins_schema`), 195, 231, 255, 422, 486:** the prices and balances come from the test's own inline `CATALOGUE` fixture (lines 52-86), from `set_station_cash` calls in the test, or from the wiki-recorded pairs cited in the header. The engine does not read `data/content/`. Line 486 sits in the `#[ignore]` test that reads the private lab extract named by `OSFR_PIECE_021_CATALOGUE`, not a shipped file. Retuning a `data/content` row cannot break these assertions.
- `data/content/vendors_unresolved.json:10242` mentions "Seaside Lot", but it carries no 270/300 price that the test reads.
