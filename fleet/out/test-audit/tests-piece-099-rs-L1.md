<!-- fleet job=test-audit id=tests-piece-099-rs-L1 status=done turns=6 usd=0.0067 tokens(read,write,in,out)=[81612, 25150, 14, 5452] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_099.rs lines 1-727 of 727

Window reviewed: `prototype/osfr-tools/tests/piece_099.rs` lines 1-727 (plus `src/restoration/piece_099.rs` 560-1000 and 1-200 for the code under test). Most assertions are meaningful: the wire-byte round trips, malformed-wire refusals, the trade silent-drop verdicts, the activity refusals with state checks, and the per-stream divergence paths all check real behavior. The findings below are the weak spots.

- **[medium] tests/piece_099.rs:503 trade_case_records_the_silent_drop_on_the_real_gateway - `compare(&report, &report.clone())` compares a run with its own clone, so the check is true by construction.**
  - Why it cannot catch a regression: `first_difference` returns `None` for equal JSON, so any change to `compare`'s diffing, or to what `to_json` emits, still gives `Identical`, as long as the two sides are the same. The `digest: report.digest()` expectation is also computed from the code under test.
  - Fix: delete the assertion, or replace it with a comparison against an independently built run (for example, the same script run through a second fresh gateway, or a run with one verdict changed) that must come back `Identical` with a digest pinned to a literal, or must `Diverged` at the expected path.

- **[medium] tests/piece_099.rs:322-327 party_case_is_deterministic_and_compares_identical - the expected value is `first.digest()`, which is the same `digest()` that `compare` uses for `Identical`.**
  - Why it cannot catch a regression: if `digest()` changed how it hashes, or ignored a stream, both sides would still agree. The `Identical` match only restates the function's own output. The `assert_eq!(first, second)` at line 321 is the real determinism check.
  - Fix: assert `first.digest()` equals a literal 64-hex value that was captured once, or drop the `digest:` payload and match only `Comparison::Identical { .. }` after the `first == second` check.

- **[medium] tests/piece_099.rs:127 trade_vocabulary_is_pinned_to_the_supplied_client_and_community_sources - the name says the table is pinned to the supplied client and community sources, but the body only compares `TradeMessage::CLASS_TABLE` against a hand-typed copy of the same table (line 129).**
  - Why it cannot catch a regression: nothing reads the client pseudocode or the Sanctuary/OFR reader. If both the source table and this copy were changed together, or if the source table was mistyped from the binary in the first place, the test still passes. The "ORIGINAL" claim is only as good as the human transcription.
  - Fix: rename the test to say it pins the vocabulary table to this file's copy. Or add a check that reads the cited evidence (for example, the `PacketCodes.cs` `BaseTradePacket` rows, or a sha-pinned extract of the `FUN_00c6a7b0` call sites) and compares against it.

- **[low] tests/piece_099.rs:340-345 party_case_is_deterministic_and_compares_identical - `all(|record| record.index < first.log.len())` cannot fail.**
  - Why it cannot catch a regression: `run` sets `index` from `enumerate()` over the steps (src/restoration/piece_099.rs:942-946), so the index is always below the log length whatever the dispatcher does. A bug that reordered or duplicated records would still pass.
  - Fix: assert the indices are exactly `0..steps.len()` in order, for example `first.log.iter().map(|r| r.index).eq(0..first.log.len())`, and that `first.log[i].tick` matches the scenario tick.

- **[low] tests/piece_099.rs:206 trade_commands_round_trip_the_recovered_client_wire - `assert_eq!(cases.len(), 6, ...)` checks a literal array length against itself.**
  - Why it cannot catch a regression: the array is written inline in the test, so the count is fixed by the test source. It says nothing about the codec. It is also an incidental count pin that churns with unrelated edits to the case list.
  - Fix: remove it, or compare the set of variants covered against `TradeMessage::ALL` filtered to the six recovered client-to-server rows, so that a dropped row fails.

No `#[ignore]`, missing-fixture early returns, or `is_ok()`-only checks were found in the window.
