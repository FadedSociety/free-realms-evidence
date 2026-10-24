<!-- fleet job=test-audit id=tests-piece-014-rs-L1 status=done turns=6 usd=0.0050 tokens(read,write,in,out)=[37058, 14017, 14, 5715] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_014.rs lines 1-149 of 149

Window: `prototype/osfr-tools/tests/piece_014.rs` lines 1-149. Code under test read: `prototype/osfr-tools/src/restoration/piece_014.rs` (PATTERNS 90-, EQUIPMENT 345-442, SLOTS 444-448, CLASS_OWNERS 450-475, PROFILES 477-498, `allows` 534-546, `check_equip` 550-558). No `#[ignore]` or early-return skips in the window, and no pure self-comparison. The main problems are names that claim more than the bodies check, plus a few over-pinned counts.

- **[medium] tests/piece_014.rs:118 `unknown_definitions_profiles_and_slots_are_rejected` - the name says slot rejection is covered, but the body only checks UnknownDefinition and UnknownProfile; no SlotNotAllowed is asserted through `check_equip`.**
  - Why it cannot catch a regression: every EQUIPMENT entry has slot 7 (src 345-442), and both PROFILES include slot 7 (src 486, 496). So `check_equip` cannot return SlotNotAllowed for any real input. Removing the slot check from `allows` (src 540-544) would leave this test green. The slot path is only reached in the separate test at 134-149, which calls `allows` directly.
  - Fix: either rename the test to drop "slots", or add an assertion through the public entry point, e.g. a fixture profile with `slots: &[1]` and an allowlisted class, asserting `allows(...)` returns `SlotNotAllowed { slot: 7 }`. Then also check `check_equip` on a real profile/definition pair that the slot check rejects.

- **[medium] tests/piece_014.rs:82 `blacksmith_crafts_the_pattern_but_only_brawler_equips_the_hammer` - the name says the Blacksmith crafts the pattern, but nothing links pattern 2506 (or any pattern) to the Blacksmith; only class-allowlist membership of 58 is checked (line 97).**
  - Why it cannot catch a regression: the crafting relationship is never exercised. Changing pattern 2506's category or class, or the owner of class 58 in CLASS_OWNERS (src 450-475), would not fail this test. Line 70 covers class 58 owner separately, but not in this test.
  - Fix: assert `pattern(2506)` exists, that `class_owner(58).profile_id == profile(BLACKSMITH).id`, and that the product class (71) owner is BRAWLER, all in this test. Or rename the test to describe only the equip restrictions.

- **[medium] tests/piece_014.rs:17 `pattern_catalogue_matches_recovered_class58_records` - the name claims the whole catalogue matches the recovered records, but only three of the 28 records (2506, 869, 838) are checked for their fields, plus the length.**
  - Why it cannot catch a regression: a wrong name, name_id, description_id, category, or type on any of the other 25 entries in PATTERNS (src 90-) still passes. The length check on line 18 compares against `PATTERN_COUNT`, which is a constant in the same module. It only checks count, not content.
  - Fix: iterate over a table of expected (id, name, name_id, description_id, param1, category_id, type_id) tuples and compare every record, or rename the test to say it checks three sample records.

- **[low] tests/piece_014.rs:110 `slot_seven_is_the_recovered_weapon_slot` - the exact `slot_count() == 1` pins the size of the slot table, which is unrelated to what the test is about (slot 7 being Weapon).**
  - Why it is churn: adding a second slot definition, which is harmless and unrelated to weapon-slot identity, would break this test. The real question is the lookup of slot 7.
  - Fix: drop the count assertion, or move it to a dedicated test of table shape. Keep `slot(7)` name/is_weapon checks and `slot(1).is_none()` only if slot 1 is still meant to be absent.

- **[low] tests/piece_014.rs:42 `spunky_family_is_one_weapon_definition_with_ten_tints` - `equipment().len() == 12` pins the whole EQUIPMENT table size.**
  - Why it is churn: adding any unrelated equipment record (for example another class 25 item) fails a test about the hammer family. The test is about the 30280..=30289 family and the substitute/tool records.
  - Fix: remove the global count, or assert that the family IDs are all present and are the only records with name "Spunky Scrapper Hammer" (e.g. `equipment().iter().filter(|e| e.name == ...).count() == 10`).

- **[low] tests/piece_014.rs:113 `slot_seven_is_the_recovered_weapon_slot` - the exact array `&[1, 2, 3, 4, 5, 7, 13]` pins the full recovered spool for the Blacksmith profile, when the test's point is that slot 7 is allowed and slot 8 is not.**
  - Why it is churn: a legitimate update to the Blacksmith spool (for example adding slot 6 from a newly recovered record) fails this test even though the weapon-slot claim still holds.
  - Fix: assert `slots.contains(&SLOT_WEAPON)` and `!slots.contains(&8)` (already on line 115), and keep the full-spool pin in a single fixture-data test if it is wanted.
