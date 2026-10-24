<!-- fleet job=test-audit id=tests-shared-field-kill-quest-credit-rs-L1 status=done turns=8 usd=0.0108 tokens(read,write,in,out)=[158517, 38953, 18, 8677] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs lines 1-1200 of 1383

Window reviewed: `prototype/osfr-tools/tests/shared_field_kill_quest_credit.rs` lines 1-1200. No `#[ignore]` and no early `return` in the window, so no silent skips. The kill-credit assertions I checked against `src/encounter/field_rewards.rs` (`credit_field_kill` 227-281, `claim_kill_credits` 288-321, `pay_field_reward` 328) are real: a dropped-newest or uncapped list would fail the 16/oldest-drop checks, and the claimant-only event and expiry paths are exercised. The findings below are name and scope overclaims.

- **[medium] `tests/shared_field_kill_quest_credit.rs:579` `a_failing_quest_event_for_one_player_does_not_stop_the_other` - the name promises a failing quest event that is isolated per player, but the body (and its own comment at 580-586) says the kill-time quest event cannot fail; the only failures driven are A's stale catalogue bind (602-607) and an invalid position (624-630).**
  - Why it cannot catch a regression: a change that made a real quest-event failure in one session abort the whole shared request, or leak into the other session, would not be exercised here, since no kill-time event failure is ever produced. The test still passes as long as A's bind is refused and B's kill credits.
  - Fix: rename to reflect what it drives (e.g. `a_stale_bound_session_is_refused_while_the_other_still_credits`), or add a real per-player failure at the event layer and assert A's state is untouched and B's counter is 1.

- **[medium] `tests/shared_field_kill_quest_credit.rs:649` `the_existing_field_and_arena_suites_stay_green` - the name claims the existing field and arena suites stay green, which a single test cannot prove; the body only checks one 35/8 swing value and one 32/7 attack result for a single kill.**
  - Why it cannot catch a regression: the claimed coverage lives in other test targets; this test passes even if `shared_field_state.rs`, `shared_field_interest.rs` or `field_kill_rewards.rs` break, and it would also pass on any change to the reward or HP behaviour that leaves those two packets intact.
  - Fix: rename to what it checks (e.g. `a_shared_kill_emits_the_swing_and_attack_result_packets`), and drop the claim about other suites from the name and doc comment.

- **[low] `tests/shared_field_kill_quest_credit.rs:669` `the_existing_field_and_arena_suites_stay_green` - exact constants `1099` (swing animation value) and the unexplained byte slices `hit[46..50] == 0` pin incidental packet details unrelated to quest credit.**
  - Why it cannot catch a regression: it is churn, not a missed bug; a re-timed basic swing or a reordered padding field breaks it without touching quest credit.
  - Fix: assert only the fields this test is about (actor guid, target guid, and that a swing and an attack result exist), or reference the named constant from the swing definition.

- **[low] `tests/shared_field_kill_quest_credit.rs:450` `a_solo_arena_kill_still_credits_and_is_unchanged` - the name says the solo path is "unchanged", but nothing compares against a baseline of the non-shared path beyond the credit and removal counts.**
  - Why it cannot catch a regression: a change to the solo path's reply ordering, reward bytes, or save fields would still pass, because only counts and one update packet are checked.
  - Fix: drop "is_unchanged" from the name, or compare the solo kill's full reply set and serialized state against a pinned snapshot taken before the change.

- **[low] `tests/shared_field_kill_quest_credit.rs:407` `a_second_tick_or_close_does_not_double_credit` - the name says "close", but no field close or session close is exercised; the test covers a replayed lethal ability (`Ability`) and a `Select` on the corpse, then extra ticks.**
  - Why it cannot catch a regression: a regression where closing the field or session re-fires the kill credit would not be caught, because the close path is never driven.
  - Fix: either remove "close" from the name, or add a call that closes the field/session (the production close seam) and assert `counts` and `saved` are unchanged afterwards.

- **[low] `tests/shared_field_kill_quest_credit.rs:1071` `a_group_member_who_never_hit_or_engaged_gets_no_credit` - the name says "group member", but no party or group is created; D is only co-present in the same field.**
  - Why it cannot catch a regression: if group or party membership were ever added as a credit source, D would be credited only if it also hit or was engaged, so this test would still pass on a group-only credit change.
  - Fix: either rename to `a_co_present_non_contributor_gets_no_credit`, or set up a real group membership for D and assert D still receives no credit.
