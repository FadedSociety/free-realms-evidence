<!-- fleet job=bug-hunt id=src-soe-rs-L1 status=nothing_found turns=5 usd=0.0159 tokens(read,write,in,out)=[65845, 40461, 12, 20451] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soe.rs lines 1-540 of 540

I read `prototype/osfr-tools/src/soe.rs` lines 1-540 in full and checked the callers in `osfr-gateway.rs` (handle/send, expire_reassembly), `osfr-login.rs`, and `osfr-bot.rs`. I found no defect I could tie to a line and show reachable from client input.

Checked and cleared:
- **Indexing in `decode` / `decode_kart_pose_datagram` (145-219):** the `wire.len() < header_len + crc_len` guard keeps `content[0]`, `content[1]` and `content[2]` in bounds. The 95-byte pose checks short-circuit on `payload.len() != 95` before any index.
- **`inflate_bounded` (228-249):** `consumed <= input.len()` and `written <= chunk.len()` are checked before use. `max_payload - output.len()` cannot underflow because `output.len()` never exceeds `max_payload`. Every loop iteration consumes input or produces output, and a zero-progress `Ok` is an error, so the loop terminates.
- **`ReliableReceiver::receive_at` (376-456):** `payload.len() >= 3` is checked before any `payload[..]` access, and the buffered path is covered by the same check. `buffered_bytes` is incremented on insert and decremented on removal, and `expire_reassembly` resets both. Errors from `process_ordered` on the in-order path occur before any mutation. Buffer and reorder growth are bounded by `max_buffered` and by the window (< 0x8000).
- **`process_ordered` (493-539):** `expected_length` is bounded by `max_message`, and continuation fragments are bounded by the remaining expected length using `saturating_sub`. The partial is only created after all checks pass.
- **Doc-versus-code:** the stated behaviours in the doc comments (CRC trailer order, the 100-byte compression threshold, the ack opcodes, the expiry rules, and the poisoning on a rejected queued packet) match the code.

The only fatal-looking paths (AmbiguousSequence at distance 0x8000, ConflictingDuplicate, BufferLimit) are deliberate errors that end the caller's own session. They are not remote crashes or cross-player effects.
