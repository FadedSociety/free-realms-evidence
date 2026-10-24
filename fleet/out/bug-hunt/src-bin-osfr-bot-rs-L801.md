<!-- fleet job=bug-hunt id=src-bin-osfr-bot-rs-L801 status=nothing_found turns=7 usd=0.0107 tokens(read,write,in,out)=[95137, 28370, 16, 12487] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-bot.rs lines 801-1167 of 1167

No reportable defects in `prototype/osfr-tools/src/bin/osfr-bot.rs` lines 801-1167. I read the whole window and the helpers it depends on (`auth_exchange`, `take`/`word`/`login_string`, `read_bounded`, `net_policy::allowed`, and the server side of the handoff in `login.rs:372-435` and `login.rs:689-706`). Nothing I checked is reachable from a remote peer with a panic, unbounded growth, a trust gap, or a mis-ordered save.

What I checked and why it holds:

- **Broker reply indexing (816-847):** `auth_exchange` returns a fixed `[u8; 69]` (`:706`), so `challenge[0]`, `[1..33]`, `[65..69]` and `token[33..]` cannot go out of range. The 32-byte pin is length-checked at `:791`, so the `try_into().unwrap()` calls at 832-833 cannot panic.
- **Server identity (819):** the pin is a shared 32-byte id that the broker echoes (`osfr-login.rs:249`), not a public key. The signature covers the pin, nonce and handle, so the echo is not a forgery gap I can show.
- **Native login parsing (879-904, 917-951):** every length comes from `word()` and goes through `take()`, which uses `get(..count)`, so there is no unbounded allocation. The character count is capped at 32. The handoff length must match exactly (925-928). The gateway address is checked with `net_policy::allowed` (932), and the ticket must be 16/24/32 ASCII bytes and equal the echoed key (937-943). The discarded 8-byte and 3-string fields match what the server writes (`login.rs:696-702`).
- **Secret hygiene (866-874):** `token` and `body` are zeroed on the success path. The early-return paths leave `seed` unzeroed (805-808), but that is a local hygiene nit with no remote impact, so I did not report it.
- **CLI assembly (965-1097):** the broker-profile conflict check, the account-store owner lookup, the `guid.unwrap()` at 1072 (guaranteed by the preceding branches), and the connection-id default are all consistent.
- **Minor, not reported:** `--connection-id` is truncated with `as u32` (1016), and the default ticket falls back to the public fixed ticket (1090). Both affect only the local dev tool's own CLI behaviour.
