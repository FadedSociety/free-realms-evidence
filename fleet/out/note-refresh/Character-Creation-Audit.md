<!-- fleet job=note-refresh id=Character-Creation-Audit status=done turns=15 usd=0.0120 tokens(read,write,in,out)=[324700, 36726, 32, 8220] model=claude-haiku-5-5 -->
# notes/Research/Character Creation Audit.md

**Verdict:** minor drift. Most code claims hold at the tip. The closing scope sentence is now false: the login service routes delete, the account store has multi-character slots, and key-pair authentication is built.

**Corrections:**

- `old:` Account authentication, multiple characters and deletion are outside the current local implementation.
  `new:` The account store routes character delete (opcode 9) and allows up to six characters per account by default. Launcher key-pair authentication (`login_auth.rs`) is built but has not been run natively. Two-character create/list/select/delete is still untested natively.
  `why:` repo:prototype/osfr-tools/src/login.rs:460-479 (opcode 9 calls `account::delete_character`, which is also in account.rs:371); repo:prototype/osfr-tools/src/account.rs:110 (slot limit check); repo:prototype/osfr-tools/src/bin/osfr-login.rs:68 (`max_characters = 6` default); repo:prototype/osfr-tools/src/login_auth.rs:1 (key-pair authentication module); repo:notes/Design/Build Ledger.md:35-36 (key-pair mode built, never run natively; two-character flow still open).

**Checked and holding:**

- Native creation body: four strings and 21 `i32` choices (repo:prototype/osfr-tools/src/identity.rs:20-31).
- Creation and selection accept server 0 or 1 and reject others (repo:prototype/osfr-tools/src/login.rs:347, 391).
- Creation rejection diagnostics carry only the reason string (repo:prototype/osfr-tools/src/login.rs:348, 367; repo:prototype/osfr-tools/src/bin/osfr-login.rs:614-620).
- The private oracle tests are `#[ignore]`d and require private inputs (repo:prototype/osfr-tools/tests/login.rs:639, 666).

**Unsure:**

- "Seven ordinary login tests pass": `tests/login.rs` has 15 `#[test]` functions, two of them `#[ignore]`, so 13 run by default. The count may refer to a narrower subset from the run, so I did not change it.
- "The Rust implementation supports one local identity": the identity file is single-character (identity.rs:111, `guid != 1` rejected; login.rs:360-362 saves only guid 1), but the account store holds several characters. The sentence may be read either way, so I left it.
- "Seven ordinary login tests" and the `LoginService previously attempted creation only for server1` history claim could not be verified without git history.
- External claims (client logs, launcher manifest, hashes, asset packs, and the Sanctuary comparison) are outside the repo and were not checked.
