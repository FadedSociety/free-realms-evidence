<!-- fleet job=note-refresh id=World-and-Instances status=done turns=17 usd=0.0200 tokens(read,write,in,out)=[537556, 58176, 36, 14795] model=claude-haiku-5-5 -->
# notes/Research/World and Instances.md

**Verdict:** badly stale. The coordinator is now registered and wired into the gateway binary, and the startup path has moved out of `gateway.rs`. The state machine and packet order described in the Model and Entry sections still match the code.

**Corrections:**

1. `old:` Status: W20 isolated coordinator candidate. It is not registered in `lib.rs` or routed through `gateway.rs`; tests use `#[path]` while the lead owns integration.
   `new:` Status: Integrated. `world` is registered in `lib.rs` (`pub mod world;`), and the gateway binary `src/bin/osfr-gateway.rs` owns a `World` (`prepare_membership` / `commit_membership`, and `collect_empty_instances` each step). `tests/world.rs` imports `osfr_tools::world` directly, with no `#[path]`.
   `why:` repo:prototype/osfr-tools/src/lib.rs:99; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:35, 3671; repo:prototype/osfr-tools/tests/world.rs:1,5; repo:notes/Autopilot/F149.md, F182.md (`prepare_membership` / `commit_membership` are the live entry path).

2. `old:` 1. Register `world` in shared `lib.rs`; keep this worker candidate isolated until review.
   `new:` 1. Done: `world` is registered in shared `lib.rs` (`pub mod world;`, line 99).
   `why:` repo:prototype/osfr-tools/src/lib.rs:99

3. `old:` 2. Route login entry and opcode-31 transfers through `enter_public` / `enter_instance`.
   `new:` 2. Login entry and opcode-31 transfers go through `World::prepare_membership` and `commit_membership` (commit after save). `collect_empty_instances` runs at the top of each gateway step.
   `why:` repo:prototype/osfr-tools/src/world.rs:990, 1049; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:3671. `enter_public` is used only by `dormant_fields.rs:35`.

4. `old:` `gateway.rs::templates_for` substitutes current zone details in startup slot 03 and still replays static captured 35/2 messages in slots 10–32.
   `new:` `gateway.rs::startup_for` builds the startup slots through `StartupSnapshot::build_packet`. Slot 03 is `build_zone`, with the current scene override. Slots 10–32 are 35/2 AddNpc built from the snapshot's NPC rows, and they are skipped during opening. Nothing is replayed as captured bytes.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:1892-1911 (no `templates_for` exists in `gateway.rs`); repo:prototype/osfr-tools/src/startup_snapshot.rs:307, 312, 323-330; repo:notes/Design/Build Ledger.md:39 ("no longer replayed").

5. `old:` The current gateway's initial-zone packet is `initial_zone` in `gateway.rs`; its zone type is 2.
   `new:` The current gateway's zone-details packet is `StartupSnapshot::build_zone` in `startup_snapshot.rs` (slot 03 via `gateway.rs::startup_for`). Its zone type is 2.
   `why:` no `initial_zone` function exists in `src/gateway.rs`; repo:prototype/osfr-tools/src/startup_snapshot.rs:370-380 (zone type 2 at :379); repo:prototype/osfr-tools/src/gateway.rs:1909-1911

6. `old:** (R) Its instance ID equals the zone ID so the existing zone-0 startup identity remains stable.`
   `new:` (R) Zone 0 keeps instance ID 0. Other seeded zones use their zone ID when that ID is free, and otherwise the lowest free positive ID. Zone 0's startup identity is unchanged.
   `why:` repo:prototype/osfr-tools/src/world.rs:1137-1163 (`stage_public`), :1148 (`zone_id == 0 → 0`), :1167-1171 (`instance_id_free`).

7. `old:` - One public instance per zone; public instance ID equals zone ID. Private IDs are in-memory only.
   `new:` - One public instance per zone; zone 0's public instance ID is 0, and other zones use their zone ID unless it is taken. Private IDs are in-memory only.
   `why:` repo:prototype/osfr-tools/src/world.rs:1148-1158

8. `old:` 3. Feed the actual client ready/load callback to `mark_zone_ready`.
   `new:` 3. Still open. `mark_zone_ready` is called only from `commit_membership` for already-ready entries (world.rs:1077). The gateway's `Event::Loaded` arm calls `game.initialize_world`, not `mark_zone_ready`.
   `why:` repo:prototype/osfr-tools/src/world.rs:1077, 1324; repo:prototype/osfr-tools/src/gateway.rs:1477-1484. Grep of `src/` finds no other caller.

**Unsure:**

- Test count. The note reports "7 passed" (line 78) and "6 passed" (line 88). `tests/world.rs` now has 8 `#[test]` functions (including `npc_visibility_loads_content_caps_the_view_and_respects_startup_exclusions`). These are historical run results, so I did not correct them. Re-run the suite before quoting a count.
- `housing.rs::Lot::instance_index` (line 78). I found no `fn instance_index` in `src/`, so the dead-code warning reference may be stale. Not confirmed.
- Disconnect routing (line 104, "Route disconnects through `leave`"). `commit_membership` calls `leave` internally, but I did not confirm a disconnect call site in the gateway. Not corrected.
- Related note, outside scope: `notes/Design/Build Ledger.md:56` says "The `world::World` instance coordinator exists but is unused." That conflicts with the tip, where the gateway binary uses it. Worth a separate check.
- Lines 25–44 (opcode-31 and 43 field values, packet order, `wait_for_zone_ready=true`, zone type 2 default) match `world.rs:1456-1516` and were not contradicted.
