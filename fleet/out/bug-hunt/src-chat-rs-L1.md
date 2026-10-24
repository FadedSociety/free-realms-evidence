<!-- fleet job=bug-hunt id=src-chat-rs-L1 status=nothing_found turns=5 usd=0.0054 tokens(read,write,in,out)=[41508, 22698, 12, 4257] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/chat.rs lines 1-152 of 152

No defects in `prototype/osfr-tools/src/chat.rs` lines 1-152 that can be reached from a client packet.

What I checked:

- **Bounds and panics (`Reader`, lines 13-33):** every read goes through `take`, which uses `checked_add` and `slice.get`. The `try_into().unwrap()` calls at lines 21 and 45 are safe because `take(4)` and `take(2)` return exactly that many bytes or an error. The string length is checked against `limit` (128 for names, 2048 for the message) before `take`, so a client-supplied u32 cannot cause an oversized allocation or slice.
- **Layout (`request`, lines 37-63):** the field sequence matches the pinned reference `PacketChat.TryDeserialize` (refs `Lxzxrus-Free-Realms-Server/.../PacketChat.cs`). Channel is an `i16` enum, GUIDs are two u64s (16 bytes), names are 12 bytes plus two strings, then Position (16) + GuildGuid (8) + LanguageId (4), with AreaNameId only for WorldArea. `ChatChannel.WorldArea` is the only channel that carries the extra 4 bytes, and the window's `channel == 8` test matches it. Line 59 requires the packet to be consumed exactly, so trailing bytes are rejected.
- **Trust (`request` ignores `_guid`):** only the text is returned. The GUIDs and names are consumed and discarded, so a client cannot choose the sender, recipient, or identity. The caller (`osfr-gateway.rs:1895`) uses only the text.
- **Developer commands:** `realm ` text reaches the developer path, but `gameplay.rs:3675` `developer_command_denied` gates it by account role. That lies outside my window and is not a defect here.
- **`system` (lines 82-92):** escaping order is correct (`&` first), and the length is a u32 cast of a server-built string, not client-controlled.
- **`local_request` (lines 67-80):** it is test/tooling-only and its `as u32` cast is not reachable from a client.

The `channel > 10` bound is a loose range check, not a safety defect. I did not find any mutation-before-error sequence, unbounded growth, or logic contradiction in the window.
