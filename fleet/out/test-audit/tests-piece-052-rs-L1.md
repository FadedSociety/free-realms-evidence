<!-- fleet job=test-audit id=tests-piece-052-rs-L1 status=done turns=4 usd=0.0058 tokens(read,write,in,out)=[26004, 18504, 10, 6441] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_052.rs lines 1-362 of 362

Window: `prototype/osfr-tools/tests/piece_052.rs` lines 1-362, checked against `prototype/osfr-tools/src/restoration/piece_052.rs` (tick, validation and packet encoders). The contract tests (`recovered_contract_constants`, both packet-layout tests, `patrol_cycles_run_and_stand_between_waypoints`, and `patrol_rejects_malformed_routes`) hold up: their expected values are literals or built independently, and I traced each rejection case to the validation order in `PatrolRoute::new`, so they would fail on regressions. The findings below are the gaps I could confirm.

- **[medium] tests/piece_052.rs:187 `patrol_heading_is_always_a_unit_horizontal_vector` - the test passes if the controller never moves, and the "every visited position" check only looks at the final position.**
  - Why it cannot catch a regression: if `tick` stops emitting movement (for example, it returns early on every call, or `heading` is never written), the `for reply in ...` body never runs, so the unit-length and state-byte checks are skipped. The final position stays at `[0,0,0]`, which satisfies `(-0.001..=10.001).contains(&0.0)`, `position[1]==0` and `position[2]==0`. The test is green with no movement at all. The comment on line 210 ("every visited position stays inside the route box") also overclaims, because only the last position is checked.
  - Fix: count the movement messages seen and assert the count is at least some N (for example, `assert!(moves > 50)`). Also assert `patrol.waypoint_index()` advanced or that `patrol.position()[0] > 0.0` after the loop. Inside the loop, check `patrol.position()` on each tick that emits movement, not only at the end.

- **[low] tests/piece_052.rs:218 `patrol_step_is_time_bounded` - it asserts only an upper bound on travel, so a controller that never moves passes.**
  - Why it cannot catch a regression: `travelled <= 0.75 + 1e-3` holds for `travelled == 0`. If the controller stops moving entirely, the test still passes. The ceiling is also hard-coded as `3.0 * 0.25` instead of coming from `MAX_STEP_MS`/speed, so it does not name the constant it is meant to pin.
  - Fix: also assert `travelled > 0.5` (the expected step after the 60 s jump is about 0.75 m, since the step is clamped to `MAX_STEP_MS` = 250 ms at 3 m/s). Add a lower bound so a stall fails. Optionally take the ceiling from `MAX_STEP_MS`/`MAX_PATROL_SPEED` (import them) rather than repeating literals.

- **[low] tests/piece_052.rs:353 `patrol_never_targets_the_player_guid` - the name says the enemy never targets the player, but the body only checks that the constructor rejects guids 0 and 1.**
  - Why it cannot catch a regression: a change that accepts guid 1 in a different path (for example, a setter, or a `tick` that emits packets for a guid it was given by other means) still passes this test. Only `PatrolController::new` is exercised; no packet or `tick` output is checked for the player guid.
  - Fix: rename to something like `patrol_constructor_rejects_player_guid`, or add a check that a controller built with a valid guid emits packets carrying that guid and never 0 or 1 (for example, `movement_packet` bytes 2..10 equal `GUID` for every reply from `tick`).

No `#[ignore]`, no early-return skips, and the `#[path]` fixture `src/restoration/piece_052.rs` exists, so there is no silent skip.
