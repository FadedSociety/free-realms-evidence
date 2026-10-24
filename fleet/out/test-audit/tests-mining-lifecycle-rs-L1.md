<!-- fleet job=test-audit id=tests-mining-lifecycle-rs-L1 status=done turns=4 usd=0.0048 tokens(read,write,in,out)=[31002, 19253, 10, 4126] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mining_lifecycle.rs lines 1-582 of 582

Window reviewed: `prototype/osfr-tools/tests/mining_lifecycle.rs` lines 1-582 (whole file). No `#[ignore]` or early-return skips in this file. Fixtures are generated in-test, so there is no missing-fixture skip. Findings:

- **[medium] prototype/osfr-tools/tests/mining_lifecycle.rs:508-517 `loss_has_no_payout_and_close_allows_try_again` - the "no payout" claim is backed by comparing `before`'s inventory and profiles with clones taken from `before` itself, which can never differ.**
  - Why it cannot catch a regression: `before` is only ever passed as `&RewardState` (to `tick`-adjacent `handle` at line 521 and never to `tick` at all), so Rust's borrow rules already guarantee those comparisons hold. A change where the lost run writes a grant to disk, or to a shared store that `before` does not reflect, still passes. The only live check is `lost.reward_state.is_none()` and the empty packet/quest lists.
  - Fix: after the `Lost` tick, reload the inventory and profile state from `fixture.path` (or a fresh `Inventory::load` / `RewardState` from disk) and compare it to the pre-loss snapshot. Also assert the duplicate `FRServer_GameOver` leaves that reloaded state unchanged.

- **[medium] prototype/osfr-tools/tests/mining_lifecycle.rs:551-572 `quit_and_disconnect_preserve_materials_and_create_no_grant` - the "preserve materials" assertions compare `before` against its own clone, so they are tautological.**
  - Why it cannot catch a regression: `before` is borrowed immutably throughout, so `before.inventory.state() == &inventory` (553, 571) and `before.profiles == profiles` (554, 572) can never fail. A quit or disconnect path that grants or deducts materials through any other route (for example a separately persisted inventory) passes. The `reward_state.is_none()` checks cover only the returned value.
  - Fix: reload the inventory and profile files from `fixture.path` after quit and after disconnect, and compare them with the state recorded before `begin_play`. Assert the ore count is still 4 from the reloaded state, not from `before`.

- **[low] prototype/osfr-tools/tests/mining_lifecycle.rs:444-447 `seeded_full_round_wins_and_grants_ore_xp_and_quest_events_once` - the exact `actions == 96` pins the planner's search output, which is not what this test is about.**
  - Why it cannot catch a regression: it is not a payout or event check. Any change to `find_chain` ordering, the node budget, or the ranking heuristic that still wins the round in a different number of chains fails the test, while the payout, XP and quest-event assertions are unaffected. This creates churn without guarding the lifecycle.
  - Fix: keep the bound `actions <= 200` already in `drive_seeded_round` (line 419) and the `collected == [6, 6]` and timer checks. Drop the exact 96, or move it to a separate determinism test that names the planner.
