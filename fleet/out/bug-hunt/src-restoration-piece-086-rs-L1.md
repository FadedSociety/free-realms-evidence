<!-- fleet job=bug-hunt id=src-restoration-piece-086-rs-L1 status=nothing_found turns=5 usd=0.0049 tokens(read,write,in,out)=[34657, 18739, 12, 4334] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_086.rs lines 1-383 of 383

Reviewed `prototype/osfr-tools/src/restoration/piece_086.rs` lines 1-383 in full (constants, `CurrencyKind`, `Producer`, `Flow`, `audit`, `CoinLedger`). No finding meets the bar for a remote or save-driven defect.

Candidates examined and dropped:

- **`audit`, lines 296-302: unchecked `i64` `+=` on the totals.** `coins_sourced`, `coins_sunk` and the Station Cash totals are summed before any validation. Two huge `i64` amounts would overflow and panic in a debug build. The only caller is the lead's producer audit, and nothing in `src/` calls `audit` (the only reference is `tests/piece_086.rs`, which includes the file via `#[path]`). Its amounts come from local reconstructed producers, not from a packet or save, so there is no client-controlled path. The doc comment at lines 269-270 says the totals are raw sums over every listed flow, so the pre-validation summing is intended. Dropped as unreachable from client input.
- **`CoinLedger::new`, line 350: accepts any `i64`, despite the doc at lines 341-343 saying the balance stays in `0..=COIN_MAX`.** Only `credit` and `debit` change the balance, and both keep the result in range once the start is in range. The constructor has no production caller, and the balance it would take (a coin count) is an `i32` on the wire, so the out-of-range case cannot arise from client input today. This is a documentation gap, not a reachable defect. The risk is for a future spend path that builds a ledger from an unchecked value.
- **`credit` (358-369) and `debit` (371-382): checked arithmetic.** `checked_add`/`checked_sub` plus the range filters prevent overflow, wrap and overdraw. Rejected amounts `<= 0` return an error before any mutation, so there is no partial state.
- **`audit` duplicate detection (304-328).** Zero instance and negative amount are rejected before the `seen` check. The key is `(producer, instance)`, which matches the doc comments and the test at `tests/piece_086.rs:173-183`. No bypass found.
- **Constant and table definitions (lines 48-88) and the enum classifications (lines 184-243).** These match the test assertions in `tests/piece_086.rs`. No index or slice operations occur in the window.

No panic, unbounded growth, or trust-the-client path reaches this window from a packet or save. The module is also not registered in `src/lib.rs`; the lead must do that before any of this code is reachable.
