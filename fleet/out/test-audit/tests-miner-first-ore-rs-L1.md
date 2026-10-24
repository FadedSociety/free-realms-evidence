<!-- fleet job=test-audit id=tests-miner-first-ore-rs-L1 status=done turns=9 usd=0.0167 tokens(read,write,in,out)=[252206, 53037, 20, 14998] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/miner_first_ore.rs lines 1-1200 of 2296

Window `prototype/osfr-tools/tests/miner_first_ore.rs` lines 1-1200 read in full (plus the support helpers it calls: `npc_quest_chain.rs` 420-719 and `mining_quest_chain.rs` 218-362). Most assertions are sound: expected values such as (5, 15), `{"14": 15}` and the 49/1 ids are hard-coded rather than read back from the code under test, and `assert_no_offer` / `assert_packet_changes_nothing` compare serialized state. The findings below are the ones that hold up.

- **[medium] miner_first_ore.rs:194 `assert_inert` (and its only helper `save_envelope` at :213) - the save-bytes refusal proof is dead code; no test in the file calls it.**
  - Why it cannot catch a regression: the doc at :192-193 and :211-212 promise that refusals are proven equal at the real `game_store` save boundary, but a grep of the whole file finds no call to `assert_inert`. Every refusal test (for example `refusals_and_replay_change_nothing` at :581, `a_full_bag_refuses_the_node...` at :484, and `two_miners_progress_independently` at :763) compares only the in-memory `saved()` JSON. A change that writes a different envelope on refusal, or that persists a refused grant, passes.
  - Fix: call `assert_inert(&fixture, &mut miner, &character, &quest_reply(MINER_FIRST, true), 100, "a forged 49/2 with no offer")` in `refusals_and_replay_change_nothing` (and on the full-bag refusal at :484), or delete the helper and its doc claim. The file has no `allow(dead_code)`, so the unused helper is also a compile warning.

- **[medium] miner_first_ore.rs:327 `mining_one_copper_then_talking_to_therin_pays_once` - the message says "the return step opens after the ore", but the check is `count(&game, 1) == 0`, which holds whether or not objective 1 activates.**
  - Why it cannot catch a regression: a change that never activates the Talk-to-Therin objective (no 49/8 for objective 1) leaves count 1 at 0 and still passes. Nothing in the window checks activation, even though `objective_activated` and `objective_activated_packet` are imported at :63-64. The later `finish_quest` passes because `open_end_screen` releases the 49/13 regardless of the objective state.
  - Fix: capture the outcome of the gather step and assert `objective_activated(&gather_outcome, MINER_FIRST, 1)`, or assert the 49/8 with `objective_activated_packet(MINER_FIRST, 1, 1)`, so the return step's activation is what fails.

- **[low] miner_first_ore.rs:581 `refusals_and_replay_change_nothing` - the comment says "a disabled prerequisite's ids" but the loop at :602-610 covers DRAINED_RECORDS (3100001 and 3100005, "Gem Appraisal"), which are not prerequisites.**
  - Why it cannot catch a regression: the name and comment overclaim. The loop checks only that disabled records stay refused, and the prerequisite gate for 3100002 (`prerequisite_quest_ids == []`, asserted at :962) is never exercised.
  - Fix: correct the comment to "disabled Gem Appraisal records", or add an actual prerequisite-gated refusal (for example a 3100003 accept before 3100002 is complete) that asserts `saved` is unchanged.

- **[low] miner_first_ore.rs:530 `a_turn_in_with_no_item_does_not_check_bag_space` - the comment at :551 says "fill the bag at the save boundary and reload it", but :554 rebuilds the session in memory with `fixture.game_with_state(state)`, with no `game_store` round trip.**
  - Why it cannot catch a regression: a bag-space check that runs only on a persisted reload path would not be exercised. The test therefore overclaims a save-boundary proof.
  - Fix: round-trip the state through `fixture.save_and_reload` (or `save_envelope`) after `fill_bag`, and keep the item-ledger and coin/XP assertions.

- **[low] miner_first_ore.rs:1032 `therin_is_drawable_and_the_quest_content_resolves` - `copper_spawns.len() == 5` pins an exact content count unrelated to Therin's quest wiring.**
  - Why it cannot catch a regression: it is churn, not a missed bug. Adding or moving a copper vein for unrelated content fails this test even though the quest's gather target is intact.
  - Fix: assert `copper_spawns.len() >= 1` and that at least one spawn is within 20 m of Therin, which is what the test actually needs.
