<!-- fleet job=test-audit id=tests-emotes-rs-L1 status=done turns=9 usd=0.0075 tokens(read,write,in,out)=[108309, 22970, 20, 7117] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/emotes.rs lines 1-374 of 374

Window `tests/emotes.rs` 1-374 reviewed against `src/social_chat.rs` (authorize_emote 461, emote_context 485, decode/encode/resolve 507-933), `src/restoration/piece_093.rs` (validate_emote_phrase 934, FREEZE_MOVEMENT_ANIMATIONS 787, EMOTE_COMMANDS/ACTIONS) and the real gateway handler `src/bin/osfr-gateway.rs` 1875 and 2294-2320. Most assertions are real: the expected values (3001 freeze, 3354 no freeze, 184 dance, 3306 vs 3317 mismatches, the `[1,2]` control in the echo test, the ignore direction `add(recipient, ignored)`) are consistent with the code, and the canary at 368 is sound. Findings:

- **[medium] tests/emotes.rs:307 forbidden_emote_fails_the_same_way_on_every_channel_and_reaches_nobody - "reaches nobody" is never checked against the real gateway; every route goes through a test-local `route()` helper (lines 202-243) that copies the gateway order.**
  Why it cannot catch a regression: `route()` is the test's own pipeline. If `osfr-gateway.rs` (around 2306-2320) resolved recipients or sent the echo before calling `authorize_emote`, or dropped the authorize call entirely, this test would still pass, because it never touches the gateway. The only part that does reach the real code is `ChatError::client_reply()`, which is not a fan-out check.
  Fix: drive the real gateway handler (or a recipient/send sink it writes to) with a mounted sender and assert that the recipient sink receives nothing and that no echo packet is written, not only that `route()` returns `Err`.

- **[low] tests/emotes.rs:137 an_unknown_phrase_is_refused_and_supplies_no_animation - the name claims "supplies no animation" but the body only compares the `UnknownQuickChatId` variant.**
  Why it cannot catch a regression: nothing checks animation data or the encode path. A change that returned a non-error animation for unknown ids through `encode_quick_chat_*` or the decode path would not be caught, since those calls are not in this test.
  Fix: rename it to match (e.g. `an_unknown_phrase_is_refused_by_authorize`), or add `decode_quick_chat_request` and `encode_quick_chat_channel`/`_tell` assertions that return `UnknownQuickChatId` for these ids.

- **[low] tests/emotes.rs:190 moving_window_is_inferred_from_the_last_accepted_movement - the name says the window is inferred from the last accepted movement, but the body only exercises the pure `social_chat::emote_context` function.**
  Why it cannot catch a regression: the gateway wiring, `gateway.rs:1322` (`emote_context(now_ms)` reading `self.last_movement_ms`) and `osfr-gateway.rs:1875`, is never exercised. Recording `last_movement_ms` on movement, or passing the wrong clock, would not fail here.
  Fix: a test that feeds a movement update through the gateway state, then checks that `emote_context(now)` reports `moving` within 500 ms and not after.

- **[low] tests/emotes.rs:108 mounted_actors_cannot_emote_but_can_still_use_plain_chat - the plain-chat half is only `authorize_emote`, not the chat route.**
  Why it cannot catch a regression: a change that blocks plain quick-chat for mounted actors at decode, resolve or encode would still pass this test. The route-level check exists only in `normal_quick_chat_and_tells_still_work_while_mounted_or_moving` (278), so this name overstates what this test checks.
  Fix: either narrow the name to "authorization" or add a `route(..., mounted(), ...)` assertion that plain phrases reach recipients [1, 2].
