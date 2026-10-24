<!-- fleet job=note-refresh id=Login-Integration status=done turns=29 usd=0.0273 tokens(read,write,in,out)=[1021882, 67209, 60, 17361] model=claude-haiku-5-5 -->
# notes/Research/Login Integration.md

**Verdict:** Minor drift. Most of the Result and Reconstructed-policy sections hold at the tip (login routing, SHA-256 login-name hash, `load_or_migrate`, staged create/delete, `characters/<guid>.json`, HMAC binding ticket, defaults 6 / false / true, `chess`/`guilds`/`matchmaking` in `src/lib.rs`). One statement about the gateway ticket is false in account-store mode. The routing sentence and two test-count rows are stale.

**Corrections:**

1. `old:` A fixed configured gateway ticket remains the compatibility route for account 1 / character 1.
   `new:` With `--account-store`, the fixed configured gateway ticket is refused for every account, including account 1 / character 1; the HMAC binding ticket is required. The fixed value is only the `--ticket` default.
   `why:` `repo:prototype/osfr-tools/src/login.rs:416-418` (L023: every account, 1/1 included, gets an HMAC binding ticket, because the public fixed ticket would let anyone in as 1/1); `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1121-1127` (store mode calls `verify_gateway_binding_ticket` and logs an AuthFailure on refusal); `repo:prototype/osfr-tools/src/login.rs:27` (`DEFAULT_GATEWAY_TICKET`, a synthetic default); `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:315-343` (`--ticket` only sets the default value).

2. `old:` This is API registration only. No gateway or gameplay routing was added for those services.
   `new:` This is API registration only as of W55. Later work added routing for two of them: guild family 129 through the gateway (`src/bin/osfr_gateway/t006_guild_routing.rs`) and matchmaking list/stat/leave requests through `src/gameplay/matchmaking_route.rs`. Chess routing was not checked. `notes/Design/Build Ledger.md:46` still says "Not routed", so that row needs the same update.
   `why:` `repo:prototype/osfr-tools/src/bin/osfr_gateway/t006_guild_routing.rs:1-4`; `repo:prototype/osfr-tools/src/gameplay/matchmaking_route.rs:1-17` (calls `matchmaking::handles`/`route`); `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:3370` (`GuildWorld::load` in the gateway world).

3. `old:` | `tests/chess.rs` | 12 | 0 | 0 |
   `new:` | `tests/chess.rs` | 19 | 0 | 0 |
   `why:` `repo:prototype/osfr-tools/tests/chess.rs` holds 19 `#[test]` functions and no `#[ignore]`. This row is from an earlier run; the table's "latest" label is no longer accurate.

4. `old:` | `tests/matchmaking.rs` | 11 | 0 | 1 |
   `new:` | `tests/matchmaking.rs` | 16 | 0 | 1 |
   `why:` `repo:prototype/osfr-tools/tests/matchmaking.rs` has 17 `#[test]` functions, one of them `#[ignore]` (line 327-328), so 16 pass and 1 is ignored. Also update the verification-row text "chess 12/12 ... matchmaking 11 passed / 1 ignored" and the total "56 passed" to match a fresh run.

**Checked and holding (no change):** `login.rs:207-261` (SHA-256 login-name hash, `load_or_migrate` path); `login.rs:12-16`/`login.rs:486-548` (temp CharacterState projection, legacy files only read); `login.rs:333-479` (create/delete staged and saved; name-check via tunnelled 210; character-list and select routed to `account::`); `login.rs:611-634` (account-info reports configured max, no admin byte); `bin/osfr-login.rs:68` (defaults 6, false, true); `bin/osfr-gateway.rs:1114-1188` (GUID ownership from its own AccountStore, initial full-snapshot `fs::copy` to the per-character path); `bin/osfr_gateway/paths.rs:23-30` (`characters/<guid>.json`); `lib.rs:10,28,52` (chess, guilds, matchmaking registered); `tests/login.rs` 13 `#[test]` with 2 `#[ignore]` (matches 11/2); `tests/guilds.rs` 11 tests (matches 11/11); client addresses `00719330`, `00719550`, `00fa4370`, `00fa5ce0`, `00fa5e50`, `00710e20`, `007198b0` all exist in the client database.

**Unsure:**
- The "Latest full-suite" counts for other targets (`piece_050`, `soccer*`, `movement`, `npc_interaction`, `pets`) were not re-counted.
- Whether the native-client, startup-oracle, and byte-identical claims still hold; these need a live run.
- The `Build Ledger.md:46` "Not routed" status conflicts with the routing code above. I did not decide which is current for chess.
