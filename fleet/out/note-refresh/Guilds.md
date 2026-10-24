<!-- fleet job=note-refresh id=Guilds status=done turns=15 usd=0.0162 tokens(read,write,in,out)=[366146, 43229, 32, 14305] model=claude-haiku-5-5 -->
# notes/Research/Guilds.md

**Verdict:** badly stale. The note describes the W48 standalone state. T006 (and F273) later registered the module, routed family 129 and wired persistence, and the Scope, Checks and Open-gates sections still say otherwise. The name rules, member cap, MOTD and invite-window constants, the `GuildResultCode` keys, `guild_guid_for`, the 11-test count and the sub-opcode set (1–11, 13–16; no 12) still match the code.

**Corrections:**

1. `old:` it is not registered in the shared library or gateway.
   `new:` it is registered in the shared library (`pub mod guilds;`) and in the gateway (`#[path = "osfr_gateway/t006_guilds.rs"] mod t006_guilds;`); `tests/guilds.rs` links the library module through `osfr_tools::guilds`.
   `why:` repo:prototype/osfr-tools/src/lib.rs:28; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:42-43; repo:prototype/osfr-tools/tests/guilds.rs:5

2. `old:` The test includes the module with `#[path]`;
   `new:` The test links the library module (`use osfr_tools::{guilds, social_chat}`);
   `why:` repo:prototype/osfr-tools/tests/guilds.rs:5 (no `#[path]` in the file; the module is the library's `guilds`)

3. `old:` - Module registration, request routing, session-to-character lookup, persistence wiring and packet
   `  delivery remain lead integration work.`
   `new:` - Module registration (`src/lib.rs:28`), request routing (`src/bin/osfr-gateway.rs:2135-2136`), session-to-character lookup (`src/bin/osfr-gateway.rs:849`), persistence (`src/bin/osfr_gateway/t006_guilds.rs:38`) and packet delivery are wired by T006 (`notes/Autopilot/T006.md`); native guild-window acceptance is still open.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2135-2136, :849, :3370; repo:prototype/osfr-tools/src/bin/osfr_gateway/t006_guilds.rs:38, :137 (`route_guild`)

4. `old:` - Full roster serialization (129/22) and member-status packet serialization (129/17) remain open;
   `new:` - Full roster serialization (129/22) and member-status packet serialization (129/17) are encoded (`full_data_message`, `member_status_message`) but not checked against native acceptance;
   `why:` repo:prototype/osfr-tools/src/guilds.rs:1118 and :1168

5. `old:` the module returns typed notices and roster data only.
   `new:` the module also returns encoded 129/22 and 129/17 bodies, which the gateway sends; no native acceptance was run.
   `why:` repo:prototype/osfr-tools/src/guilds.rs:1118, :1168; repo:prototype/osfr-tools/src/bin/osfr_gateway/t006_guilds.rs:137

6. `old:` The client `GuildDataFullPacket` body remains too incomplete to safely encode a full native
   `new:` `full_data_message` (`src/guilds.rs:1118`) encodes the 129/22 roster body from the recovered layout; the dwords the client never recovered are written as zero, and no native acceptance was run. A full native
   `why:` repo:prototype/osfr-tools/src/guilds.rs:1118; repo:notes/Autopilot/T006.md:99-101 (the reader-shaped fields written as zero/repeated)

7. `old:` Guild names are trimmed, 3-32 Unicode characters, and limited to letters, digits, spaces, hyphens
   `new:` Guild names are trimmed, 3-32 Unicode characters and at most 96 UTF-8 bytes, with no leading or repeated spaces, and limited to letters, digits, spaces, hyphens
   `why:` repo:prototype/osfr-tools/src/guilds.rs:2136-2155 (`name.len() > 96`, `index == 0 || previous_space`)

8. `old:` MOTD is limited locally to 1,024 UTF-8 bytes.
   `new:` MOTD is limited locally to 1,024 UTF-8 bytes and refuses control characters.
   `why:` repo:prototype/osfr-tools/src/guilds.rs:789 (`motd.len() > MAX_MOTD_BYTES || motd.chars().any(char::is_control)`)

**Unsure:**
- Lines 120-121: "its small test-only replacement shim stands in for `character_store::replace_bytes`" and "the production module calls the shared atomic replacement helper". I found no `replace_bytes` call in `src/guilds.rs`; the T006 notes place the atomic write in `commit_outcome` / `t006_guilds.rs`. I did not confirm the test shim, so I left it alone.
- Line 130, "No original guild packet capture, server guild implementation ... exists": if "server guild implementation" means our code, it is now false (T006 built one). I read it as "original", so I left it.
- The Create/Delete "unknown" sender labels and the Rename "parsed only" row were not checked (no native-map lookup in scope). T006 says rename is refused with `GuildCantRenameAtThisTime`; that does not contradict "out of scope", so no change.
- Outside this note: `notes/Design/Build Ledger.md:46` still says guilds are "Not routed", which the T006 routing evidence contradicts. That row belongs to the ledger, not this note.
