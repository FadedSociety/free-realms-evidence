<!-- fleet job=bug-verify id=src-session-rs-L1-f1 status=done turns=13 usd=0.0112 tokens(read,write,in,out)=[229802, 34019, 28, 9234] model=claude-haiku-5-5 -->
# medium: session.rs:80

**Verdict:** confirmed

**Severity if confirmed:** medium. A peer that coalesces a child of 254+ bytes gets its whole datagram dropped (or a misparsed bundle accepted), so its reliable packets are never acked and it retransmits. Nothing here corrupts saves or grants items or coins, and it does not crash the server.

**Evidence:**

1. **In the real server.** `src/lib.rs:79` declares `pub mod session;`, and `session.rs` lives at `prototype/osfr-tools/src/session.rs` (not under `restoration/`, and not `#[path]`-included). It is used by the live binaries: `bin/osfr-gateway.rs:20` and `:1271`, `bin/osfr-login.rs:11` and `:522`, and `bin/osfr-bot.rs:21`.

2. **Reachable from the wire.** In `osfr-gateway.rs:1233`, only datagrams whose first byte is `5` are diverted to `decode_kart_pose_datagram`. Opcode 3 (Multi) falls through to `decode_controls(&self.codec, wire)` at `:1271`. `decode_controls` (`session.rs:52-65`) calls `codec.decode`, which has no special case for opcode 3 (`soe.rs:145-170`), and then `flatten`. No check upstream of `flatten` handles the escape.

3. **The defect is at the cited line.** `session.rs:80` reads `let length = usize::from(remaining[0]);` as a single byte. `session.rs:82` then rejects `length < 2 || length > remaining.len()`. There is no `0xFF` escape anywhere in `session.rs` or `soe.rs`.

4. **The reference uses the escape.** `refs:Sanctuary/src/Sanctuary.UdpLibrary/Internal/UdpMisc.cs:94-113` (`GetVariableValue`) reads `0xFF` as a 2-byte big-endian length, or a 4-byte length when the next two bytes are `FF FF`. `PutVariableValue` (`:115-143`) writes `FF hi lo` for values ≥254. The receive loop at `UdpConnection.cs:1152` uses `GetVariableValue`.

5. **The reference does emit such children.** `UdpParams.cs:483` sets `Reliable[0].Coalesce = true`, and `UdpReliableChannel.cs:106-109` sets `MaxCoalesceAttemptBytes = MaxDataBytes - 5`. That is a few hundred bytes at default fragment sizes, so children of 254+ bytes are allowed through `SendCoalesce` (`:969-1017`). Note that `:1005` writes the length with `PutVariableValue`.

6. **Failure arithmetic checks out.** For a final child of exactly L=254 bytes, the Rust code reads `FF` as 255, consumes 255 bytes, and leaves 1 trailing byte. That byte is always `<2` or `>0` remaining, so `flatten` returns `Err`, as claimed. For L≥255 the misframing does not always reject. The tail can parse as valid children, so garbage opcodes could reach the reliable receiver. The original report understates this case, but the defect stands.

**Corrected fix:** the proposed fix matches the reference decoder. In `flatten`, if `remaining[0] == 0xFF`: when `remaining.len() >= 3` and `remaining[1..3] == [0xFF, 0xFF]`, take a 4-byte big-endian length from `remaining[3..7]` (after checking `remaining.len() >= 7`), consuming 7 bytes in total. Otherwise take a 2-byte big-endian length from `remaining[1..3]` (after checking `remaining.len() >= 3`), consuming 3 bytes in total. Otherwise use the single byte. Keep the `length < 2` and `length > remaining` checks. No test covers the escape: `tests/login.rs:724` and `tests/login_broker.rs:480` use `decode_controls`, but the test files contain no Multi child of 254+ bytes.
</result>
