<!-- fleet job=test-audit id=tests-inventory-v2-fixes-rs-L1 status=done turns=4 usd=0.0025 tokens(read,write,in,out)=[11354, 7194, 10, 3015] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/inventory_v2_fixes.rs lines 1-89 of 89

Window reviewed: `prototype/osfr-tools/tests/inventory_v2_fixes.rs` lines 1-89. I read the code under test in `prototype/osfr-tools/src/inventory_v2_fixes.rs` (`encode_definition_batch_v2` lines 35-90, `encode_item_update_v2` lines 108-121). The real assertions are sound: the expected bytes and error values are hand-written constants, not derived from the code under test, and the missing-ID, byte-length, count, record-order, and 38/3 field-order checks would each fail on the regressions they name. No high or medium findings.

- **[low] tests/inventory_v2_fixes.rs:43 catalogue_encoder_rejects_owned_ids_missing_from_35_37 - the only assertion here on the "old" path checks the test-local mirror `current_definition_encoder`, not the product's `definitions_packet`.**
  - Why it cannot catch a regression: the check `old[8..12] == 1` only verifies the hand-written helper's own count field. Changing or deleting the real inventory path leaves it passing, and it says nothing about the gate. The test's real assertion (line 45-46) is still valid.
  - Fix: remove line 43 and the `old` mirror, or replace it with a check against the production `definitions_packet` output, so the "current behavior" claim rests on real code.

- **[low] tests/inventory_v2_fixes.rs:87 item_update_uses_stored_count_and_last_cast_not_ability_or_rental_fields - `assert_ne!(old, fixed)` compares against the test-local `current_item_update` mirror, so it adds no coverage.**
  - Why it cannot catch a regression: line 86 (`assert_eq!(fixed, expected)`) already pins the exact 38/3 bytes, so this line is redundant. It would still pass if the mirror and the encoder drifted together, and it does not show anything about the production code.
  - Fix: delete line 87, or assert on the production old-layout encoding if one exists. Keep line 86 as the canary; it fails if ability_count or rental fields are written, or if field order changes.

Low-severity churn note: none. The tests do not pin incidental counts or offsets beyond the wire layout the name claims to check.
