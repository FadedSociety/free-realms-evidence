<!-- fleet job=test-audit id=tests-common-item-catalogue-rs-L1 status=nothing_found turns=2 usd=0.0009 tokens(read,write,in,out)=[2303, 3166, 6, 987] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/item_catalogue.rs lines 1-32 of 32

Reviewed `prototype/osfr-tools/tests/common/item_catalogue.rs` lines 1-32 (the whole file). It contains no `#[test]` functions and no assertions. It is a fixture module with four helpers: `row`, `sized_row`, and `write` build synthetic catalogue JSON, and `write` writes it to `item-catalogue.json`.

Checked against the five categories:
1. **Cannot fail:** no test body exists here, so there is no assertion to compare against its own computation. `row` derives `sha256` from the same bytes it serializes, but that is fixture construction, not a check. Any test that relies on that sha256 matching the bytes is in a different file and outside this window.
2. **Asserts nothing:** not applicable, since there are no tests.
3. **Name overclaims:** not applicable. The module doc says the helpers serve the budget tests and the `inventory_catalogue` fixture, and nothing here claims to prove anything.
4. **Silently skipped:** no `#[ignore]` and no early `return`.
5. **Over-pinned:** no exact counts or offsets are asserted in this window.

No findings in this window. The real assertion-level risk would sit in the test files that call these helpers, which are outside my window and were not reviewed.
