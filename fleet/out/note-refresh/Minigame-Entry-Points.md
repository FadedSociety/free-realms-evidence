<!-- fleet job=note-refresh id=Minigame-Entry-Points status=done turns=9 usd=0.0148 tokens(read,write,in,out)=[193977, 55105, 20, 11842] model=claude-haiku-5-5 -->
# notes/Research/Minigame Entry Points.md

**Verdict:** badly stale on the derby side. The kart gate list and the 12 m reach match the tip, but the note's central derby claim (no package ships, so no driver offers the derby) is false now that `derby_entry.json` and `derby_gates.json` are in `data/content`.

**Corrections:**

1. `old:` The shipped package has **no** `derby_entry.json`, so `DerbyGateway::load` returns `None` and
   `new:` The shipped package includes `derby_entry.json`, so `DerbyGateway::load` returns `Some` and the four arena drivers offer the derby from the NPC menu.
   `why:` `repo:prototype/osfr-tools/data/content/derby_entry.json:1-76` exists; `repo:prototype/osfr-tools/src/derby_gateway.rs:194-198` loads it; `repo:prototype/osfr-tools/src/gameplay.rs:1075-1077` passes `derby_gates.json` to `set_derby_gates`.

2. `old:` no driver offers the derby today (the existing dormant-content rule).
   `new:` the derby is live through the shipped package (T313 tests the playable route from the four drivers); the dormant-content rule applies only when an operator removes `derby_entry.json`.
   `why:` `repo:prototype/osfr-tools/tests/derby_shipped_package.rs:1-17` (the shipped package is playable from the four arena drivers); `repo:prototype/osfr-tools/src/derby_gateway.rs:191-193` (absent content leaves the route disabled).

3. `old:` the client arena assets and the recovered type-11 lifecycle exist, but the vehicle/rule values are unrecovered.
   `new:` the client arena assets and the type-11 lifecycle exist; the vehicle definition is the captured `ReadVehicleDefinition` bytes, and the rule values are reconstructed (R) in `derby_entry.json`.
   `why:` `repo:prototype/osfr-tools/tests/derby_shipped_package.rs:3-13`.

4. `old:` No derby content package ships, so the four derby drivers correctly offer nothing until an operator
   `new:` The derby package ships (`derby_entry.json` and `derby_gates.json`), so the four derby drivers offer the derby from the NPC menu. Nothing is missing for entry.
   `why:` `repo:prototype/osfr-tools/data/content/derby_entry.json`, `repo:prototype/osfr-tools/data/content/derby_gates.json`, `repo:prototype/osfr-tools/tests/derby_shipped_package.rs:12-13`.

5. `old:` adds `derby_entry.json`.
   `new:` (delete this line; the package is already in the tree).
   `why:` as in correction 4. The "Open gaps" bullet is now wrong in full.

Checked and still true (no change): `kart_gates.json` lists the five kart NPCs, including Johnny Thunder (9500000911) and Spud Edgins (9500000630) (`repo:prototype/osfr-tools/data/content/kart_gates.json:3-10`); `derby_gates.json` has `menu_string_id` 3053 and the four derby ids (`repo:prototype/osfr-tools/data/content/derby_gates.json:3-9`); the 12 m NPC interaction reach (`repo:prototype/osfr-tools/src/npc_interaction.rs:52`); the 3052 "Kart Race Lobby" label (`repo:prototype/osfr-tools/src/kart_racing.rs:60-61`); `begin_kart_race` in `repo:prototype/osfr-tools/src/gameplay/npc.rs:862`; `begin_derby` in `repo:prototype/osfr-tools/src/gameplay/derby_session.rs:100`; `src/activity_portal.rs` lists battles, soccer and chess only, and not races (`repo:prototype/osfr-tools/src/activity_portal.rs:39-45`); the kart scene `sg_kt_track` is the one scene used by the kart tests (`repo:prototype/osfr-tools/tests/kart_gateway.rs:58`).

**Unsure:**

- The note says the T221 entry test package sets completion rewards to 0 (`repo:prototype/osfr-tools/src/gameplay/s15_npc_transactions.rs:197-198`). That is true for the fixture. But the shipped `derby_entry.json` pays 25 coins and 10 XP (`repo:prototype/osfr-tools/tests/derby_shipped_package.rs:12`, `:861-862`). I did not verify the shipped values in the JSON bytes, so the note should not imply the shipped payout is 0.
- The Build Ledger row "Soccer, chess, derby, housing, pets | Built (registered, not routed)" (`repo:notes/Design/Build Ledger.md:109`) may also be stale for derby. It is outside this note, so I did not change it.
- The claim that the content test asserts click identity and emits `NpcVisibility` actors (lines 96-98) and the 25 m test reach (line 119) were not checked.
