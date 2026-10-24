<!-- fleet job=guide-refresh id=Gameplay-Fishing status=done turns=21 usd=0.0237 tokens(read,write,in,out)=[800704, 64626, 44, 15146] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Fishing.md

**Verdict:** minor drift. The client-side narrative (function addresses, state machine, field tables) is outside what I can check against the Rust tip and I left it alone. The server-side "What the Rust server must do" list (lines 220-232) has drifted from `prototype/osfr-tools`. Its status is wrong in four places and one count is wrong. The generated function counts (216 = 41 `game.fishing` + 71 `minigame.fishing` + 104 `net.fishing`) match the client DB.

**Corrections:**

1. `old:` The registration response carries only 16 player-config values and 6 zone values
   `new:` The registration response carries only 16 player-config values and 5 zone values
   `why:` `repo:prototype/osfr-tools/data/content/fishing.json:35-41` lists five `zone_words`; `repo:prototype/osfr-tools/src/fishing_service.rs:1074-1080` writes that array as the zone block.

2. `old:` Answer a good cast with sub 8 to every fisherman in range
   `new:` Answer a good cast with sub 8 to the casting player (the built code returns it only in the caster's reply; it does not fan out to other fishermen in range)
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:789` pushes `bobber_reply` into the caster's `change.replies`. `repo:prototype/osfr-tools/src/gameplay.rs:2600` routes the reply back to that one connection.

3. `old:` Echo subs 5 and 7 to nearby players.
   `new:` Not built: the server does not echo sub 5 (the code says it "carries presentation only; the server does not echo it"), and the sub 7 reel-in path returns only the escape or catch replies to the caster.
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:760-762` (sub 5 comment); `repo:prototype/osfr-tools/src/fishing_service.rs:792-811` (sub 7 arm, no echo packet).

4. `old:` then drive fish with subs 10 and 18 and schools with subs 11, 13 and 12.
   `new:` then drive fish with sub 10 (built, `update_fish`), schools with sub 11 (sent on registration) and sub 12 (sent on leave and disconnect). Sub 13 (UpdateSchool) and sub 18 (SpawnFishRun) have no builder in the server, so they are not sent.
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:852`, `:860`, `:876` (sub 10); `:712-722` (sub 11); `:341`, `:379` and `:1186` (sub 12); no `Sub::UpdateSchool` or `Sub::SpawnFishRun` constructor outside `repo:prototype/osfr-tools/src/fishing.rs` (decode and enum only).

5. `old:` Validate the aim against `MinCastDistance`, `MaxCastDistance`, the target radii and the rod's reach (client text: short, greater, deepest).
   `new:` Validate the aim against the minimum and maximum cast distance only (`player_words[1]` and `player_words[2]`, currently 2 m and 35 m). Target radii and rod reach are not checked yet.
   `why:` `repo:prototype/osfr-tools/src/fishing_service.rs:1234-1248` (`validate_cast`); `repo:prototype/osfr-tools/data/content/fishing.json:16-33`.

**Checked and holding:**
- Fishing on/off via the player status flag (bit 22, `STATUS_FISHING = 0x40_0001`), set on start and cleared on end: `repo:prototype/osfr-tools/src/fishing_service.rs:55`, `:626-629`, `:666-681`.
- Sub 4 on fisherman level change: `repo:prototype/osfr-tools/src/fishing_service.rs:411-432`.
- Server-owned timers and the 50 m leash ending the round on zoning: `repo:prototype/osfr-tools/src/fishing_service.rs:55-61`, `:638-661`.
- Sub 14 result is built: `repo:prototype/osfr-tools/src/fishing_service.rs:1189`.

**Unsure:**
- The Lua line numbers (`ScriptsBase.lua` 44185 ff., 44223 ff.) were not checked line by line. `StartCasting` is at 44170 and `Ui.FindSelectedFish` at 44358, so the ranges look plausible.
- The client-side claims about the sub 3 field layouts, the sub 14 kinds and the sub 6 "never accepted inbound" rule were not re-derived. They are outside the Rust tip.
- Whether "sub 8 to every fisherman in range" is meant as a design target or a description of current behaviour. I corrected it as a status statement because the surrounding list reads as both.
