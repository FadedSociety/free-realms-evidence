<!-- fleet job=bug-hunt id=src-quest-engine-rs-L1601 status=done turns=27 usd=0.0359 tokens(read,write,in,out)=[1157819, 72211, 56, 30625] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/quest_engine.rs lines 1601-2400 of 3000

I read `quest_engine.rs` 1601-2400 in full and traced the candidates back to their callers. Most suspected defects did not hold up:

- `accept` (1702) and `offer` (1585) index `definitions[&quest_id]`, but both run after a check that the definition exists.
- `on_event` (1807) indexes `definitions` for Active quests only. `validate_state` (2549-2560) and `repair_counters` (2484-2531) drop or reject Active quests that are unknown or disabled, so that index cannot panic on a save.
- `on_event` (1825, 1848) indexes `counts`. `validate_state` (2555) requires `counts.len() == objectives.len()`.
- `accept` (1737) `expect` is backed by `offer`/`dev_mark_offered` inserting the entry, and by `validate_state` (2574-2580) requiring the pending quest to be Offered.
- `finish_turnin` (2036-2039) `expect` is backed by `validate_state` (2587-2594) and by `open_pending_turnin` only being called for Active, complete quests.
- `finish_turnin` (2033-2034) runs `apply_grant` before any mutation, so the `?` leaves state unchanged. The job-lock branch (2021-2031) is a deliberate release, documented in the code.
- Reward sums (2376-2390) use `checked_add`. `within` (2901) is bounded by `validate_event` (2683-2685) to finite values with |x| <= 1e6.
- `ClientReported` (45/7) completion is client-judged by design (W175, `npc.rs:198-212`, `notes/Autopilot/F339.md:157`), so I did not report it.
- `dev_mark_offered` (1604) is reachable only from the dev-gated offer experiment (`gameplay.rs:3994-3996, 4150`).
- `named_target_quest_for_talk` (`npc_interaction.rs:771-811`) and the `TalkToNpc` path in `npc.rs:962` use server-known NPC keys.

One real but minor finding:

**[low] prototype/osfr-tools/src/quest_engine.rs:1935 - `begin_turnin` checks the turn-in NPC before the pending-screen reopen, which contradicts its doc comment at 1928-1930.**
- Failure scenario: a named-target or TalkToNpc-objective Talk (`on_event` 1911, `begin_named_target_turnin` via `npc.rs:996`) opens a pending 49/13 at a non-turn-in NPC X. The player later picks the `TurnInQuest` option at X (`npc_interaction.rs:836`, built from `npc.quests_accepted`). `begin_turnin(quest, X)` returns `WrongTurnin` at 1935-1936 and never reaches the reopen branch at 1938-1939. Nothing is re-sent, although the doc says repeating at the opening actor "re-sends the end screen". The pending state is left intact, and the Talk recovery path (`npc.rs:974-981`, which calls `reopen_turnin` directly) still works, so impact is limited to a silent no-op from that one option.
- Reach: client option choice → `npc_interaction.rs:558-562` → `begin_turnin` (1931). The NPC/quest pair is server-generated options, so this is a logic mismatch rather than a remote exploit.
- Fix: move the `if self.state.pending_turnin.is_some() { return self.reopen_turnin(quest_id, npc_id); }` block above the `npc_id != definition.turnin_npc_id` check at 1935.
- Confidence: medium-low on reach, since I did not confirm whether a named-target NPC lists the quest in `quests_accepted`.
