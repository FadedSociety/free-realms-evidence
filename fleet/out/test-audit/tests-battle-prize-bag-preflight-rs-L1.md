<!-- fleet job=test-audit id=tests-battle-prize-bag-preflight-rs-L1 status=done turns=4 usd=0.0058 tokens(read,write,in,out)=[37936, 20850, 10, 5723] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/battle_prize_bag_preflight.rs lines 1-843 of 843

Window: `prototype/osfr-tools/tests/battle_prize_bag_preflight.rs` lines 1-843. Four findings.

- **[high] prototype/osfr-tools/tests/battle_prize_bag_preflight.rs:809 the_preflight_answers_like_the_payout_path - the test only checks that the preflight agrees with `grant_bundle`, and the preflight is defined as `grant_bundle` on a clone, so the assertion is a tautology.**
  - Why it cannot catch a regression: `accepts_reward_bundle` (src/inventory.rs:532-534) is `items.len() <= MAX_REWARD_BUNDLE && self.clone().grant_bundle(0, items).is_ok()`. The loop at lines 814-831 asserts `accepted == paid` with `paid = grant_bundle(...).is_ok()`, and never asserts an expected truth value. If `grant_bundle` starts refusing a valid row such as `vec![(item, 1)]`, or starts accepting an invalid one such as `(0, 1)`, both sides move together and the test still passes. Only the 17-row case at 835-837 pins a concrete value, and that one is a `grant_bundle` expectation too.
  - Fix: keep the equality, and add a hard-coded expected value per case, for example `assert!(accepts_reward_bundle(&[(item, 1)]))`, `assert!(!accepts_reward_bundle(&[(0, 1)]))`, `assert!(!accepts_reward_bundle(&[(item, 0)]))`, and `assert!(accepts_reward_bundle(&[(item, max_stack), (item, 1)]) == false)` on the full-bag fixture. Those fail when the shared rule changes, which the equality alone cannot see.

- **[medium] prototype/osfr-tools/tests/battle_prize_bag_preflight.rs:663 a_bundle_that_fits_still_starts_and_pays - the doc says "the arena spawns" but the return value of `arena_spawned` is discarded and nothing is asserted about the spawn.**
  - Why it cannot catch a regression: `arena_spawned(&mut gateway, 1_100);` (line 663) returns a `GatewayOutcome` that is ignored. A change that starts the battle and zones the player but never spawns the arena (no replies, no 41/114-type or arena packets) still passes, because the later checks only cover the chat win payout and the Close.
  - Fix: `let spawned = arena_spawned(&mut gateway, 1_100); assert!(spawned.replies.iter().any(|p| !p.is_empty()), ...)`, or better, assert a concrete spawn packet from `field_battle_roster`'s pinned shape, so a missing spawn fails the test.

- **[low] prototype/osfr-tools/tests/battle_prize_bag_preflight.rs:548-549 the_whole_previewed_bundle_must_fit_before_the_battle_starts (doc) - the doc says "Every shipped row passes the single-row check", but no line checks the shipped rows.**
  - Why it cannot catch a regression: the single-row claim is only checked for the synthetic `item` at line 567 (`runtime_inventory().accepts_reward(item, max_stack)`). If shipped rows were changed to fail the single-row check, this test would still pass, so the doc's premise is unverified.
  - Fix: either drop the sentence, or assert over the shipped battle rows: iterate `battle_row()`-style prizes from `field_battles.json` (other than 12310) and assert `accepts_reward(item_id, quantity)` for each.

- **[low] prototype/osfr-tools/tests/battle_prize_bag_preflight.rs:582-586 the_whole_previewed_bundle_must_fit_before_the_battle_starts - `assert_eq!(refused.replies.len(), 1, ...)` pins the exact reply count, which is incidental to the refusal being tested.**
  - Why it is churn: any unrelated extra reply (for example a new inventory or status packet on a refused start) breaks this test even though the refusal itself is still correct. The refusal's real contract is the chat line plus the unchanged saved bytes, and those are already checked at lines 583 and 588.
  - Fix: drop the exact count and assert that the only chat packet is the refusal line, for example by checking `chat_text(&refused).contains(REFUSAL)` and that no encounter or zoning packet appears (`!refused.began_zoning`, `!encounter_active`), which the test already does.

No `#[ignore]` attributes or early-return fixture skips appear in the window. The runtime content and reference fixtures are expected via `expect`/`unwrap`, so a missing fixture fails rather than passes.
