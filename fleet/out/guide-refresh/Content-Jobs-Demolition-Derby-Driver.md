<!-- fleet job=guide-refresh id=Content-Jobs-Demolition-Derby-Driver status=done turns=14 usd=0.0180 tokens(read,write,in,out)=[433736, 63318, 30, 11431] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Demolition Derby Driver.md

**Verdict:** Current apart from one misleading code claim. The note is almost entirely client-locale and wiki material, and it cites almost no repo paths, so only a few claims can be checked against our code. Those few hold except the one below.

**Corrections:**

1. `old:` packets for NPC count, player count, countdown, pickups, hits, announcer messages and the leader's crown, so the server supplies AI drivers and a config.
   `new:` packets for NPC count, player count, countdown, pickups, hits and announcer messages, so the server supplies AI drivers and a config. The server has no crown packet: the crown is a client actor and the leader is computed on the client (see [[Demo Derby]]).
   `why:` `repo:prototype/osfr-tools/src/derby.rs:70-174` lists the server-facing subtypes (3 UpdatePlayerCount, 4 UpdateNpcCount, 7 CountdownStatus, 12/13 pickups, 14-16 pickup hit and VehicleHit, 19 SetDerbyConfig, 20 AnnouncerMessage) and has no crown subtype. `grep -i crown prototype/osfr-tools/src` returns nothing. The server's only leader logic is for scoring (`derby.rs:1413-1457`, `leader_knockout_points` at `derby.rs:675`). `repo:notes/Build Guides/Gameplay/Demo Derby.md:41` and `:73` place the crown actor and leader computation in the client.

**Checked and holding:**
- The derby packet list in "Where the job levels" matches `derby.rs:70-174`, apart from the crown item above.
- The four shipped arena driver gates match `repo:prototype/osfr-tools/tests/derby_shipped_package.rs:41` ("The four arena drivers shipped by `derby_gates.json`").
- The "Demo Derby Lobby" locale 3053 matches `derby.rs:21` (`DEMO_DERBY_LOBBY_NAME_ID = 3053`).
- The text of the Crash Cup, Dalton Narrowbrow, Garrison Gold and Wildwood Derby 1000 strings exists in the locale, which supports the quoted client text (checked by text, not by id).
- Links to [[Demo Derby]], [[Kart Driver]] and the NPC zone pages resolve to files in the vault.

**Unsure:**
- `notes/Design/Build Ledger.md:109` says derby is "Built (registered, not routed)". Other evidence points the other way: `repo:notes/Autopilot/F131.md` (derby entry through the NPC menu and Close route, `derby_route` tests), `prototype/osfr-tools/tests/derby_route.rs`, and `derby_gateway.rs` (gate NPCs from `derby_gates.json`). This note does not make that routing claim, so I left it alone. The ledger row probably needs checking by whoever owns it.
- Whether the server enforces the 22-point Wildwood Derby 1000 win condition, and whether a non-member level cap exists in code. The note treats both as client or wiki facts and I did not search for either.
