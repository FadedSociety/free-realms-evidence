<!-- fleet job=note-refresh id=Kart-Native-Gateway-Lobby-Binding status=done turns=17 usd=0.0113 tokens(read,write,in,out)=[278253, 31062, 36, 9278] model=claude-haiku-5-5 -->
# notes/Research/Kart Native Gateway Lobby Binding.md

**Verdict:** minor drift. Most claims hold at the tip (codec, 256 KiB cap, cache, inner 102/1 to 102/2, module registration, test shape). One behavioural claim is false: developer-disabled inertness does not hold while a race is active.

**Corrections:**

1. `old:` Other subtypes, disabled developer tools and missing content remain inert.
   `new:` Other subtypes and missing content remain inert. The opt-in 102/1 branch is gated on developer tools, but an exact 102/1 received while a kart race is active is answered by the in-race branch with the cached reply, with no developer-tools check. An ordinary NPC race entry can make the race active with developer tools off, so the catalogue can be served in that state.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:2302 (the `self.dev_tools` gate on the opt-in branch); repo:prototype/osfr-tools/src/gameplay.rs:2713-2716 (`if inner == [102, 0, 1, 0]` pushes `kart_lobby_reply` with no dev-tools check, reached from `handle_kart_entry` at gameplay.rs:2654 whenever `kart_entry` is active, per gameplay.rs:2273-2284); repo:prototype/osfr-tools/src/gameplay/npc.rs:574-577 (ordinary NPC `Race` selection calls `begin_kart_race` without a developer-tools check).

**Checked and holding (no change):**
- `kart_lobby_native` is registered (`src/lib.rs:43`); `zone_transition` (`lib.rs:102`) and `kart_progress_native` (`lib.rs:45`) are registered; `gameplay.rs:18` imports `kart_lobby_native`.
- Load path: optional `kart_lobby.json` (gameplay.rs:1043-1064); missing file gives `None` (inert); symlink and non-regular files refused; 256 KiB cap enforced before parse (gameplay.rs:1048-1058); the encoded reply is cached once in an `Arc` (gameplay.rs:1060-1062).
- The body is `LobbyNativeBody` with five tables and `deny_unknown_fields` (`kart_lobby_native.rs:148-156`).
- The inner packet is opcode 102, sub 2, with a length prefix (`kart_lobby_native.rs:569-580`); the tunnel envelope is a separate `encode_tunnel` (`kart_lobby_native.rs:583-600`).
- Truncated (<4 bytes) and trailing-byte 102/1 requests are refused in the dev branch (gameplay.rs:2302-2315).
- `tests/kart_lobby_gameplay.rs` has 3 tests, all `#[ignore]` and gated on private inputs (lines 70-157), matching "private integration" wording.
- The `kart_progress_native` and `zone_transition` tests import the production modules through `osfr_tools::` paths, not `#[path]`.
- The linked notes exist: `Research/Kart Native Lobby Codec.md`, `Research/Kart Native Progress Codec.md`, `Research/Native Zone Transition Codec.md`, `Reviews/Kart Progress and Gateway Catalogue Review.md`.

**Unsure:**
- "with unknown fields positional" (line 3): I could not map this to code. The body rejects unknown fields (`deny_unknown_fields`), and the note's own load sentence says unknown fields are refused. It may be intended wire-format wording; left unchanged.
- The pass counts and logs (`gateway-green.log` 3 passed, the two earlier red-then-green runs, `../lab/reports/.../receipt.json`, and the `../lab/references/...` package with 45 byte-identical files) are outside the repo and were not verified. The repo does show `Reviews/Delegated Racing Readiness.md:116` recording 3 passed for this gate, which is consistent.
- "The gateway adds its normal tunnel envelope": the gameplay layer returns raw inner replies (gameplay.rs:2312, 2715). I did not trace the gateway wrap, so I did not verify the "wrapped once" claim.
