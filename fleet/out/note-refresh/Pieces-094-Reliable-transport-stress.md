<!-- fleet job=note-refresh id=Pieces-094-Reliable-transport-stress status=done turns=12 usd=0.0113 tokens(read,write,in,out)=[214836, 31353, 26, 10460] model=claude-haiku-5-5 -->
# notes/Research/Pieces/094 Reliable transport stress.md

**Verdict:** minor drift on line citations, plus one substantive error: the note says the gateway is single-peer and multi-client serving is absent. The code keys sessions per peer. The harness, test count, CRC seed, the zero-trailer refusal and the not-yet-registered `pub mod piece_094;` all still hold.

**Corrections:**

1. `old:` single-peer: datagrams from any other peer are ignored while a session is active.
   `new:` multi-session: sessions are keyed by peer (`session_key_for_peer`), capped at `MAX_SESSIONS` = 16 and `MAX_SESSIONS_PER_IP` = 4. Without an account store, a second live session is refused with `single configured character state is already in use`. A non-handshake datagram from a peer with no session is not routed to any session; a new handshake from another peer is accepted.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:3717 (`else if let Some(key) = self.session_key_for_peer(peer)`), :4305-4306 (`session_key_for_peer`), :4330-4333 (replace the same peer's session), :4339-4346 (caps and the single-character refusal), :2943-2944 (`MAX_SESSIONS`, `MAX_SESSIONS_PER_IP`).

2. `old:` Multi-client serving is genuinely absent, not merely untested: the gateway handles one peer.
   `new:` Multi-client serving is only partly present: the gateway keys sessions per peer (up to 16, 4 per IP), but with no account store it still admits one live character session. The several-peer path is not exercised by 094.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:4305-4346 and :2943-2944. Piece 099 (`src/restoration/piece_099.rs:1`) is the multi-client integration harness.

3. `old:` `generation = generation.wrapping_add(1)` (line 301)
   `new:` `generation = generation.wrapping_add(1)` (line 4358)
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:4358

4. `old:` `seed = CRC_SEED ^ generation`
   `new:` `seed = CRC_SEED ^ generation` (line 4359; the note's "line 302" is now stale)
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:4359

5. `old:` line 130). The running gateway itself is
   `new:` line 1006). The running gateway itself is
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1005-1006 (`gateway requires a nonzero CRC trailer`)

6. `old:` `Codec` line 77
   `new:` `Codec` line 89
   `why:` repo:prototype/osfr-tools/src/soe.rs:89 (`pub struct Codec`)

7. `old:` `ReliableReceiver` line 255, `receive` line 306
   `new:` `ReliableReceiver` line 315, `receive` line 369
   `why:` repo:prototype/osfr-tools/src/soe.rs:315 (`pub struct ReliableReceiver`), :369 (`pub fn receive`)

8. `old:` `ReliableSender` line 80, `queue_message` line 131, `poll` line 206, `acknowledge` line 253
   `new:` `ReliableSender` line 81, `queue_message` line 137, `poll` line 212, `acknowledge` line 259
   `why:` repo:prototype/osfr-tools/src/soe_send.rs:81, :137, :212, :259

9. `old:` line 291)
   `new:` line 297)
   `why:` repo:prototype/osfr-tools/src/soe_send.rs:297 (`pub fn pending_packets`)

**Checked and holding:**
- `session.rs:6` is `CRC_SEED = 1_884_358_976`.
- `tests/piece_094.rs` has 5 `#[test]` functions, matching "5 passed".
- `src/restoration/piece_094.rs` exists.
- `pub mod piece_094;` is not yet in `src/lib.rs`, so the integration step is still pending.
- `scripts/pieces/piece_094.py` and `tests/pieces/test_piece_094.py` exist.
- `SELECTIVE_ACK` = 17 and `CUMULATIVE_ACK` = 21 (`soe.rs:18-19`).
- `max_queued_bytes` is in `SenderConfig` (`soe_send.rs:24`).
- `SendError::RetryLimit` exists (`soe_send.rs:41`).

**Unsure:**
- The acceptance-table counts (for example 1200/1200, stale rejected 16, retained peak 1614/8192) come from a lab report outside the roots. I could not check them, and I did not run the tests.
- The note's `lab/reports/...` run IDs are not visible from the repo, so I did not check them.
- Gateway replacement: a new handshake from the same peer replaces that peer's old session (`osfr-gateway.rs:4330-4333`). The note does not describe this path, so I did not change it.
- The note's "Session replacement" ordering claim was not checked beyond the `generation`/`seed` lines.
