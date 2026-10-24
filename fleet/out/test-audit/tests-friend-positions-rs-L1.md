<!-- fleet job=test-audit id=tests-friend-positions-rs-L1 status=done turns=5 usd=0.0067 tokens(read,write,in,out)=[49421, 21602, 12, 6934] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/friend_positions.rs lines 1-635 of 635

Window reviewed: `prototype/osfr-tools/tests/friend_positions.rs` lines 1-635. Most tests check concrete byte layouts and exact recipient sets, and the canaries are real. One assertion pair is vacuous.

- **[medium] prototype/osfr-tools/tests/friend_positions.rs:379 online_friend_rows_open_the_atlas_gate_and_offline_rows_do_not - the offline half (line 394) passes when B's friend row is missing entirely, so it does not prove the row's flag is 0.**
  - Why it cannot catch a regression: `encode_friend_list` (`src/social_lists.rs:1299-1309`) always writes the 74/1 header and an `i32` count. With zero friends the message is `[74,0,1, 0,0,0,0]`, whose last byte is 0. So if B's row were dropped from the list after B logs out, or the row's flag were wrongly written as 0 with the row missing, `*list(...).last().unwrap() == 0` still holds. The name's claim that "offline rows do not open the gate" is therefore not exercised by this line. The online half (line 391) is sound, because an empty list would give 0 and fail it.
  - Fix: assert the full 74/1 body for both states. For example, decode the count and require `count == 1`, then check that the row's final byte equals 1 when B is online and 0 when B is offline. Alternatively compare against `encode_friend_list` output built from the expected state. Either change makes a dropped row fail the test.

- **[low] prototype/osfr-tools/tests/friend_positions.rs:331 offline_one_sided_ignored_unknown_and_unplaced_identities_are_absent - the comment says B's location is "not shared" after B removes A, but no assertion checks B's own view or the one-sided case directly.**
  - Why it cannot catch a regression: the only check is the global `after.is_none()` at line 338. It is still sensitive to a one-sided leak (B would then appear and make the result `Some`), but it is not tied to B. A fix that hides the entry for another reason would pass the same check while the comment's claim goes untested.
  - Fix: after `remove_friend(B, A)`, assert `positions(&social, B, &spots)` is empty, and assert that A's reply contains no entry for B. Keep the global `is_none()` check as well.
