<!-- fleet job=test-audit id=tests-piece-035-rs-L1 status=done turns=6 usd=0.0083 tokens(read,write,in,out)=[72355, 25444, 14, 8856] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_035.rs lines 1-446 of 446

Window reviewed: `prototype/osfr-tools/tests/piece_035.rs` lines 1-446, against `src/restoration/piece_035.rs` (read in full). No `#[ignore]` or early-return skips in the window. The decode, toolbar, reach, and line-of-sight assertions do exercise the real code paths and their boundary cases (e.g. 30.0 admitted, 30.01 refused, wall segments that just miss). The findings below are the real gaps.

- **[medium] tests/piece_035.rs:102-106 archer_kit_is_the_recovered_ranged_kit_and_outreaches_the_melee_kits - the name says it outreaches the melee kits, but no melee value is compared; the only melee claim is a hard-coded `WIZARD_AUTO_TARGET_REACH > 7.0`.**
  - Why it cannot catch a regression: `MELEE_AUTO_TARGET_REACH` (src line 108) is never imported or asserted. Changing it to 25.0 or 30.0 leaves this test green, so the "melee kits are at 7u" claim goes unchecked, and the Archer-outreaches-melee claim is never tested against melee at all.
  - Fix: import `MELEE_AUTO_TARGET_REACH` and assert `ARCHER_AUTO_TARGET_REACH > MELEE_AUTO_TARGET_REACH` and `MELEE_AUTO_TARGET_REACH == 7.0`. Or rename the test to drop "melee kits".

- **[medium] tests/piece_035.rs:327-368 composed_gate_checks_reach_then_geometry_and_refuses_non_finite_positions - the name says reach is checked before geometry, but the order is not observable.**
  - Why it cannot catch a regression: `admit_ranged_action` (src 445-453) returns the same `NoCastReason::Targeting` for both reach and geometry refusals, and both checks are side-effect-free. Swapping to `sight.admit(...)?; gate.admit_position(...)` still passes every assertion (the 100u case and the wall case return `Targeting` either way). `LineOfSight` is a closed enum, so the test cannot spy on evaluation order.
  - Fix: either rename the test to drop "checks reach then geometry" and keep only the outcome claims, or give the ordering a visible effect (e.g. a `LineOfSight` variant or counter that records whether it was consulted, so an out-of-reach request asserts geometry was never evaluated).

- **[low] tests/piece_035.rs:431-446 projectile_subs_are_known_but_their_payloads_stay_unrecovered - the constructor assertions compare each constructor with `Unrecovered(SAME_CONST)`, and the last line asserts a hard-coded `has_recovered_layout() == false`.**
  - Why it cannot catch a regression: the expected values come from the same constants the code uses (src 517-531). The constructor mapping is still pinned, so a swap is caught; but the `has_recovered_layout` line only pins a stub that returns `false` for any input, so a layout that is recovered and wired in would need only this assertion changed and gives no evidence of the layout itself.
  - Fix: keep the constructor checks, and add a comment or a dedicated check that this is a placeholder to be replaced when a payload layout is recovered (no real canary is possible until one is).

- **[low] tests/piece_035.rs:267-287 start_casting_frame_matches_the_client_constructor_defaults - the name claims a match against the client constructor, but the test never reads the client; it only encodes the literals it was given and checks them against the encoder's byte offsets.**
  - Why it cannot catch a regression: if the client's constructor defaults changed (e.g. animation -1 to 0), this test would still pass because the expected defaults are typed into the test itself, not read from the client source or a fixture.
  - Fix: rename to `start_casting_frame_has_the_recovered_layout` or cite the constructor (`FUN_00a2ed30`) in a doc comment and drop "matches the client constructor defaults" from the name.
