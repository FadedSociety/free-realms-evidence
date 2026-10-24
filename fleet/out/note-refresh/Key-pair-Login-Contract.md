<!-- fleet job=note-refresh id=Key-pair-Login-Contract status=done turns=31 usd=0.0320 tokens(read,write,in,out)=[1316641, 77031, 64, 18313] model=claude-haiku-5-5 -->
# notes/Research/Key-pair Login Contract.md

**Verdict:** minor drift. The protocol and limit contract (frame sizes, 69-byte replies, 134-byte proof, 60 s lifetimes, IP/account/global budgets, UDP caps, 30 s/120 s/10 min deadlines, `--auth-bind` default, `--allow-lan`, 32-byte server ID, `osfr-login-v1` transcript, 256-entry caps, `AccountStoreLock`) matches the tip. Three "still open" gap statements are stale, and the test-client retry detail is wrong.

**Corrections:**

1. `old:` `LoginService::new` still rejects a non-loopback gateway address (`src/login.rs:177-179`).
   `new:` `LoginService::new` accepts a loopback or private-network gateway address (`src/login.rs:177-180`, `net_policy::allowed(address.ip(), true)`); public addresses are still refused. `osfr-login` gates a private one behind `--allow-lan` (`src/bin/osfr-login.rs:105-107`).
   `why:` repo:prototype/osfr-tools/src/login.rs:177-180 (comment at 178-179: "loopback, or a private-network/VPN gateway"); repo:prototype/osfr-tools/src/bin/osfr-login.rs:102-107.

2. `old:` Current character-selection/gateway ticket policy still includes deterministic v1 and the account-1/character-1 fixed-ticket path.
   `new:` With `--account-store`, character selection and the gateway require the HMAC binding ticket for every account, account 1 / guid 1 included; the public fixed ticket is refused there (L023). The fixed ticket remains only in the no-account-store development path, where the gateway does no binding check.
   `why:` repo:prototype/osfr-tools/src/login.rs:416-418 (HMAC ticket for "every account, the host's 1/1 included"); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1108-1127 (binding verified when an account store is present; returns early otherwise); repo:prototype/osfr-tools/src/login.rs:27 (`DEFAULT_GATEWAY_TICKET`); also notes/Design/Build Ledger.md:37 (L023, 2026-10-21).

3. `old:` removal of the 1/1/v1 bypasses
   `new:` removal of the remaining no-account-store fixed-ticket bypass (the 1/1 bypass is already refused in account-store mode, L023)
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1121-1123 and repo:prototype/osfr-tools/src/login.rs:416-418; the no-store bypass is at osfr-gateway.rs:1108-1110 and login.rs:27.

4. `old:` The client now polls the existing sender on 100 ms receive timeouts, bounded to five seconds/256 packets.
   `new:` The client now polls the existing sender from its service loop (`flush()` on each `service()` pass). The login-path drain is bounded to 256 datagrams per pass, and the native-login wait is 5 seconds. The socket read timeout is 10 ms before the handshake and nonblocking after it.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-bot.rs:269 (10 ms read timeout), :310 (nonblocking after handshake), :384-388 (`flush` polls `sender`), :451-456 (256 budget), :875 (5 s wait).

**Unsure:**

- Gate-output counts in "Gate commands and outputs" (`login_broker: test result: ok. 5 passed; 0 ignored`, "Total distinct gates: 51 passed"). The file now has 8 `#[test]` items: 7 active and 1 `#[ignore]` (`private_broker_bind_admits_private_peers_and_keeps_failure_limits`, tests/login_broker.rs:227-229). These are dated cargo logs, so I did not change them. `login_auth` (10 tests) and `login` (11 tests) match their counts.
- Whether the "High, pre-existing outside W94" row's severity should now be lowered after L023. This is a judgement call, not a code fact, so I left it.
- The "v1" label in `gateway_binding_ticket` (`b"osfr-login-binding-v1"`, login.rs:557) is a keyed HMAC domain string, not a deterministic ticket. I did not treat it as a false claim.
- Launcher statements ("launcher work", "no launcher was edited") could not be checked against a launcher in this repo. `osfr-bot --broker-profile` is a test client, not the launcher.
- I did not verify the W94 "exact 60-second expiry" and "native token launch" claims beyond the code paths above, or the Gateway v2 statements in the lead-owned gaps section.
