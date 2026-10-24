<!-- fleet job=bug-verify id=src-combat-rs-L1-f1 status=done turns=8 usd=0.0074 tokens(read,write,in,out)=[114445, 29343, 18, 5087] model=claude-haiku-5-5 -->
# medium: combat.rs:232

**Verdict:** refuted

**Severity if confirmed:** n/a

**Evidence:**

1. **Module tree (passes):** `lib.rs:13` `pub mod combat;`, `lib.rs:26` `pub mod gameplay;`, `lib.rs:27` `pub mod gateway;`, `lib.rs:56` `pub mod movement;`, `lib.rs:68` `pub mod players;`. `combat.rs` is the real module, and `gameplay.rs:2333` calls `self.handle(inner, character.guid, character.position, now_ms)`, so the range gate is live.

2. **Input does not reach `combat.rs` unvalidated (the claim fails here).** The claim says nothing upstream compares the reported position with server state. That is wrong. Client movement is handled in `gateway.rs` `Event::Position` (around lines 1499-1590):
   - `gateway.rs:1516-1518`: `elapsed` is computed from the server clock (`now_ms - last_movement_ms`).
   - `gateway.rs:1522-1533`: every client position goes through `movement::validate(&movement_state, update, state.zone_id, elapsed, SpeedModifiers { base_speed_per_second: 10.0, ... }, ...)`.
   - `gateway.rs:1547-1558`: `RejectAndSnapBack` sets `state.position = validated.state.position` (the previous server-held pose) and sends a location packet back. The position is not committed.
   - `gateway.rs:1536-1546`: `Ignore` leaves the position unchanged.
   - `gateway.rs:1566-1581`: only `Accept`/`Clamp` write `state.position = validated.state.position`.

3. **The validator does check speed and distance (the claim's premise is false).** `movement.rs:200-290`: non-finite and out-of-bounds positions are rejected. It requires `server_zone_id == previous.zone_id` unless a server-issued discontinuity token matches (`:263-269`). It computes `dx`, `dz`, and `dy` against `previous.position` (`:281-285`). It derives `soft_horizontal`/`hard_horizontal` from `max_speed * dt` (`:287-288`), where `dt` is the server elapsed time (`:280`). Over-speed is rejected or clamped. A teleport-to-enemy pose is therefore snapped back, and `state.position` never takes the reported value.

4. **The players.rs path is not the authority for gameplay.** `players.rs:378-417` (`update_pose_with_state`) stores the position only after `validate_pose`. That is a broadcast/registry copy. The gameplay `character.position` used by `combat.rs` comes from the gateway's `state`, which was already validated in step 2. The claim's chain (`players.rs:412` → `gameplay.rs:2333`) skips the gateway validator.

5. **Other sources of position.** The only position writes that bypass the client are server-owned: zone/scene/relocation placement at `gateway.rs:1735-1872`, and dev teleport, which emits a server location packet. None of these comes from a client-chosen coordinate in a movement packet.

**What remains (not a defect in the claimed sense):** a player can still walk to the training enemy at the validator's allowed speed (10 units/s with soft/hard multipliers), so the 8-unit range is enforced by movement in the normal way. Repeated farming is then limited by the 4 s cooldown, as the report itself notes. That is ordinary gameplay, not a range bypass.

**Corrected fix:** none needed for this finding. Drop it.
