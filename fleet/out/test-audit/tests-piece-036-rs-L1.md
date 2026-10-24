<!-- fleet job=test-audit id=tests-piece-036-rs-L1 status=done turns=4 usd=0.0062 tokens(read,write,in,out)=[33347, 22717, 10, 6045] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_036.rs lines 1-535 of 535

Window: `prototype/osfr-tools/tests/piece_036.rs` lines 1-535, checked against `prototype/osfr-tools/src/restoration/piece_036.rs` (`WizardCastState::cast`, `regenerate`, `WizardToolbar`). Most tests are sound. I traced the lock/recast ordering (lines 202, 213, 235), the regen carry (283), the inclusive 20-unit reach boundary (314), and the denial ordering (343, 394, 471, 518), and each would fail on a plausible regression. Three findings:

- **[medium] tests/piece_036.rs:447 a_ground_targeted_request_keeps_its_position_and_skips_actor_checks - the name claims the actor checks are skipped, but the body passes `None` as the target, so it never shows that a supplied target is ignored.**
  - Why it cannot catch a regression: if `CastTargeting::Position` were changed to run the dead, disposition, or reach checks against a target whenever one is supplied (src lines 387-391 only check finiteness), this test still passes, because it never supplies a target that would fail those checks.
  - Fix: pass a `Some(&hostile_target(..))` that is dead, or non-hostile, or 30 units away, with `CastTargeting::Position([1.0, 2.0, 3.0, 1.0])`, and assert `Ok` plus the position echo. Add a second assertion that the same request with a non-finite position returns `NonFiniteTarget` even when that target is valid.

- **[low] tests/piece_036.rs:393 unresolved_malformed_and_non_finite_requests_are_rejected - "malformed" is not exercised as a distinct case; the test covers unresolved, mismatched and zero guids, plus one non-finite position.**
  - Why it cannot catch a regression: nothing checks a malformed request other than the cases already listed, so a change to how a malformed request is parsed or rejected would not be caught. The name promises more than the body proves.
  - Fix: either rename it to cover what is tested (for example `unresolved_guid_and_non_finite_position_are_rejected`), or add a case the code can actually distinguish, such as a non-finite caster position with a Guid target expecting `NonFiniteCaster` before `UnknownTarget` (src lines 357-359 define that order).

- **[low] tests/piece_036.rs:107 the_three_recovered_wizard_abilities_carry_their_real_effects - the body pins presentation fields (`icon_id`, `name_id`, `animation_id`, `hit_effect_id`, `target_animation_id`) that have nothing to do with the cast effects the name claims.**
  - Why it cannot catch a regression: it is not a missed bug. Any icon or string-id refresh from the community data would fail this test even when the cast behaviour is unchanged, which is churn that hides the real signal.
  - Fix: keep the damage, energy cost, and effect family assertions in this test. Move the icon and name id pins into a separate data-table test, or pin them only when a cast-facing field changes.

No `#[ignore]`, no early returns on missing fixtures, and no `is_ok()`-only tests that cannot fail were found in the window. The 235 "exactly once" test was checked: a double energy spend would make `state.energy()` go negative and fail line 256, so it is not a hole.
