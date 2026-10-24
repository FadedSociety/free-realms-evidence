<!-- fleet job=bug-hunt id=src-gameplay-npc-turnin-rs-L1 status=nothing_found turns=8 usd=0.0064 tokens(read,write,in,out)=[82212, 21046, 18, 5968] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/npc_turnin.rs lines 1-57 of 57

No defect found in `prototype/osfr-tools/src/gameplay/npc_turnin.rs` lines 1-57 that a remote client or a save can reach.

Candidates checked and dropped:

- **`npc_turnin.rs:23-30` (`find_map` over `parse_add_npc`):** `packets` are server-built 35/x packets, not client bytes. Parse errors are skipped with `.ok()?`, and nothing indexes or slices by a client length.
- **`npc_turnin.rs:31` (`quest_end_packet(...)?` after no mutation):** the function mutates nothing before this `?`, so there is no half-applied state here. Its failures are an unknown quest id (`quest_engine.rs:1282`, guarded by the save repair at `quest_engine.rs:2524-2526`, which clears `pending_turnin` for unavailable quests) or an invalid static reward bundle (`quest_engine.rs:2940-2960`). Neither is reachable from client input.
- **Caller `gameplay/npc.rs:29` (`?` after `visibility.update` has already committed):** a failure there would drop visibility packets whose spawns were already recorded. This is a real ordering issue, but it needs `quest_end_packet` to fail, which requires a static content defect, so I did not report it.
- **`npc_turnin.rs:25-26` and `npc_turnin.rs:52-55`:** the match uses `content_key`, which returns `None` for excluded GUIDs (`world.rs:537-541`). This matches the doc comment, which says only the opening-scene exclusion in `content_npc_key` should not apply. The startup-snapshot exclusion from `gateway.rs:845-851` still applies here, which may skip a re-send for a startup NPC. That depends on where startup 35/2 packets are sent, which is outside this window and I could not show it as a defect.
- **`npc_turnin.rs:37-43` (shared path):** the error is logged and not propagated, as the doc comment says.
