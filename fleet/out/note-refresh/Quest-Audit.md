<!-- fleet job=note-refresh id=Quest-Audit status=done turns=17 usd=0.0192 tokens(read,write,in,out)=[493556, 51348, 36, 15752] model=claude-haiku-5-5 -->
# notes/Research/Quest Audit.md

**Verdict:** badly stale. The status line and census predate the W104 merge of the eight referrals, and most `path:line` citations in the engine-route section have moved or point at the wrong code. The audit's own numbers were correct when run.

**Corrections:**

1. `old:` status: staged, bot-proven for three quests; lead integration and native acceptance pending
   `new:` status: merged into `data/content/quests` by W104; bot-proven for three quests; native acceptance pending
   `why:` repo:notes/Design/Build Ledger.md:86 ("W92's eight talk referrals are merged"); repo:notes/Design/Build Plan.md:125; repo:prototype/osfr-tools/data/content/quests/adventurer.json:1645 (and the other seven referrals' `evidence` lines, e.g. blacksmith.json:796, ninja.json:760, pet_trainer.json:462)

2. `old:` The census matches the current Ledger: **653 regional quests, 14 authored objective lists, 639 hollow records, 215 absent giver keys**.
   `new:` The census was taken before the W92 merge. The current Ledger reports 653 regional quests, 631 still without objectives (`"enabled": false`) and 215 absent giver keys (639 − 8 merged referrals = 631).
   `why:` repo:notes/Design/Build Ledger.md:86 ("the 631 quests that still have no objectives"; "215 name a giver that isn't spawned"); repo:notes/Design/Build Plan.md:125

3. `old:` Eight conservative referrals are staged.
   `new:` Eight conservative referrals were staged in the W92 run and have since been merged into the shipped content (W104).
   `why:` repo:notes/Design/Build Ledger.md:86; repo:prototype/osfr-tools/data/content/quests/brawler.json:485 (3030008), adventurer.json:1627/1709 (3000021/3000022), blacksmith.json:778 (3020014)

4. `old:` Read-only source verification found the regional route in `Gameplay::handle_npc_packet` (`gameplay.rs:1095`, TalkToNpc)
   `new:` Read-only source verification found the regional route in `Gameplay::handle_npc_packet` (`gameplay/npc.rs:70`; the TalkToNpc emission is in `talk_to_npc`, `gameplay/npc.rs:962`)
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:70 and :962. `gameplay.rs:1095` is now inside the startup loader (`apply_node_changes`).

5. `old:` encounter defeat handling (`gameplay.rs:4482`, KillActorKind)
   `new:` encounter defeat handling (`gameplay.rs:4903-4913`, KillActorKind; `enemy_defeated` at `gameplay.rs:5387-5388`)
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4903-4913 and :5387-5388. Line 4482 is now the interaction-selection parser.

6. `old:` `gateway.rs` routes family 49/2 and 49/14
   `new:` `gateway.rs` routes family 49/2, 49/14 and 49/15 to `quest_engine`
   `why:` repo:prototype/osfr-tools/src/gateway.rs:500

7. `old:` `content.rs:162-194` accepts five goal variants: defeat, talk_to_npc, collect_item, reach_poi and visit_zone. `quest_engine.rs:1565-1607` adapts them.
   `new:` `content.rs:162-255` accepts fourteen goal variants (defeat, talk_to_npc, collect_item, reach_poi, visit_zone, job_level, gather_resource, craft_recipe, finish_minigame, equip_item, visit_position, client_reported, interact_actor, complete_dungeon). The adapter that maps them to `QuestObjective` is `quest_engine.rs:2204-2360`.
   `why:` repo:prototype/osfr-tools/src/content.rs:163-255 (enum `ContentGoal`); repo:prototype/osfr-tools/src/quest_engine.rs:2160-2247. `quest_engine.rs:1565-1607` is `set_auto_switch_selected`/`offer`/`dev_mark_offered`.

8. `old:` `quest_engine.rs:1293` evaluates authoritative events; only talk and kills currently have regional gameplay producers.
   `new:` `quest_engine.rs:1789` (`on_event`) evaluates authoritative events. Regional gameplay callers now exist for talk and kill, and also for collect, gather, craft, minigame, equip and visit: `gameplay.rs:5428` (reward-driven CollectItem), `gameplay.rs:4567` (GatherResource), `gameplay/crafting.rs:403` (CraftRecipe), `gameplay.rs:1956` (FinishMinigame), `gameplay/npc_quests.rs:314` (EquipItem), `gameplay.rs:1820` (VisitPosition).
   `why:` repo:prototype/osfr-tools/src/quest_engine.rs:1789 (line 1293 is the quest-end packet builder); the producer lines listed above; repo:notes/Design/Build Plan.md:125 (W104 routes these events)

9. `old:` Loaded regional requirements remain `QuestRequirements::default()` (`quest_engine.rs:1651`).
   `new:` Loaded regional requirements remain `QuestRequirements::default()` (`quest_engine.rs:1095`).
   `why:` repo:prototype/osfr-tools/src/quest_engine.rs:1095 (the definition loop). Line 1651 is now `is_enabled`.

10. `old:` `world.rs:181-184` skips placements other than `legacy_data`
    `new:` `world.rs:284-286` skips placements other than `legacy_data`
    `why:` repo:prototype/osfr-tools/src/world.rs:282-286

**Unsure:**
- "1,199 regional NPC records" and "16,551 missing runtime items / 478 raw text hashes / 17,276 warnings" are checker outputs under `lab/`, which I could not read, so I did not verify them.
- The 653 and 215 totals match the Ledger. The 639 hollow figure is the pre-merge value (see correction 2), and I did not recount objectives in the data.
- "Several corresponding games are still unrouted" (minigame row) and the "native Round5" review references were not checked against the tip.
- The Build Plan (line 125) says the W104 change routes collect, gather, craft, minigame and visit events to the regional engine. I checked call sites but did not run a test to confirm that they reach the regional catalogue for these 86/55/18/57/13 quests.
- Native client label addresses (`00c7cd40`, `00c7a990`, `00a95420`) were not checked (client data was out of scope for this pass).
