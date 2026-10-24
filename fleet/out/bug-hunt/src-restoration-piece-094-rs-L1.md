<!-- fleet job=bug-hunt id=src-restoration-piece-094-rs-L1 status=nothing_found turns=8 usd=0.0152 tokens(read,write,in,out)=[132916, 38546, 18, 18068] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_094.rs lines 1-656 of 656

No reportable defects in `prototype/osfr-tools/src/restoration/piece_094.rs` lines 1-656. I read the whole file, plus the production callees it drives (`soe.rs` Codec::new/encode/decode, ReliableReceiver::new/receive_at, `soe_send.rs` ReliableSender::new/queue_message/poll/acknowledge/pending_packets).

Candidates checked and dropped:

- **pump, piece_094.rs:525-526** (`packet.payload[0], packet.payload[1]` with no length check). Can panic only if a sender-produced wire decodes to a payload shorter than 2 bytes. Every RELIABLE_DATA/FRAGMENT payload starts with the 2-byte sequence (`soe_send.rs:152, 177`), and the wires come only from `sender.poll`, not from the network. Not reachable from client input.
- **apply_ack, piece_094.rs:638 and 649** (`retained_bytes -= bytes`, underflow?). `retained_bytes` is incremented only on a fresh `outstanding` insert, decremented only on a successful `remove`, and both are reset together in `replace_session` (lines 328-329). The two counters stay consistent, so no underflow.
- **apply_ack cumulative release, piece_094.rs:645** (circular `< 0x8000` comparison). Matches the production cumulative pop in `soe_send.rs:280-284` for in-window sequences. Selectively acked entries are already removed from `outstanding`, so nothing is double-subtracted.
- **replace_session, piece_094.rs:311-333** (mutation before a fallible step). The only fallible call, `Client::new`, runs before any field is touched. Stale in-flight frames are rejected by the codec seed or the session tag, as the doc comment says.
- **deliver, piece_094.rs:604-606 and 596-600** (stale/corrupt accounting). Counters only; no state corruption.
- **deliver, piece_094.rs:607-613** (ignores `ReceiveOutcome.rejected_buffered`, soe.rs:302). Dropped as unreachable here: the harness feeds only sender-produced, uncorrupted frames, and the reassembly failure that sets this field cannot arise from a correctly sequenced sender. The later `ReceiverPoisoned` errors still surface in `receive_errors`, so the failure is not silent.
- **replace_session discarded count, piece_094.rs:323** (`pending_packets` also counts sent-unacked packets, while the doc says "unsent"). Observational counter only, not a defect.
- **Session/seed collisions across clients** (client 0's replacement session equals client 1's initial session). Datagrams are routed per client, so no cross-client acceptance is possible.
- **`crc_len == 0` accepted by the harness** (`Codec::new` allows it). This is the documented unguarded counterfactual, not an unintended path.
- **Unbounded `backlog`, `delivered`, `in_flight`.** Harness-owned; the caller controls them, and the production send queue is the bounded one.
