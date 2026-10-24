<!-- fleet job=test-audit id=tests-piece-044-rs-L1 status=done turns=4 usd=0.0041 tokens(read,write,in,out)=[21528, 14053, 10, 4286] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_044.rs lines 1-252 of 252

Window: `prototype/osfr-tools/tests/piece_044.rs` lines 1-252. I read the window and the module under test (`src/restoration/piece_044.rs`, lines 1-303). The parser, refusal, and preservation paths the window exercises all behave as the assertions expect, and I found no cannot-fail assertion, no `#[ignore]`, and no early return. The findings are name and composition gaps.

- **[medium] prototype/osfr-tools/tests/piece_044.rs:232 switch_decision_and_guard_compose_into_one_accepted_activation - the test claims decision and guard compose into one activation, but the guard is fed a hand-written `after` (`active_profile_id: 43`) rather than the profile from `outcome`.**
  - Why it cannot catch a regression: a caller or wiring change that passes a different profile to `preserve` than `decide_switch` activated still passes. Line 250 checks `outcome` in isolation, and line 246 compares `guard.profile_id` with the test's own literal-derived `after`, so nothing links the two.
  - Fix: build `after` from the outcome, e.g. `let SwitchOutcome::Activate { profile_id } = outcome else { panic!() }; let after = PreservedValues { active_profile_id: profile_id, ..before.clone() };`, then assert `guard.profile_id == profile_id`.

- **[medium] prototype/osfr-tools/tests/piece_044.rs:117 unlocked_profile_switches_and_an_unowned_profile_is_refused_without_mutation - the name promises a "without mutation" check, but the body only compares return values.**
  - Why it cannot catch a regression: nothing is snapshotted or compared after the refusal. `decide_switch` takes `&[i32]` and returns a value, so the test cannot observe state change. It also never asserts the refusal's failure packet (`ProfileRefusal::packet`), which is the only observable output of the refusal path.
  - Fix: either rename it to drop "without mutation", or add an assertion on the refusal packet, `ProfileRefusal::NotOwned.packet(99) == [26,0,26,0,99,0,0,0,0,0,0,0]`, plus a check that `unlocked` is unchanged (e.g. a snapshot compared before and after the call).

- **[low] prototype/osfr-tools/tests/piece_044.rs:162 switching_carries_health_gear_and_the_active_profile_through_unchanged - the name says a switch is exercised, but the body never calls `decide_switch` or any switching code; it only feeds hand-built `before`/`after` values into `preserve`.**
  - Why it cannot catch a regression: a change in how the switch itself alters health, gear or abilities is invisible here. The test only checks that `preserve` copies fields from `after` when they are already equal.
  - Fix: rename to something like `preserve_copies_unchanged_fields_into_the_certificate`, or drive the case through `decide_switch` and a real before/after sample.
