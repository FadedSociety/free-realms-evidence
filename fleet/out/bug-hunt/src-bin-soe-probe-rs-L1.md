<!-- fleet job=bug-hunt id=src-bin-soe-probe-rs-L1 status=nothing_found turns=5 usd=0.0026 tokens(read,write,in,out)=[22506, 9220, 12, 2421] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/soe-probe.rs lines 1-81 of 81

No defects found in `prototype/osfr-tools/src/bin/soe-probe.rs` lines 1-81.

What I checked:
- **Client-input path (lines 10-12, 28-31, 41):** every datagram goes to `SessionRequest::parse` (`src/session.rs:16-33`). That function rejects any length other than 24 before indexing, then checks the fixed `CGAPI_527\0` tag at bytes 14..24. The `from_be_bytes` reads at 2..6, 6..10 and 10..14 are inside the checked length. The CRC length (`> 4`) and buffer size (`64..=65_507`) are range-checked before use, so there is no panic, overflow or unbounded allocation on client bytes. The 65535-byte receive buffer covers the maximum UDP payload.
- **Loop (lines 29-43):** a rejected datagram is only logged and the loop continues. No state grows, and the loop ends after one valid response.
- **Send path (lines 33-35):** a failed `send_to` propagates an error. A short send is treated as an error, and nothing is mutated before it.
- **Loopback gate (lines 21-24):** non-loopback bind addresses are refused before `UdpSocket::bind`.
- **Response layout vs. the test (lines 63-69):** `session.rs:35-46` writes the id at bytes 2..6 and the buffer size at 13..17. The test offsets match, so the test is not wrong.
- **Tests (lines 53-81):** the index and slice operations are on fixed-length fixtures or within the checked lengths.

Not reported: the 10-second timeout (line 26) is applied per `recv_from` call, so a steady stream of junk datagrams keeps the probe alive. That fits the "idle" wording and the probe is a one-shot local tool, so I did not count it as a defect.
