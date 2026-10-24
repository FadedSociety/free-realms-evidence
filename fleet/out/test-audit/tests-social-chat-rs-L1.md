<!-- fleet job=test-audit id=tests-social-chat-rs-L1 status=done turns=8 usd=0.0096 tokens(read,write,in,out)=[107847, 30087, 18, 9550] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/social_chat.rs lines 1-367 of 367

Window: `prototype/osfr-tools/tests/social_chat.rs` lines 1-367. Read the window in full, plus `src/social_chat.rs` (spam gate, recipients, ignores, quick-chat catalog, filters) and `src/restoration/piece_093.rs` (`validate_emote_phrase`).

- **[medium] prototype/osfr-tools/tests/social_chat.rs:109 packet_chat_bytes_match_client_writer_and_reader_for_every_channel - the expected bytes are built from the code under test, so the channel wire values are never pinned.**
  - Why it cannot catch a regression: `golden_chat_packet` (line 58) writes `packet.channel.wire()`, the same mapping the encoder uses. If `wire()` and `from_wire()` are changed together (for example, Say moves from 0 to 1 in both), the golden, the encoder and the round-trip all still agree, and the test passes against the wrong client wire value. The `0..=10` loop never compares `channel.wire()` with the literal `wire` it iterated over.
  - Fix: assert `chat_packet(ChatChannel::from_wire(w)).channel.wire() == w` explicitly, or write the expected channel word as a literal (the loop index) in `golden_chat_packet` instead of calling `.wire()`.

- **[medium] prototype/osfr-tools/tests/social_chat.rs:151 account_flags_enforce_quick_chat_only_and_filter_is_pluggable - the "pluggable filter" claim is never checked on the refusal path.**
  - Why it cannot catch a regression: the only call through the filter (lines 171-174) is an allowed message, expecting `Ok(())`. `authorize_free_text_with_filter` (src/social_chat.rs:621-636) could ignore `filter` entirely, or stop mapping `allows()==false` to `TextFiltered`, and this test would still pass. `TextFiltered` is never asserted anywhere in the window. The `!filter.allows("hello 123")` checks (line 164) test `WhitelistFilter` directly, not the authorization path.
  - Fix: add `assert_eq!(AccountChatPermissions::new(false,false).authorize_free_text_with_filter("hello 123", &filter), Err(ChatError::TextFiltered));`, and assert that `QuickChatOnly` is returned for the restricted account with the filter applied.

- **[medium] prototype/osfr-tools/tests/social_chat.rs:297 quick_chat_fanout_uses_session_scope_and_ignore_lists - the name says ignore lists are covered, but no ignore is ever added.**
  - Why it cannot catch a regression: `IgnoreLists::default()` is passed (line 308) and nothing calls `add()`. Removing the `retain(!ignores.ignores(..))` step in `resolve_quick_chat_recipients` / `resolve_recipients` (src/social_chat.rs:880) would leave the test green. The `Tell` arm's ignore check (src/social_chat.rs:926) is also untested here.
  - Fix: add `ignores.add(202, 101)` (member ignores sender) and expect `[1]`, or rename the test to drop "ignore_lists".

- **[medium] prototype/osfr-tools/tests/social_chat.rs:353 catalog_from_rows_keeps_membership_and_plain_rows_stay_unrestricted - the animated row is only checked for "any error", and no animated row is ever allowed.**
  - Why it cannot catch a regression: line 362 is `.is_err()`. That passes for `Mounted`, `ForeignAnimation`, `AnimationMismatch` or `Moving`. A change that refuses every animated row regardless of context would still pass. The Ok path for an animated row (unmounted, stationary) is never asserted, so the emote gating is only half-tested.
  - Fix: assert `Err(ChatError::EmoteRefused(EmoteRejection::Mounted))` for the mounted case (line 362), and add an unmounted, stationary `EmoteContext` case for animation 3306 expecting `Ok(())`.

- **[low] prototype/osfr-tools/tests/social_chat.rs:178 quick_chat_ids_are_checked_against_startup_rows_and_packets_roundtrip - the name says the ids are checked against startup rows, but the rows are test-local literals.**
  - Why it cannot catch a regression: `rows` is a local array fed to `QuickChatCatalog::from_ids`. It never calls the startup_world loader or any real table reader, so a bug in how startup rows populate the catalog (for example, dropping rows or mis-keying `id`) would not be caught. The name overclaims.
  - Fix: load rows through the real startup_world path (fixture file or the table loader), or rename the test to describe the local-catalog round trip only.
