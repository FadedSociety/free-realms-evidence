<!-- fleet job=bug-hunt id=src-soe-send-rs-L1 status=nothing_found turns=7 usd=0.0099 tokens(read,write,in,out)=[73954, 27707, 16, 11388] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soe_send.rs lines 1-309 of 309

Reviewed `prototype/osfr-tools/src/soe_send.rs` lines 1-309 in full, plus the `Codec::encode` contract in `soe.rs:117-140` and the ACK opcode constants (`soe.rs:16-22`). No defect I could tie to a line and show reachable from client input.

Checked and ruled out:

- **Underflow in `queue_message`** (`soe_send.rs:147`, `171`, `194`, `203`): `retained_bytes` only grows by `bytes`, and each addition is gated by `wire.len() <= available - bytes`, so `bytes <= available` always holds. The constructor's `datagram_limit >= empty_wire.len() + 5` (line 108) guarantees `data_capacity >= 5`, so `data_capacity - 4` cannot underflow.
- **Shrink loop termination** (`soe_send.rs:173-193`): an oversize result reduces `take` by at least 1, and the constructor's 7-byte probe (line 110) guarantees a small uncompressed fragment fits, so `take == 0` (the `InvalidConfiguration` return) is not reachable from a server-generated message. Every error path returns before any state is mutated.
- **Atomicity**: `sequence`, `next_sequence`, `retained_bytes` and `queued` change only after the last fragment is accepted (lines 203-205). `poll` returns `RetryLimit` before mutating anything except the terminal `failed` flag, and `acknowledge` returns `InvalidAcknowledgement` before any mutation.
- **ACK handling** (`soe_send.rs:259-294`): ACKs can only match entries in `pending`, which holds only sent packets, so unsent data cannot be released. Selective ACK on an already-released entry returns an error. The `pop_front().unwrap()` on line 281 is bounded by `position <= len-1`. Subtraction from `retained_bytes` mirrors additions, so it cannot underflow. ACK payload length is checked as 2 before indexing.
- **Duplicate sequences**: `pending` is always contiguous and capped at `window < 0x8000` (line 97, 241), so a `u16` match is unambiguous.
- **Clock and retry logic** (`soe_send.rs:216-240`): `sent_at` is always set from the monotonic `now_ms`, `saturating_sub` is used, and the `max_retries` semantics match their doc comment.
- **Unbounded growth**: queued and retained bytes are capped by `max_queued_bytes`, message size by `max_message` (capped at `MAX_LOGICAL_MESSAGE`), and the number of in-flight packets by `window`. ACK input cannot grow any collection.

Opcode mapping (17 = selective, 21 = cumulative) matches the constants in `soe.rs` and the Sanctuary `Ack1`/`AckAll1` references. I did not independently verify the wire semantics beyond that comparison.
