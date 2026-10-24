<!-- fleet job=test-audit id=tests-brawler-mongo-chain-rs-L1 status=done turns=6 usd=0.0097 tokens(read,write,in,out)=[100488, 35407, 14, 8477] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/brawler_mongo_chain.rs lines 1-1200 of 1830

Window reviewed: `prototype/osfr-tools/tests/brawler_mongo_chain.rs` lines 1-1200. Read the window in full, plus `tests/support/npc_quest_chain.rs` (helpers `saved`, `assert_packet_changes_nothing`, `interact`, `npc_select`) and `src/encounter/field.rs:392-420` (`battle_spawners`, `battle_prizes_available`). Most assertions are real: state is compared through `saved()`, and the economy and counts are checked against constants. The findings below are the gaps I could confirm.

- **[medium] tests/brawler_mongo_chain.rs:1093 the_battle_and_quest_content_load_with_real_targets - "every battle 12400 prize resolves" passes vacuously if battle 12400 is missing from the engine.**
  - Why it cannot catch a regression: `battle_prizes_available` (`src/encounter/field.rs:411-420`) returns `true` when no battle matches the id (`.is_none_or(...)`). Nothing in lines 1063-1098 asserts that the engine holds battle 12400. The gate spawner check at 1076-1080 finds the GATE guid, not battle 12400. A change that drops 12400 from the engine's battle list (while the JSON keeps it) would still pass this assertion.
  - Fix: before line 1093, assert that the engine has battle 12400, for example by checking that `battle_spawners()` includes the battle's guid, or by asserting the prize closure was called at least once with the expected count of prizes (3 from `battle_row(BATTLE)["prizes"]`).

- **[medium] tests/brawler_mongo_chain.rs:609-620 the_brawling_ring_gate_starts_the_mongo_battle - the comment says an out-of-reach Go "drops the open screen", but nothing checks that.**
  - Why it cannot catch a regression: the body only asserts `zoning.is_none()` and `!changed` (lines 615-620). A change that leaves the 41/114 screen open, or keeps the pending encounter, still passes. The later `open_gate` at line 624 re-opens the gate and hides the stale state. No `saved()` comparison is made around the Go.
  - Fix: take `saved(&game)` before line 615 and assert it is unchanged, or assert that a second `go(&details)` from the reachable position is refused (no zoning). If the screen is meant to close, assert the pending battle-start state is cleared.

- **[medium] tests/brawler_mongo_chain.rs:631-634 the_brawling_ring_gate_starts_the_mongo_battle - the comment says "the wallet is untouched", but no wallet or economy value is compared.**
  - Why it cannot catch a regression: after `leave(second_instance)` only `active_phase(&game).is_none()` is asserted (line 634). A leave path that pays coins or items, or that credits the battle prize, would pass. Lines 601-603 have the same gap for the first run.
  - Fix: take `economy(&game)` before the `send` at line 631 and assert equality afterwards (`assert_eq!(economy(&game), before_leave)`). The same applies to the first leave at line 601.

- **[low] tests/brawler_mongo_chain.rs:1084-1087 the_battle_and_quest_content_load_with_real_targets - the "crossed-swords nameplate is visible" claim is only checked as `gate.5 > 0`.**
  - Why it cannot catch a regression: the tuple's sixth field is `nameplate_image_id` (`src/encounter/field.rs:402`). Any positive image id passes, so a change to the wrong overhead icon still passes.
  - Fix: pin the exact nameplate image id that the crossed-swords icon uses in the content, or assert it against the battle row's `nameplate_image_id` value.

- **[low] tests/brawler_mongo_chain.rs:1174-1186 the_battle_and_quest_content_load_with_real_targets - the comment says "no pre-existing battle or Brawler record was removed or duplicated", but no Brawler record is checked.**
  - Why it cannot catch a regression: the loop only counts battle rows by id (1178-1186). A removed or duplicated Brawler job or quest row would not fail this test, and the test name does not claim it either.
  - Fix: either narrow the comment to battles only, or add a count check for the Brawler record (for example profile id 43 in `profiles.json`) that fails when it is removed or duplicated.

- **[low] tests/brawler_mongo_chain.rs:1187-1194 the_battle_and_quest_content_load_with_real_targets - the content of unrelated battles 96, 12301-12311 is pinned to exact numbers (guids, positions, levels), which the test does not otherwise need.**
  - Why it cannot catch a regression: this is not a missed bug. Any retune of a neighbouring battle's spawn point, prize or level breaks this test even though the slice under test (battle 12400, the gate and the quest chain) is unchanged. This is the over-pinned churn the audit scope calls out.
  - Fix: keep the existence and single-count checks (1178-1186) and drop the tuple pins, or move them into the test that owns each battle.
