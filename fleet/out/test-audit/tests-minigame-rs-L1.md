<!-- fleet job=test-audit id=tests-minigame-rs-L1 status=done turns=4 usd=0.0049 tokens(read,write,in,out)=[30627, 18842, 10, 4400] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/minigame.rs lines 1-573 of 573

Window: `prototype/osfr-tools/tests/minigame.rs` lines 1-573. Code under test read: `prototype/osfr-tools/src/minigame.rs` 440-560 (`disconnect`, `score`, `choose_wheel_prize`, `finish`/`finish_win_without_reward`/`finish_inner`).

- **[medium] tests/minigame.rs:403 leave_and_disconnect_cancel_without_reward_or_activity_mutation - the reward and activity non-mutation assertions can never fail because neither cancel path receives reward or activity state.**
  - Lines 418-419 and 430-431 check `reward_state.inventory` (coins 10, item count 3) after `handle_client(&request(6,125))` and `disconnect()`. `handle_client(&[u8])` and `disconnect(&mut self)` (minigame.rs:295, 443) take no `RewardState` or activity argument, so the fixture value is never touched by the code under test. The `reward_state` object is a local that the runs API cannot reach.
  - Why it cannot catch a regression: a change that makes leave or disconnect pay a grant, or mutate an activity, would still pass, since the test checks a fixture no code path can modify. Nothing asserts on the activity at all, despite the name.
  - Fix: pass the state into the cancel path (or assert on whatever the outcome exposes, e.g. `left.reward_state.is_none()` already exists), and add an assertion that the run's score and state are unchanged by the cancel (e.g. call `runs.score(...)` or a `runs.state` check after cancel, and confirm no `reward_packets`/`reward_state` appear for a `Playing` run with a non-zero score).

- **[low] tests/minigame.rs:485 prize_wheel_landing_is_server_selected_and_stop_report_cannot_pay - the "server-selected" part is not exercised; the test passes the entry in and checks it is echoed.**
  - Lines 493-508 pass a hand-written `RewardBundleRow { type_id: 3, body }` and expect the same bytes back. `choose_wheel_prize` (minigame.rs:484-511) performs no selection; it only frames and stores whatever the caller passes.
  - Why it cannot catch a regression: if the server-side selection were moved or bypassed (e.g. the wheel accepted a client-supplied index), this test would still pass as long as the packet encodes the entry it was given.
  - Fix: rename to reflect what is checked (e.g. `wheel_prize_packet_echoes_entry_and_stop_report_cannot_pay`), or add a test that exercises the real selection source and asserts the landing comes from it.

- **[low] tests/minigame.rs:560 persisted_counter_never_reuses_ids_and_wrong_instance_is_rejected - the restarted offer is checked only for non-emptiness.**
  - `assert!(!second.replies.is_empty())` (line 560) would pass for any offer packet, including one carrying the wrong instance id or a stale spec. The `current_instance_id()` checks at 558-559 cover the id, but the packet is not compared to `expected_info(129, &spec())`.
  - Why it cannot catch a regression: a restore that emits a reply for a different instance or an outdated spec still passes.
  - Fix: `assert_eq!(second.replies, vec![expected_info(129, &spec())]);`.
