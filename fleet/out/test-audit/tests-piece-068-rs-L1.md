<!-- fleet job=test-audit id=tests-piece-068-rs-L1 status=done turns=6 usd=0.0067 tokens(read,write,in,out)=[70193, 24181, 14, 5868] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_068.rs lines 1-532 of 532

Window `tests/piece_068.rs` 1-532. I read the test file in full and the code under test (`src/restoration/piece_068.rs`, 1-460). Most assertions are sound: the event-to-route equality checks (`every_typed_event_credits_only_its_matching_route`), the zero-identifier and validation refusals, the visit zone/radius checks, and the JSON schema rejection all compare against hard-coded expectations and would fail on realistic regressions. The ignored cross-check at 519-532 has a reason string, so it is not a silent skip. Three findings:

- **[medium] tests/piece_068.rs:304 gather_and_craft_credit_clamps_to_the_required_count - the craft half never reaches the clamp, so the name overclaims.**
  - Why it cannot catch a regression: the craft test uses `quantity: 2` against `required: 5` (recipe 2002, lines 320-332), and the other craft case uses quantity 1 (lines 213-222). Dropping `.min(route.required)` from the Craft arm (`src/restoration/piece_068.rs:419`) would give credit 2 and still pass, because 2 < 5. Only the gather arm (quantity 10 clamped to 4, line 306-318) actually exercises clamping.
  - Fix: add `Craft { recipe_id: 2002, quantity: 9 }` and assert the credits are `credit(910005, 91000504, 5, 5)` and `credit(910015, 91001502, 5, 5)`. A missing or wrong clamp on craft would then fail.

- **[low] tests/piece_068.rs:274-277 unrecovered_kill_targets_are_refused_instead_of_guessed - the first assertion cannot fail.**
  - Why it cannot catch a regression: `QuestEventRouter::recovered()` goes through `new()`, which already rejects `Kill` with `definition_id <= 0` (`src/restoration/piece_068.rs:336`, returning `ZeroIdentifier`). The `recovered().unwrap()` on line 273 therefore already enforces this invariant, and the `all(...> 0)` check repeats it. Its only effect is to restate the constructor's guard.
  - Fix: delete it, or replace it with a check that can fail on a real regression, e.g. `assert!(recovered.routes().iter().all(|r| r.objective_key != 14096))`, which guards the un-routable Petty Yeti objective the test name is about.

- **[low] tests/piece_068.rs:57-61 recovered_table_carries_every_typed_kind_with_its_recovered_identifiers - exact route count of 36 is incidental to this test's purpose.**
  - Why it cannot catch a regression: the test is about kinds and identifiers, but adding or removing any single extraction row (for example a new stage in `RECOVERED_ROUTES_JSON`, `src/restoration/piece_068.rs:41-81`) breaks it even when every checked identifier is still right. This is churn, not a missed bug. The per-objective `find` checks below already pin what matters.
  - Fix: drop the `routes.len() == 36` assertion, or keep it only in the embedded-table cross-check, and rely on the per-objective assertions.
