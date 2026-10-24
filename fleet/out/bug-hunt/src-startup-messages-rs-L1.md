<!-- fleet job=bug-hunt id=src-startup-messages-rs-L1 status=nothing_found turns=8 usd=0.0040 tokens(read,write,in,out)=[59046, 14151, 18, 3283] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/startup_messages.rs lines 1-110 of 110

Reviewed `prototype/osfr-tools/src/startup_messages.rs` lines 1-110 in full (constants, `ZoneDetails`, `tunnel`, `counted_string`, and the builders for login reply, initialization parameters, zone details, hit points, mana, journal set and preload-done). No finding meets the bar.

Candidates checked and dropped:

- **startup_messages.rs:49-52 - `assert!` that the environment has no NUL byte.** This is the only panic site in the window. Its input is `login.environment` from the startup snapshot. `startup_snapshot.rs:672-681` (`parse_environment`) rejects embedded NULs when the snapshot is parsed, and `startup_snapshot.rs:254-256` (`validate`) rejects them again. `StartupSnapshot::load` calls `validate()` at `startup_snapshot.rs:219`. The snapshot is an operator-supplied file, not a live client packet, and `gateway.rs:838` is the only load site I found. So a NUL cannot reach the assert from a remote player. It is a latent panic only if a future caller skips validation.
- **`counted_string` (line 38) and `tunnel` (line 32) - `len() as u32` truncation.** Only reachable for strings or payloads of 4 GiB or more. Zone names and skies come from server content (`world.rs:1498`, `startup_snapshot.rs:376-385`).
- **`build_journal_set` (lines 95-105) - unbounded `entries` and `as u32` count.** The entries come from server-side quest/journal state (`quest_engine.rs:1310`) and the snapshot catalogue, not from a client-supplied count. The snapshot's `journal_entries` are capped by `MAX_ROWS` in `validate()`.
- **Doc comments versus code (lines 42-45, 47-57, 59-61, 77-92, 94-109).** These match the byte layouts written.
- **Zone, hit-point and mana values (lines 62-92).** They are server-side state, and no client packet reaches these builders directly.

No client-controlled value reaches an unchecked index, unwrap, division, or unbounded allocation in this window.
