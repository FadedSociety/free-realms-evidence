<!-- fleet job=test-audit id=tests-multiplayer-rs-L2401 status=done turns=13 usd=0.0142 tokens(read,write,in,out)=[250974, 34109, 28, 14824] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/multiplayer.rs lines 2401-3109 of 3109

Window `prototype/osfr-tools/tests/multiplayer.rs` 2401-3109 (read in full). Most tests here assert concrete values (exact coin sums, item ids, 35/6 and AddPc wield values, per-character save reloads) and I found no circular expectations, no `#[ignore]`, and no early-return skips. Two findings:

- **[low] prototype/osfr-tools/tests/multiplayer.rs:2727 one_players_disconnect_or_bad_packet_does_not_stop_the_other - the comment at 2728-2729 says A's disconnect "its save is written", but after `disconnect(&first, ...)` (2730) the test only checks `active_session_count()` and never reads A's save.**
  - Why it cannot catch a regression: a disconnect path that drops A's session without writing A's character save (or writes a stale save) still leaves the session count at 1, and every later assertion concerns B. The test would still pass.
  - Fix: after line 2735, add `assert_eq!(saved_coins(&temp, 2), a_coins);` and `assert_eq!(saved_quest_state(&temp, 2), a_quests);`, or drop the "save is written" claim from the comment.

- **[low] prototype/osfr-tools/tests/multiplayer.rs:3103-3108 no_weapon_unknown_definition_and_negative_values_are_zero - the positive control calls `defaults.equipped_wield_type(2)` and expects the magic value `9`; `2` is a guid-style literal, not a named profile constant, and the test does not say which profile it is (3105-3107).**
  - Why it cannot catch a regression: the control is tied to an unexplained fixture value. If profile 2's weapon is renumbered or the fixture changes, the test fails for reasons unrelated to the unknown-definition or negative-clamp behaviour. Conversely, the control does not prove the Brawler's own default weapon (item 4235) still reads, since the Brawler profile is the one forced to 0 at 3103.
  - Fix: use a named profile constant and assert the value the default Brawler weapon should have if its definition is present, or add a comment naming the profile and the item behind the 9.

Not reported: `the_social_loop_uses_no_dev_commands` depends on the helper `assert_no_dev_commands`, which I could not locate by search (the file reports as a binary match), so I could not verify what it inspects. The test's name and body are consistent with each other as far as I could read.
