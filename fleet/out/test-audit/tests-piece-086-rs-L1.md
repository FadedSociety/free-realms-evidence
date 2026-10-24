<!-- fleet job=test-audit id=tests-piece-086-rs-L1 status=done turns=4 usd=0.0048 tokens(read,write,in,out)=[22662, 15432, 10, 5188] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_086.rs lines 1-248 of 248

Window: `prototype/osfr-tools/tests/piece_086.rs` lines 1-248. Read against `src/restoration/piece_086.rs` (all 383 lines). Checked the audit totals (237 = 25+10+40+15+5+30+100+12), the duplicate/negative/overflow/zero-instance paths, and the CoinLedger bounds. Those assertions match the code and would fail on the obvious regressions. No `#[ignore]`, no early return, and the `#[path]` fixture exists.

- **[medium] tests/piece_086.rs:98 producers_classify_currency_direction_and_evidence - the name says it classifies evidence, but only 4 of the 15 producers have their evidence grade asserted (lines 135-147).**
  - Why it cannot catch a regression: `Producer::evidence()` can change for any of the other 11 producers (for example `CoinShopPurchase`, `TradeGive`, `PaidRevive`, `KartRace`, `EncounterClear`, `StationCashStorePurchase`) and the test still passes. A recovered Original flow could be downgraded to Reconstructed, or a reconstructed local payout promoted to Original, without any failure.
  - Fix: add a table of all 15 `(producer, evidence)` pairs, like the existing currency/direction table at lines 100-128, and assert each one with `assert_eq!(producer.evidence(), expected, "{producer:?}")`.

- **[low] tests/piece_086.rs:55 recovered_coin_wire_constants_match_the_supplied_packet_enums - the name says the constants match the supplied packet enums, but the body only compares them with hand-typed literals and never reads `decompiled/server/...` or any shipped source.**
  - Line 65 (`COIN_MAX, i32::MAX as i64`) also restates the definition in src line 65 rather than checking it against an independent value.
  - Why it cannot catch a regression: the test pins the current literals and would fail on an edit to them. It would not fail if a literal were wrong relative to the supplied enum, because the enum is never read. The name claims a cross-check that does not exist.
  - Fix: rename it to something like `recovered_coin_wire_constants_are_pinned`, or add a check against the supplied source (for example, the pinned hash or a parsed `ClientUpdatePacketCoinCount = 19` line from `BaseClientUpdatePackets.cs`). For `COIN_MAX`, assert the wire size is 4 bytes against the i32 field, not against the same expression.

- **[low] tests/piece_086.rs:212-216 account_wallet_funding_is_the_only_station_cash_source - `assert_ne!(producer.evidence(), EvidenceGrade::Reconstructed)` is a weak check for the Station Cash producers.**
  - Why it cannot catch a regression: both Station Cash producers are currently `Original`. Changing either one to `Community` (or to any future non-Reconstructed grade that is wrong for a wallet flow) still passes. The test says the wallet split is recovered, but the assertion only excludes one value.
  - Fix: assert `assert_eq!(producer.evidence(), EvidenceGrade::Original, "{producer:?}")` for the two Station Cash producers, matching the `Original` grades the comment at line 204-205 relies on.
