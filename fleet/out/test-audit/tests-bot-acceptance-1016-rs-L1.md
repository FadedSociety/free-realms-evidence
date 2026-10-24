<!-- fleet job=test-audit id=tests-bot-acceptance-1016-rs-L1 status=done turns=9 usd=0.0115 tokens(read,write,in,out)=[181840, 36318, 20, 10187] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bot_acceptance_1016.rs lines 1-1200 of 1780

Window reviewed: `bot_acceptance_1016.rs` lines 1-1200. Helper code in `osfr-bot.rs` (`wait_for` consumes the inbox up to the match, so stale messages cannot satisfy later waits) and the gateway's deferred pose save (`osfr-gateway.rs:2461`) were checked as needed. No `#[ignore]` or silent early returns in the window. The fixtures the rig requires are asserted to exist.

- **[medium] prototype/osfr-tools/tests/bot_acceptance_1016.rs:854 `walk_disconnect_reconnect_restores_the_last_pose` - the logout flush is never isolated from the periodic pose tick, so the test does not prove the logout writes the newest pose.**
  - Why it cannot catch a regression: the gateway's deferred pose tick (`POSITION_SAVE_MS`, `osfr-gateway.rs:2461`) writes the newest pose on its own. `disconnect(bot)` followed by `save_when(None, ...)` polls for up to 30 s, so a build that drops the logout flush still passes once the tick fires. The restore at 862-867 then reads the same file.
  - Fix: use the `logout()` helper (which waits for the `client_disconnect` count to increase), then read `rig.save(0)` once with no polling and assert the saved x and z match `last`. Optionally assert the save's mtime or `saved_at` changed after the logout.

- **[medium] prototype/osfr-tools/tests/bot_acceptance_1016.rs:846-853 `walk_disconnect_reconnect_restores_the_last_pose` - the coalescing check is silently skipped whenever the login is more than 3.5 s old, although the doc claims it proves 4ba97ad.**
  - Why it cannot catch a regression: if the gateway saves every pose immediately (coalescing removed), the `if logged_in.elapsed() < 3500ms` guard turns the check off on a loaded machine, and the test passes.
  - Fix: make the mid-walk assertion unconditional by sampling the save right after the third pose, or fail when the guard is false. Alternatively, drop the coalescing claim from the doc and name the test accordingly.

- **[low] prototype/osfr-tools/tests/bot_acceptance_1016.rs:790-799 `builder_realm_command_runs_without_dev_tools_and_player_is_refused` - the security-log wait accepts two `dev_command` rows, which the player's own refusal and canary (lines 767 and 783) already produce, so the logging of the builder's `realm god` refusal (802-814) is never checked.**
  - Why it cannot catch a regression: the `>= 2` count is satisfied by the player's refusals alone. Logging of a refusal for the builder's cheat, or the role attached to each row, can change without failing.
  - Fix: after the cheat refusal, require the count to rise by one, and check that a `dev_command` row exists with the player's and the builder's `account_id` (or the command text).

- **[low] prototype/osfr-tools/tests/bot_acceptance_1016.rs:1052 `warpstone_attunes_by_walking_travel_relocates_and_locked_ids_do_not` - the name says "locked ids" (plural), but only id 4 is ever tested.**
  - Why it cannot catch a regression: a change that lets other locked ids relocate the player, or that treats id 4 specially, passes.
  - Fix: rename to `locked_id_4_does_not`, or loop over several locked ids (e.g. 0, 4, 6) and assert each is refused with no move.

- **[low] prototype/osfr-tools/tests/bot_acceptance_1016.rs:913-914 and 955-964 `eligible_equip_succeeds_and_ineligible_equip_is_refused_without_state_change` - the doc promises "one chat line each", but the refusal check only uses `wait_for`, which consumes the first match, so a duplicate refusal line is never detected.**
  - Why it cannot catch a regression: a handler that sends the refusal text twice still passes, because the QUIET wait (961) only looks for a 38/5 acknowledgement.
  - Fix: after each refusal, `wait_for(QUIET, |m| system_text(m) == Some(text))` must return Err. Otherwise the test should assert the line count is exactly one.
