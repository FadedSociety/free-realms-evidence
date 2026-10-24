<!-- fleet job=note-refresh id=Quest-Engine status=done turns=21 usd=0.0215 tokens(read,write,in,out)=[568222, 56518, 44, 17470] model=claude-haiku-5-5 -->
# notes/Research/Quest Engine.md

**Verdict:** badly stale in its status, routing and content-schema claims. The code-level claims (function names, `encode_exact` opcode list, `startup_world::build_journal_definitions` / `startup_messages::build_journal_set`, the `QuestAdd`→49/8 accept order, the 49/4 then 49/12 turn-in order, the 47/15 limit path) still hold.

**Corrections:**

1. `old:` `Status: focused candidate module. `quest_engine.rs` is not registered in `lib.rs`, is not routed through the gateway, and has no native acceptance of its own.`
   `new:` `Status: wired module. `quest_engine.rs` is registered in `lib.rs` and is driven by the gateway's gameplay layer: NPC offer, accept, decline and turn-in run through `gameplay/npc.rs` and `gameplay/npc_quests.rs`. The Build Ledger lists the regional quest engine (49/1, 49/2, 49/3, 49/13, 49/14) as Native-verified, citing R5 runs.`
   `why:` repo:prototype/osfr-tools/src/lib.rs:72 (`pub mod quest_engine;`); repo:prototype/osfr-tools/src/gameplay/npc.rs:157, 276, 278, 329 (`offer`, `accept`, `decline`, `finish_turnin`); repo:prototype/osfr-tools/src/gameplay/npc_quests.rs:181-234; repo:notes/Design/Build Ledger.md:85.

2. `old:` `Current `ContentGoal` can encode only defeat/model id, NPC talk, item collection, POI reach and zone visit.`
   `new:` `Current `ContentGoal` encodes defeat/model id, NPC talk, item collection, POI reach, zone visit, job level, gather, craft, finish-minigame, equip, position visit, client-reported, interact-actor and complete-dungeon goals.`
   `why:` repo:prototype/osfr-tools/src/content.rs:162-260 (enum `ContentGoal`).

3. `old:` `Finish-minigame and use-item definitions cannot yet be expressed in ContentDb JSON; the new event API supports those kinds, but a later shared content-schema change is needed to author them as data.`
   `new:` `Use-item definitions cannot yet be expressed in ContentDb JSON, because `ContentGoal` has no use-item variant; `QuestEvent::UseItem` exists, so a later shared content-schema change is needed to author them as data.`
   `why:` repo:prototype/osfr-tools/src/content.rs:162-260 (no `UseItem` variant; `FinishMinigame` at :222); repo:prototype/osfr-tools/src/quest_engine.rs:630 (`QuestEvent::UseItem`).

4. `old:` `` `CharacterEligibility` and `QuestRequirements` are policy inputs because current `ContentDb::Quest` does not store player/job level or membership requirements. ``
   `new:` `` `CharacterEligibility` and `QuestRequirements` are policy inputs because current `ContentDb::Quest` does not store membership requirements. It does store an optional `min_level` and `job`, which `definition_from_content` maps into `QuestRequirements`; `members_only` is still set to false. ``
   `why:` repo:prototype/osfr-tools/src/content.rs:285-302 (`min_level`, `job`; no membership field); repo:prototype/osfr-tools/src/quest_engine.rs:2413-2416.

5. `old:` `ContentDb also lacks quest description/helper locale ids, turn-in NPC, level/job/membership fields and reward-display item rows.`
   `new:` `ContentDb also lacks quest description/helper locale ids, turn-in NPC, membership fields and reward-display item rows.`
   `why:` repo:prototype/osfr-tools/src/content.rs:285-302 (`Quest` has `min_level` and `job` but no membership, turn-in or description field).

6. `old:` `These are typed opcode intents with no encoded body. Do not send an intent as a packet.`
   `new:` ``encode_exact` returns `None` for these three intents, but the gameplay layer turns them into packets: `QuestInfo` through `quest_offer_packet`, `QuestAdd` through `quest_add_packet`, and `QuestEnd` through `quest_end_packet`. Send them only through that path, never as a raw intent.`
   `why:` repo:prototype/osfr-tools/src/quest_engine.rs:580 (`QuestInfo | QuestAdd | QuestEnd => None`), :1278 (`quest_end_packet`), :1399 (`quest_add_packet`); repo:prototype/osfr-tools/src/gameplay/npc_quests.rs:187-223; repo:prototype/osfr-tools/src/gameplay/npc.rs:1233 (`quest_offer_packet`).

7. `old:` `Final result: **8 passed, 0 failed, 0 ignored**.`
   `new:` ``tests/quest_engine.rs`` now contains 11 `#[test]` functions (content DB drive, empty-objective gate, six objective kinds, prerequisite/level/job/member/limit gates, decline/abandon/reload, duplicate turn-in, opening parity, protocol builders, and two more); the Autopilot reports record 11 passed. Re-run before quoting a result.`
   `why:` repo:prototype/osfr-tools/tests/quest_engine.rs:188, 270, 305, 352, 446, 506, 661, 755, 771, 787, 882; repo:notes/Autopilot/F133.md:83 (`11 passed`); repo:notes/Autopilot/F191.md:122 (`quest_engine` 11).

8. `old:` `1. Register the module in `src/lib.rs`; preserve the current `quests.rs` and `opening.rs` routes during staging.`
   `new:` `1. (Done: `pub mod quest_engine;` is at `src/lib.rs:72`.) Preserve the current `quests.rs` and `opening.rs` routes during staging.`
   `why:` repo:prototype/osfr-tools/src/lib.rs:72.

**Unsure:**
- Membership gating: `members_only` is hard-set to false (quest_engine.rs:2416), so the note's "membership" gate is unexercised from content. I did not trace whether the limit check (quest_engine.rs:1681-1694) is the only member-dependent path.
- The "17 local opening rows" and "sequential prerequisites" in the `from_opening` paragraph: I read the adapter (quest_engine.rs:1043-1104) but did not count the stages in the opening content.
- The fixture "provenance index" (line 40): the fixture has per-entry `provenance` strings (opening.json:28 and onward), and I did not check whether a separate top-level index exists.
- Whether the 49/1, 49/3 and 49/13 builders are "verified" as the note's Lead step 4 requires. I saw the code paths but did not check the Build Guide evidence.
- I did not run `cargo test`, so the pass count is taken from the test-function count and the Autopilot reports.
