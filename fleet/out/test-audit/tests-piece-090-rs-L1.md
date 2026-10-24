<!-- fleet job=test-audit id=tests-piece-090-rs-L1 status=done turns=7 usd=0.0109 tokens(read,write,in,out)=[109853, 35931, 16, 10663] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_090.rs lines 1-547 of 547

Window reviewed: `prototype/osfr-tools/tests/piece_090.rs` lines 1-547, checked against `prototype/osfr-tools/src/restoration/piece_090.rs` (parser at 356-425, member_status at 512-534, store at 602-974). No `#[ignore]` and no early-return skips. The lifecycle test's expected values match the store logic, and I found no test that compares a value with the function's own output. The findings below are gaps in what the tests actually check.

- **[medium] tests/piece_090.rs:72 sub_opcode_table_matches_the_original_enum - the name says the whole table matches the original enum, but only 6 of the 28 `SUB_OPCODES` names are checked (lines 75-79), plus 3 `None` cases.**
  - Why it cannot catch a regression: renaming or swapping any of the other 22 entries (e.g. 17 to "GuildMemberStatusUpdate", or 25 and 31 swapped) still passes, because nothing iterates `SUB_OPCODES` against an expected list.
  - Fix: assert the full 28-entry list in order (`assert_eq!(expected_table, SUB_OPCODES)` with the enum literal copied in), or iterate and compare every id/name pair.

- **[medium] tests/piece_090.rs:439 capacity_removal_and_leader_succession_are_enforced (asserts at 468) - the succession rule is "lowest role id, then lowest character id", but both remaining candidates are Recruit, so the role ordering is never exercised.**
  - Why it cannot catch a regression: an implementation that ignores role and picks the lowest guid (or the first BTreeMap entry) still makes `second` (guid 2) Leader and passes. Dropping the `row.role.id()` key from `min_by_key` at `piece_090.rs:918` would not be caught.
  - Fix: before `store.quit(leader)`, promote `third` to Officer (`store.promote(leader, third)` twice through Member). Then assert `role_of(third) == Some(GuildRole::Leader)` and `role_of(second)` is still Recruit. That fails if role ordering is dropped, since guid 2 would win.

- **[low] tests/piece_090.rs:434 guild_lifecycle_creates_invites_and_changes_roles - the comment at 409 says "no self targets", but the only self-target case checked is `promote(leader, leader)` (line 418). The demote self-target is asserted as `CantPromoteAbove` for an officer (line 434), so the `SelfTarget` branch in `demote` (`piece_090.rs:860`) is never reached by any test.**
  - Why it cannot catch a regression: removing or reordering the `actor == target` check in `demote`, or changing it to a different error, still passes for the officer case. For a leader self-demote, `demote` would return `SelfTarget`, but no test covers that.
  - Fix: add `assert_eq!(Err(GuildError::SelfTarget), store.demote(leader, leader))`, and either fix the comment or assert the officer case by name.

- **[low] tests/piece_090.rs:543 rename_is_leader_only_and_state_survives_a_round_trip (lines 543-546) - the name is about rename authority and persistence, but the tail asserts four `MEMBER_UPDATE_*` wire constants against literals.**
  - Why it cannot catch a regression: these assertions say nothing about rename, the round trip, or the name limit. They only pin constant values, so the name overstates what the test covers and the constants are checked in an unrelated test. A change to `MEMBER_UPDATE_*` would fail a test named for rename, and rename regressions would not point at these lines.
  - Fix: move the constant checks into a test named for member status updates, and cover the remaining constants there too (`ONLINE`=6, `NONE`=7). Keep this test on rename and persistence.

- **[low] tests/piece_090.rs:300-304 replies_encode_the_recovered_field_order - the member-status expectation is built with `expected.insert(49, 1)`, a hand-computed byte offset, in the middle of a push-based build.**
  - Why it is churn: any new field or a changed string length in the name block (e.g. the `last_name` push at line 299) shifts the offset and fails this test even when the Online byte is still in the right place. The offset also hides the field order in the middle of the build, so the failure message points at byte 49 and not at the field that moved.
  - Fix: build the expected bytes in the same field order as the struct (role, then Online byte, then the five i32s) with the online byte pushed right after the role, and drop the magic index. Keep the order check, but express it as named pushes.
