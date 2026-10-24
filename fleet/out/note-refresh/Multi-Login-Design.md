<!-- fleet job=note-refresh id=Multi-Login-Design status=done turns=20 usd=0.0258 tokens(read,write,in,out)=[717176, 66033, 42, 20700] model=claude-haiku-5-5 -->
# notes/Research/Multi Login Design.md

**Verdict:** badly stale. The "Verified baseline" table (lines 36-56) describes the pre-W76 tree. Several rows are now false: the single-session login, the `guid_owners` map, the 1/1 ticket bypass (both login and gateway), and the no-credential schema-2 account record. The key-pair design (lines 13-22) has since been built in part (`login_auth.rs`, schema 3 with `public_keys`), which the note does not mention. The superseded password/Argon2 sections are marked as superseded and are not corrected below.

**Corrections:**

1. `old:` Login has one transport session; a different valid handshake replaces it, including one from another peer. Later traffic is accepted only for that session's peer.
   `new:` Login keeps one session per source peer in `HashMap<SocketAddr, Session>` (cap 32). An identical retry resends the saved response. A different Request from an occupied peer is refused, so one handshake cannot replace another peer's session.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-login.rs:826 (`sessions: HashMap<SocketAddr, Session>`), :845-852 (exact-retry resend; `sessions.len() < 32`).

2. `old:` Login already expires its single session after 120 seconds idle or sender failure.
   `new:` Login expires each peer session on its own: 120 seconds idle, 600 seconds absolute, 30 seconds unauthenticated (when authentication is on), or sender failure. One peer's expiry leaves the others running.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-login.rs:893-909.

3. `old:` PlayerRegistry combines account IDs and character GUIDs in `guid_owners`. Join checks/inserts both numbers; leave removes both. Thus account 2 can incorrectly conflict with another account's character 2.
   `new:` PlayerRegistry keeps separate `account_owners` and `character_owners` maps. Join checks both before inserting either. Leave removes only entries owned by that session. Equal numbers across the maps are legal, so account 2 and character 2 no longer collide.
   `why:` repo:prototype/osfr-tools/src/players.rs:184-188 (separate maps, with a W103 comment), :278-285 (checks), :304-305 (inserts), :319-326 (owner-only removal).

4. `old:` but account 1 / character 1 receives the fixed configured ticket. Other pairs receive a deterministic truncated HMAC.
   `new:` every account and character pair receives the same truncated HMAC ticket (v1 format, no nonce or expiry). The fixed 1/1 ticket is no longer issued.
   `why:` repo:prototype/osfr-tools/src/login.rs:412-418 (comment "L023: every account, the host's 1/1 included, gets an HMAC binding ticket").

5. `old:` The bypass is exactly `login.rs:414-418`.
   `new:` The bypass was removed (L023). The unconditional HMAC issue is at `login.rs:416-418`.
   `why:` repo:prototype/osfr-tools/src/login.rs:416-418.

6. `old:` Gateway derives the account from the selected character's stored owner, accepts the same 1/1 fixed-ticket bypass, otherwise verifies HMAC, and uses `characters/<guid>.json`.
   `new:` Gateway derives the account from the selected character's stored owner and always verifies the HMAC binding ticket. There is no 1/1 bypass. Selection is at `osfr-gateway.rs:1101-1127`.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1118-1127 (`verify_gateway_binding_ticket` for every account; the old `:742-773` / `:798-812` citations no longer match).

7. `old:` This narrows the duplicate risk but does not establish ownership before selection-time writes or cover an account selecting another character.
   `new:` This narrows the duplicate risk but does not establish ownership before selection-time writes (`osfr-gateway.rs:1138-1173`). Selection now also rejects a second selected session for the same account or character (`:1132-1137`).
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1132-1137 (checks `session.account_guid == account.id || session.character_guid == guid`), :1172 (save still runs at selection).

8. `old:` new cleanup guard: `:2451-2459`
   `new:` new cleanup guard: `:4421-4433`
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:4421-4433 (`another_owns` check before the save). Lines 2451-2459 are now in `tick`.

9. `old:` Account records currently have no credential field.
   `new:` Account records now carry launcher public keys (`public_keys`, one `Vec<[u8; 32]>` per account, enrolled via `add_public_key`). The store is at schema 3. No password field exists.
   `why:` repo:prototype/osfr-tools/src/account_store.rs:19 (`SCHEMA_VERSION: u32 = 3`), :91-94 (`public_keys`), :217 (`add_public_key`).

10. `old:` The schema-2-to-3 migration preserves roles and adds only `password_phc: null` and credential generation 0 to each existing account.
    `new:` The schema-2-to-3 migration preserves roles and adds an empty launcher public-key list (no password field) to each existing account. Existing accounts stay disabled until a key is enrolled.
    `why:` repo:prototype/osfr-tools/src/account_store.rs:453-457 (`public_keys` set to an empty `Vec` per account; "Migration never enrols keys implicitly").

11. `old:` Dependency decision, after checking `prototype/osfr-tools/Cargo.toml:9-13` and Cargo.lock: the checkout provides SHA-256, serde and compression, not password hashing, OS randomness or a dedicated constant-time compare.
    `new:` Dependency decision, after checking `prototype/osfr-tools/Cargo.toml:13-16`: the checkout now declares `sha2` 0.10, `ed25519-dalek` 2.2, `getrandom` 0.2.17 and `subtle` 2.6. No password-hashing crate (`argon2`) is present, which matches the key-pair decision.
    `why:` repo:prototype/osfr-tools/Cargo.toml:13-16.

12. `old:` `prototype/osfr-tools/src/bin/osfr-login.rs:82-83`, `:468`; `prototype/osfr-tools/src/login.rs:177-179`; `prototype/osfr-tools/src/bin/osfr-gateway.rs:1831`
    `new:` `prototype/osfr-tools/src/bin/osfr-login.rs:99-112`, `:840`; `prototype/osfr-tools/src/login.rs:180`; `prototype/osfr-tools/src/bin/osfr-gateway.rs:370`, `:3314`, `:3682`
    `why:` repo:prototype/osfr-tools/src/bin/osfr-login.rs:99-112 (`net_policy::allowed` on bind and peers), :840 (per-datagram filter); osfr-gateway.rs:370, :3314, :3682. Line numbers have moved. Note that `login.rs:180` calls `net_policy::allowed(address.ip(), true)`, so it is not a loopback-only check.

**Unsure:**
- Row 41's citation `login.rs:293-329` now sits at `login.rs:311-332`. The opcode-1 behaviour is unchanged: 1024/4096 bounds, the second string discarded, and `login_name == local_session` at `:316`. I did not verify the `osfr-login.rs:72` / `:112-122` citations for `--session`.
- Row 42's `login.rs:205-258` now reads `login.rs:207-261`. The auto-create on a missing account (`:252`) still holds. The LoginService still caches its own AccountStore (`:257`), so the lost-update risk is still open.
- The "Ordered function-level changes" table lists `src/login_auth.rs` as new. The file now exists (`login_auth.rs`: `LoginAuth` challenge/verify/redeem, `LoginFailures`, Ed25519 `validate_public_key`). It contains no Argon2 code. `src/login_handoff.rs` does not exist, so the v2 grant-record design (`osfr-login-binding-v2`, `.used` markers) is still unbuilt. The ticket is still v1 (`login.rs:557`).
- The regression-test specifications, the native table, and the two-client runbook were not checked against code. Build Ledger line 35 and Build Plan line 57 record key-pair login as built and bot-proven but never run natively, which contradicts the note's "no native run" framing only in scope, not in fact.
- The note's Build Plan citations (`Build Plan.md:21`, `:51`, `:53-57`) were not checked.
