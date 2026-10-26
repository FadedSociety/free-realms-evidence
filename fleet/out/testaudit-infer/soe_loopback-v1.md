<!-- fleet job=testaudit-infer id=soe_loopback-v1 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[15191, 11213, 8, 1186] model=claude-haiku-5-5 -->
# tests/soe_loopback.rs

{"file": "tests/soe_loopback.rs",
 "tests": [
  {"name": "exchanges_reference_handshake_over_loopback_udp", "verdict": "keep", "covered_by": null,
   "reason": "Only end-to-end check that the soe-probe binary, launched as a process, binds loopback UDP, ignores a malformed datagram, answers the synthetic session request with the exact compiled response bytes from the sender's address, and exits after one reply. tests/session.rs::shared_session_matches_compiled_fixture_and_real_client_crc_length checks the same fixture bytes only in-process via SessionRequest::parse(..).response(), with no socket, no process, and no malformed-then-valid ordering. The probe's unit tests in src/bin/soe-probe.rs cover the handshake in-process too, not the real wire path. Not clearly covered elsewhere, so keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Single test, slow-ish (spawns a process, 3s read timeout) but it is the only real-socket check of the probe binary. Overlaps in fixture bytes with tests/session.rs and tests/transport_fuzz.rs (which use the same fixtures in-process), but those do not exercise the UDP/process boundary. Probe is documented as historical in notes/Project Map.md; if the probe is retired, this file becomes obsolete together with src/bin/soe-probe.rs, not before."}
