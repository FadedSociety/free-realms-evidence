<!-- fleet job=bug-verify id=src-kart-service-rs-L1601-f1 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[26455, 16778, 10, 3971] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/kart_service.rs:1787-1804

**Verdict:** confirmed (as a trust-the-client gap and a misleading comment). It is not a crash, coin, or save-corruption defect.

**Severity if confirmed:** low. A modified client can get unlimited race boosts. Nothing persists, no coins or economy awards are minted, and nothing crashes.

**Evidence:**

1. **Module tree.** The code is live. `src/lib.rs:48` has `pub mod kart_service;`. The gateway calls it: `kart_gateway.rs:697` runs `race.handle_inner(inner, now_ms)` for non-entry subtypes during a race. So this is not test-only code.

2. **Input reach and upstream checks.** `kart_service.rs:1775-1779` validates the owned guid (`owned_id`, `own_guid`). Line 1780 requires `phase == Racing`. Line 1787 calls `race_elapsed`, which refuses only a clock before Go (1395-1397 path, `ClaimRate`) and a frame past `max_race_ms` (2399-2403). No check limits the request count, the time between requests, or the queue state beyond `len() >= ITEM_QUEUE_CAP` (1799).

3. **The mechanics in the claim are accurate.**
   - 33/22 pushes `BOOST_ITEM_TYPE` (1804) and sets `last_boost_epoch` (1803). That field is only stored, never compared to the clock.
   - 33/19 uses `queued_items.first()` (1834) and removes it (1860). It then returns item 5 in `USE_ITEM_RESPONSE_SUBTYPE` (1870-1873).
   - So each request/use pair leaves the queue empty. The three-slot cap bounds only simultaneous unused entries, not the rate.
   - `BOOST_INTERVAL_MS` (kart_service.rs:163) is documented as "not a pacing gate". The same is true of `last_boost_epoch`.

4. **The comment is misleading.** Lines 1795-1798 say "the recovered three-slot queue is the pacing bound". That is not true for a repeated request/use cycle. The native-client evidence cited at 1791-1794 explains why there is no interval. It does not show that the server has a rate bound.

5. **Other points in the report.** The snapshot validator at 2190 bounds `last_boost_epoch` by `max_race_ms / BOOST_INTERVAL_MS`. That suggests a per-race budget was intended, but the request path never enforces one.

**Corrected fix:** The claim's fix is sound, but the first step should be to confirm the design with the owner. Either (a) correct the comment at 1795-1798 and 151-162 so it no longer calls the queue a pacing bound, or (b) add a server-side budget. Option (b) could be a minimum `elapsed` gap between accepted 33/22 grants, enforced against `last_boost_epoch` or a saved last-grant time, or a per-race cap on boost grants. Any such change should be checked against the native refill timings the comment cites (~10.6 s to minutes after Go), because a gap that is too tight would refuse legitimate requests.</result>
