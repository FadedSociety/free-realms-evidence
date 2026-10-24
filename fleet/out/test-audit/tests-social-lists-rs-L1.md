<!-- fleet job=test-audit id=tests-social-lists-rs-L1 status=done turns=6 usd=0.0079 tokens(read,write,in,out)=[75916, 26282, 14, 7737] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/social_lists.rs lines 1-621 of 621

Window reviewed: `prototype/osfr-tools/tests/social_lists.rs` lines 1-621. Code under test read: `src/social_lists.rs` (SocialLists::load/save 145-181, FriendResultCode 202-234, encode_friend_status 1255, encode_group_result 1616, invite_to_group 719-815, respond_group_invite 818-870).

- **[high] tests/social_lists.rs:598 friend_validation_and_group_result_tables_reject_invalid_requests_cleanly - the name promises rejection handling, but the only rejections exercised are SelfFriend and SocialService::new(1); the group loop (610-620) just round-trips `encode_group_result` and never touches the reject paths.**
  - Why it cannot catch a regression: the loop checks `bytes[2..4] == sub_op` and `bytes[4..8] == code`, where `encode_group_result` writes exactly those fields from the same inputs. Any change to refusal logic (e.g. `invite_to_group` returning the wrong result code for a full group, an offline target, or a not-grouped accept at 719-870) still passes, and the test never checks that state is left unmutated.
  - Fix: after the existing self-friend check, assert on the server's behaviour: e.g. `invite_to_group` for an offline or ignored target returns 40/2 with the expected result code and `group_of`/`group_invitee` stay `None`; `respond_group_invite` with no pending invite returns 40/5 code 3 and leaves `group_invitee` unchanged. Keep the table only as a secondary wire check, or rename it.

- **[medium] tests/social_lists.rs:400 group_reader_builders_match_recovered_headers_and_member_order - the name says "member order", but the body encodes one row (`encode_group_update(&[row])`) and never checks ordering of multiple members.**
  - Why it cannot catch a regression: reversing or re-sorting the member list inside `encode_group_update` (or `encode_group_snapshot`) leaves this single-row test green.
  - Fix: build two or more `GroupMemberRecord`s in a known order, assert the count at `group_update[8..12]` and that the first member guid at the expected offset is the first input (e.g. `group_update[12..20] == 202u64.to_le_bytes()` for the first row), or rename the test to drop "member order".

- **[medium] tests/social_lists.rs:339-343 client_autorefuse_group_answer_declines_and_disconnect_cleans_state (and the same pattern at 557-561 in refused_group_invites / grouped_acceptance test) - the only check of the decline reply is `declined.iter().all(|p| family==40 && sub==4)`, which passes vacuously when the reply is empty.**
  - Why it cannot catch a regression: if `respond_group_invite(.., accepted=false, ..)` stops sending the 40/4 notice (returns `Vec::new()`, as at 828-870 would if the decline branch changed), the `all` succeeds and `group_invitee(202).is_none()` is still true, so the test passes.
  - Fix: assert the reply is non-empty and has the expected shape, e.g. `assert_eq!(declined.len(), 1); assert_eq!((family(&declined[0]), sub(&declined[0])), (40, 4));` in both places (339 and 557).

- **[medium] tests/social_lists.rs:192 ignore_add_remove_and_target_ignore_blocks_group_invite - the name claims "remove" is covered, but `remove_ignore` (210-213) is checked only by its returned 112/3 packet; nothing verifies the ignore was actually cleared, and `chat_ignore_lists()` at 199 is bound to `_` with no assertion.**
  - Why it cannot catch a regression: a `remove_ignore` that returns the 112/3 packet without deleting the entry from the profile's `ignored` map still passes. The invite-blocking check at 201-208 runs before removal, so it never tests the post-removal state.
  - Fix: after `remove_ignore`, call `social.invite_to_group(202, &name_a, ...)` again and assert it now yields 40/2 with result 0 (not 2) and a `group_invitee(101)`; also assert on the `chat_ignore_lists()` contents instead of `let _:`.

- **[low] tests/social_lists.rs:166-171 friend_decline_timeout_duplicate_and_login_logout_presence - the decline check `declined.iter().any(|p| p.bytes.get(3) == Some(&5))` matches any packet of any family whose byte 3 is 5, not the 74/8 RequestSent for player 101.**
  - Why it cannot catch a regression: an unrelated packet with byte 3 == 5 (or a changed family/sub on the requester's packet) would satisfy it, so the check does not prove the decline cleared the pending request.
  - Fix: filter on recipient and header as the earlier checks do: `declined.iter().any(|p| p.recipient_guid == 101 && family(p) == 74 && sub(p) == 8 && p.bytes[3] == 5)`.
