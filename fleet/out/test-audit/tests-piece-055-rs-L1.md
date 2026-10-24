<!-- fleet job=test-audit id=tests-piece-055-rs-L1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[24369, 15799, 10, 4454] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_055.rs lines 1-280 of 280

Window: `prototype/osfr-tools/tests/piece_055.rs` lines 1-280 (read in full), checked against `prototype/osfr-tools/src/restoration/piece_055.rs` 1-326.

Most tests in the window are sound. I checked each lifecycle test against the state machine (`begin_cast`, `advance`, `interrupt`, `resolve`) and each would fail on the regressions it names. The pinned-constant tests compare against literals, not against the code under test, so they are not circular. Two findings:

- **[medium] tests/piece_055.rs:220 timing_overflow_is_refused_instead_of_wrapping - the name claims all timing overflow is refused, but only the cast-time overflow in `begin_cast` is exercised.**
  - Why it cannot catch a regression: `advance` computes `resolve_at_ms = ready_at_ms.checked_add(flight_time_ms)` at src/restoration/piece_055.rs:274-276. Replacing that with `wrapping_add`, or `ready_at_ms + flight` without a check, would still pass this file. Nothing here reaches that line, because `begin_cast(u64::MAX - 10, 1.0)` with `cast_time_ms = u32::MAX` overflows at line 247-249 first.
  - Fix: add a case with `profile(0, u32::MAX, 30.0)`, `begin_cast(u64::MAX - 10, 1.0)` (ready_at does not overflow), then `assert_eq!(attack.advance(u64::MAX - 10), Err(CastError::Invalid))`. Also assert `attack.state() == EnemyCastState::Casting { ready_at_ms: u64::MAX - 10 }`, so the test shows the refused advance does not move the state. Or rename the existing test to say it covers the cast-time overflow only.

- **[low] tests/piece_055.rs:155 resolution_applies_once_and_maps_to_the_recovered_combat_frames - the name says the resolution maps to the recovered combat frames, but the body only checks the returned `resolution` field, never `.frame()`.**
  - Why it cannot catch a regression: if `EnemyAttackIntent::frame()` for `AttackResolution` (src/restoration/piece_055.rs:151) were changed, for example to return `ABILITY_FAMILY`, this test would still pass. The frame mapping is only checked in `intents_map_to_recovered_frames` (lines 264-279), so the name overclaims.
  - Fix: in this test, add `assert_eq!(resolved.frame(), (COMBAT_FAMILY, COMBAT_SUB_ATTACK_TARGET_DAMAGE))` on the `Ok` value, and the matching `Dodged` assertion. Otherwise rename the test to drop the frame claim.
