<!-- fleet job=pin-audit id=src-bin-osfr-gateway-lead-trade-commit-rs status=nothing_found turns=2 usd=0.0012 tokens(read,write,in,out)=[2190, 5569, 6, 877] model=claude-haiku-5-5 -->
# src/bin/osfr_gateway/lead_trade_commit.rs

No findings in `prototype/osfr-tools/src/bin/osfr_gateway/lead_trade_commit.rs`. Every screened assertion compares against a value the test's own fixture sets, not a shipped data file:

- **Lines 85-88 (`a_settled_trade_moves_coins_in_both_saves_and_both_live_sessions`):** Starting balances come from `with_coins(&mut a, 25)` and `with_coins(&mut b, 5)` (lines 75-76). The 10-coin transfer is the literal `delta` of `-10` / `+10` in the test's `settlement()` helper (lines 39-55). The expected 15 is 25-10 and 5+10, so it follows from the fixture alone. It does not come from a data file.
- **Lines 121-122 (`a_stale_trade_moves_nothing_and_writes_nothing`):** The 24 is set by `with_coins(&mut a, 24)` at line 109, and the 5 is the fixture balance from line 107. Neither is a data value.
- **Lines 168-169 (`an_interrupted_trade_is_finished_from_its_journal_at_start`):** The 15 is set by `with_coins(&mut a, 15)` and `with_coins(&mut b, 15)` at lines 139-140. The test's own fixture sets it.

The 38/19 bytes at line 92 and the pet roster are outside the screened list and were not assessed.
