<!-- fleet job=test-audit id=tests-multiplayer-rs-L1 status=done turns=10 usd=0.0122 tokens(read,write,in,out)=[240083, 40709, 22, 9451] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/multiplayer.rs lines 1-1200 of 3109

Window: `prototype/osfr-tools/tests/multiplayer.rs` lines 1-1200. Findings, most serious first:

- **[high] prototype/osfr-tools/tests/multiplayer.rs:982 the_seventeenth_connection_is_refused - the 17th probe is malformed, so the test passes whether or not the 16-session cap exists.**
  - Why it cannot catch a regression: line 997 sends `b"CGAPI_527 "` (trailing space) where every other handshake uses `"CGAPI_527\0"`. `session::SessionRequest::parse` (src/session.rs:20) requires `&wire[14..] == b"CGAPI_527\0"`, so the probe is rejected as malformed and never reaches the cap check at osfr-gateway.rs:4339. Deleting or raising `MAX_SESSIONS` still yields "no reply" at lines 1002-1005. The `active_session_count() == 16` checks at 988 and 1006 do not involve the 17th probe at all.
  - Fix: send a well-formed request with a fresh connection id (`"CGAPI_527\0"`, 24 bytes), and assert that the reply is absent AND that the refusal is the cap, e.g. via `refuse("session_cap")` in the security log or the trace. Add a control: after one of the 16 is dropped, the same well-formed request gets a `[0,2]` reply.

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:1048 two_clients_share_world_routing_but_keep_their_sessions_and_saves (say and tell checks at 1100-1112) - the delivery checks pass on the sender's own echo.**
  - Why it cannot catch a regression: `first.send(...)` returns the sender's own messages, and the result is unioned with `second.drain()`. The gateway deliberately echoes say back to the sender (osfr-gateway.rs:2267 "never the sender's echo"; `chat_candidates` at 854-877 does not exclude the sender). So line 1103 passes on first's echo even if the say is never delivered to second. The tell check at 1108 has the same union shape.
  - Fix: drain only the recipient and assert on the recipient's socket, e.g. `second.drain(&mut server)` must contain 15/1 with `"synthetic say"` bytes present. Check the text, not only the family.

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:1027 a_vanished_client_does_not_stop_the_server - the reset path is not exercised on Linux, so the test cannot fail for that regression.**
  - Why it cannot catch a regression: the comment says Windows reports ConnectionReset, but the server's socket is unconnected (osfr-gateway.rs:3760-3771). On Linux no ICMP error is delivered, so removing the `ConnectionReset` arm leaves the test green. The only assertion, `active_session_count() == 2` at 1044, is true before any datagram is sent to the closed port.
  - Fix: either exercise the reset deterministically (e.g. a connected test socket or a fault-injection hook that returns `ConnectionReset` from `recv_from`), or assert on the post-reset behaviour, i.e. that the chat at 1040 is actually delivered to `first` after the reset (check the echo bytes "still here"), and mark the Windows-only limit in the name or doc.

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:1013 a_connection_that_never_logs_in_is_dropped - the count cannot tell which session was dropped, so the "logged-in player is unaffected" half is never checked.**
  - Why it cannot catch a regression: after the sleep, `active_session_count() == 1` (line 1021) is satisfied by the lurker surviving and the player being dropped. The doc's "KeepAlive or not" is also never exercised: no keepalive traffic is sent.
  - Fix: after the step, send a chat or move from `_player` and assert it is still answered (or that `_player` is in the session set). Assert the lurker's removal by its id (e.g. the `login_deadline` event in the security log), not just the count.

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:942 an_account_past_its_action_budget_is_dropped_and_logged - the rate-limit bound goes vacuous when the run is slow.**
  - Why it cannot catch a regression: `refill` is derived from wall time (line 961). When the 30 sends take 4 s or more, `accepted <= 10 + refill.ceil()` is at least 30 and cannot fail. The refusal-log check is also gated on `refill < 15.0` (line 973). A server with no budget at all would pass on a slow machine.
  - Fix: drive the bucket deterministically (a fixed clock or `spine_pins`-style injected time) and assert `accepted == 10` plus the `budget_refusal` log line. If wall time must stay, assert the refusal count directly for the burst window (requests issued within <1 s) and fail if the run is too slow to test it instead of passing silently.

- **[low] prototype/osfr-tools/tests/multiplayer.rs:708 audit_content_social_delivers_without_trace - the name says "without trace", but the body never inspects the trace/log output.**
  - Why it cannot catch a regression: the body only asserts delivery (say/tell/friend/group). A regression that writes character names or chat bodies to the trace would pass.
  - Fix: after `server.shutdown()`, read the trace/security log in `temp` and assert it does not contain the say/tell text or the character names, or rename the test to drop "without_trace".

Notes: the ignored tests at 708 and 786 do carry reasons. The second one's final `println!` at 934-936 claims "tracing off; Studio disabled", which nothing asserts; I did not list it separately. Line 1142 and the other `saved["profile"]` checks look sound.
