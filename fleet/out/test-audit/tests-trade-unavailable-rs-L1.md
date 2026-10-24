<!-- fleet job=test-audit id=tests-trade-unavailable-rs-L1 status=nothing_found turns=6 usd=0.0044 tokens(read,write,in,out)=[33396, 11679, 14, 5242] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/trade_unavailable.rs lines 1-179 of 179

No findings in `prototype/osfr-tools/tests/trade_unavailable.rs` lines 1-179.

What I checked against `src/trade.rs` (`unavailable_replies` at 1136-1161, `end_packet` at 1490, `status_packet` at 1497, `TradeStatus::Cancelled = 1` at 77):

- **Expected bytes are independent of the code under test.** `end()` and `CANCELLED = [0x3b, 0, 15, 1]` are hand-built in the test. They match the code's layout (sub 5 + session; sub 15 + status byte 1), so they are not derived from the function.
- **Each branch is pinned by an exact-value assertion.** Sub 3 with 0 gives no reply (line 53). Sub 3 with 1 or 0xff gives end (40-48). Sub 7 gives end (57-62). Subs 6, 8 (both accepted values), 9 and 10 give status then end (65-81). The gating on the idle session (111-118), on body length including every strict prefix (120-134), on unknown or server-side subs (137-150) and on other families (153-162) all match the `match` and early returns in the code.
- **The canary test (84-98) and the replay test (100-108) are not vacuous.** The canary is a full 4-byte pattern, so a regression that echoes the counter, item id or coins would fail. The replay loop would catch a stateful implementation that changes its second answer.
- **No `#[ignore]`, no early returns, no fixture dependencies** in this window.
- **Pinned values are semantic, not incidental.** The `len() <= 7` and `len() <= 2` bounds are intentional limits, not exact counts.

Minor observation, not reported as a finding: the canary test at line 84 does not assert the session id in the replies. That gap is covered by the exact-bytes assertions at lines 40-42, 58-60 and 75-79, so I did not count it as a hole.
