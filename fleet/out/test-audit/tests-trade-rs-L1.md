<!-- fleet job=test-audit id=tests-trade-rs-L1 status=done turns=5 usd=0.0065 tokens(read,write,in,out)=[45615, 20438, 12, 6912] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/trade.rs lines 1-746 of 746

Reviewed `tests/trade.rs` lines 1-746 against `src/trade.rs` (`TradeMessage` at 68-72, `disconnect` 756, `enter_instanced_zone` 779). Most tests check exact byte layouts, inventory contents, and rejection errors with hand-derived expectations, so they are not circular. Two tests overclaim what their names say.

- **[medium] tests/trade.rs:703 timeout_closes_active_trade_without_settlement - the name says the trade is closed, but the body never checks that the session is gone.**
  - Why it cannot catch a regression: a `timeout` that returns the `15`/`5` messages with status 1 but leaves the session active and still lockable would pass. The test only checks the message statuses and that both inventories are unchanged.
  - Fix: after line 716, assert `world.trades.session_counter(session) == None` and `world.trades.session_id_for(A) == None` and `session_id_for(B) == None`. This matches what the disconnect test does at line 607.

- **[medium] tests/trade.rs:732 instanced_zone_exit_sends_viewer_relative_statuses_and_end - the name claims viewer-relative statuses, but no recipient is checked.**
  - Why it cannot catch a regression: the test checks `status(&messages[0]) == 8` and `status(&messages[2]) == 7`, but never checks `messages[i].recipient`. `enter_instanced_zone` (src/trade.rs:787-797) picks the status order from the session index. If both messages were addressed to B, or the recipients were swapped, the status values would still match and the test would pass.
  - Fix: assert `messages[0].recipient == SessionId(A + 1_000)` and `messages[2].recipient == SessionId(B + 1_000)`, which are the session ids that `world()` registers (line 90). Also assert the sub-5 end messages go to the same recipients as the preceding status 15 messages.

Lower-priority note, not a missed bug: lines 308, 318 and 527 pin exact session counter values (3, 4, Some(1)). Unrelated changes to the counter bump policy would break these even though the tests are about layout and rejection. Consider comparing against a counter read taken before the call instead.
