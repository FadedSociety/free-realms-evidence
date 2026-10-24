<!-- fleet job=note-refresh id=Accounts-and-Characters status=done turns=15 usd=0.0179 tokens(read,write,in,out)=[361025, 51454, 32, 15629] model=claude-haiku-5-5 -->
# notes/Research/Accounts and Characters.md

**Verdict:** Badly stale on integration status. The account modules are now registered and wired into login, so the "not integrated / not registered" framing is false. The file paths, status codes, name thresholds, and reconstructed-policy statements still hold, apart from one schema version.

**Corrections:**

1. `old:` This is a Rust candidate slice, not login/gateway integration or native acceptance.
   `new:` The Rust slice is registered in `lib.rs` and wired into `LoginService` (`login.rs:207-260`). The Build Ledger records the account store as wired with an HMAC gateway handoff (`notes/Design/Build Ledger.md:37`). Native acceptance is still not established.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:4-5` (`pub mod account; pub mod account_store;`); `repo:prototype/osfr-tools/src/login.rs:4-9`, `:207-260`.

2. `old:` `login.rs`, `gateway.rs`, and `lib.rs` still use the existing single-identity flow; W11 modules are intentionally not registered.
   `new:` `lib.rs` registers `account` and `account_store`. `login.rs` loads the account store by login-name hash and routes list (opcode 11), name-check (210), create (5), select (7), and delete (9) through the W11 handlers. The gateway loads the account store when `--account-store` is set.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:4-5`; `repo:prototype/osfr-tools/src/login.rs:274-294`, `:312-318`, `:333-336`, `:351-364`, `:392-399`, `:451`, `:465-476`; `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1012-1026`, `:1114`.

3. `old:` 1. In a lead-owned integration change, register `account` and `account_store` in `prototype/osfr-tools/src/lib.rs`.
   `new:` 1. Done: `account` and `account_store` are registered in `prototype/osfr-tools/src/lib.rs:4-5`.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:4-5`.

4. `old:` Extend `LoginService` in `src/login.rs` to load the account store using an authentication-derived login-name hash.
   `new:` Done: `LoginService` loads the account store by login-name hash (`login.rs:207-260`) and routes list, name-check, create, delete, and select through the handlers (`login.rs:274-294`, `:351-364`, `:451`, `:465-476`). Create and delete save the store (`login.rs:359`, `:467`). The first-use path calls `migrate_legacy_account_store` and `AccountStore::load` directly, not `AccountStore::load_or_migrate`.
   `why:` `repo:prototype/osfr-tools/src/login.rs:207-260`, `:351-364`, `:465-476`; `repo:prototype/osfr-tools/src/account_store.rs:480` (`load_or_migrate` exists, but login.rs does not call it).

5. `old:` Account-info reply construction, server-authentication lookup, actual slot settings, profanity policy, suggestion encoding, and underage/open-chat semantics need lead decisions and client-backed evidence where available.
   `new:` Actual slot settings, profanity policy, suggestion encoding, and underage/open-chat semantics need lead decisions and client-backed evidence where available. The account-info reply is built from account state (membership and maximum characters, `login.rs:323-327`, `:611-624`). Admin stays false because no admin flag is stored locally (`login.rs:619`).
   `why:` `repo:prototype/osfr-tools/src/login.rs:323-327`, `:611-627`.

6. `old:` `AccountStore` has JSON schema version 1
   `new:` `AccountStore` has JSON schema version 3 (it still loads legacy v1 and role-era v2 documents)
   `why:` `repo:prototype/osfr-tools/src/account_store.rs:19-21` (`SCHEMA_VERSION = 3`, `ROLE_SCHEMA_VERSION = 2`, `LEGACY_SCHEMA_VERSION = 1`) and `:452-470` (the load match).

**Unsure:**

- **Test count (line 46, "GREEN: 5 passed, 0 failed").** This is a dated record of the W11 run and may stay as history. `tests/account.rs` now defines seven `#[test]` functions (lines 114, 236, 376, 454, 517, 555, 618). `notes/Autopilot/L049.md` says three tests were added later. Not corrected.
- **Step 4 (session binding and gateway handoff).** Binding is implemented (`login.rs:392-399`), and delete clears the binding (`login.rs:469-476`). The gateway HMAC handoff is cited by the Build Ledger at `osfr-gateway.rs:742-814`, which I did not open.
- **"Two-character native creation ... remain untested" (line 57).** I did not check the Autopilot reports for a native two-character run. Build Ledger line 37 cites a native run that logged in one character, which does not settle the question.
- **Cross-root paths.** I did not check `scripts/native_map/nmq.py`, the Build Guide line cites (`:70-78`, `:237-242`, `:285-290`), or the client-side `00fa…` addresses. These refer to the `lab/` and client trees, which I did not open.
- **Lines 19 and 20.** The `Account` struct has no role field (`account.rs:36-42`). Roles live in `account_store.rs` (W78, per Build Ledger line 49), so the note is not false, only silent on roles.
