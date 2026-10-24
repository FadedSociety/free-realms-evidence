<!-- fleet job=test-audit id=tests-piece-087-rs-L1 status=done turns=6 usd=0.0064 tokens(read,write,in,out)=[73879, 22128, 14, 5710] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_087.rs lines 1-703 of 703

Window reviewed: `prototype/osfr-tools/tests/piece_087.rs` lines 1-703 (read in full), checked against `src/restoration/piece_087.rs` (`friend_list` 934-943, `add_request` 956-997, `confirm` 999-1012, `positions_for` 1195-1217). The family/sub-opcode, byte-layout, and wire-rejection tests are sound. The problems are in the roster, position, and recipient tests.

- **[medium] prototype/osfr-tools/tests/piece_087.rs:607 position_requests_return_only_local_friends_and_reject_bad_input - the name promises a local-only filter that the body never exercises.**
  Why it cannot catch a regression: `positions_for` (src 1195-1217) filters only on friendship and `account.online`; it never reads `is_local`. A change that returns online friends in other zones would still pass, because the only non-friend in the test (STRANGER, 611) is excluded by friendship, not by locality. No friend is set up with a non-local state.
  Fix: give REED (or a third friend) a non-local state, e.g. a roster entry with `is_local = false` or a zone flag, and assert that `positions_for(NOVA)` omits it. Alternatively rename the test to drop "local" if locality is not meant to filter here.

- **[medium] prototype/osfr-tools/tests/piece_087.rs:645 position_requests_return_only_local_friends_and_reject_bad_input - the comment says an encounter friend is "reported without coordinates", but the test only checks `in_encounter`.**
  Why it cannot catch a regression: `positions_for` (src 1207-1213) still copies `x`/`z` into the `PositionEntry` when `in_encounter` is true. The "no coordinates" behaviour is only applied at wire encoding (src 618-619, 729-731). A change that breaks that encoder-side omission would not be caught here, and the test also asserts nothing about the coordinates it claims to check.
  Fix: assert the encoded body (`encode_notification(&Notification::UpdatePositions { entries })`) omits the coordinate bytes for that entry, or assert the entry's coordinates are the neutral values the encoder expects. Otherwise reword the comment to match what is checked.

- **[medium] prototype/osfr-tools/tests/piece_087.rs:529 only_the_addressed_recipient_may_answer_a_request - the name claims the addressed recipient can answer, but no positive case is run.**
  Why it cannot catch a regression: the test only shows that STRANGER (538) and NOVA (543) are refused. It never shows REED succeeding, and it never checks that the pending request (NOVA, REED) survives the refused attempts. A change where a refused `confirm` removes the pending entry would still pass, because the later NOVA-answers-REED call (543) fails for an unrelated reason.
  Fix: after the two refusals, assert `registry.confirm(REED, NOVA, Accepted)` succeeds and `is_friend(NOVA, REED)` holds. Alternatively assert `add_request(NOVA, REED)` still returns `AlreadyPending` between the refusals, which would catch consumption of the pending entry.

- **[medium] prototype/osfr-tools/tests/piece_087.rs:693 deliveries_recover_the_decoded_notification - the roster round trip and the List notification checks never require a non-empty roster.**
  Why it cannot catch a regression: `friend_list(NOVA)` (src 934-943) returns whatever the roster holds. The test asserts only that the encoded list round-trips and that the List notification equals `encoded`. If `friend_list` returned an empty Vec (for example, if `confirm` stopped recording the friendship), `encoded` would be the 4-byte zero count and every assertion would still pass.
  Fix: add `assert_eq!(list.len(), 1)` and `assert_eq!(list[0].guid, REED)` after line 693, so an empty roster fails the test.

Not reported (noted for completeness): the 143-146 provenance loop only checks that the string contains "pseudocode.c", which is weak but not a cannot-fail case. Lines 208-227 pin exact byte offsets, but that is the purpose of the layout test, so I did not flag it as churn.
