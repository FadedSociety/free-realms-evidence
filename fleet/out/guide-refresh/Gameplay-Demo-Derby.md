<!-- fleet job=guide-refresh id=Gameplay-Demo-Derby status=nothing_found turns=25 usd=0.0358 tokens(read,write,in,out)=[1392498, 98280, 54, 19081] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Demo Derby.md

**Verdict:** current. I found no claim about our code that is now false. I read about 60% of the note (lines 1–275 of 704, plus the generated-function summary) and stopped at the tool budget, so the back half (generated function tables, video and wiki evidence) is only partly checked.

**Corrections:** none.

**What I checked and found consistent with the tip:**
- Network table (lines 163–180): every subtype's direction matches `SUBTYPE_SPECS` in `prototype/osfr-tools/src/derby.rs:54-175`, and the sender/reader addresses listed there (`009f1550`, `009f1680`, `009f1790`, `009ee190`, `009eeeb0`, and others) match the same spec table.
- Active status bit 11 (line 195): `DERBY_ACTIVE_STATUS_BIT = 11` at `derby.rs:24`. The derby status word uses the kart's 35/20 carrier (`derby_gateway.rs:366`, `kart_gateway::player_status`), which fits the note's "R: use a 35/20 player update".
- Server flow in the "What the Rust server must do" list: 34/1 values 3 to 11 in order (`derby.rs:1166-1269`, `1662`); countdown starts at 4 (`derby.rs:1241`); 34/19 and 34/3/4 before 34/10 (`derby.rs:1131-1167`); NPC fill to eight, solo allowed (`derby.rs:1171-1175`); points 2 and 3 for the leader, with a loss of 1 (`derby.rs:674-728`, `1423-1437`); 34/20 kinds 2 and 1 (`derby.rs:1444-1460`); kinds 0 for shield, attack and ultimate pickups (`derby.rs:1550-1558`); 34/17 expiry (`derby.rs:1722`); a score target or time limit (`derby.rs:1463-1469`, `1724-1730`); abort with no humans (`derby.rs:1744`).
- Generated counts (line 253): the label table gives game.derby 124 and net.derby 112, with confirmed 128, likely 59, speculative 18 and unknown 31. These match the 236 total.
- Client addresses in the key-functions and lifecycle tables: the 33 addresses I checked in the client `fn` table have the names and roles the note gives (for example `009f39b0`, `009f1b80`, `009f2d90`, `009f22c0`, `00c659b0`, `0105f170`).

**Unsure:**
1. Step 10 (line 204) says to "grant rewards and job experience". This is prescriptive, and it is now partly built: T219 added a flat completion payout (`derby_gateway.rs:448-476`, `gameplay/derby_session.rs:198`), default 0 coins and 0 XP. The note's "Reward amounts are unknown (R)" still holds, so I did not mark it false.
2. Step 7 (line 201) says to "send 34/13 when taken and respawn later". `pickup_hit` sends `DestroyPickup` (`derby.rs:1537`), but I found no pickup respawn code. This is a to-do, not a status claim, so I left it.
3. The Build Ledger (`notes/Design/Build Ledger.md:109`) calls derby "Built (registered, not routed)". `derby_route` tests and F131 report the NPC menu route as working, so the ledger row may be stale. It is outside this note, so it is not a correction here.
4. Line 253 "Network-linked (wire): 63" matches the 63 `net.derby` confirmed rows, but I did not verify the `wire` field itself.
