<!-- fleet job=test-audit id=tests-combat-rs-L1 status=done turns=5 usd=0.0052 tokens(read,write,in,out)=[32874, 15737, 12, 5875] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/combat.rs lines 1-290 of 290

Window: `prototype/osfr-tools/tests/combat.rs` lines 1-290. I read the window in full and checked it against `src/combat.rs` (load, handle, attack, spawn, menu/relevance encoders, and path validation). Most assertions are sound: the spawn offsets (name at 106+9, texture at 81, range at 133+9+10) match the field shifts that `replace_empty_string` makes, and the cooldown boundaries at 999/1599/1600 and the respawn-resets-cooldown check at line 200 would each fail on a real regression. Three findings:

- **[high] tests/combat.rs:244 corrupt_private_template_and_escaping_filename_are_rejected - the `../npc.bin` rejection is asserted after the template was already corrupted, so the assertion does not isolate the path guard.**
  - Why it cannot catch a regression: `npc.bin` is corrupted at line 247 and never restored. The second `Combat::load` at line 258 fails on the hash mismatch (`combat.rs:111`) regardless of the path guard. If the guard at `combat.rs:104-109` were deleted, `directory.join("../npc.bin")` would point outside the fixture, most likely at a missing file, so the load still returns an error and the test still passes.
  - Fix: before line 250, rewrite `npc.bin` with its valid bytes (or use a fresh `Content`) so the traversal case is the only fault. Then assert the specific error, e.g. `Combat::load(...).unwrap_err().to_string().contains("local filename")`. Also assert the hash-mismatch message in the first half so that `is_err()` is not satisfied by an unrelated I/O error.

- **[low] tests/combat.rs:116-121 interaction_and_menu_layout_are_bounded_by_identity_and_range - the test pins the menu label IDs 79 and 22498, which the test name does not cover.**
  - Why it is churn, not a gap: the test is about identity and range gating, but any change to the label constants in `combat.rs:298` or `:309` fails it, even when the gating is correct.
  - Fix: assert `u32_at(menu, 25)` against the `INTERACTION_*` label constant, or check only that the entry count and the identity-based `replies` shape are correct, and leave the label value to a dedicated content test.

- **[low] tests/combat.rs:277-288 private_capture_template_loads_and_relocated_packets_keep_expected_shape - the ignored private-content test hard-codes timings (0, 600, 1200, 1800 ms) and the four-hit kill sequence.**
  - Why it is fragile: these only match if the private `combat.json` has `cooldown_ms <= 600` and `hit_damage` of 25 (or otherwise 4 hits). The test passes its reason gate (`#[ignore = "..."]` at line 262 has a reason) and fails with a misleading message when those values differ.
  - Fix: read `cooldown_ms` and `hit_damage`/`max_health` from the loaded content (or expose them from `Combat`) and compute the hit times and count from those values.
