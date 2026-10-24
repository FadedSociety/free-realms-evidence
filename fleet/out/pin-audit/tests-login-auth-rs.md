<!-- fleet job=pin-audit id=tests-login-auth-rs status=nothing_found turns=3 usd=0.0022 tokens(read,write,in,out)=[6907, 12745, 8, 1121] model=claude-haiku-5-5 -->
# tests/login_auth.rs

No findings in `prototype/osfr-tools/tests/login_auth.rs` for the two screened lines.

- **login_auth.rs:25** (`credential_failure_lockout_recovery_success_reset_and_unknown_capacity`): the 59 s check is a just-inside-window bound. The window comes from the hard-coded `Duration::from_secs(600)` in `prototype/osfr-tools/src/login_auth.rs:321` (the `LoginFailures` lockout). It is not in any file under `data/content/`, so it is not a data-file value.
- **login_auth.rs:41** (same test): the 600 s expiry matches that same code constant at `src/login_auth.rs:321`. It is not read from data. Nothing in `data/content/` sets it.

Both numbers are code constants, not shipped data values, so retuning data would not break them. The other timer in the file, `AUTH_LIFETIME` (`src/login_auth.rs:23`, 60 s), is also a code constant. Keeping these as literals is outside the data-tunable rule, so no change is required by that rule. If Bryce wants the lockout window to be live-tunable, that is a code move (into `data/content`), not a test fix.
