<!-- fleet job=bug-verify id=src-bin-osfr-gateway-rs-L2401-f1 status=done turns=8 usd=0.0051 tokens(read,write,in,out)=[70267, 15051, 18, 5037] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/bin/osfr-gateway.rs:2427-2428

**Verdict:** confirmed (the defect is real and reachable, but the claim understates its effect in one way and the severity is closer to low-medium).

**Severity if confirmed:** medium. Nothing here is a crash, save corruption, or item/coin gain. The effect is a skipped group heal for the other members, a state/display mismatch for the refused member, and a disconnect of the picker.

**Evidence:**

1. **Real server code.** `heal_group` is at `src/bin/osfr-gateway.rs:2387`, a binary file, not a test-only `#[path]` module. Its caller is `commit_outcome`, which calls `self.heal_group(heal, world, membership, sessions)?` at `osfr-gateway.rs:2038-2039` (called from the gateway dispatch at `:2449`).

2. **Claimed path is accurate.** At `osfr-gateway.rs:2399`, `membership.claim_group_heal(...)` is recorded before the member loop. That claim is stored in `world.rs:875-886`, so a retry for the same kill returns `None` at 2400. At `:2422-2425`, the staged member state is saved and assigned before the reply is queued. At `:2427-2429`, `session.queue_shared_message(...)?` propagates the error. The loop at `:2407` is therefore aborted, and later members are skipped with no retry.

3. **QueueFull is a normal, reachable condition.** `soe_send.rs:154-158` and `:194-196` return `SendError::QueueFull` when the queued bytes exceed the limit. Nothing upstream of `heal_group` checks queue state. The gateway's `queue_shared_message` at `osfr-gateway.rs:2373-2381` just forwards the error.

4. **Inconsistency with the field path is real.** `osfr-gateway.rs:3147-3149` and `refuse_field_delivery` at `:3176-3182` refuse only the affected recipient and continue. `queue_field_deliveries` at `:3192-3193` does the same.

5. **Extra effect the claim understates.** The `Err` from `commit_outcome` propagates to the picker's `handle` path. In `osfr-gateway.rs:3735-3754`, `Err(error)` calls `self.end_session(key, current, ...)`, so the picker's session is ended after its own commit. A member's full queue therefore disconnects the picker, not just skipping the other members.

6. **Not a unique defect.** The claim that "M1 has healed HP the client was never told about" is also true of the field path. There the state is saved before the reply is queued, and a refused reply is simply dropped. So that part is consistent with the existing design. The real inconsistency is the abort of the whole loop and the picker disconnect.

**Corrected fix:** the claimed fix is correct. Replace the `?` at `osfr-gateway.rs:2428` with a logged refusal and `break` from the reply loop, so the member loop continues. `session.character_guid` is already used the same way at `:3179`:

```rust
for reply in healed.replies {
    if let Err(error) = session.queue_shared_message(&wrap_application(&reply)) {
        event(json!({"event":"group_heal_refused","character":session.character_guid,"reason":error.to_string()}));
        break;
    }
}
```

This also stops the picker's session from being ended by a member's queue state.
