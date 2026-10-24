<!-- fleet job=test-audit id=tests-abilities-rs-L1 status=done turns=5 usd=0.0072 tokens(read,write,in,out)=[53470, 27627, 12, 6496] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/abilities.rs lines 1-587 of 587

Window `prototype/osfr-tools/tests/abilities.rs` lines 1-587. I read the window in full and the code under test (`src/abilities.rs` lines 60-200, 473-760) plus the fixture `tests/fixtures/abilities/medic.json`. Most tests hold up: `assert_failure` compares caster and target before and after, the byte helpers are hand-encoded rather than derived from the code, and the cooldown test checks the exact boundary (199 rejected, 200 accepted, matching `now_ms < until` in `validate_use`). The findings are below.

- **[medium] tests/abilities.rs:14 job_effect_bounds_reject_zero_timers_unbounded_targets_and_nonfinite_numbers - every assertion is a rejection (`!valid()` or a deserialize error), so there is no positive control.**
  - Why it cannot catch a regression: an implementation of `JobEffect::valid()` that returns `false` for every input (for example, a gate that rejects all job effects) passes every assertion. The same holds if the upper bounds were loosened, as long as the five sample values stay rejected. The boundary values are never checked either: `max_targets` 16 (accepted by `(1..=16)` at src/abilities.rs:138), `interval_ms == duration_ms`, and `multiplier` at 0.01 and 10.0 are not exercised.
  - Fix: add a valid-accepting case for each variant at its inclusive boundary, e.g. `AreaDamage{radius:0.1,max_targets:16,..}`, `DamageOverTime{multiplier:10.0,duration_ms:30000,interval_ms:30000}`, `Stun{duration_ms:10000}`, and `Buff{..damage_multiplier:3.0..}`, each asserting `valid()` is true, plus one value just past each bound asserting false.

- **[low] tests/abilities.rs:565 applied_effect_expires_once_with_remove_tag_message - the name promises "once", but nothing checks that a later tick stays silent.**
  - Why it cannot catch a regression: the test ends with `active_effects.is_empty()` and never calls `tick_effects` again. If the removal were re-emitted on a later tick, for example because `tick_effects` stopped removing entries, or because a refresh re-added the tag with a stale deadline, the test would still pass at its last assertion.
  - Fix: after line 585, add `assert!(abilities::tick_effects(&mut target, 2101).is_empty());` and `assert!(abilities::tick_effects(&mut target, 5000).is_empty());`, or rename the test to drop "once".

- **[low] tests/abilities.rs:169 medic_fixture_loads_with_source_tags_and_client_profile - the exact `count() == 3` pins the fixture size, which is unrelated to the test's subject (source tags and the client profile).**
  - Why it cannot catch a regression: it is not a gap. Adding or removing a catalogue entry (the fixture is data, and the other tests depend on ids 10001-10003 only) fails this test even when every source tag is still present, which causes churn.
  - Fix: drop the count, or assert that ids 10001, 10002 and 10003 are each present with `catalog.get(id).is_some()`.
