<!-- fleet job=note-refresh id=Kart-Native-Lobby-Codec status=done turns=10 usd=0.0139 tokens(read,write,in,out)=[206498, 43810, 22, 12806] model=claude-haiku-5-5 -->
# notes/Research/Kart Native Lobby Codec.md

**Verdict:** badly stale on integration status. The codec facts (framing, five tables, 10 committed tests plus 1 ignored gate, the `kart_racing` 140-byte subset writer) still hold. The note's "not wired, not registered, `#[path]` include" framing is no longer true: the lead's integration step has landed.

**Corrections:**

1. `old:` no gateway wiring, no content and no playability claim.
   `new:` gateway wiring is in place as an opt-in dev-tools responder (`gameplay.rs:1061` encodes `kart_lobby.json` once with `encode_inner`; `gameplay.rs:2302-2312` serves it for an exact 102/1 when `dev_tools` is set; `gameplay.rs:2713-2717` also pushes it). No native client acceptance, no content and no playability claim.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:1043-1064, 1061, 2302-2312, 2713-2717. Also notes/Current Progress.md:209 ("Root's native Kart lobby responder ...").

2. `old:` No shared `lib.rs`, `kart_racing.rs`, gateway, gameplay, `Cargo.toml`, content, save, UI or release
   `new:` No shared `kart_racing.rs`, `Cargo.toml`, content, save, UI or release path was touched. `lib.rs` now declares the module, and `gameplay.rs` wires it (see 1 and 3).
   `why:` repo:prototype/osfr-tools/src/lib.rs:43 (`pub mod kart_lobby_native;`); repo:prototype/osfr-tools/src/gameplay.rs:18 (import). The old line also spans a line break into "path was touched.", so apply it to the sentence as one unit.

3. `old:` path was touched. The module is a `#[path]` include in the test target until the lead registers it.
   `new:` path was touched by the codec work itself. Registration came later: `lib.rs:43` declares `pub mod kart_lobby_native;`, and the test target imports it from the crate (`use osfr_tools::kart_lobby_native::{...}`), so there is no `#[path]` include.
   `why:` repo:prototype/osfr-tools/src/lib.rs:43; repo:prototype/osfr-tools/tests/kart_lobby_native.rs:23-27 (the header now says "registered production library module").

4. `old:` through `kart_lobby_native::encode_tunnel` (and deciding the fate of the subset writer) is the lead's
   `new:` through `kart_lobby_native::encode_inner` is done (`gameplay.rs:1061`, `:2715`). `encode_tunnel` has no production caller (defined at `kart_lobby_native.rs:583`, used only by tests), and deciding the fate of the subset writer is still open.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:1061, 2715; repo:prototype/osfr-tools/src/kart_lobby_native.rs:569, 583. A grep of `src/` finds no `encode_tunnel(` call outside its definition.

5. `old:` include, and route the 102/2 response through `encode_tunnel`.
   `new:` include (done: `lib.rs:43`, test imports at `tests/kart_lobby_native.rs:27`), and route the 102/2 response through `encode_inner` (done: `gameplay.rs:2715`; `encode_tunnel` is unused in production). Gate 1 is closed.
   `why:` as in 1, 3 and 4 above.

**Checked and still current:** 
- The owned codec path `src/kart_lobby_native.rs` and the test path `tests/kart_lobby_native.rs` exist. 
- The test target has 11 `#[test]` functions, one of them `#[ignore]` (the private gate at line 370-371), so 10 committed + 1 ignored is right.
- `kart_racing::LobbyGameDefinition::encode` exists (`kart_racing.rs:152`) and matches the "i32 count, per-entry key plus four i32, four zero i32" layout (4 + 6×20 + 16 = 140 bytes).
- Framing constants (`TUNNEL_OUTER_OPCODES = [5, 6]`, opcode 102, sub 2, 20/16/16/16+len/24 row sizes) match `kart_lobby_native.rs:38-59`.
- The `TrailingBytes::Strict` and `Tolerant` policy exists (`kart_lobby_native.rs:94-97`).

**Unsure:**
- Gate 3 ("native acceptance: the original client's lobby list must render"): nothing in the repo proves or disproves it. The note still says it is open, which is consistent with the progress notes. I left it unchanged.
- The `lab/reports/...` paths (the evidence directory, the 2393-byte capture, and its sha256). `lab/` is not visible from the repo root in this environment, so I could not check the files or hashes. I did not verify the `FUN_008d67a0` / `FUN_008bfc00` client claims or the "re-checked 2026-10-12" date either.
- The verification-table counts (24/13/12, full-suite "no failures") are historical run logs. I did not re-run them. Later Autopilot reports (F166, F181, F188, F207, F211, F231) still report `kart_lobby_native` at 10 passed / 1 ignored, so they look consistent.
