<!-- fleet job=test-audit id=tests-harvesting-review-rs-L1 status=done turns=7 usd=0.0076 tokens(read,write,in,out)=[73832, 24437, 16, 7547] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/harvesting_review.rs lines 1-342 of 342

Window reviewed: `prototype/osfr-tools/tests/harvesting_review.rs` lines 1-342. Three findings, all confirmed against `src/harvesting.rs` and `src/mining.rs`.

- **[high] prototype/osfr-tools/tests/harvesting_review.rs:157-178 every_supported_region_spec_executes_and_requests_farming_assets - the goal values and bundle item ids are checked against the same lookups (`harvesting::produce_value_for`, `harvesting::produce`) that `board_spec` uses to build them (harvesting.rs:946-965).**
  - Why it cannot catch a regression: if `produce_value_for` or `produce` is changed to map a slug to the wrong value or item definition, `board_spec` and the test's expected side change together and the assertions still pass. The name and message say "recovered produce values (farmingValue401..416)" and "bound to the recovered produce order", but no literal 401..416 or recovered item id is asserted in this test.
  - Fix: pin literals per region, e.g. assert `spec.goals` values equal the recovered 401..416 values for each slug, and `spec.outputs` definition ids equal the recovered item ids, as the reward test already does with `(2885, 5), (2887, 5), (2890, 5), (2877, 5)`.

- **[medium] prototype/osfr-tools/tests/harvesting_review.rs:278-341 harvested_bundles_grant_once_from_a_serialized_completion_state - the name says "serialized" and "persisted", but the body builds a `Type8State` in memory and passes it straight to `Type8Engine::load` (lines 308-321).**
  - Why it cannot catch a regression: nothing is serialized, written, or parsed, so a break in state persistence or restart recovery would still pass. The only restart-related behavior exercised is the in-memory resume.
  - Fix: round-trip the state through the real persistence path (save the run, reload it from disk, then call `OnNextLevelMsg`), or rename the test to drop "serialized" and "persisted".

- **[medium] prototype/osfr-tools/tests/harvesting_review.rs:217-273 emitted_geometry_is_engine_compatible_and_labels_the_fidelity_gap - the fidelity-gap part checks a different shape than the one emitted, and "engine-compatible" is never checked against the engine.**
  - Lines 257-262 assert that `harvesting::diamond_shape(10, 10)` has 76 nonzero cells. That is the unused observed artifact (harvesting.rs:878), not `spec.shape`, and the check does not depend on `game_id`, so it runs identically for every region. The label check (lines 263-271) only looks for the substrings "screenshot" and "fidelity gap" in `rule_notice`, which any wording containing them would satisfy.
  - The test never calls the engine loader. "Engine-compatible" rests only on the shape grammar checks in lines 222-256. The loader is exercised in the first test, but this test's name does not say so.
  - Fix: drop or move the `diamond_shape` count into a separate test that says it covers the artifact. Assert the notice text against a fixed phrase (or the exact `RULE_NOTICE`). Add `Type8Engine::load` for each region in this test, or rename it to drop "engine-compatible".

Not reported: the gap-profile test (lines 184-212) asserts `is_err()` for board, content and write, checks the message, and checks that no file exists. The reward grants (`5` per goal) follow from `RECONSTRUCTED_QUOTA_TILES / RECONSTRUCTED_PER_REWARD_TILES * RECONSTRUCTED_BUNDLES_PER_CLUSTER` (harvesting.rs:780-798; mining.rs:1705-1710). The pinned 11x11 grid and the 76-cell count are intentional, so I did not flag them as over-pinned.
