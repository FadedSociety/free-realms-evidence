<!-- fleet job=test-audit id=tests-trade-definition-rs-L1 status=done turns=5 usd=0.0029 tokens(read,write,in,out)=[21741, 9201, 12, 3085] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/trade_definition.rs lines 1-84 of 84

Two findings in `trade_definition.rs` lines 1-84. Everything else in the window checks out: the NO_TRADE byte at +44 is read from the row, and the short row (id 8, 8 bytes) passes the loader's `>= 4` check and then returns `None` from `get(44)`. The fixture hashes are computed from the input bytes, so there is no circularity.

- **[medium] prototype/osfr-tools/tests/trade_definition.rs:74 no_trade_and_max_stack_come_from_the_definition_row - the name says max stack comes from the definition row, but the value is only the JSON `max_stack` field the fixture writes (line 60), and the row bytes never carry it.**
  - Why it cannot catch a regression: a change that takes max stack from anywhere except the row, such as a content-level table, still passes, because the fixture sets the JSON field directly. Only the NO_TRADE byte is actually read from the row.
  - Fix: rename the test to something like `trade_flags_read_no_trade_from_the_row_and_max_stack_from_the_content_field`, or make the test's claim true by asserting the source of max stack explicitly (for example, changing the JSON `max_stack` without changing the row bytes and checking the result moves).

- **[medium] prototype/osfr-tools/tests/trade_definition.rs:78-79 (and the fixture at lines 43-45) - the comment promises "zero or less means uncapped", but no row uses zero, and every positive row uses 7.** The implementation is inventory.rs:558-560, `u32::try_from(max_stack).ok().filter(|max| *max > 0)`.
  - Why it cannot catch a regression: changing `> 0` to `>= 0` makes a max stack of 0 come back as `Some(0)` (a cap of zero, so nothing can be stacked) instead of uncapped, and every assertion still passes. A mutation that hardcodes the cap to 7 for any positive value also passes, because no test uses a second positive value.
  - Fix: add a row with `max_stack` 0 and assert `trade_flags(id) == Some((false, None))`, and use a positive value other than 7 (for example 3) on one row and assert `Some((false, Some(3)))`.
