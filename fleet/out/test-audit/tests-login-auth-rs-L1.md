<!-- fleet job=test-audit id=tests-login-auth-rs-L1 status=done turns=6 usd=0.0074 tokens(read,write,in,out)=[50619, 21354, 14, 8528] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/login_auth.rs lines 1-372 of 372

Window: `prototype/osfr-tools/tests/login_auth.rs` lines 1-372. Read the code under test in `prototype/osfr-tools/src/login_auth.rs` (lines 20-365).

- **[medium] prototype/osfr-tools/tests/login_auth.rs:146 signature_is_bound_to_server_handle_and_nonce - the test only shows that three hand-altered transcripts are refused and never shows that the specified transcript is accepted.**
  - Why it cannot catch a regression: the loop at lines 148-169 only asserts `Err(InvalidCredentials)`. There is no positive control with the unaltered transcript at lines 151-158. If `LoginAuth::verify` and `signing_message` were changed together to a different transcript, for example one without the `osfr-login-v1` domain prefix, every case would still be refused and the test would still pass. The honest-login test at line 79 uses the same helper on both sides, so it cannot detect this either.
  - Fix: in the same loop, build the spec transcript at lines 151-158 with no alteration (`changed == 3`, or a separate case) and assert `verify(...)` returns `Ok(_)` for it. Also assert that `signing_message(...)` equals those spec bytes, so the helper is pinned to the spec.

- **[medium] prototype/osfr-tools/tests/login_auth.rs:343 weak_keys_and_bad_signatures_never_create_tokens - the name says no token is created, but the final check at lines 368-371 does not look at token state.**
  - Why it cannot catch a regression: `redeem(&[b'0'; 32])` is a fixed guess. Tokens are random, so this call fails whether or not a token was minted. A verify path that minted a token for a bad signature or a weak key would still pass this check. The only real evidence is the `Err` results at lines 349-367, and those would stay green if a token were minted and returned only on a path the test does not reach.
  - Fix: after the failed attempts, complete one valid login with the same account and assert that it returns a fresh token that redeems to `id`, and that tokens are not left behind. Alternatively, expose a test-only token count and assert it is 0 after each refused attempt. A canary that minted a token on refusal should then fail.

- **[low] prototype/osfr-tools/tests/login_auth.rs:285 revoked_keys_disable_pending_challenges_and_tokens - the test hardcodes account ID `1` and discards the real `id` from `setup()` (line 281).**
  - Why it is a problem: the test depends on the store's first ID being 1, which is an incidental detail of `AccountStore`. The `.unwrap()` would turn a changed ID into a panic instead of a meaningful failure, and that is churn, not a missed bug.
  - Fix: bind the ID as `let (mut store, id, key, mut auth, now) = setup();` and call `store.remove_public_key(id, ...)`.
