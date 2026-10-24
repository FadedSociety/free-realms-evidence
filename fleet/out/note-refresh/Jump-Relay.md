<!-- fleet job=note-refresh id=Jump-Relay status=nothing_found turns=17 usd=0.0189 tokens(read,write,in,out)=[539465, 57312, 36, 12684] model=claude-haiku-5-5 -->
# notes/Research/Jump Relay.md

**Verdict:** current. Every code claim I checked matches the tip. The one open point is a client-side IDA statement that the client database now contradicts; I left it as Unsure rather than correct it.

**Corrections:** none.

What I checked and found true:
- **Constants and layout:** `OPCODE = 164`, `BODY_LEN = 40`, `MAX_VERTICAL_SPEED = 100.0`, `RELAY_RATE_PER_SECOND = 10.0`, `RELAY_BURST = 4.0` (`repo:prototype/osfr-tools/src/jump_relay.rs:15-32`). `decode` checks the length, opcode and GUID, and checks position and direction for finiteness and the 1,000,000 bound. It clamps the velocity and refuses a non-finite one (`jump_relay.rs:98-128`). `relay` writes the 40-byte layout with the impulse's state/unknown/velocity (`jump_relay.rs:135-146`).
- **Parse arm and staging:** the 164 arm calls `jump_relay::decode` and reads 38 more bytes before `reader.end()` (`repo:prototype/osfr-tools/src/gateway.rs:630-635`). `Event::Position` carries `Option<JumpImpulse>` (`gateway.rs:391`). An application child clears the impulse (`gateway.rs:1638`). A later accepted jump replaces it, so the last one wins (`gateway.rs:1582`). The body is built once after the last child (`gateway.rs:1807-1808`). `reset_session` clears it (`gateway.rs:1402`).
- **Delivery:** `jump_fanout` uses `nearby_sessions` plus `knows_character`, excludes the sender, applies the budget with `Instant::now()`, and runs only after commit via `post_commit` (`repo:prototype/osfr-tools/src/bin/osfr_gateway/delivery.rs:21-84`; `osfr-gateway.rs:1669-1684`). `forget_jump_relay` is called from `end_session` (`osfr-gateway.rs:4401`, `4450`).
- **Budget state:** `Security.jump_relays` is a `KeyedBuckets<u64>` (`osfr-gateway.rs:508-522`). `KeyedBuckets::remove` exists (`repo:prototype/osfr-tools/src/net_policy.rs:100`).
- **Tests named in the note exist:** `tests.rs:936` (directed cap and throttle), `tests.rs:1514` (end_session leave cleanup), `tests/gateway.rs:284` and `:299` (reset and a later application child), `tests/app_fuzz.rs:897` (hostile 164 seed), and the `jump_relay.rs` unit tests at `:171` and `:202`.
- **Client addresses:** `FUN_008b3b70`, `FUN_009127f0`, `FUN_008e5ba0`, `FUN_0092e670`, `FUN_008fb810`, `FUN_00984960` and `FUN_008b3180` all exist in the client DB. The sender's `+0x868` gate and `+0x3e4` / `+0x674` reads appear in its pseudocode.
- **Reference:** `PlayerUpdatePacketJumpHandler.cs` exists in `refs` (FreeRealms-Legacy).

**Unsure:**
- The Recovered client facts section says the handler "`0090e470` (disassembly; IDA does not define this body as a function)". The client DB (`client_sql`, `fn` table) has `FUN_0090e470` as a defined function, `__thiscall FUN_0090e470(int, float, int)`, 3,271 bytes of pseudocode. It calls `FUN_008e5ba0`, `FUN_00984960` and `FUN_008b3180`, and tests `param_1+200` against the actor. Either the note predates the function being defined, or the body is defined only in the DB and not in the IDB the note cites. I could not confirm the bit-2 / bit-0 branch offsets (`0x0090e5f5`, `0x0090e627`, `0x0090e62f`) against the pseudocode, because the decompile does not show them in a form I could grep. A human with the `.i64` should settle this.
- The header's "native two-client acceptance pending" and the Known gaps entry are consistent with `notes/Autopilot/F266.md`, F290 and F323, which record no native two-client run. I did not look for a later run.
