<!-- fleet job=test-audit id=tests-soccer-entry-rs-L1 status=done turns=8 usd=0.0075 tokens(read,write,in,out)=[138205, 26482, 18, 5683] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soccer_entry.rs lines 1-1005 of 1005

Window reviewed: `prototype/osfr-tools/tests/soccer_entry.rs` lines 1-1005. The fixture panics when the opening content is missing (line 51-55), so nothing is silently skipped. No `#[ignore]` appears. Most tests compare state before and after, so I found no test that cannot fail. Three findings:

- **[medium] prototype/osfr-tools/tests/soccer_entry.rs:704 progress_only_tick_reward_does_not_emit_achievement_progress - the test never checks that the achievement counter moved, so the "no progress packet" assertions can pass when the counter never moves.**
  - Why it cannot catch a regression: the doc says "the tick settle observes the moved counter", but the body only asserts that no `150/7` packet appears (lines 709-720) and that rank XP lands in 1800..1900 (lines 731-734). That XP check is the rank counter, not the achievement counter. If the payout stopped touching the achievement counter, or the observation were skipped entirely, both negative checks would still pass. Also, `sync_achievement_progress` in `src/gameplay/progression.rs:97-106` only extends packets when a rule completes, so the negative check is nearly vacuous.
  - Fix: after the settle, read the achievement counter for this rule from the gameplay state (or the snapshot's achievement state) and assert it is 18 (from 17). Also assert it is still below the level-20 threshold. Then the progress-only claim is exercised rather than assumed.

- **[low] prototype/osfr-tools/tests/soccer_entry.rs:982 a_reconnect_mid_match_drops_the_match_and_restores_the_pre_match_pose - the doc says the reset drops "no result, no reward", but no result is ever produced and no win is settled before the reset.**
  - Why it cannot catch a regression: the match is never shot to a settled win (lines 986-988), so the `coins` equality at lines 989-1003 only shows that a reset with no pending result pays nothing. A reset that flushes a settled-but-unpaid win would not be exercised. The "no result" half of the name is never checked: there is no assertion that no `39/18` result packet is sent during or after the reset.
  - Fix: call `settle_win` before `reset_session` only if the scenario is meant to test an unpaid result; otherwise shoot part-way, then reset and assert that no `39/18` packet arrives on the next tick and that coins are unchanged.

- **[low] prototype/osfr-tools/tests/soccer_entry.rs:326 forged_entries / quitting tests - `after.replies.is_empty()` pins the entire reply list of a later tick, so any unrelated packet breaks the test.**
  - Why it cannot catch a regression: it is not a regression gap. It is churn. The test is about "a second tick cannot pay again", but it fails on any heartbeat, state refresh, or unrelated packet. The same pattern appears at line 782-785 (`after.is_empty()`).
  - Fix: assert that no `39/18` win packet and no coin change appears in `after.replies`, and drop the blanket emptiness check.
