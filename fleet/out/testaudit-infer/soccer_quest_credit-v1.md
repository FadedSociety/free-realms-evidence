<!-- fleet job=testaudit-infer id=soccer_quest_credit-v1 status=no_submit turns=3 usd=0.0046 tokens(read,write,in,out)=[25369, 21425, 8, 3311] model=claude-haiku-5-5 -->
# tests/soccer_quest_credit.rs

```json
{"file": "tests/soccer_quest_credit.rs",
 "tests": [
  {"name": "a_finished_soccer_match_advances_the_quest_once", "verdict": "keep", "covered_by": null,
   "reason": "Main positive path: one settled match gives one 49/9 update 0->1, one payout, no completion, and a near-cap case capped at 2. Its post-settle section (lines 331-352) overlaps a_duplicate_settle_or_close_does_not_replay, but the near-cap and first-match credit checks are unique here."},
  {"name": "the_reward_is_paid_once_and_the_result_precedes_the_event", "verdict": "keep", "covered_by": null,
   "reason": "Pins the packet order (OnGameWonMsg, 39/18, 39/47, 39/19, coin update, reward bundle, 49/9) and the no-job-XP rule on the soccer payout. I did not find another test asserting this exact sequence, so it is kept."},
  {"name": "a_loss_or_cancel_does_not_advance", "verdict": "keep", "covered_by": null,
   "reason": "Refusal check: a loss, a cancel (39/19) and an early close all credit nothing and pay nothing. tests/soccer_star_chapter.rs::a_loss_or_quit_does_not_credit_the_quest covers the loss and quit cases on a different chapter quest, but this test also covers the early close, so it is not an equal superset and is kept."},
  {"name": "a_different_game_id_does_not_advance", "verdict": "keep", "covered_by": null,
   "reason": "Scoping check: games 43 and 44 win and pay but never credit quest goal 42. Not seen elsewhere in the set."},
  {"name": "a_duplicate_settle_or_close_does_not_replay", "verdict": "keep", "covered_by": null,
   "reason": "Once-only guard: 39/7 ack, post-result quit, extra ticks and Close after settlement add no objective or coin. It overlaps the post-settle section of a_finished_soccer_match_advances_the_quest_once but is longer and adds the 39/7 and 39/6 inert checks. Kept as a canary for replay."},
  {"name": "the_event_is_not_client_reported", "verdict": "keep", "covered_by": null,
   "reason": "Security/refusal check: a forged client GoalMade, client 39/14 won claim and client 39/18 claim are refused or ignored, with no score, phase, coin or quest change. Only the server-built result settles."},
  {"name": "the_credit_survives_a_reconnect", "verdict": "keep", "covered_by": null,
   "reason": "Persistence check on the soccer path: the saved counter and reward survive Gameplay::load plus bind, the login sync carries [1], and no replay occurs. tests/shared_field_kill_quest_credit.rs::the_credit_survives_a_reconnect exercises a different credit path, so it does not cover this one."},
  {"name": "kart_chess_and_fishing_completions_are_unchanged", "verdict": "keep", "covered_by": null,
   "reason": "Weak negative canary: 8 ordinary world ticks with an active soccer goal emit no 49/9. The other games' suites are named only in a comment. Kept because the file's only check of the non-soccer producers is this one, though it is weak."},
  {"name": "a_failing_quest_event_for_one_player_does_not_stop_the_other", "verdict": "keep", "covered_by": null,
   "reason": "Isolation and refusal check: a stale save belonging to another character is refused with InvalidData and kept. Player A still settles and pays without credit, and player B credits its own goal. Same name as several other files, but the path differs (a bind refusal, not a failing event), so it is not a duplicate."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Every test is kept. Overlaps found: (1) inside this file, the post-settle section of a_finished_soccer_match_advances_the_quest_once repeats much of a_duplicate_settle_or_close_does_not_replay; (2) the loss and quit half of a_loss_or_cancel_does_not_advance overlaps tests/soccer_star_chapter.rs::a_loss_or_quit_does_not_credit_the_quest. Trimming either overlap would be a judgement call, not a clear removal, so I did not mark them. I did not read the helper module support/soccer_play.rs or the other files' bodies in full; the verdicts rest on the test bodies here and the names and bodies of the similar tests I checked."}
```
