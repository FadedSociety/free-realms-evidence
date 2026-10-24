<!-- fleet job=note-refresh id=Kart-Lobby-Definition-Framing status=done turns=12 usd=0.0167 tokens(read,write,in,out)=[373628, 57645, 26, 11567] model=claude-haiku-5-5 -->
# notes/Research/Kart Lobby Definition Framing.md

**Verdict:** minor drift. The byte-layout, counts, test-catalogue and community-writer claims hold at the tip. What went stale is the status framing: the Rust serializer the note calls "future" now exists and is wired into the gateway.

**Corrections:**

1. `old:` derive private synthetic serializer vectors for the future Rust builder
   `new:` derive private synthetic serializer vectors for the Rust builder, which now lives in `prototype/osfr-tools/src/kart_lobby_native.rs` (see [[Research/Kart Native Lobby Codec]])
   `why:` repo:prototype/osfr-tools/src/kart_lobby_native.rs:1-33 is a shipped codec (`decode_body`, `decode_inner`, `decode_tunnel`, `encode_body`, `encode_inner`, `encode_tunnel`, lines 342-601). repo:notes/Research/Kart Native Lobby Codec.md exists.

2. `old:` A future Rust serializer should emit the inner packet form; the gateway's tunnel wrapper supplies outer/flag/length.
   `new:` The Rust serializer exists. `kart_lobby_native::encode_inner` (`kart_lobby_native.rs:569`) emits the inner 102/2 form, and `encode_tunnel` (`:583`) adds outer/flag/length. The gateway serves it only as an opt-in reply: with `dev_tools` set, an inner 102/1 is answered from `kart_lobby.json` through `encode_inner` (`gameplay.rs:1043-1062`, `gameplay.rs:2302-2312`). Routing it as a default live 102/2 response is not done.
   `why:` repo:prototype/osfr-tools/src/kart_lobby_native.rs:569-601; repo:prototype/osfr-tools/src/gameplay.rs:1043-1062 and 2302-2312.

3. `old:` ## Synthetic vectors for the future builder
   `new:` ## Synthetic vectors for the builder
   `why:` The encoder and decoder are in the tree (see correction 2). The `lobby-minimal-kart` body hex in this note matches the test constant `MINIMAL_BODY_HEX` at repo:prototype/osfr-tools/tests/kart_lobby_native.rs:62-65 (`01000000 01000000 01000000 01000000 25000000 ec0b0000`, then four zero counts). The test's `minimal_kart_body()` (lines 38-49) is the same row: key 1, id 1, type 1, field4 37, name_id 3052. The vector sizes (40/48/55 B) also agree with the codec's layout.

**Checked and holding (no change):**
- Framing: `kart_lobby_native.rs:5-7` (`u16 opcode 102 | u16 sub 2 | i32 body_length`, `inner_length = 8 + body_length`) and `LOBBY_INNER_OPCODE`/`LOBBY_INNER_SUB` at lines 44-47.
- Row widths and table order (`kart_lobby_native.rs:10-14`, 48-57) match the note's table: games 20 B, options/values 16 B, display 16 B fixed plus bytes, settings 24 B.
- Captured counts 6/30/43/37/17 and body 2378 (`kart_lobby_native.rs:15-16`; `repo:notes/Reviews/Kart Native Lobby Codec Review.md:21-22`).
- Test catalogue: "Test Lobby Game" with NameId 3030 and Unknown 37 in the pinned community handler (`refs:Sanctuary/src/Sanctuary.Gateway/Handlers/BaseLobbyGameDefinitionPacket/LobbyGameDefinitionPacketDefinitionsRequestHandler.cs:34-35`; same in FreeRealms-Legacy and Lxzxrus). The community writer leaves four zero counts (`refs:Sanctuary/src/Sanctuary.Packet.Common/LobbyGameDefinition.cs:47-50`).
- Cited note links resolve: `Research/Kart Racing Restoration` and `Research/Go Kart Native Integration Readiness` both exist.

**Unsure:**
- `The client parser does **not** require exact consumption ... trailing bytes after the last table are ignored.` The note states this as settled. Our code says the opposite is unproven: `kart_lobby_native.rs:22-26` calls client tolerance "**not** proven" and offers a `Strict` default. `repo:notes/Reviews/Kart Lobby Independent Worker Review.md:77-78` says "tolerance is not tested". The native reading may still be right, so I did not write a correction. It should probably say "unverified" unless the Ghidra read is re-checked.
- The `lab/reports/kart-lobby-framing-20261009T145825Z/` artifacts and their sha256 values are not in the repo. `.gitignore:27-28` puts lab data in the sibling `../lab`, so I could not check the hashes or the reproducer.
- Table 4's consumer `FUN_00894b10`, the 666-byte display-order size, and the 70 blob bytes were not re-checked against the client.
