<!-- fleet job=test-verify id=tests-social-lists-rs-L1-f1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[9059, 8621, 8, 3239] model=claude-haiku-5-5 -->
# high: tests/social_lists.rs:598

**Verdict:** `confirmed`

**Evidence:**

- The whole test is `tests/social_lists.rs:598-621`. It makes exactly three kinds of assertion:
  1. `request_friend(101, &self_name, &directory) == Err(SocialError::SelfFriend)` (601-604).
  2. `SocialService::new(1)` matches `Err(SocialError::InvalidGroupLimit)` (605-608).
  3. For `(2, 0..=7)`, `(5, 1..=3)`, `(7, 1..=3)`: `encode_group_result(sub, code)` has `bytes[2..4] == sub` and `bytes[4..8] == code` (610-620).
- Assertions 1 and 2 are real. A change that stops `request_friend` returning `SelfFriend`, or that accepts a group limit of 1, would fail them (`social_lists.rs:489` and `:351` are the refusal sites).
- Assertion 3 is a round-trip. `encode_group_result` (`src/social_lists.rs:1616-1620`) writes `group_header(sub)` and then `code.to_le_bytes()`, which is exactly what the loop reads back. It cannot fail on any refusal logic. It only checks the encoder's header layout.
- The test never calls `invite_to_group` (`:719`), `respond_group_invite` (`:818`), or any accept/decline path. It never reads `group_of`, `group_invitee`, or `group_members`, so it never checks that state is left unmutated.
- Walk-through of the claimed regression: change `invite_to_group` so a full group returns the wrong code, or an offline target gets the wrong refusal, or a not-grouped accept returns Ok. This test makes none of those calls, so every assertion still passes.

The claim is accurate. Its "only rejections exercised" statement holds. Its "cannot catch" statement holds for the refusal logic it names. The first reader is right that the name promises more than the body checks. This does not show the suite has no coverage of group refusals; other tests in the repo, such as `social_lists.rs:479-562` and `tests/group_invite_expiry.rs`, do assert on `group_invitee`. That is a suite-level point and does not refute this claim about this test.

**Minimal fix:** After the self-friend check, add a call that must fail, plus a state check. For example, `invite_to_group` to an offline or ignored target should return `40/2` with the expected code and leave `group_of`/`group_invitee` as `None`. Also, `respond_group_invite` with no pending invite should return `40/5` code 3 and leave `group_invitee` unchanged. Alternatively, rename the test to drop "group_result_tables_reject_invalid_requests_cleanly".
