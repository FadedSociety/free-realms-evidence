<!-- fleet job=test-verify id=tests-fishing-service-rs-L1-f1 status=done turns=4 usd=0.0050 tokens(read,write,in,out)=[26198, 19774, 10, 4604] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/fishing_service.rs:264

**Verdict:** `confirmed` (the diagnosis is correct; the proposed fix's expected error is wrong).

**Evidence:**

- The forged packet is `request(14, handle_bytes(ACTOR))` plus `5u32`, a 12-byte body (`tests/fishing_service.rs:267-268`). `fishing.rs:103` maps `14 => Self::Result`, so `Sub::from_u16(14)` succeeds. `ClientRequest::decode` then falls through to `other => Err(Error::UnknownSub(other.as_u16()))` (`src/fishing.rs:322`). That happens at `fishing_service.rs:688`, the first line of `handle`, before any bite, stage, or phase check.
- Therefore the only assertion that can fail is `assert!(service.handle(&forged, PLAYER, T0 + 1).is_err())` (line 269), and it fails for a decode reason. Any change to the no-bite logic in `handle` (lines 739-817, including the `Casting | Nibbling` escape arm and the `_ => OutOfOrder` arm) leaves this test green. The reward-inventory check at lines 270-278 is also trivially true because no catch occurred. The test therefore cannot detect removal or weakening of the bite guard.
- **The suggested fix is wrong on one point.** A reel sent after the cast at `T0+1`, before the bite, does not return `OutOfOrder`. In `fishing_service.rs:794-797`, `Some(AttemptStage::Casting | AttemptStage::Nibbling)` produces an escape reply and `Ok(change)`. The pre-bite reel is an escape, not an error. Asserting `Error::OutOfOrder` would fail against the current code.
- Mitigation: the pre-bite reel path is already covered by `early_reel_escapes_without_grant` (lines 241-261). That test sends a reel at `T0+2` after the cast, asserts the escape packets, asserts `at_18 == 0`, and asserts no quest events and an empty inventory. A regression that granted a catch on an early reel would fail there. The specific "client sends a catch with no bite" case, however, is not exercised by line 264.

**Minimal fix:** Either delete the sub-14 forgery (it tests decode, not the guard), or replace it with a pre-bite `reel_request()` at `T0+1` that asserts the escape result (`at_18 == 0`) and an empty inventory, plus `service.phase(PLAYER)` unchanged. Do not assert `OutOfOrder` for that case.
