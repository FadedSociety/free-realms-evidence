<!-- fleet job=test-audit id=tests-derby-route-rs-L1201 status=done turns=6 usd=0.0059 tokens(read,write,in,out)=[63421, 19468, 14, 5726] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/derby_route.rs lines 1201-1651 of 1651

Window `derby_route.rs` 1201-1651 read in full, with `derby_gateway.rs` (`restore_ledger`, `validate_content`, `MAX_*` constants) and the `drive_to_results` helper (lines 520-552) checked. Most assertions in the window are sound: the ledger bound, the `first + 6` resume (newest+1, which matches `restore_ledger`), the `[0]`/`[-1]`/over-length refusals, and the over-bound reward refusal all test real behaviour. Three findings:

- **[medium] prototype/osfr-tools/tests/derby_route.rs:1311 `a_reconnect_keeps_the_ledger...` (the replay-close step inside `staying_to...` / close sequence, lines 1311-1314) - the replayed close asserts only `!replay_close.changed`, with no state or reply comparison.**
  - Why it cannot catch a regression: a replayed `[26, 0, 42, 0]` that returns `changed: false` but still re-sends the restored outfit, re-applies the active job, or re-pays coins would pass, because nothing compares the state or replies after the replay.
  - Fix: capture `let closed_state = game.state();` after the first close and assert `game.state() == closed_state` and `replay_close.replies.is_empty()` (or that no `[35, 0, 7, 0]` / `[50, 0, 1]` packets are present) after the replay.

- **[low] prototype/osfr-tools/tests/derby_route.rs:1400-1404 `a_reconnect_keeps_the_ledger_and_the_next_match_pays_again` - the doc comment is misplaced and overclaims.** The first two doc lines ("Contacts and damage never size the payout... four reports...") describe `collision_reports_never_change_the_payout` (line 1468, which has no doc), and the reconnect test itself uses only one report, so its doc claims a four-report case it never runs.
  - Why it cannot catch a regression: a reader (and reviewers) would believe the reconnect test covers the report-count invariant; it does not, and the collision test carries no doc of its own.
  - Fix: move the first two doc lines onto `collision_reports_never_change_the_payout` at line 1468, and give the reconnect test a doc that only describes the ledger/reconnect behaviour.

- **[low] prototype/osfr-tools/tests/derby_route.rs:1295 `staying`/close block (`close_switch` comparison) - the outfit check slices the packet by hard-coded byte offsets `[12..close_switch.len() - 4]`.**
  - Why it is churn-prone: any change to the trailing field layout of the `[35, 0, 7, 0]` announce (for example, adding a trailing flag) breaks the test even though the test is about the restored outfit, not the packet's trailing bytes; conversely, the 4-byte tail is never checked, so it is pinned yet unverified.
  - Fix: compare the outfit as a sub-slice located by searching for `restored_outfit` inside `close_switch` (e.g. `close_switch.windows(restored_outfit.len()).any(|w| w == &restored_outfit[..])`), which pins the content, not the framing.
