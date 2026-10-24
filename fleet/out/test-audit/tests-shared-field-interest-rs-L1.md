<!-- fleet job=test-audit id=tests-shared-field-interest-rs-L1 status=done turns=5 usd=0.0090 tokens(read,write,in,out)=[86260, 34819, 12, 7567] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/shared_field_interest.rs lines 1-1200 of 1213

Window: `prototype/osfr-tools/tests/shared_field_interest.rs` lines 1-1200 (all read, plus 278-301, 563-601, 866-901, 1181-1200 where the first reads truncated). Two findings in the window; the rest checked out.

- **[medium] prototype/osfr-tools/tests/shared_field_interest.rs:969-973 w127_two_bot_attacker_pc_excluded - the "attacker PC excluded" check in the lethal batch tests actor GUID `1`, which is not a participant, so it can never fail.**
  - Why it cannot catch a regression: the attacker in this test is PC 101 (A) and PC 202 (B). The loop over `lethal` asserts `!any(is_sub(p, 32, 7) && p.get(4..12) == 1_u64)`. No code path produces an attack from GUID 1 in this fixture, so that predicate is always false. If the server started sending A's hit to B with the real attacker GUID 101, the test would still pass. Only the three narrow `hits_from(...)` checks at lines 964-966 touch the claim, and they cover one batch each.
  - Fix: replace the GUID-1 predicate with `hits_from(packets, 101) == 0` for the recipient that must not learn the PC (B's batches in `first`, `second`, `lethal`), and `hits_from(packets, 202) == 0` for A's batches. That makes a leak of the real attacker GUID fail the test.

- **[low] prototype/osfr-tools/tests/shared_field_interest.rs:711-728 t032_a_seeded_zone_is_seeded_by_public_entry - the name says the zone is "seeded" by public entry, but the body only checks the instance kind is Public and that some field exists.**
  - Why it cannot catch a regression: `World::field(..).is_some()` passes for any installed runtime. The seed from `install_field_seed` (world.rs:915-920, `ensure_field_from_seed` at world.rs:924) is never compared. A regression that installs an empty or wrong-content field would still pass.
  - Fix: after `enter_public`, assert `world.field(entered.instance_id).unwrap().health(E) == Some(300)` (the seeded full HP), and optionally `interest_candidates` contains E, so the seed content is what gets checked.
