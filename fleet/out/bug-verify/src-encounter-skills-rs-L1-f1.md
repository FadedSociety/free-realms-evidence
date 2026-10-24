<!-- fleet job=bug-verify id=src-encounter-skills-rs-L1-f1 status=done turns=18 usd=0.0151 tokens(read,write,in,out)=[413235, 39349, 38, 12044] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/encounter/skills.rs:432-453`

**Verdict:** `refuted`

**Severity if confirmed:** n/a (the panic path is not reachable from a client packet as described).

**What holds:** the module tree is real, and steps 1, 2 and 4 are accurate. `encounter.rs:22-27` declares `mod field; mod shared; mod skills;` and `lib.rs:19` has `pub mod encounter`. `encounter.rs:1779-1786` makes `enemy()` return field actors whenever `shared_sender` is set. `shared.rs:420-423` moves `runtime.dots[sender]` into the engine, and `encounter.rs:1334-1336` (`reset_session`) does not clear it on `begin()`. The `.unwrap()` at `encounter.rs:1937` is real (`find(...).unwrap().health = hp`). The gap is step 3, which is blocked by the dungeon entry itself.

**Why step 3 (A stays a ready, loaded field participant while its engine is active) does not happen:**

1. **Dungeon entry emits a zone change.** `encounter.rs:1404-1408` (`begin`) returns `zoning: Some(d.zone.clone())`. `gameplay.rs:4933` (`apply_encounter`) passes it to `out.zoning`. `gateway.rs:1851-1864` then sets `began_zoning = true`, moves `state.zone_id` to the dungeon zone, and sets `ready = false` and `loaded = false`.
2. **Membership moves out of the field.** `osfr-gateway.rs:1742-1755` computes `transfer = began_zoning || zone changed`. The target is the pending transfer or `None` (`.or_else(|| (!transfer).then_some(old_instance)...)`), so `prepare_membership` builds a new instance for the dungeon zone. `world.rs:1049-1066` (`commit_membership`) calls `leave` and inserts the player into that instance. The field instance no longer lists A.
3. **The field tick filters A out.** `osfr-gateway.rs:3025-3030` only adds a session to `active` when `player_location(...).instance_id == instance && l.ready` and `is_world_loaded()`. A is in the dungeon instance and not ready, so `tick_shared_effects` (`osfr-gateway.rs:3093-3095`) never runs for A on the field instance.
4. **The shared-action path is also guarded.** `gameplay.rs:527` returns early when `engine.active()`, so the player-initiated `shared_job_ability` path is blocked too.
5. **Caster DoTs are dropped.** `osfr-gateway.rs:2981-2983` says a field tick "drops departed casters' DoTs", and the field's `retain_casters` (`encounter/shared.rs:165`) is run each tick with the current `active` set (`osfr-gateway.rs:3040`). A's DoTs are cleaned up once A leaves.

**Residual caveat (not enough to confirm):** the chain depends on the dungeon zone (`d.zone.zone_id`) differing from the field's zone. `begin` does not enforce that. If a dungeon's zone equalled the field zone and `stage_public` returned the field's public instance, A would be back in the field instance after the zone-ready handshake, and the path would become live. I did not check dungeon content to rule this out. Nothing in the reviewed code makes it happen, and the bixie hive dungeon test is set up as a separate zone, but I have not verified it.

**Corrected fix:** not needed for this claim. Defence in depth is still worth doing: replace `encounter.rs:1937` `.unwrap()` with a non-panicking `let Some(..) else` branch. Clearing `runtime.dots[sender]` on dungeon entry is also reasonable hygiene, since the stale DoTs currently persist until the next field tick drops them.
