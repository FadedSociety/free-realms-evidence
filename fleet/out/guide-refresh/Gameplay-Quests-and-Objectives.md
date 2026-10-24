<!-- fleet job=guide-refresh id=Gameplay-Quests-and-Objectives status=done turns=34 usd=0.0406 tokens(read,write,in,out)=[1882699, 92418, 72, 20497] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Quests and Objectives.md

**Verdict:** minor drift. One wrong packet id is repeated in three places. The other server-side claims I checked hold: the routing, the journal widths, the 47/15 limit message, the 47/14 pin, and the 45/6, 45/10 and 45/11 registrations.

**Corrections:**

1. Line 90, Selection and limit section:
   - `old:` (id 202 / `0xca`; constructor `0089bab0`)
   - `new:` (id 100 / `0x64`; constructor `0089bab0`)
   - `why:` The client dispatcher `009471a0` has `case 0x64` calling `FUN_0089bab0`, the `PacketMembershipActivation` constructor, which sets `param_1[1] = 100`. The `0xca` case in the same dispatcher is a different handler. Our encoder writes opcode 100: `repo:prototype/osfr-tools/src/game_rules.rs:294-299`, with the byte layout pinned by `repo:prototype/osfr-tools/tests/game_rules.rs:184-192`.

2. "What the Rust server must do", item 3, Login:
   - `old:` Send `PacketMembershipActivation` (id 202; it sets `player+0x464`, body not decoded here)
   - `new:` Send `PacketMembershipActivation` (id 100; it sets `player+0x464`; body is an i16 kind then an i32 member flag). Our encoder `encode_membership_activation` exists (`game_rules.rs:294`) but has no production caller; only its tests use it.
   - `why:` `repo:prototype/osfr-tools/src/game_rules.rs:294-299` and `repo:prototype/osfr-tools/tests/game_rules.rs:184-192`. A grep of `src/` and `bin/` finds no caller of `encode_membership_activation`, so the login path does not send it.

3. Open questions, "Quest-limit pair" bullet:
   - `old:` the id 202 body is not decoded.
   - `new:` the id 100 body is an i16 kind followed by an i32 member flag (our encoder, `repo:prototype/osfr-tools/src/game_rules.rs:294-299`).
   - `why:` Same evidence as correction 1. The body is partly decoded on our side.

**Unsure:**

- The "What the Rust server must do" items 6, 7, 11 and 12 tell the server to send 49/7 (add objective), 49/11 (fail objective), 49/5 (quest failed), 49/16 (end blocked), 47/1 to 47/4, 47/10 and 45/12. I found no encoder for any of these in `repo:prototype/osfr-tools/src` (outside `restoration/`). `quest_engine.rs:515-580` encodes only 49/1, 3, 4, 6, 8, 9, 10, 12, 13 and 47/15. These read as to-do guidance, not status, so I did not correct them. The team may want to know that 49/16 and 45/12 are not built.
- The Overview claim that "our native run showed '1/30'" because the server sent 30 could not be checked. No production config sets quest limits; `game_rules.rs:91-94` defaults both to `None`.
- Checked and consistent: 49/2, 49/14 and 49/15 route to `quest_engine` (`gateway.rs:500`); 47/12, 47/13 and 45/7 route to it (`gateway.rs:502-504`); 47/14 is built (`quest_journal.rs:252`, `gameplay.rs:2192`); 47/15 is sent with 1 for member and 2 for non-member (`quest_engine.rs:579`, `1576-1581`); 45/6, 45/10 and 45/11 are registered (`quest_engine.rs:2865-2886`); 45/x minigame objectives exist (`encounter.rs:2973-2978`); 209/1 then 209/2 at login (`quest_engine.rs:1302`); the journal widths of 7, 10, 3 and 9 dwords (`startup_world.rs:312-336`).
- The status ledger (`notes/Design/Build Ledger.md:90`) says "47/14 tracked-target pin not built", which contradicts the code. This is not a claim in the note, so I left it alone, but the ledger is stale.
