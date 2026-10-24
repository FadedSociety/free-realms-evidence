<!-- fleet job=test-audit id=tests-bandit-hideout-dungeon-rs-L1201 status=done turns=9 usd=0.0095 tokens(read,write,in,out)=[157840, 35693, 20, 6884] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bandit_hideout_dungeon.rs lines 1201-2382 of 2382

Window `bandit_hideout_dungeon.rs` 1201-2382 reviewed. No `#[ignore]`, no early-return fixture skips, and no bare `is_ok()` in the window. Findings:

- **[medium] prototype/osfr-tools/tests/bandit_hideout_dungeon.rs:2007 a_live_change_before_the_close_survives_the_payout - "exactly one prize is added" only counts the number of prize ids whose count rose, so it never checks the amount or that the id is a row prize.**
  - Why it cannot catch a regression: if the payout grants two of the same prize (count +2), or grants a non-row item that is counted in `economy().prizes`, `gains.len()` is still 1 and the assertion passes. The sibling helper `assert_payout` (line 888-890) checks `prize_ids.contains(&gains[0].0)` and `gains[0].1 == 1`; this test does neither.
  - Fix: after line 2006, assert `gains.len() == 1`, `prizes.contains(&gains[0].0)` and `gains[0].1 == 1`, or call `assert_payout` with the live-change baseline adjusted for the 7 coins and the 2 filler items.

- **[medium] prototype/osfr-tools/tests/bandit_hideout_dungeon.rs:2297 the_shipped_rows_are_unchanged_and_the_new_row_is_appended - the name says every earlier row is "unchanged", but the body pins only title, difficulty, required level and reward coins.**
  - Why it cannot catch a regression: changing a shipped row's enemies, prizes, spawner, zone, or GUIDs (or deleting one of its prizes) still passes. The inline comment at 2317-2319 explains the relaxed scope, but the doc comment at 2295-2296 does not.
  - Fix: either narrow the doc to "title, difficulty, level and payout keep their values and order", or add a canary that hashes each shipped row's `prizes` and `enemies` (or compares them to a pinned copy) so any edit to an earlier row fails.

- **[medium] prototype/osfr-tools/tests/bandit_hideout_dungeon.rs:1196-1197 the_start_screen_carries_the_instance_and_roster_count - the doc says the screen carries title, icon, description and difficulty, but the body (1199-1235) only checks the instance (i32_at 8), the roster count, and the four prizes.**
  - Why it cannot catch a regression: a start screen with a wrong title, icon, description or difficulty id would pass. The comment at 1233-1234 also says the level floor is reported in chat, but no assertion here checks it.
  - Fix: assert the title, icon, description and difficulty fields at their offsets in `screen` (the same offsets used by `open_battle` / the fixture decoder), and drop the vacuous `assert!(screen.len() > DETAILS_ROSTER)` at 1235 in favour of a field check.

- **[low] prototype/osfr-tools/tests/bandit_hideout_dungeon.rs:2189 the_marker_is_on_the_ground_and_clear - `assert_eq!(disc.len(), 105)` pins the sample count of the test's own `disc_points` helper (1002-1017), not a property of the game.**
  - Why it cannot catch a regression: it only changes when the helper's sampling changes, which is unrelated to the marker's ground or clearance. This is churn, not a missed bug.
  - Fix: drop the count, or assert that every disc sample is within 5 m of the marker, which is the property that matters.

- **[low] prototype/osfr-tools/tests/bandit_hideout_dungeon.rs:1919-1930 a_second_session_sees_the_marker_not_the_arena - the final `assert_eq!(marker_packet(&second_entry.replies, ...), first_packet)` re-reads the stale world-entry replies that were already compared at 1884-1887, so it adds nothing after the second session's arena refresh.**
  - Why it cannot catch a regression: the arena refresh for the second session is not in `second_entry`; a change that altered the second session's marker after its arena refresh would not be seen.
  - Fix: take the marker packet from `again` (the second session's post-arena refresh) and compare it with `first_packet`, or delete the redundant assertion.
