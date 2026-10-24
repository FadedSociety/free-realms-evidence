<!-- fleet job=note-refresh id=SOE-Transport-Notes status=done turns=11 usd=0.0127 tokens(read,write,in,out)=[253863, 47347, 24, 8555] model=claude-haiku-5-5 -->
# notes/Research/SOE Transport Notes.md

**Verdict:** minor drift. Most checkable claims hold at the tip. One sentence is false: it says the Rust transport has no socket server or reliable sender, and both now exist.

**Corrections:**

- `old:` No socket server or reliable sender exists yet.
  `new:` The reliable sender now exists in `src/soe_send.rs` (bounded send window and queue, fragmentation, selective and cumulative ACKs, timed retransmission, retry failure). The loopback-only UDP servers `osfr-gateway`, `osfr-login` and `osfr-bot` use it with `ReliableReceiver`. Application bundles, encryption and persistence remain unimplemented.
  `why:` `repo:prototype/osfr-tools/src/soe_send.rs:81-94` (`ReliableSender`); `repo:prototype/osfr-tools/README.md:19` (`soe_send` row); `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:32,423-424,1047` and `repo:prototype/osfr-tools/src/bin/osfr-login.rs:15,441-442,463`; `repo:prototype/osfr-tools/src/bin/osfr-bot.rs:25,237-238`; `repo:notes/Design/Build Ledger.md:34` (the ledger's "SOE transport and sessions" row records the loopback-only binding).

**Checked and holding (no change needed):**

- Session probe: `session.rs:6` sets `CRC_SEED = 1_884_358_976`. `session.rs:35-47` builds a 21-byte response: opcode 2, echoed id, seed, crc length, flag 1, flag 0, echoed buffer size, trailing u32 3. The request layout matches `session.rs:17-24`.
- `soe.rs` has the codec and `ReliableReceiver` (`soe.rs:315`). Future DATA is size-checked before the selective ACK (`soe.rs:407-420`), and `poisoned` exists (`soe.rs:324`).
- Test counts: `tests/soe_transport.rs:71` asserts 105 serializer vectors. `soe_transport.rs:346-380` uses 131,104 sequences across rollover. The 1,253 frames and 46 messages / 627,566 bytes match `tests/fixtures/TRANSPORT.md:19`, `MODLOG.md:177` and `notes/Tasks.md:72`.
- Three-byte CRC negotiated by the real client, and the two-byte synthetic fixture (`fixtures/README.md:7`), match `notes/Research/Client Baseline.md:24`. Sequences 0–1258 and the single out-of-order notice match `Client Baseline.md:38-40, 73`.
- Linked notes exist: `Client Baseline.md`, `Legacy Gateway Oracle.md`, `fixtures/README.md`, `fixtures/TRANSPORT.md`.

**Unsure:**

- `lab/manifests/legacy-handshake-probe.json` and `lab/decompiled/server/LibSOE` are not in the repo tip (`lab` is not a directory here), so the live-probe claim and the `HandlePacket` CRC-loop claim (`4 - CRCLength`, loop while `< CRCLength`) could not be checked against the supplied binary. `refs:OpenSourceFreeRealms/ofrserver/Server/LibSOE/Core/SOEProtocol.cs:111-112` shows the same loop, so the note is consistent with that copy.
- Receiver semantics: `soe.rs:365` says a direct `Err` leaves state unchanged except when it first expires a timed-out fragment. The note's sentence "Direct errors leave receive state unchanged" omits that exception. This is a nuance, not a falsehood, so I did not propose a change.
