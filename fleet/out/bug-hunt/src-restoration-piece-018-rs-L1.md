<!-- fleet job=bug-hunt id=src-restoration-piece-018-rs-L1 status=nothing_found turns=7 usd=0.0068 tokens(read,write,in,out)=[91091, 24998, 16, 5604] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_018.rs lines 1-422 of 422

I read `prototype/osfr-tools/src/restoration/piece_018.rs` lines 1-422 in full and found no defect I could tie to a line and show is reachable from client input.

What I checked:

- **Panics and indexing (`resolve`, `handle`, `plan`, `listing`, `usage`):** no indexing, slicing, or unwrap on client-supplied data. The `strip_prefix` and keyword-boundary logic at lines 322-326 handles `gamex`, `game`, and whitespace-only remainders without panicking. `resolve` lowercases, so the `from_utf8`-style concerns do not apply (input is `&str`).
- **Unbounded growth:** the only client-sized data is the query string, which is echoed once into a reply and matched against 9 fixed routes. Nothing grows with it.
- **Trusting the client:** the `WorldActor` route only proceeds when exactly one loaded actor matches the constant name in `WORLD_ZONE` (lines 377-403). The actor's GUID comes from the server-side `ActorView` list, not from the packet. The returned `Command::Route` carries the constant `actor` name, and the caller re-resolves that name through `dev_teleport::handle`.
- **Integration mismatch checked:** `dev_teleport::resolve` (`src/dev_teleport.rs:209-247`) looks up by exact lowercase name in the character's zone first, then unique prefix, and refuses ambiguity. Zone 0 is enforced at `dev_teleport.rs:102`. Because `plan` already requires one zone-0 actor with the exact name, the name-based `goto` either hits that actor or returns an "ambiguous"/"unknown" refusal. It cannot silently teleport to a different actor. The GUID in `Command::Route` is only shown in the reply text, which is harmless.
- **Logic against doc comments and tests:** `resolve` matches its doc (exact slug, then exact alias, then unique prefix; no alias collides with another slug). The `handle` doc (returns `None` while the gate is closed and for non-`game` text) matches the code. The test expectations I checked in `tests/piece_018.rs` (lines 318-333) agree with the implementation.

Caveat: the module is not yet registered in `src/lib.rs` and is only compiled through the test's `#[path]` include, so it has no live gateway caller yet. The integration step (lead-owned) is where a name-versus-GUID mismatch could appear, but that code is outside this window and I found no defect in what it would call.
