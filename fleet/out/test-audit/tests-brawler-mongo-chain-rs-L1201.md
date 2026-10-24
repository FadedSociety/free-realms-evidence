<!-- fleet job=test-audit id=tests-brawler-mongo-chain-rs-L1201 status=done turns=6 usd=0.0074 tokens(read,write,in,out)=[72733, 27673, 14, 6372] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/brawler_mongo_chain.rs lines 1201-1830 of 1830

Window `brawler_mongo_chain.rs` 1201-1830 read in full, plus the helpers it calls (`economy`, `win_mongo`, `open_gate`, `enter_arena`, `saved`, `assert_packet_changes_nothing` in `support/npc_quest_chain.rs`). Most assertions here are real. The one tautology is in `a_failed_quest_event_for_one_player_does_not_stop_the_other`; the other two findings are a doc overclaim and a name overclaim.

- **[high] prototype/osfr-tools/tests/brawler_mongo_chain.rs:1609 a_failed_quest_event_for_one_player_does_not_stop_the_other - "B's wallet is untouched by A's payouts" compares B's coins with B's coins, so it can never fail.**
  - Why it cannot catch a regression: the left side is `b.state().inventory.coins` and the right side is `coins(&b)`, which is `game.state().inventory.coins` (support/npc_quest_chain.rs:583-585). Both read the same value on the same session at the same moment. No "before" snapshot of B's wallet is taken anywhere in the test (the only `before` at line 1597 is `economy(&a)`). So a change that pays B on A's turn-in, or moves B's wallet in any other way, still passes.
  - Fix: before `finish_quest` at line 1599, record `let b_before = saved(&b);` (or `coins(&b)`), then assert after the payout that `saved(&b) == b_before` (or `coins(&b) == b_before`), with the label "B's wallet is untouched by A's payouts".

- **[low] prototype/osfr-tools/tests/brawler_mongo_chain.rs:1343-1344 (C6 block in the quest-records test) - the comment says T331 enabled C6 "with its one Talk objective, Brawler gate and reward", but the reward is never asserted.**
  - Why it cannot catch a regression: the block checks `enabled`, `job`, `objectives.len() == 1`, and the objective's `npc_id`. Nothing reads `c6["rewards"]`, so C6 can lose its coin or XP reward and this block still passes. The comment says it is covered when it is not.
  - Fix: add `assert_eq!(c6["rewards"][0]["coins"], QUEST_COINS)` or the C6 reward values from the data. Or narrow the comment to what is actually checked.

- **[low] prototype/osfr-tools/tests/brawler_mongo_chain.rs:1355 the_fight_survives_a_reconnect_mid_battle - the name says "mid battle", but both halves reconnect after the fight is already Won.**
  - Why it cannot catch a regression: the first half closes the won run before dropping. The second half drops after `win_mongo` has set the phase to Won and before the results Close. The test never drops a session while the encounter is in Fighting, so a bug that loses an in-progress fight on reconnect would not be caught. Its own comments say "Close the won run" and "between the killing blow and the results Close".
  - Fix: either rename it to something like `the_won_fight_survives_a_reconnect`, or add a third section that reloads during Fighting (after `enter_arena`, before `win_mongo`) and asserts the encounter is either restored or cleanly released, with no credit.

No findings for the rest of the window. The reconnect, gate-spawner, loss/retry, two-player, and replayed-close tests compare post-state against real before-state snapshots (`saved`, `counts`, `economy`) and check the refusal results.
