<!-- fleet job=bug-hunt id=src-restoration-piece-072-rs-L1 status=nothing_found turns=6 usd=0.0053 tokens(read,write,in,out)=[61680, 22415, 14, 3848] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_072.rs lines 1-470 of 470

Window reviewed: `prototype/osfr-tools/src/restoration/piece_072.rs` lines 1-470 (the whole file), plus the test file `tests/piece_072.rs` lines 100-240 for the intended behaviour.

No defect I can tie to a line and show is reachable from client input or a save.

What I checked:
- **Panics on client bytes:** `decode_client_completion` (459-470) checks `packet.len() == 7` before any indexing, so `packet[0..=6]` is in range. `i32::from_le_bytes` on the four-byte slice cannot fail. Opcode and message type are checked before the id is used.
- **Integer overflow:** `encode_ui_event_registration` (437-451) casts `bytes.len() as i32` only after `validate_event_name` caps it at 64. The capacity sum cannot overflow.
- **Atomicity:** `register` (310-338), `complete` (353-377), `complete_failed` (380-390) and `clear` (393-398) all validate and return errors before any mutation. `complete` marks `completed = true` only on the final success path. The `change_scope` clear is an intentional scope reset.
- **Trusting the client:** the completion packet carries only the id. The scope comes from the caller (`actor_scope`), and the id must already be in the server-side `BTreeMap`. Event strings come from server-side `register` calls, not from packets.
- **Unbounded growth:** registrations are keyed by `i32` in a map. No client-driven path reaches `register` in this file.

Reach: the module is not wired into the production server. The only consumers are `tests/piece_072.rs` (via `#[path]`) and the Python script. Nothing in `src/` calls `ClientObjectiveRegistry`, `complete`, or `decode_client_completion`, so no live packet reaches this code today.

Not reported: `validate_event_name` (line 429) rejects the space character, while the doc comment at line 211 says "printable ASCII". This is a doc/code mismatch, but it fails closed, the event names are server constants, and it has no reachable effect, so I do not count it as a defect.
