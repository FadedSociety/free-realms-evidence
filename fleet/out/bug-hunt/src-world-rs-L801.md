<!-- fleet job=bug-hunt id=src-world-rs-L801 status=nothing_found turns=10 usd=0.0197 tokens(read,write,in,out)=[266922, 48354, 22, 21997] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/world.rs lines 801-1600 of 1624

No defect I could tie to a line in `world.rs` 801-1600 that a remote client can reach. Read the full window and the callers that matter (`osfr-gateway.rs` 1690-1975 transfer/commit path, 2387-2420 `heal_group`; `f160_field_views.rs`; `t020_group_routing.rs`).

Candidates checked and dropped:

- **`commit_membership` 1049-1080, `.expect` calls at 1063 and 1078:** the prepared instance is either validated in `prepare_membership` or inserted by the same commit, and nothing runs between prepare and commit (the gateway only commits after save succeeds). The invariant holds.
- **`prepare_membership` 990-1046, target path:** the client never supplies `target`. The gateway passes a server-side pending transfer or the player's existing instance, and the zone match at 1012 is checked anyway.
- **`enter_instance` 1275-1320:** `build_sequence`, which can fail, runs before any membership mutation, so a failure leaves the previous instance and pose intact. The `unwrap` at 1304 follows a successful lookup at 1282.
- **`enter_public` 1192-1215 and `enter_dungeon` 1241-1271:** on failure the created instance and its public mapping are rolled back. The only leftover is a skipped `next_instance_id` value, which is harmless.
- **`claim_group_heal` 875-886:** the claim is keyed by (instance, guid, ms), and `kill` comes from server-side `encounter.rs` drops, not from the client. The 256-entry cap works as documented.
- **`stage_public` 1137-1163 and `instance_id_free`/`instance_id_available` 1167-1180:** ids cannot collide with live instances, public mappings, or zone ids. `available_public_id` ends at `i32::MAX`, so it cannot overflow.
- **`collect_empty_instances` 1363-1394:** parents are kept until their children are gone, public instances are never collected, and a player's instance always has that player as a member, so no live player's instance is removed.
- **`mark_zone_ready` 1324-1344 and `field_for_player` 891-901:** the `unwrap` at 1341 follows a successful lookup, and `field_for_player` checks `ready` and the zone.
- **`build_sequence` 1447-1516 and `to_wire_npc` 1518-1557:** all fallible conversions return errors, and the pose is checked for finiteness.

Non-defect observation (not reported as a finding because the code comment at 1426 documents it as intended): `available_instance_id` at 1425-1435 caps non-public instances at 16 and counts retained empty children. One client that changes unseeded scenes 16 times within the empty grace window can make later unseeded entries fail with `InstanceIdsExhausted` until the grace expires. This is a sizing and fairness question, not a memory or panic defect.

Out of window, noted only: `mark_zone_ready` is never called from the client's ready callback in production; `commit_membership` drives readiness from `is_world_loaded()`. `notes/Research/World and Instances.md` line 105 records this as a known pending step.
