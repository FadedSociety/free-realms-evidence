<!-- fleet job=test-audit id=tests-kart-service-rs-L3601 status=done turns=11 usd=0.0121 tokens(read,write,in,out)=[251189, 42114, 24, 8713] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_service.rs lines 3601-4095 of 4095

Window `kart_service.rs` 3601-4095 read in full, with the code under test in `src/kart_service.rs` (restore checks ~2130-2360, construction validation ~1236-1312, snapshot struct ~795-955). Most assertions in the window are real: the `track`, `session_id`, `attempts`, `observations`, `shield_expiry` and `bounds` restore refusals all match checks in `restore`, and the schedule and gate-floor cases hit the correct error variants. The `#[ignore]`d capture test has a reason string and no early return. Four findings:

- **[medium] tests/kart_service.rs:3623 abort_and_replay_paths_never_offer_a_reward - the name claims replay paths are covered, but the body only exercises abort and a claim after abort.**
  - Why it cannot catch a regression: the replay refusal (`ServiceRefusal` for a gate the racer already passed, src/kart_service.rs:388) is never triggered. A change that let a replayed gate hit through after a legitimate lap would still pass, because the test never sends one.
  - Fix: after the lap, re-send the gate-1 claim at a later time (a replay, not an abort) and assert the replay refusal with `service.snapshot()` equal to the pre-claim snapshot. Or rename the test to `abort_never_offers_a_reward`.

- **[medium] tests/kart_service.rs:3639 snapshot_restore_round_trips_and_preserves_the_one_shot - "round-trips" is asserted only for `laps_completed`, `phase`, `observations` and `finish_flag`.**
  - Why it cannot catch a regression: `snapshot()` or `restore()` could drop or reset `claim_credit_m`, `queued_items`, `weapon_pose`, `pickups_consumed`, `last_boost_epoch` or `countdown_sent`, and every assertion here would still pass. The save-decision equality (`save_decision_eq`) covers these fields, but this test never compares them.
  - Fix: assert `KartService::restore(synthetic_content(), snapshot.clone()).unwrap().snapshot().unwrap() == snapshot` right after the lap (the flood-budget field is excluded from `save_decision_eq`, so compare the full struct or use `save_decision_eq` on the two snapshots). Then the round-trip claim is actually tested.

- **[low] tests/kart_service.rs:3828 content_bounds_are_refused_at_construction - the name says the bounds are refused at construction, but the last two cases (3917-3924, `ZeroSession` and `ZeroPlayerGuid`) are checked through `service.begin`, not `KartService::new`.**
  - Why it cannot catch a regression: a change that moves the context validation out of `begin` would still pass the test under this name, and nothing checks that `new` accepts the context-free content.
  - Fix: move those two cases into a test named for `begin` (for example `begin_refuses_a_zero_binding`), or rename this test to cover `begin` as well.

- **[low] tests/kart_service.rs:3881-3889 content_bounds_are_refused_at_construction - the `ScheduleCountdown` case pins `index: 12`, which is the length of the `recovered_schedule()` fixture (tests/kart_service.rs:87-138), not a property of the bound.**
  - Why it cannot catch a regression: it does not fail on a bug. It fails on unrelated schedule edits, such as adding a step to the recovered cadence, even though the countdown bound is unchanged.
  - Fix: compute the index from the schedule (`content.schedule.len()` before the push), or compare only the variant with `ServiceError::ScheduleCountdown { value: 9, .. }`.
