<!-- fleet job=bug-hunt id=src-account-store-rs-L1 status=nothing_found turns=13 usd=0.0241 tokens(read,write,in,out)=[404590, 49462, 28, 27688] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/account_store.rs lines 1-800 of 824

No defects I can show in `prototype/osfr-tools/src/account_store.rs` lines 1-800. I read the whole window and checked the callers it depends on.

What I checked:

- **Mutation before failure.** `create_account` (161-197), `insert_character` (314-361), `adopt_legacy_character` (363-407) and `add_public_key` (217-239) run every fallible check before touching `self.data`. The `expect("account checked above")` calls at 357 and 403 are safe because the account map is not changed between the lookup and the `get_mut`.
- **Login path.** `login.rs:207-261` and `login.rs:340-370` and `460-475` clone the store into `staged`, save it, and only then publish it. A failed save leaves the in-memory store unchanged. `load_or_migrate` (480-501) saves last, so a failed save leaves no half-migrated state. `AccountStoreLock::acquire` removes its own lock file if the PID write fails.
- **Client-sized input.** `load` and `read_legacy_state` cap reads at `MAX_FILE_BYTES + 1` and `character_store::MAX_FILE_BYTES + 1`. `save` enforces the same 1 MiB limit. No indexing or unwrap sits on client bytes. Recursion is bounded by serde_json.
- **Authority.** Roles and keys are server-side state. Network role changes go through `gateway.rs:1151-1180`, which takes the lock, checks the verified actor binding, and saves. Login creates accounts only when `login_name == config.local_session` (`login.rs:316`), so a remote client cannot mint unbounded accounts. Character creation is limited by `slots` and `validate()`.
- **Schema migration.** Versions below 3 are rejected if they carry keys, unknown versions return `Err`, and `validate()` enforces the role and key maps against the accounts.
- **Name folding.** `LATIN_FOLDS` covers every uppercase letter in the client-creatable range U+00C0..=U+024F that has a case pair, so I found no uniqueness gap reachable from client names. Names outside that range (e.g. U+1E9E) can only come from legacy identity files, not from a client packet.

Drop-only candidates I rejected: the 1 MiB store cap making new accounts fail (not reachable by a remote client because of the `local_session` gate), the `name_key`/`name_keys` split (documented as intentional), and the `can_run_realm_command` key matching (fails closed).
