<!-- fleet job=test-audit id=tests-guild-routing-rs-L1 status=done turns=10 usd=0.0134 tokens(read,write,in,out)=[230778, 41756, 22, 11838] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/guild_routing.rs lines 1-873 of 873

Window reviewed: `prototype/osfr-tools/tests/guild_routing.rs` lines 1-873, checked against `prototype/osfr-tools/src/guilds.rs` (`GuildStore::invite` ~331, `expire_invites` ~518, `finish_invite` ~524, `GuildService::handle_decoded` ~1394, sweep at ~1651). No `#[ignore]`, no early-return skips, and no circular expectations were found. Most of the file is sound: the refusal tests compare store bytes before and after, and the sweep and timeout tests (722, 808, 842) match the code's ordering (accept runs before the sweep, and `finish_invite` does not check expiry). Findings:

- **[medium] guild_routing.rs:751 `an_expired_invite_does_not_block_a_new_one` - the test never checks that the second invite was recorded; its only state assertion, `guild_guid_for(202) == None`, is true before and after any invite.**
  - Why it cannot catch a regression: `GuildStore::invite` could return `Ok(..)` without inserting into `pending_invites` (line 398) and the test would still pass, because the `unwrap()`s only check for `Ok`. The expiry-branch logic is only half covered.
  - Fix: after line 755 add `assert!(store.has_pending_invite(202), "the new invite replaces the expired row");`, and optionally check that a third invite at `now=250` returns `InviteAlreadyPending`. Together these fail if the row is not stored.

- **[low] guild_routing.rs:339-342 `two_bots_create_invite_accept_and_chat` - pins the exact message order (`messages.first()` must be the founder's recipient 101) in a test whose subject is the invite, accept and chat flow.**
  - Why it is churn, not a bug catch: reordering the founder's can-create, name-update or roster messages (all sent to 101) fails this test while the flow still works.
  - Fix: drop the `first()` assertion, or assert `created.messages.iter().all(|m| m.recipient_guid == 101)` if the recipient is what matters.

- **[low] guild_routing.rs:505 `non_members_forged_guids_and_bad_names_change_nothing` - the name promises bad-name refusals, but the body only sends a forged-guid set and one valid rename; no bad name is sent.**
  - Why the name overclaims: a regression in name validation would not fail this test. The bad-name coverage is in `oversize_and_invalid_names_are_refused` (line 567), which does check the store.
  - Fix: rename the test to something like `non_members_and_forged_guids_change_nothing`, or add a `create("x".repeat(64))`/`rename(guild, "bad\u{0}name")` step with the same `store_bytes` comparison.
