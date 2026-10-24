<!-- fleet job=test-audit id=tests-mount-follow-rs-L1 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[17025, 11179, 10, 3592] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mount_follow.rs lines 1-125 of 125

Window: `tests/mount_follow.rs` lines 1-125. Read against `src/players.rs:332-341` (`set_mount`), `src/players.rs:621` (AddPc reads `self.mounts`), and `src/mounts.rs:628-643` (`MountTail`, `NONE`).

- **[medium] tests/mount_follow.rs:124 setting_a_mount_sends_nothing_and_clearing_it_restores_the_sentinel - the "An unknown session is ignored" tail is a bare call with no assertion, so the guard is never checked.**
  - Why it cannot catch a regression: `set_mount` (players.rs:333-334) returns early for an unknown session. If that guard were deleted, `set_mount(SessionId(999), seated())` would insert a stale entry into `self.mounts`. Nothing here reads that entry, and the test still passes. The stale entry would only surface if session 999 later joined, because AddPc (players.rs:621) looks up `self.mounts` by GUID. No test does that join.
  - Fix: after line 124, join `SessionId(999)` (with a fresh GUID and zone) and assert its AddPc tail equals `MountTail::NONE` (or assert `tail_of(add_pc_of(...))` for a viewer is the sentinel). Alternatively, assert that the registry state is unchanged by checking that a later viewer's AddPc for 999 is still the plain frame.

- **[low] tests/mount_follow.rs:91-92 setting_a_mount_sends_nothing_and_clearing_it_restores_the_sentinel - the name says "sends nothing", but no assertion checks outbound messages from `set_mount`.**
  - Why it cannot catch a regression: `set_mount` is called at lines 96 and 111 with its return value discarded, and nothing inspects the messages. `set_mount` returns `()`, so the "sends nothing" claim is only true by signature. A change that returned messages would not be caught by this test, and the name overclaims what the body covers. The "clearing restores the sentinel" part is covered (lines 111-121).
  - Fix: either rename the test to drop "sends nothing", or make the claim checked by having `update_pose` at line 96 captured as a baseline, and asserting that no message is addressed to the rider between the `set_mount` calls (for example, compare the outbound list from an identical run without `set_mount`).

- **[low] tests/mount_follow.rs:85-88 a_viewer_who_arrives_later_gets_the_riders_mount_block - the byte-length and split comparison pins the frame layout to exact offsets.**
  - Why it cannot catch a regression: the check hard-codes the 40-byte tail and 20-byte split, the same as `tail_of` (line 41). This is about the mount block's position, so it is intentional. But any unrelated AddPc field added before the tail (for example a field in the head) would fail this assertion even though the mount block is still correct. This is churn, not a missed bug.
  - Fix: keep the `tail_of` assertion at line 77 as the real check, and drop or relax lines 85-88 to compare only that the frame length is unchanged when the mount is set (or that head bytes match the plain frame), so the test fails only on mount-block changes.
