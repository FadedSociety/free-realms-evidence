<!-- fleet job=bug-verify id=src-login-rs-L1-f1 status=done turns=8 usd=0.0091 tokens(read,write,in,out)=[128382, 30277, 18, 7982] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/login.rs:351-359

**Verdict:** confirmed (the defect is real; the reviewer's mechanism is slightly imprecise, see below).

**Severity if confirmed:** medium. It is data loss (character records overwritten on disk), not a crash, save corruption of a whole store, or an item/coin gain. It needs two sessions on the same host, since the unauthenticated path is loopback-only.

**Evidence:**

1. **In the real server.** `src/lib.rs:50` has `pub mod login;`, and `bin/osfr-login.rs:8` imports `login::{LoginService, ...}`. `login.rs` is not test-only.

2. **Reachable from the network.**
   - `bin/osfr-login.rs:117`: without `--account-store`, the bind must be loopback. `net_policy.rs:22-23` gives `allowed = ip.is_loopback() || (allow_lan && private)`, so peers are loopback-only unless `--allow-lan` is set.
   - `bin/osfr-login.rs:852`: `else if sessions.len() < 32` creates a new `Session` per peer.
   - `bin/osfr-login.rs:482`: `service: options.service()?` gives each session its own `LoginService` with its own `account_store` cache.
   - `bin/osfr-login.rs:730-731`: with no broker, `application` calls `self.service.handle(bytes)` directly. There is no reload.
   - `login.rs:316-318`: opcode 1 logs in when `login_name == config.local_session`, and the default is `"local-session"` (`bin/osfr-login.rs:63`). Any loopback peer that knows the name can authenticate, so the path is reachable.
   - `bin/osfr-login.rs:117` also means the account store path defaults to `identity.with_extension("accounts.json")` (`:145-146`). Unauthenticated sessions therefore share one disk file.

3. **Stale-copy write confirmed.**
   - `login.rs:218-259`, `authenticate_account`: each session loads the store at login and keeps it in `self.account_store`.
   - `login.rs:351`: `let mut staged = store.clone();`, then `account::create_character(&mut staged, ...)` (`:352`), then `staged.save(&self.config.account_store_file)` (`:359`) and `self.account_store = Some(staged)` (`:364`). Nothing reloads from disk.
   - `login.rs:464-468`: delete has the same `store.clone()` → `save` pattern.
   - `account.rs:132-134` and `:143-145` run `character_name_taken` only on the session's cached copy, so a name created by another session is not seen.
   - `account_store.rs:334`: `guid = self.data.next_character_guid` comes from the stale copy, so a collision with another session's guid is possible.
   - `account_store.rs:423-440`: `save` writes the whole document via `replace_bytes`, so the last writer wins.

4. **Authenticated path differs as stated.** `bin/osfr-login.rs:769-774` calls `options.service_for(handle)` before each request, which reloads the store through `login.rs:218`. The `AccountStoreLock` at `:793-796` is held for the whole process (cross-process coordination with the offline writer), not per request.

**Precision note on the mechanism:** the server loop is single-threaded (`bin/osfr-login.rs:830-870`), so there are no true parallel writes. The lost update comes from interleaved packets. Session B logs in (caches guid 1), session A creates and saves, then B creates from its stale cache and overwrites A's record. The fix is the same either way.

**Corrected fix:** the suggested fix is sound. In the create (`login.rs:351`) and delete (`login.rs:464`) branches, reload from `self.config.account_store_file` with `AccountStore::load` first. Re-run the account lookup and the ownership or slot checks on the fresh copy, then clone, mutate and save. Also refresh `self.account_store` from that copy. Because the loop is single-threaded, reloading just before the mutation is enough. A shared store handle is only needed if true parallelism is introduced.
