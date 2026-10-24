<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-rs-L3201 status=nothing_found turns=17 usd=0.0253 tokens(read,write,in,out)=[585683, 58641, 36, 24255] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-gateway.rs lines 3201-4000 of 4671

Window `prototype/osfr-tools/src/bin/osfr-gateway.rs` 3201-4000 read in full (plus 3150-3200, 3456-3500, 3741-3800, 4001-4030 and the callers/helpers needed to judge reachability). No finding survives verification, so nothing is reported.

Checked and dropped:

- **`sync_field_views` (3199-3311), the `nearby` union filter (3211-3240).** `nearby` is a union over candidates, so a session near any actor gets every candidate in `fields`. That looks coarse but is not wrong: `NpcVisibility::shared_view` (world.rs:171-227) re-applies the exact per-viewer `NPC_VISIBILITY_RADIUS` and `NPC_VISIBILITY_LIMIT` cap, and any viewer within radius of a candidate is necessarily in `nearby`. Not a defect.
- **`known.retain` on revision change (3269-3279).** Passive NPCs (no `field.position`) are dropped and re-added by `shared_view` (world.rs:221-225). Enemies and battle spawners always have `Some(position)` (shared.rs:128-145), so no lost-AddNpc case exists.
- **`?` on `shared_npc_view` (3281) and `initialization` (3296).** An error aborts the whole instance pass, but `tick_shared_instance` runs under `contain` and `tick_shared_fields` (2984-3011) marks the instance faulted. This is contained per instance, and the only non-finite-position input is rejected earlier. Not a remote crash.
- **`try_for_each` refusal (3298-3304).** A partial queue followed by a retry can duplicate an AddNpc, but that needs a full reliable queue and gives a cosmetic client effect. Too weak to show.
- **`step()` receive path (3677-3773).** Packet and byte budgets are checked before `handle`. The handshake rate limit applies to non-loopback peers. Sessions are reinserted on refusal and ended on error. `recv_from` errors other than WouldBlock, TimedOut and ConnectionReset return from `step`. That is a Windows-only theoretical concern with no client-driven trigger, so I did not report it.
- **Idle, login and reassembly timeouts (3801-3815).** Behaviour is as documented.
- **Studio routes (3819-4030).** Every route requires `options.dev_tools` (3881) and a loopback listener. The request reader is bounded (studio.rs: 16 KiB head, 1 MiB body, 500 ms timeout). Savestate names are whitelisted to `[A-Za-z0-9_-]`, max 48 characters, so there is no traversal. The `unwrap`s on `sessions[&key]` and `gameplay()` (3850, 3948, 4009) follow a `studio_session()` check that guarantees them. The `/api/send` hex is capped at 64 KiB. Savestate load is admin-only and non-atomic on copy failure, which is out of scope for a remote player.
- **`new()` (3313-3407).** Startup-only. No client-controlled input and no mutation that a later failure leaves inconsistent in a way a player can reach.
- **`contain`, `run` and `main` (4478-4517).** Panics are contained per session. `main` exits on `run` error, which is expected at startup.

Not addressed: `#[cfg(test)]` helpers (3448-3654) are out of scope.
