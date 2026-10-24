<!-- fleet job=test-audit id=tests-derby-rs-L1 status=done turns=10 usd=0.0102 tokens(read,write,in,out)=[172088, 31860, 22, 9004] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/derby.rs lines 1-583 of 583

Reviewed `prototype/osfr-tools/tests/derby.rs` lines 1-583 against `src/derby.rs` (contact handler ~1320-1450, `finish_match` 1602, `tick` 1634). Most tests hold up: the refusal/cooldown test is valid (a refused 10-damage hit at 5100 does not consume the cooldown, so the 5-damage hit at 5200 still lands), the contact-gate test's `hit(50.1)` rejection is real (`impact > max_impact` at derby.rs:1331), and the relay/disconnect test pins the recipients. Findings:

- **[medium] tests/derby.rs:351 `contacts_apply_server_damage_knockout_scores_and_four_second_respawn` - the "four-second respawn" is never checked; the test only asserts that a respawn has happened by t=10100.**
  - Why it cannot catch a regression: knockout at t=6000 sets `respawn_at_ms = now + respawn_delay_ms` (derby.rs:1436), and `tick` respawns once `deadline <= now` (derby.rs:1675). A change that makes the respawn 1 s (fires at 7000) or 4.1 s would still pass the `tick(10_100)` check at line 382-385. Nothing asserts that the respawn does not happen early.
  - Fix: call `derby.tick(9_999)` and assert no `ResetVehicle(OTHER)` is emitted and `driver(OTHER).health == 0`; then `tick(10_000)` and assert `ResetVehicle(OTHER)` and health 20.

- **[low] tests/derby.rs:380 `contacts_apply_server_damage_knockout_scores_and_four_second_respawn` - the repeat hit at 6100 is asserted to be empty, but that is the dead-victim gate (derby.rs:1383-1386), not the pair cooldown.**
  - Why it cannot catch a regression: the victim has health 0 at that point, so the empty result would hold even if the cooldown were removed. The test does not exercise the cooldown here, although a reader would take it as doing so.
  - Fix: either drop the assertion, or add a non-knockout scenario that repeats a hit at +100 ms with the victim still alive and expects it to be empty. The cooldown is already covered by the `refused_contact...` test.

- **[low] tests/derby.rs:439 `each_powerup_type_applies_once_and_expiry_uses_client_categories` - `boost > 0.0` does not pin the boost grant.**
  - Why it cannot catch a regression: the boost pickup is configured as `boost_pickup: 15.0` (test fixture line 36), but a change that grants any positive amount (for example 0.01, or a wrong constant with the wrong sign handling) would still pass.
  - Fix: `assert_eq!(derby.driver(OWNER).unwrap().boost, 15.0)`, which is exact since boost starts at 0.0 (derby.rs:880).

No `#[ignore]`, no early-return fixture skips, and no tautological expected values were found in this window. The hard-coded payload lengths in `all_twenty_client_records_roundtrip_with_reader_widths` (lines 263-284) are independent constants, so they are not a self-reference problem; I did not verify them against the client's reader widths.
