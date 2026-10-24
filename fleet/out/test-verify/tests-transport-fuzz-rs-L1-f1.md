<!-- fleet job=test-verify id=tests-transport-fuzz-rs-L1-f1 status=done turns=5 usd=0.0044 tokens(read,write,in,out)=[31209, 13823, 12, 4809] model=claude-haiku-5-5 -->
# high: transport_fuzz.rs:335

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. The test never routes anything that could extend the deadline through the receiver between the t=0 fragment and the t=30s expiry check.

- `transport_fuzz.rs:335-363`. `receive_at` is called only at t=0 (line 339) and at t=31s (line 357). Between those, the only calls are `reassembly_deadline()` (344), `decode_controls(&codec, &[0, 6])` ten times (349-351), and `expire_reassembly(+29s)` / `expire_reassembly(+30s)` (352-353).
- `session.rs:52` `decode_controls` is a pure function of `(codec, wire)`. It takes no `ReliableReceiver`, so the loop cannot touch `partial.started_at`.
- Walk the regression "`receive_at` resets or extends `partial.started_at` on any non-fragment reliable packet, or the gateway resets it on KeepAlive". The t=0 assertion at 344-346 still passes. The loop at 349-351 does not reach the receiver. `expire_reassembly(+29s)` (352) still returns false, and `expire_reassembly(+30s)` (353) still returns true. Lines 354-355 pass, and the t=31s call (357-361) still returns `ReceiverPoisoned`. Every assertion passes.
- The regression is real in the sense that the code path exists. `soe.rs:376-377` runs `expire_reassembly(now)` at the start of `receive_at`, so a non-fragment packet at t=20s would reach the receiver. The test never sends one. The gateway poll at `osfr-gateway.rs:3801-3804` is also not reached by the test.
- The only expiry-adjacent assertion that depends on timing is at t=29/30, and it is fixed to `start`, not to any later receive. The keepalive/receive extension path is therefore unexercised.

Minor accuracy notes on the claim: the t=31s fragment is poisoned at t=30 by `expire_reassembly` (soe.rs:469), so it is not an extension case. The reviewer's line references are correct.

**Minimal fix:** after line 342, add a non-fragment reliable packet at t=+20s and assert the deadline is unchanged. For example: `receiver.receive_at(&packet(RELIABLE_DATA, 2, b"zz"), start + Duration::from_secs(20)).unwrap();` followed by `assert_eq!(receiver.reassembly_deadline(), Some(start + Duration::from_secs(30)));`. Add the same assertion after a continuation fragment at t=+29s. Note that a gateway-only KeepAlive regression lives in `osfr-gateway.rs` and cannot be caught by this unit test. The receiver-level canary is what this test can add.
