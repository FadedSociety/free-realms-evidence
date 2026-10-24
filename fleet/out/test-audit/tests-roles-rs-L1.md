<!-- fleet job=test-audit id=tests-roles-rs-L1 status=done turns=6 usd=0.0045 tokens(read,write,in,out)=[53537, 18699, 14, 3210] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/roles.rs lines 1-202 of 202

Reviewed `prototype/osfr-tools/tests/roles.rs` lines 1-202 against `src/account_store.rs` (`can_run_realm_command`, `parse`, `create_account`, `set_account_role`, `set_account_role_offline`, `load`, `save`, `validate`) and the `accounts-v1.json` fixture. Most assertions are sound: `schema_two_rejects_missing_role_records` fails under today's code only because `validate()` checks `roles.len() == accounts.len()`, and `only_admins_can_change_roles_and_changes_persist` checks state before and after the denied call and after the save/reload round trip. One real gap:

- **[medium] roles.rs:38 roles_allow_only_the_documented_commands - the Builder list omits `reload power_ups`, which `can_run_realm_command` grants to Builder, so the "only the documented commands" claim is not fully pinned.**
- **Why it cannot catch a regression:** `account_store.rs:72` grants Builder `"reload power_ups"`, but the test's `builder_commands` array (lines 39-56) has no such entry. Removing that arm from the `matches!` (or moving it to Admin-only) leaves every assertion in this test passing, since the test never checks that Builder can run it and never checks that Player cannot.
- **Fix:** add `"reload power_ups"` to `builder_commands` (lines 39-56). The Builder and Admin `true` assertions and the Player `false` assertion will then fail if that grant is removed.
