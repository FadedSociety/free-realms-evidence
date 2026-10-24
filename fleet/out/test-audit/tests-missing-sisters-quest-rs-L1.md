<!-- fleet job=test-audit id=tests-missing-sisters-quest-rs-L1 status=done turns=5 usd=0.0078 tokens(read,write,in,out)=[72070, 29738, 12, 6767] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/missing_sisters_quest.rs lines 1-1008 of 1008

Window reviewed: `prototype/osfr-tools/tests/missing_sisters_quest.rs` lines 1-1008 (helpers in `tests/support/npc_quest_chain.rs` read for `counts`, `coins`, `profile_xp`). No test is `#[ignore]`d, and no early return passes on a missing fixture. The `lab/reports/locale-id-to-text.json` fixture is used by several other tests, so its absence would fail loudly. Most assertions compare against independent expectations (the packet bytes, the quest-state counters, and the saved-state round trip), so I found no "cannot fail" tests. The findings are below.

- **[medium] prototype/osfr-tools/tests/missing_sisters_quest.rs:1007 a_failing_quest_event_for_one_player_does_not_stop_the_other - "the level-1 field reward pays B" only checks `coins(&b) > 0`, which is not a payout check.**
  - Why it cannot catch a regression: B's wallet is never captured before the kill, so the check passes whenever B already holds any coins from the opening fixture. A field-kill change that stopped crediting the wallet (while still emitting the 38/19 packet, which is checked at 997-999) would still pass.
  - Fix: capture `let b_coins_before = coins(&b);` before `kill_shared_target` at line 988 and assert `coins(&b) == b_coins_before + <the level-1 reward amount>` (or at least `coins(&b) > b_coins_before`). Do the same for XP with `profile_xp`.

- **[medium] prototype/osfr-tools/tests/missing_sisters_quest.rs:907-913 and 957-978 a_failing_quest_event_for_one_player_does_not_stop_the_other - the comment says A's over-cap reward is "actually generated and refused", but the test only asserts that no 38/19 or 38/14 packet appears for A.**
  - Why it cannot catch a regression: if A's kill never generates a reward (for example, the reward lookup is skipped for the stale-catalogue player, or the table is not consulted), the absence assertions still pass. The test does not prove that the refusal path ran.
  - Fix: assert a positive signal from the reward-generation path for A's kill, such as a refusal log/outcome entry or a reply carrying the refused reward, and keep the absence checks. Alternatively, assert on A's wallet and XP being exactly unchanged after a reward that is known to be generated, which is the case the comment describes.

- **[low] prototype/osfr-tools/tests/missing_sisters_quest.rs:330-331 geoffrey_is_drawable_and_offers_the_missing_sisters - the comment says "with [the extra spawn row] removed there is no AddNpc for Geoffrey", but no negative check exists in the test.**
  - Why it cannot catch a regression: the test only checks the positive draw (340-346). If the extra-spawn row were ignored and Geoffrey were drawn from another source, the test would still pass, and the comment misstates what is verified.
  - Fix: either add the negative case (load `NpcVisibility` from a content dir copy without `npc_spawns_extra.json` and assert no AddNpc with `actor_id == GEOFFREY`), or reword the comment to describe only the positive check.

- **[low] prototype/osfr-tools/tests/missing_sisters_quest.rs:762-771 the_spawn_is_unique_and_the_quest_target_resolves - the exact enabled quest list `[QUEST, 3_000_032, 3_000_033, 3_000_034]` pins sibling quest rows that the test is not about.**
  - Why it cannot catch a regression: it is not a missed bug. Enabling or adding any other Chapter 1 row for Geoffrey, or any unrelated content change, fails this test even though the Missing Sisters spawn/target resolution is unchanged, which causes churn.
  - Fix: assert `enabled.contains(&QUEST)` and that every enabled id is in the expected chapter set, or check only that the quest's own giver resolves, and leave the sibling rows to the quest-content tests.

- **[low] prototype/osfr-tools/tests/missing_sisters_quest.rs:231-236 assert_end_reward - the exact 99-byte length pins an incidental framing detail on every reward check.**
  - Why it cannot catch a regression: a change that appends or pads a trailing field would fail all end-reward checks (used at 462, 550, 664, 861) even when the actor, success flag, coins, and XP are correct. The test's intent is the reward fields, not the total size.
  - Fix: keep the fixed-offset field assertions and drop the exact length, or assert `packet.len() >= 35` and document that 35 bytes are the required prefix.
