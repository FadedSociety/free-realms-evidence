<!-- fleet job=test-audit id=tests-soccer-quest-credit-rs-L1 status=done turns=4 usd=0.0055 tokens(read,write,in,out)=[42182, 23442, 10, 4373] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soccer_quest_credit.rs lines 1-804 of 804

Window `prototype/osfr-tools/tests/soccer_quest_credit.rs` 1-804 (read in full; checked `src/gameplay/npc_quests.rs:12-58` for the bind path). The main settle/once-only/loss/cancel/reconnect assertions are concrete and would catch a double credit or a missing credit, so most of the file holds. Findings:

- **[medium] tests/soccer_quest_credit.rs:748 kart_chess_and_fishing_completions_are_unchanged - the name claims kart, chess, fishing and type-8 completions are unchanged, but the body only ticks an idle soccer-capable player 8 times and checks no `49/9` appears for QUEST.**
  - Why it cannot catch a regression: no kart, chess, fishing or type-8 producer is driven at all. Any change to those producers still passes, and the comment's "those suites run as separate gates" is the only link. The check is really "an ordinary world tick with no match emits no soccer credit".
  - Fix: rename it to something like `ordinary_world_ticks_emit_no_quest_credit`, or drive at least one real producer from each named family (e.g. a fishing or kart completion) and assert that the quest counter is unchanged and that only the intended packets appear.

- **[medium] tests/soccer_quest_credit.rs:763 a_failing_quest_event_for_one_player_does_not_stop_the_other - the name says a failing quest event is isolated, but the failure exercised is a refused `bind_npc_quest_catalogue` for a stale save (lines 772-786), not a failing quest event.**
  - Why it cannot catch a regression: the body never produces a failing event. A change that makes event failures bleed into B's session would not be caught by this test, because the only failure it checks is the bind refusal. The comment's "keeps the stale save for a later retry" is also not checked; only `character_id == OTHER` is compared, not a retry or a re-bind.
  - Fix: rename it to match the bind refusal (e.g. `a_refused_stale_bind_does_not_stop_the_other_player`), or add a real failing event path (such as a `finish_minigame` event on a quest A's engine rejects) and assert that A's settle still pays while B's count is 1. Add a retry assertion: a second `bind_npc_quest_catalogue` on the kept save must be refused the same way, or succeed after the save is corrected.

- **[low] tests/soccer_quest_credit.rs:674 the_event_is_not_client_reported - the refused `GoalMade` is checked only by `forged_goal.to_string().contains("goal")`.**
  - Why it cannot catch a regression: any error whose text includes "goal" passes, including an unrelated parse or routing error. A change that refuses the packet for a different reason, or that starts returning a different error kind, still passes.
  - Fix: assert the error kind (`InvalidData` or whichever kind the refusal uses) and compare the message against the exact refusal string, so the test pins why the client packet is refused.

- **[low] tests/soccer_quest_credit.rs:438 a_finished_soccer_match_advances_the_quest_once - `assert!(after.replies.is_empty(), ...)` requires any packet from the next world tick to be absent, which the test does not claim to check.**
  - Why it is over-pinned: the test is about quest credit and coins, but an unrelated ambient world packet (heartbeat, NPC idle, zone sync) would fail it. The same pattern appears at lines 619, 623 and 625 in `a_duplicate_settle_or_close_does_not_replay`.
  - Fix: assert the absence of the relevant packets, i.e. `objective_updates(&after.replies, QUEST).is_empty()` and no `[39, 0, 18]` or `[49, 0, 10, 0]` prefix, instead of requiring an empty reply vector.</result>
