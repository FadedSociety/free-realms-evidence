<!-- fleet job=bug-hunt id=src-bin-osfr-login-rs-L1 status=nothing_found turns=13 usd=0.0303 tokens(read,write,in,out)=[413977, 68156, 28, 35327] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-login.rs lines 1-800 of 946

No reportable defects in `prototype/osfr-tools/src/bin/osfr-login.rs` lines 1-800. I read the whole window and traced the client-reachable paths into `login.rs`, `login_auth.rs`, `soe_send.rs`, `session.rs` and `net_policy.rs`. Candidates I examined and dropped:

- **Broker read buffer and length checks (`poll`, 329-344):** `input` is capped at 196 bytes by `remaining`, `peer.input[..4]` is guarded by `len() >= 4`, and the `length + 4` comparison cannot overflow. The `buffer[..remaining]` slice is in range.
- **Broker `answer` (230-290):** the body length checks (`!= 10 + length`, `!= 134`) run before the `body[6..38]`, `[38..70]` and `[70..134]` slices. `reply[1..33]`, `[33..65]` and `[65..69]` are the right sizes for the 69-byte reply. Rate-limit and discard ordering is consistent.
- **`native_session` (365-391):** bounds, `checked_add` and UTF-8 are all validated before use, and the trailing-byte check is present. The tests match it.
- **`Request::parse` (408-422):** the length is checked before `bytes[..2]` and `bytes[14..]`. The CRC clamp to 2 is documented in `notes/Design/Security Model.md:40`, so it is intended.
- **`application` (724-780):** the token is only spent after `native_session` validates it. `principal` is cleared and the service reset before redeem. A failed redeem leaves no principal, so non-login packets error out. The synthetic login uses the server-owned handle, and the account/key check runs before use. No packet-supplied identity reaches the service.
- **`application[0]` at 620:** I considered an empty application message here. `ciphertext_messages` never yields an empty slice, and `LoginService::handle` errors on empty input, so this line is unreachable with empty bytes.
- **`datagram_limit` (`request.buffer`, 64..512 after clamp):** `ReliableSender::new` (soe_send.rs:95-114) rejects configurations too small for the header and first fragment, and returns an error rather than panicking.
- **`decode_controls` / `flatten` / `clock_reflect` (session.rs):** the child length is checked, and nesting depth and output count are capped. Clock reflect checks the 38-byte payload length before indexing.
- **Session table (`run`, 826-909):** capped at 32 entries, aged out by time and by a missing principal. Replacement of an occupied peer is blocked, as the comment says.
- **Atomicity:** replies are queued after the RC4 `tx` step, and any later error ends the session. No two-save ordering problem is visible in this window.

Possible but not shown (not reported): `Broker::poll` (line 319) and the main loop (line 891) propagate non-transient accept/recv errors with `?`, which would exit the process. I could not establish a remote trigger on Linux. Also, a single authenticated datagram can fan out to many `application()` calls, each reloading the account store and resources from disk. That is a performance concern, not a defect with a concrete failure.
