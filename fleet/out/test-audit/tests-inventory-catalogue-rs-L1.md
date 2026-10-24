<!-- fleet job=test-audit id=tests-inventory-catalogue-rs-L1 status=done turns=7 usd=0.0082 tokens(read,write,in,out)=[78405, 25162, 16, 8477] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/inventory_catalogue.rs lines 1-340 of 340

Window: `prototype/osfr-tools/tests/inventory_catalogue.rs` lines 1-340 (whole file). Checked against `src/inventory.rs` (`definition_replies` 1109, `route` 1145, catalogue limits 36-38, `visit_seq` 245-256, `load_catalogue` 264-283, `decode_hex` 1412) and `tests/common/item_catalogue.rs`.

Most assertions hold against the code: row/byte/file limits match the constants (65,536 rows, 32 MiB of definition bytes, 128 MiB file), the 513-row byte-limit fixture crosses the 32 MiB boundary, the 65,537-byte row trips the 131,072-hex-char check before the hash check, and the `[35,0,34,0]` / `[38,0,2,0]` / `[35,0,37,0]` packet layouts match the reply code. The two ignored tests carry reasons and the private fixture asserts the input hash. No early-return skips. I found two issues.

- **[medium] prototype/osfr-tools/tests/inventory_catalogue.rs:167 definition_requests_reject_malformed_and_oversized_input_without_mutating_state - the assertion compares `definition_replies(&valid)` with `handle(&valid).replies`, where `handle` routes the 35/34 family straight into `definition_replies` (inventory.rs:1155-1157), so the expected value is produced by the code under test.**
  - Why it cannot catch a regression: any change inside `definition_replies` (wrong ID echo, wrong length word, wrong payload) changes both sides identically and still passes. Only a divergence in the routing branch would fail it. The name's "without mutating state" claim is covered by the separate `state()==before` check at line 165, not by this one.
  - Fix: replace the self-comparison with a literal expected packet for the known row 100 (for example, `[35,0,37,0]`-style header `35,0,34,0`-to-reply bytes: family 35, opcode 34, id 100 LE, length 8 LE, then the 8 fixture bytes `[100,0,0,0,7,0,0,0]` from `row(100,7)`), asserted on both `definition_replies` and `handle`.

- **[low] prototype/osfr-tools/tests/inventory_catalogue.rs:298 private_w84_rows_grant_and_reply_byte_exactly - `assert_eq!(rows.len(), 58_835)` pins the exact size of the private W84 catalogue, which changes whenever W84 is regenerated, and the byte-exact checks that follow do not depend on it.**
  - Why it cannot catch a regression: it does not test a regression in the server; it fails on unrelated data churn. It also gives no signal about the behaviour the test name claims.
  - Fix: drop the literal count, or assert it against `report.json` (for example, the row count recorded by W84) so the expected value comes from the input manifest rather than a constant.
