<!-- fleet job=test-audit id=tests-login-broker-rs-L1 status=done turns=11 usd=0.0123 tokens(read,write,in,out)=[195209, 32312, 24, 12554] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/login_broker.rs lines 1-620 of 620

Window: `prototype/osfr-tools/tests/login_broker.rs` lines 1-620. Four findings. Other tests in the window (the ignored LAN test, the broker refusal, the good-signature/wrong-key test, and the token routing test) check real behaviour and are not reported.

- **[medium] prototype/osfr-tools/tests/login_broker.rs:604-608 `accepted` (used at 540, 542, 570, 618) - the expected success frame is built by the same encoder the server uses, so only the slot field is independently pinned.**
  - Why it cannot catch a regression: the server's success reply is `login_reply_for_account(true, membership, max)` (src/login.rs:323), which goes through `login_reply_fields` (src/login.rs:615-634). `accepted()` calls `login::login_reply(true)`, which also goes through `login_reply_fields`, and then overwrites bytes 12..16. A change to the shared layout, such as the callback offsets, the account flag byte, or the payload framing, changes both sides identically and every login test still passes.
  - Fix: pin the full success frame as a literal byte array in the test (opcode 2, success 1, the fixed header, and the account block for `max_characters` 2 and 3), so that a change to `login_reply_fields` fails the test.

- **[medium] prototype/osfr-tools/tests/login_broker.rs:186-194 `login_gateway_address_follows_the_lan_rule` - the allowed-with-`--allow-lan` case only asserts that one error string is absent.**
  - Why it cannot catch a regression: the table's third column is `true` in every row, so the "accepted" branch of the `assert_eq!` is never exercised. The positive case at 190-194 only checks `!stderr.contains("loopback gateway")`. A regression that rejects `100.64.0.1` with a different message, or that exits early for any other reason, still passes.
  - Fix: assert the specific downstream failure that the comment promises (the missing-resources error for this run), or assert that stderr does not contain the gateway-policy message and does contain the resource-error text. Add a loopback-gateway row expected to be accepted, so both sides of the gate are checked.

- **[medium] prototype/osfr-tools/tests/login_broker.rs:575-591 `account_lockout_unknown_lockout_ip_budget_and_malformed_replies_are_generic` - the lockout threshold is only checked from one side.**
  - Why it cannot catch a regression: the loop makes exactly five wrong proofs and then expects a refusal. A lockout that trips after three failures (or after four) still passes. The test never checks that the account is still usable after fewer failures, so the threshold in `LoginFailures` (src/login_auth.rs:310-364, five failures) is not pinned.
  - Fix: after four wrong proofs, assert that a correct proof for `HANDLE` still succeeds (`token` returns a reply with `[0]==1`). Then make the fifth failure lock it. A threshold change then fails the test.

- **[low] prototype/osfr-tools/tests/login_broker.rs:351 `broker_good_signature_wrong_key_wrong_server_and_no_enumeration` - the challenge TTL of exactly 60 is pinned in a test about signatures and enumeration.**
  - Why it cannot catch a regression: nothing about the test's subject depends on the lifetime. It fails on any TTL tuning (the constant is `AUTH_LIFETIME` in src/login_auth.rs:23), which is churn unrelated to what the test name claims.
  - Fix: drop the assertion, or move it to a test named for the challenge lifetime. If it stays, reference the `AUTH_LIFETIME` constant rather than the literal 60.
