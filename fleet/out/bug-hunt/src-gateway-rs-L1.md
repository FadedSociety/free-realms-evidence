<!-- fleet job=bug-hunt id=src-gateway-rs-L1 status=nothing_found turns=9 usd=0.0194 tokens(read,write,in,out)=[254991, 57367, 20, 19269] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gateway.rs lines 1-800 of 2232

No reportable defects in `prototype/osfr-tools/src/gateway.rs` lines 1-800 after reading the window and its callers.

What I checked:

- **Reader bounds (lines 165-230):** `take` uses `checked_add` and `get(..)`, so it cannot panic. `string(max)` checks the length before `take`. `vector` rejects non-finite and out-of-range values. The `unwrap`s on `try_into` follow a successful `take(n)` of the matching size.
- **Tunnel and bundle framing (lines 247-261, 655-688):** `tunnel` bounds `size` to `2..=MAX_MESSAGE` before `take`. `application_messages` rejects lengths under 2 or over `MAX_MESSAGE`, caps children at 128, and rejects nested bundles. Every loop iteration consumes at least one byte. The `child[..2]` and `bytes[..2]` indexes are safe because lengths are checked first.
- **Client-field authority (lines 589-653):** Login checks the guid and version. Position, opcode-125 and opcode-164 are checked against `state.guid`. Opcode 164 goes through `jump_relay::decode`, which requires exactly 40 bytes and the session guid (jump_relay.rs:98-107). Chat sender/recipient guids are ignored (chat.rs:37-51).
- **Role-change bundle rejection (lines 397-413):** The `.ok()` swallow on `chat::request` matches the dispatch path at gateway.rs:1657-1662 and gameplay.rs:3676. Both use the same `realm `/`role` normalisation, so a bundled role command is refused and a malformed one is not executed as a role command.
- **Combat routing (line 702):** `is_combat_request` is called per child from osfr-gateway.rs:1603-1607, so it never sees a whole bundle. Its treatment of 26/10 as combat is deliberate (encounter/shared.rs:381, f276 test) and is not contradicted by the `npc_interaction` label.
- **Handler table (lines 464-555):** Subtype offsets match their comments. The `[149,0,2]` and `[16,0]` special cases and the `word(0)` warp guard are consistent with their comments.
- **Group heal (lines 786-792):** `percent` is set server-side (encounter.rs:2236, `min(100)`), not taken from a client packet.
- **Reference loading (lines 311-385):** This reads operator-supplied files, not client input. The offset derivations check out (13 = 7 + 6 and 7 + 2 + 4), and the manifest offsets are validated against the derived ones before they are used to slice.

Possible issues I did not report because I could not show them as defects: the strict `bool()` on the tunnel flag byte, and the strict end-of-message check on opcodes 13 and 10. Whether a real client ever sends other values there is outside what I could verify.
