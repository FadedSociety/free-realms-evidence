<!-- fleet job=test-audit id=tests-soe-loopback-rs-L1 status=nothing_found turns=4 usd=0.0024 tokens(read,write,in,out)=[13391, 9451, 10, 2211] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soe_loopback.rs lines 1-52 of 52

Reviewed `prototype/osfr-tools/tests/soe_loopback.rs` lines 1-52 (`exchanges_reference_handshake_over_loopback_udp`) against `src/bin/soe-probe.rs`, which it spawns, and the fixtures.

- Cannot fail: no. The expected bytes come from `tests/fixtures/session-response.bin`, a fixture recorded from the legacy server (per `tests/fixtures/README.md`), not from `session_response()`. The test would fail if the probe stopped replying, replied with different bytes, replied from the wrong peer (line 46), or exited non-zero (line 51).
- Malformed datagram (line 40): if the probe answered it, `recv_from` on line 45 would return that reply first and the byte comparison on lines 47-50 would fail. The probe's ignore path (`eprintln!` on Err, soe-probe.rs:41) is therefore covered indirectly. It is not asserted directly, but the name does not claim it.
- Silent skip: no `#[ignore]`, no early return. The fixtures exist (they are also used by `tests/session.rs`, `tests/transport_fuzz.rs` and the probe's unit tests, and `include_bytes!` would not compile without them).
- Name vs body: "exchanges reference handshake over loopback UDP" matches the body (real UDP bind, send, receive, exit status).
- Over-pinning: the 128-byte buffer is larger than the fixture response; no incidental count or offset is pinned.

No findings in this window.
