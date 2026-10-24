<!-- fleet job=bug-hunt id=src-world-text-rs-L1 status=nothing_found turns=15 usd=0.0087 tokens(read,write,in,out)=[214020, 23144, 32, 7366] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/world_text.rs lines 1-220 of 220

No reportable defects in `prototype/osfr-tools/src/world_text.rs` lines 1-220.

What I checked:

- **Hash (`mix`, `jenkins_lookup2`, lines 26-68):** The `p[..4]` slice is only reached when `rest.len() >= 12`, so it cannot panic. The tail handling matches lookup2 (the length goes into `c`, and the byte shifts are correct). The test vectors at lines 187-189 cover it.
- **`stock_hashes` (76-88):** Parsing failures are skipped with `unwrap_or_default`/`ok()`, and no unwrap sits on file content. The file is the trusted stock locale anyway.
- **`TextPool::add` input checks (138-150):** Trim, the 1..1000 char limit, and the rejection of tab/CR/LF are all applied before any state change.
- **Mutation before save (157-164):** `add` pushes the entry and advances `next_id` before `save()`, so a failed save leaves the in-memory pool changed. This is not reachable as a defect. The only caller, `gameplay.rs:2844-2849`, calls `TextPool::load` fresh for every command, so the in-memory state is dropped on error.
- **Client reach:** `realm text` (`gameplay.rs:2842`) is reached only through `developer_cheat` (`gameplay.rs:4330`), which is gated by `may_run` (`gameplay.rs:3661`: `--dev-tools` or a server-owned role, plus `can_run_realm_command`), and `developer_command_denied` fails closed for other realm routes. Unbounded growth of `text.json` and the `i32` id arithmetic (`id += 1`, `id + 1` at lines 156 and 163) therefore need a developer or a hand-edited save, not a remote player.

Weaker observations I did not promote to findings:

- With no `--client-locale` (`osfr-gateway.rs:352-354`), `stock` is `None` and `add` does not skip ids whose locale hash is already a stock row. This is configuration-dependent and the collision odds are small, so I did not treat it as a defect.
- `TextPool::add` is an unlocked load-modify-save. Two developer sessions running `realm text` at the same time could both take the same `next_id`, and the last writer would drop the other text. I did not confirm that sessions can run concurrently against the same `live_dir`, and the trigger is developer-only.
- `load` takes `next_id` from the file with only a `.max(FIRST_WORLD_TEXT_ID)` floor. A hand-edited `text.json` whose `next_id` is below existing entry ids could hand out a duplicate id. This needs a corrupt save, not a client packet.
