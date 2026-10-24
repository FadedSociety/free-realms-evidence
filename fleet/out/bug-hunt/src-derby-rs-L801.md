<!-- fleet job=bug-hunt id=src-derby-rs-L801 status=done turns=12 usd=0.0200 tokens(read,write,in,out)=[308680, 48380, 26, 21811] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/derby.rs lines 801-1600 of 1960

## Findings

- **[medium] prototype/osfr-tools/src/derby.rs:1322-1329 - `contact` accepts a VehicleHit from an attacker whose vehicle is destroyed (`health == 0`, waiting for respawn), so a dead car still deals damage, scores knockouts, and can knock out a victim during its own respawn timer.**
  - **Failure scenario:** The owner's car is knocked out at time T (`health = 0`, `respawn_at_ms = T+4s`, `derby.rs:1436-1437`). The owner's client keeps sending `34/16` VehicleHit reports while dead, with its pose inside `contact_radius_m` of a living driver (an NPC is enough). Each report passes every guard in `contact` (phase Running, reporter/other checks, connected, impact range, fresh poses, distance, damage cap, victim alive, cooldown). Then `damage_dealt` is credited (`:1416`), the victim loses health, and on a knockout the dead attacker gains `knockout_points` (`:1430`). Each such report is relayed to the other humans as well (`:1401-1404`).
  - **Reach:** `derby_gateway.rs:373-387` (`DerbyGateway::handle`) → `DerbyService::handle_client(owner, inner, now_ms)` (`derby.rs:1086-1091`, arm at `:1120-1121`) → `contact`. Nothing upstream checks attacker health. `relay_pose` (`:1287-1314`) also accepts poses from a dead car, so the attacker's position stays fresh.
  - **Inconsistency:** `pickup_hit` refuses a dead sender with `self.drivers[&sender].state.health == 0` (`derby.rs:1481`), and `contact` refuses a dead victim (`:1383-1386`), but nothing stops a dead attacker. The rule the code applies everywhere else is that a destroyed car does nothing.
  - **Fix:** Add `|| self.drivers[&sender].state.health == 0` to the guard list at `derby.rs:1322-1329`, next to the `is_connected_human(sender)` check. Optionally add a test next to `contacts_apply_server_damage_knockout_scores_and_four_second_respawn` (tests/derby.rs:351) that a hit reported by a zero-health attacker is ignored.
  - Impact is limited to in-match score and health. The completion reward is a flat grant that does not depend on score (`derby_gateway.rs:470-488`, F164 note), so I rate this medium, not high.

## Considered and dropped

- **Gate stall on disconnect (`acknowledge` `derby.rs:1235`, `countdown` `:1262`, `RegisterPlayer` `:1102`, vs `disconnect` `:1735-1743`).** When a human leaves after the others have already passed a gate, nothing re-checks the gate, so the match can stall. It is not reachable in the shipped build: `DerbyGateway` binds one owner and only ever routes to that owner (`derby_gateway.rs:507-523`), `add_human` has no caller outside `derby.rs:946`, and `disconnect` has no caller in `derby_gateway.rs`. It would only matter for a multi-human caller that does not exist yet.
- **`handle_close` `closed` set not pruned on disconnect (`derby.rs:1778-1779`).** Same reason: single-human production path only.
- **`fill_npcs` key collision (`derby.rs:1176-1179`).** It needs a participant key in the `0xd0…` range; keys are session-assigned, and I found no client path that controls them.
- **`countdown` `countdown_value -= 1` (`:1271`) underflow.** Not reachable: the decrement runs only when `count == countdown_value != 0`.
- Panic checks on `unwrap`/indexing in the window (`:1173`, `:1299`, `:1334-1344`, `:1361`, `:1415-1436`, `:1481`, `:1512-1513`, `:1565`, `:1681`, `:1715`) are all preceded by a membership or connected-human check, or are reached only with a non-empty driver set.
- Client-supplied NaN/inf in poses, positions, impact and pickup positions is rejected before any arithmetic (`pose_position` `:1849`, `:1330-1331`, `:1490`).
- The contact multiplier and damage clamp (`:1377-1379`) cannot panic: `as u32` saturates and `clamp` bounds the value.
- Trusting client-reported contacts and poses is the documented design (F164). Only the bounds (cooldown, damage cap, radius, freshness) apply, and they are enforced.
