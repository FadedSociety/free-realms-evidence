<!-- fleet job=bug-hunt id=src-jump-relay-rs-L1 status=nothing_found turns=11 usd=0.0101 tokens(read,write,in,out)=[171325, 29880, 24, 9278] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/jump_relay.rs lines 1-250 of 250

No defects found in `prototype/osfr-tools/src/jump_relay.rs` lines 1-250 that a remote client can reach. I read the whole window and the callers that matter (`gateway.rs:630-634` decode, `gateway.rs:1499-1582` position/impulse handling, `gateway.rs:1638` application reset, `gateway.rs:1806-1816` commit, `delivery.rs:37-54` relay budget, and `movement.rs:200-384` validation).

Checks that came back clean:

- **No panic on client bytes (`checked_float`, `decode`, lines 87-128):** `decode` rejects any body whose length is not 40 before any slicing. Every offset used (opcode 0, guid 2-9, position 10-21, direction 22-33, state 34, unknown 35, velocity 36-39) is inside 40 bytes. Non-finite and out-of-range floats return `Err`. `from_le_bytes` cannot panic.
- **Gateway slicing (`gateway.rs:633`):** `reader.take(38)` runs after `reader.u16()` has consumed 2 bytes of a 40-byte inner body, so it cannot overrun.
- **No client-sized allocation:** `relay` (lines 135-146) always builds a 40-byte body, and the `debug_assert` holds.
- **Authority on pose and GUID:** the GUID is checked against the session GUID (line 105). The relayed position and direction come from `movement_state`, the validated pose, not the raw packet. `accepted_state` normalizes the horizontal direction in `movement.rs:340-361`.
- **Impulse lifecycle:** `impulse = jump.or(impulse)` (`gateway.rs:1582`) keeps a jump across a later 125 in the same bundle. The application reset at `gateway.rs:1638` drops it on zone change. `movement_state` and the other session fields are committed only at the end of the bundle (`gateway.rs:1806-1816`), after `budget.stage` can return `Err`, so there is no partial commit.
- **Velocity:** the clamp at line 120 is deliberate and matches the doc comment and the tests.

Not reported: the relayed `state`/`unknown` bytes and the clamped ±100 vertical impulse are client-supplied. The doc comments state this as intended, and the opcode-125 path already relays client state bytes the same way. Test code under `#[cfg(test)]` is excluded.
