<!-- fleet job=bug-hunt id=src-account-rs-L1 status=done turns=8 usd=0.0099 tokens(read,write,in,out)=[135157, 32535, 18, 8956] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/account.rs lines 1-501 of 501

Reviewed `account.rs` lines 1-501 and the callees they depend on (`identity.rs` `resolve`/`valid_name`, `account_store.rs` `insert_character`/`remove_character`/`character_name_taken`/`name_pairs`, `login.rs` `selection_reply`/`appearance_payload`), plus `tests/account.rs` 237-360. No panic, unbounded-growth, atomicity, or trusted-client-authority defect reaches the window from a client packet. Checked and dropped:

- `selection_reply` layout (`[12][status][0][flag][guid][1][1][len][data]`) matches the `single[26..30]` / `single[30..30+data_len]` slicing at lines 325-326, so that slice cannot go out of range.
- `NativeCreation.choices` is a fixed `[i32; 21]`, so the `c[...]` indexing in `resolve` cannot panic.
- `base64` chunks are non-empty, so `chunk[0]` is safe.
- `delete_character` and `select_and_bind_session` check owner before mutating; `create_character` mutates only through `insert_character`, which validates before it writes.
- Name uniqueness is enforced at the store level: `insert_character` checks both the displayed and temporary pairs of the resolved identity.

One finding:

- **[low] prototype/osfr-tools/src/account.rs:128-135 - a mixed displayed/temporary name collision is reported as `Failed` (code 2) instead of `NameTaken` (code 4).**
  - Failure scenario: a client sends `first_name="Bob"`, `last_name=""`, `temporary_first_name="X"`, `temporary_last_name="Smith"`, where the character "Bob Smith" already exists. `nonempty_pair(first_name, last_name)` at line 128 returns `None` because the last name is empty, and the temporary pair ("X","Smith") at line 136 is free. `resolve` then produces the identity "Bob Smith", and `insert_character` (account_store.rs:331) rejects it with `invalid_data`. Line 162 maps every store error to `fail(CharacterCreateStatus::Failed)`, so the client gets the generic failure 2 rather than the name-taken code 4. The name is still not duplicated, so this is a wrong-status bug, not a uniqueness bypass.
  - Reach: `create_character` (account.rs:95) is called from the create-character handler with client-supplied `NativeCreation`. Nothing upstream checks the mixed pair; `valid_client_name` at line 124 only checks validity.
  - Fix: at line 124, or just before `resolve`, run `store.character_name_taken(effective_first, effective_last)` and return `NameTaken` when it is true. Alternatively, map the name-taken error from `insert_character` to `NameTaken`.
