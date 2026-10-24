<!-- fleet job=test-audit id=tests-login-rs-L1 status=done turns=6 usd=0.0058 tokens(read,write,in,out)=[76336, 22977, 14, 4372] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/login.rs lines 1-763 of 763

Window reviewed: `prototype/osfr-tools/tests/login.rs` lines 1-763. Two findings; the rest of the window checked out (the RC4 vector, the reconnect/identity-preservation checks, and the ignored private oracle tests all have real assertions or documented reasons).

- **[high] prototype/osfr-tools/tests/login.rs:632 self_identity_patch_preserves_unowned_tail_and_updates_nested_lengths - the "old name is gone" check cannot fail.**
  - Why it cannot catch a regression: `"old-head-long.adr"` is 17 bytes, but `changed.windows(16)` yields 16-byte slices. A 16-byte slice never equals a 17-byte literal, so `!changed.windows(16).any(...)` is always true. A `patch_self` that leaves the old head name in the packet would still pass this line.
  - Fix: scan with the matching width, e.g. `assert!(!changed.windows(b"old-head-long.adr".len()).any(|x| x == b"old-head-long.adr"));`, or assert on the exact encoded length-prefixed old string being absent. Better still, assert that `changed` contains the new `string(head.adr)` at the expected offset and that the total length shrank by the difference in name lengths.

- **[medium] prototype/osfr-tools/tests/login.rs:541 gateway_crypto_handoff_rejects_invalid_native_key_length - the name claims a key-length check, but the body only tests the gateway ticket.**
  - Why it cannot catch a regression: the only rejected input is `gateway_ticket: "local-rust-character"` (20 characters, which fails the `16 | 24 | 32` check in `src/login.rs:184`). The `handoff_key` length check (`config.handoff_key.len() < 16`, `src/login.rs:185`) is never exercised, so removing or weakening it would leave this test green. The first assert (`DEFAULT_GATEWAY_TICKET.len() == 32`) only pins a constant and does not test the key path.
  - Fix: rename to reflect the ticket (e.g. `..._rejects_invalid_gateway_ticket_length`), and add a case with `handoff_key: b"short".to_vec()` (15 bytes) and a valid ticket that asserts `LoginService::new(...)` is an error. Optionally also add a 16-byte key that succeeds, so the boundary is pinned.
