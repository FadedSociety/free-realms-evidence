<!-- fleet job=test-verify id=tests-multiplayer-rs-L1-f1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[23278, 13399, 10, 3283] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/multiplayer.rs:982

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. The 17th probe never reaches the cap check, so the test passes with or without `MAX_SESSIONS`.

1. **The probe is malformed.** The test builds `[0,1] + 3u32 + 999u32 + 512u32 + b"CGAPI_527 "` (test lines 993-997). That is 14 + 10 = 24 bytes, so the length check passes. But `session.rs:20` requires `&wire[14..] == b"CGAPI_527\0"`, and `"CGAPI_527 "` ends in a space, not NUL. `parse` returns `Err("expected a CGAPI_527 session request")`. The CRC (3) and buffer (512) fields are in range, so the trailing byte is the only defect.

2. **The gateway drops it before the cap.** In `osfr-gateway.rs:3691-3715`, `SessionRequest::parse(wire)` runs first. On `Err` it only writes a trace record with `outcome: "rejected"` and returns. `accept_handshake` (and therefore the `MAX_SESSIONS` check at 4339-4342, which is the only place `refuse("session_cap")` is called) is never reached.

3. **Walk the regression.** Delete the cap, or set `MAX_SESSIONS` to 1000:
   - Line 1002-1005: no reply is still received, because the probe is still rejected at parse. `recv_from` errors, so the assertion holds.
   - Line 988 and line 1006: `active_session_count()` stays 16. The 16 `Client::connect` calls are unchanged, and the malformed probe creates no session.
   - No other assertion in the test reads the security log or the trace, so nothing else changes.

   So the test passes under the regression. The assertions named in the claim are the only ones in the test, and they are satisfied either way.

The claim's mechanism is also accurate. The `#[ignore]` and fixture-gate exemptions do not apply here.

**Minimal fix:** Send a well-formed probe with a fresh id (`b"CGAPI_527\0"`, 24 bytes). Assert that no reply arrives and that the refusal was the cap. The `AdmissionRefusal` count in `security` is one option, and the trace `session_cap` event is another. Add a control: drop one admitted client, then send the same well-formed probe and assert it gets a `[0,2]` reply. That proves the probe itself is valid and the silence is caused by the cap.
