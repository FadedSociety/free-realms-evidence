<!-- fleet job=bug-hunt id=src-bin-osfr-account-rs-L1 status=nothing_found turns=7 usd=0.0059 tokens(read,write,in,out)=[69666, 19387, 16, 5515] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-account.rs lines 1-287 of 287

Reviewed `prototype/osfr-tools/src/bin/osfr-account.rs` lines 1-287 in full, plus the store methods it calls (`account_store.rs` 120-310 and 420-470, `login_auth.rs` 46-65). No reportable defect.

What I checked:
- **Hex decoding (27-44):** `public_key` checks the byte length first, then decodes byte pairs with `chunks_exact(2)`. Non-ASCII bytes fail the nibble match, so there is no str slicing panic. The `<< 4` on a value of at most 15 cannot overflow. `validate_public_key` (login_auth.rs:58) rejects wrong lengths, invalid points and weak keys.
- **Argument parsing (46-68):** `--help` with extra args falls through to the usage error. Duplicate and unknown flags are rejected. A missing value is rejected. `options.len() == expected.len()` with unique keys means every required flag is present.
- **Handle (87-90):** `login_handle_hash` enforces 3-32 ASCII alphanumeric, `_` or `-` bytes before hashing, so odd argv input cannot panic.
- **Atomicity (107-147):** `create` mutates only the in-memory store. If `add_public_key` fails, the `?` returns before `save`, so nothing lands on disk. Other commands save only after a successful mutation. `save` validates first and writes via `replace_bytes`.
- **Lock (99):** `AccountStoreLock` is held for the whole run. Its Drop removes the lock file even if the pid write fails, because the guard is built before the write.
- **Store invariants:** `create_account` rejects duplicate login hashes and `max_characters == 0`. `add_public_key` rejects duplicate keys across all accounts and enforces `MAX_PUBLIC_KEYS`. `set_account_role_offline` requires the account to exist.

Not reported:
- The module doc says private keys are "never accepted", but `validate_public_key` only checks point validity. A 32-byte seed can be a valid point, so the CLI cannot tell it apart from a public key. This is a documentation overstatement only. The operator is trusted, and no client packet reaches this binary.
- `list` can print partial output before a `missing account role` error. This cannot happen with a store that passed `load` and is not a defect.

No client packet or save path reaches this window with attacker-controlled data, and the checks above stop the cases I examined.
