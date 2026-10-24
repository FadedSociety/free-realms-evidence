<!-- fleet job=test-audit id=tests-piece-061-rs-L1 status=done turns=4 usd=0.0057 tokens(read,write,in,out)=[24311, 17970, 10, 6409] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_061.rs lines 1-338 of 338

Window reviewed: `prototype/osfr-tools/tests/piece_061.rs` lines 1-338, checked against `prototype/osfr-tools/src/restoration/piece_061.rs` (`record_clear`, `report_position`, `request_gate`, `DungeonChain::new`). The position, gate-order, duplicate/out-of-order and wave-spec assertions all match what the code does, and I found no ignored tests and no early-return skips.

- **[medium] prototype/osfr-tools/tests/piece_061.rs:320 extra_clears_after_a_completed_room_are_rejected_and_change_nothing - the name promises "change nothing", but the body only compares `cleared_actors(First)` and `active_room()`; no gate state is compared.**
  Why it cannot catch a regression: a change that writes gate state on the rejected path (for example, setting `gates` to Open for the room after the rejected clear, or any other gate mutation before the `OutOfOrderClear` return at src line 397-398) would still pass, because `gate_state` is never read after the rejected clear. The First-room clear has already opened Door01, so the test should also be able to see Door02 and Door01 staying exactly as they were.
  Fix: snapshot `chain` (it derives `Clone, PartialEq`) before the rejected call and assert `chain == before` after it, or assert `gate_state(GateId::Door01) == GateState::Open` and `gate_state(GateId::Door02) == GateState::Closed` after the rejection.

- **[medium] prototype/osfr-tools/tests/piece_061.rs:94 tutorial_rooms_are_ordered_by_both_name_and_axis - the "by name" half of the claim is never checked.**
  Why it cannot catch a regression: `assert_eq!(order, [First, Second, Final])` compares `RoomId::tutorial_order()` with the same literal that the function returns (src line 103-104). Nothing reads `area_name` (`AMB_FIRST_ROOM`, `AMB_TUT_SECOND_ROOM`, `AMB_TUT_FINAL_ROOM`) or ties the order to those names, although the comment at line 98 says "the recovered names carry the room order". Reordering the `RoomId` literal and the name constants together would pass the name part, and the axis asserts at lines 100-107 do not cover it either.
  Fix: assert the order from the data, e.g. that `tutorial_order().map(|r| r.bounds().area_name)` starts with the expected prefixes (`AMB_FIRST`, `AMB_TUT_SECOND`, `AMB_TUT_FINAL`), or drop "by both name" from the test name and comment.

- **[low] prototype/osfr-tools/tests/piece_061.rs:68 recovered_room_boxes_come_from_the_original_area_table - the name says the values come from the original area table, but the test never reads that table or checks its hash.**
  Why it cannot catch a regression: the assertions compare the `AreaBox` constants in src lines 62-91 with literals typed into the test. A wrong value copied into both places passes, and the test has no link to `sg_npx_cavern_01Areas.xml` (8600 bytes, sha256 `aae003c3...`) that the module docs cite.
  Fix: either rename it to something like `recovered_room_boxes_are_pinned_to_the_documented_values`, or add a check against the extracted XML (or its recorded sha256 in the notes) so the test is tied to the original file.

- **[low] prototype/osfr-tools/tests/piece_061.rs:135 recovered_gate_clips_and_verb_sounds_are_listed - the test is a literal-to-literal pin of `DOOR_01_CLIPS`, `ROCK_BARRIER_CLIPS` and `DOOR_VERB_SOUNDS`, not a check against the manifest rows.**
  Why it cannot catch a regression: a clip name that is wrong in the source and in the test passes. The name's "recovered" claim rests only on the module comment. This is only a pin, so it is low severity.
  Fix: check the names against the asset manifest rows (or the notes table that lists them) in a fixture, or rename the test to say it pins the listed names.</result>
