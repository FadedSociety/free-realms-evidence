<!-- fleet job=test-audit id=tests-harvesting-lifecycle-rs-L1 status=done turns=8 usd=0.0096 tokens(read,write,in,out)=[138665, 32040, 18, 8375] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/harvesting_lifecycle.rs lines 1-588 of 588

Window reviewed: `prototype/osfr-tools/tests/harvesting_lifecycle.rs` lines 1-588. No `#[ignore]` and no fixture-skip early returns in the window (`Fixture::new` unwraps, and `drive_round` returns `None` into a panic). The seeded replay and quest-event equality checks are sound. The findings are below.

- **[medium] tests/harvesting_lifecycle.rs:518-519 loss_has_no_payout_and_close_allows_try_again - the "no payout" state comparisons cannot fail.**
  - Why it cannot catch a regression: `before` is an immutable local, `RewardState` has no interior mutability (checked `rewards.rs`/`profiles.rs`/`inventory.rs`), and `tick(120_000)` takes no reward argument. `before.inventory.state()` therefore still equals its clone from line 510 whatever the lifecycle does. A payout would only show up through `lost.reward_state`, which is asserted at 515.
  - Fix: assert on what the lifecycle returns. Keep `lost.reward_state.is_none()`, and add a check that the run's grant key is absent (for example `!lost.reward_packets` plus `lifecycle.activity_state()` showing no applied grant). Drop the `before == clone` lines or label them as vacuous.

- **[medium] tests/harvesting_lifecycle.rs:521-527 loss_has_no_payout_and_close_allows_try_again - the duplicate GameOver after Lost checks only `changed`, `replies` and `reward_packets`.**
  - Why it cannot catch a regression: `handle_movie` (src/harvesting_lifecycle.rs:297-304) returns early for Won/Lost runs. A change that let the duplicate stage a `reward_state` or emit `quest_events` would still pass, because lines 521-527 never check either. The seeded test's duplicate block (lines 475-482) does check both, so this one is weaker than its sibling.
  - Fix: add `assert!(duplicate.reward_state.is_none()); assert!(duplicate.quest_events.is_empty());`, and compare `before.inventory.state()` and `before.profiles` with the originals after the call.

- **[medium] tests/harvesting_lifecycle.rs:576-588 reconstructed_quota_and_time_match_visible_candidate - the name overclaims and most assertions restate constants.**
  - Why it cannot catch a regression: the body never touches a "visible candidate" (no screenshot, movie, or quota-init message). Lines 581-584 assert `RECONSTRUCTED_QUOTA_TILES / RECONSTRUCTED_PER_REWARD_TILES == 5` on two constants and never reach `board_spec`. Lines 585-587 compare `board_spec` goals with the same constants that `board_spec` assigns to them (src/harvesting.rs:955-956). The seed check at 580 has the same shape (src/harvesting.rs:1005).
  - Fix: rename to reflect what is checked (for example `board_spec_uses_reconstructed_constants`), or assert literal values (`quota == 25`, `per_reward == 5`, `seed == 2`) so the test fails if someone edits the constants. Also check that `spec.goals` have 4 entries and that `spec.outputs[i].cluster_quantity` matches the literal.

- **[low] tests/harvesting_lifecycle.rs:425 seeded_full_round_grants_produce_chef_xp_and_quest_events_once - exact reply count on the win.**
  - Why it is churn: `win.replies.len() == 4` pins the number of packets the win emits. Any packet added or split, such as a new status or reward notice, breaks the test even though the test is about rewards and events.
  - Fix: assert the packets that matter (the reward packet and the results packet exist, and their opcodes are as expected), or leave the count out.

- **[low] tests/harvesting_lifecycle.rs:416 seeded_full_round_grants_produce_chef_xp_and_quest_events_once - `actions == 22` is an exact count tied to the replay's internals.**
  - Why it is churn: the 22-action count depends on `find_chain`'s search order, budget and `MAX_CHAIN`, not only on the rules under test. The message documents the intent, so the pin is deliberate, but any change to search order fails the test without a payout regression.
  - Fix: keep the seed determinism check as a separate test, or pin the final state (`collected`, `wall_ms`, the 5-bundle outputs) instead of the action count.</result>
</invoke>
