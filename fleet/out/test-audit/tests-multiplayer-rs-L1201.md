<!-- fleet job=test-audit id=tests-multiplayer-rs-L1201 status=done turns=12 usd=0.0200 tokens(read,write,in,out)=[402591, 55875, 26, 17939] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/multiplayer.rs lines 1201-2400 of 3109

Window `tests/multiplayer.rs` 1201-2400 (plus 1473-1500 and 2034-2050, which the first reads truncated). Four findings, all in the T335 kill and replay section and the group chat test. The `two_players_...` test and the group setup/stale-accept/snapshot checks are sound as far as I read them.

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:2040 a_shared_field_kill_pays_both_and_credits_the_killer_once - the replay quest check asserts `current == 2`, a value the objective can never reach.**
  - Why it cannot catch a regression: `quest_engine.rs:1848-1850` clamps each count with `.saturating_add(increment).min(objective.required)`, and this objective has `required = 1`. A duplicate kill credit therefore sends at most `current=1` again, and `!objective_update(&replay_a, T335_QUEST, 1, 2)` still passes.
  - Fix: assert that no 49/9 update for quest T335_QUEST / objective 1 appears in the replay replies, whatever `current` is. Also assert the saved quest state is unchanged after a settle (see the next finding).

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:2035-2041 a_shared_field_kill_pays_both_and_credits_the_killer_once - the "pay and credit nothing" replay only inspects the immediate `field_attack` replies.**
  - Why it cannot catch a regression: `field_attack` goes through `Client::send`, which steps the server only until the reliable message is acknowledged (`playtest_gateway_smoke.rs:330-351`). A payout or credit that lands on a later 20 Hz field tick is never drained into `replay_a`/`replay_b`. The saved balances and XP are not re-read after the replay either, so a delayed duplicate payout passes.
  - Fix: after the two replay attacks, call `settle(&mut server, &mut [&mut first, &mut second])`, then assert that the settle output has no 38/19 for either client. Also assert `saved_coins` and `saved_job_xp` for both players are unchanged from the post-kill values.

- **[medium] prototype/osfr-tools/tests/multiplayer.rs:2032 a_shared_field_kill_pays_both_and_credits_the_killer_once - `quest_counts(...) == [1]` cannot detect a double credit, so the "credits the killer once" name overclaims for the quest half.**
  - Why it cannot catch a regression: the save's count is clamped at `required` (`quest_engine.rs:1850`), so a second kill still saves `[1]`. The same weakness applies at line 2041.
  - Fix: count the 49/9 messages for quest T335_QUEST / objective 1 across `a_replies` plus the `settle` output, and require exactly one. A duplicate credit then emits a second update, since `increment` is 1 before the clamp.

- **[low] prototype/osfr-tools/tests/multiplayer.rs:2388-2399 a_group_forms_and_party_chat_reaches_both - the comment says a refused duplicate invite "leaves the group unchanged", but the body checks only result code 3 and that B receives no 40/1.**
  - Why it cannot catch a regression: a server that refuses the invite but drops or reshuffles the roster would pass these lines. Only the later party-chat check at 2401 touches the group, and that check does not compare roster contents.
  - Fix: after the refused invite, drain both sides and assert `group_snapshot_guids` still equals `[[2, 3]]`, or drop the "unchanged" wording from the comment.
