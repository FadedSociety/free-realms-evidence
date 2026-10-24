<!-- fleet job=test-audit id=tests-bot-broker-login-rs-L1 status=done turns=4 usd=0.0060 tokens(read,write,in,out)=[28233, 19610, 10, 6507] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bot_broker_login.rs lines 1-433 of 433

Window reviewed: `prototype/osfr-tools/tests/bot_broker_login.rs` lines 1-433. The main assertions are real: the gate strings exist in `osfr-bot.rs` (784-787, 817, 820, 842), `"in world"`/`"ok expect"`/`"PASS"` are printed by the bot (605, 638, 1109), and the wrong-key and bad-pin paths return before any UDP send. No `#[ignore]`, no early-return skips, and the fixtures are generated in the test itself. The findings below are the gaps I could confirm.

- **[medium] prototype/osfr-tools/tests/bot_broker_login.rs:289-290 private_broker_profile_needs_allow_lan - the opted-in run is only checked for the absence of "private-network address", but the doc (lines 261-263) says it must get past the gate and fail later for its own reason (no login key).**
  - Why it cannot catch a regression: any early exit that does not print that phrase passes. Examples: an argument-parsing error after a rename of `--allow-lan`, a panic before the gate, or a bot that fails on something unrelated. The `!success` assertion at line 284 is satisfied by all of these.
  - Fix: assert the opted-in run's stderr contains the specific later failure (the missing `login.key` read error from `read_bounded` in `osfr-bot.rs` around line 811), and assert that the stderr does not contain "unknown" or usage text. A canary of the form `contains("login.key")` fails on any early exit.

- **[low] prototype/osfr-tools/tests/bot_broker_login.rs:427-432 broker_bot_reaches_world_and_wrong_key_sends_no_udp - the comment says the run "exercises the HMAC handoff" for account 2 / character 2, but nothing in the body checks the handoff, and the only check after the success asserts is a hex-only secret scan.**
  - Why it cannot catch a regression: a handoff regression that still reaches "in world" passes. The leak scan only catches the lowercase hex of the key. The same key in base64, decimal bytes, or a shortened form passes.
  - Fix: either remove the misleading comment or assert on a handoff-specific log line (e.g. the gateway handoff accept). For the leak check, also scan for base64 of each seed.

- **[low] prototype/osfr-tools/tests/bot_broker_login.rs:143 create_reference - `guid_offset: 21` is hard-coded in the manifest while `position_offset` and `rotation_offset` come from `startup_selfdata_fixture::self_data_packet`.**
  - Why it cannot catch a regression: if the fixture's GUID offset moves, the manifest keeps the stale 21 and the reference is silently wrong for the GUID field. Nothing in this window asserts the manifest's GUID offset against the fixture.
  - Fix: have `self_data_packet` also return the GUID offset and use it here, so the manifest cannot drift from the packet it describes.
