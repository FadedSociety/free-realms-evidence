<!-- fleet job=test-audit id=tests-world-notice-rs-L1 status=done turns=8 usd=0.0080 tokens(read,write,in,out)=[108061, 27961, 18, 6796] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/world_notice.rs lines 1-234 of 234

Window: `prototype/osfr-tools/tests/world_notice.rs` lines 1-234. Checked against `src/world_notice.rs` (parse/encode/stage), `src/chat.rs` (`request`, `local_request`), `src/gameplay.rs:4269-4331` (opening intercept and realm dispatch), and `src/gameplay/movie.rs:68-75` (`realm_message`). The rest of the file holds up: the role and refusal tests check state and reply text, the bounds are pinned to literals, and the movie test fails if the intercept is removed. The `lab/references` fixtures live outside the repo, but the tests use `unwrap`/`expect`, so a missing fixture fails loudly rather than skipping.

- **[medium] tests/world_notice.rs:179-180 `an_announcement_at_the_multibyte_boundary` (the multibyte block inside `empty_overlong_multibyte_or_control_text_is_refused`) - the packet check is only `packet.len() <= 8 + 2048 + 1`, so it never checks the text that was encoded.**
  - Why it cannot catch a regression: an `encode` that truncates the text to about 1000 bytes, or drops the trailing flag byte, still gives a packet under the bound and the test passes. The comment says "packet fits one system line", but nothing checks that the line is complete.
  - Fix: replace it with `assert_eq!(packet.len(), 8 + 800 + 1); assert_eq!(system_text(&packet), multibyte);`. The `system_text` helper already exists in this file and asserts the 15/3 header and the length prefix.

- **[low] tests/world_notice.rs:191-192 `announcement_text_is_trimmed_escaped_and_never_echoes_the_command` - the `!contains("realm")` check runs on the encoded broadcast packet, which is built from the notice text, so it cannot detect an echo.**
  - Why it cannot catch a regression: an echo of the command would go into `out.replies`, not into the broadcast packet, so line 192 passes whether or not the command is echoed. Line 189 (`out.replies.is_empty()`) is the check that actually covers the name, and line 192 adds nothing.
  - Fix: assert on the replies, for example `assert!(reply_texts(&out).iter().all(|t| !t.contains("realm")))`, or drop line 192 and rely on line 189.

- **[low] tests/world_notice.rs:158-160 `empty_overlong_multibyte_or_control_text_is_refused` - the 2049-byte wire line is checked only with `.is_err()`, which accepts any error.**
  - Why it cannot catch a regression: a failure from some unrelated cause (a malformed state, a changed local-request layout) still returns `Err` and passes. The comment's claim that the chat cap is what drops the line is never checked.
  - Fix: assert the error source, for example `assert!(chat::request(&huge_packet, 0).is_err())` on the 2058-byte packet, or match the specific `io::ErrorKind` that `chat::request` returns when `r.string(2048)` fails.
