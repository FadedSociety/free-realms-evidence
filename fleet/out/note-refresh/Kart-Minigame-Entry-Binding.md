<!-- fleet job=note-refresh id=Kart-Minigame-Entry-Binding status=done turns=13 usd=0.0155 tokens(read,write,in,out)=[227211, 42654, 28, 15759] model=claude-haiku-5-5 -->
# notes/Research/Kart Minigame Entry Binding.md

**Verdict:** badly stale. The central claim, that `39/23` is a generic status/teardown reached through `FUN_00ba74d0` case 0x17, is false. The tip's own notes already correct it. The `soccer.rs` and "no op39 serializer" claims are also false. The lab report files it cites are not in the repo.

**Corrections:**

1. old: `` `BaseMiniGamePacket` value-23 status/teardown that releases the existing
minigame UI object and fires flash/script events. ``
new: `` `BaseMiniGamePacket` value-23 message: the `MiniGameKnockOutPacket` (two i32 knockout counters), not a vehicle-race or teardown message. ``
why: `repo:prototype/osfr-tools/src/restoration/piece_016.rs:18` (`39/23` is `i32 CurrentKnockouts | i32 MaxKnockouts`); `repo:notes/Native Map/Shards/S0272 009b7660-009bd590.md:218` and `repo:notes/Native Map/Systems/net.minigame.md:51` (`009b87a0` HandleMiniGameKnockOut). `client_sql` fn `009b87a0` is the 39/23 handler.

2. old: `Native: dispatcher `FUN_00ba74d0` case 0x17 (pseudocode 1585457-1585503)`
new: `Native: `FUN_00ba74d0` is the family-33 VehicleRaceProcessor receive handler, so its case 0x17 is `33/23` (BoostAwardResponse, ctor `FUN_00b99c40`), not this message. The `39/23` handler is `FUN_009b87a0`.`
why: `repo:notes/Native Map/Shards/S0364 00ba74d0-00bac070.md:11` (00ba74d0 is VehicleRaceProcessor::vftable[19]) and `:25` (the 39/23 attribution "must not be applied"); `repo:notes/Research/Kart Entry Register Prerequisites.md:159-168` (the same correction, 33/23 vs 39/23); `repo:notes/Reviews/Kart Playable Integration.md:68`. `client_sql` fn `00ba74d0` is the 33 dispatcher.

3. old: `So `39/23` is a generic mini-game status/close message (value 23),`
new: `So `39/23` is a mini-game knockout message (`MiniGameKnockOutPacket`, value 23),`
why: `repo:prototype/osfr-tools/src/restoration/piece_016.rs:18`; `repo:notes/Build Guides/Gameplay/Kart Racing.md:135` ("39/23 is a mini-game knockout message, not 33/23").

4. old: `(idempotent; they only tear down a stale mini-game UI)`
new: `(knockout counters 0/0 with ids -1/-1/-1; they tear nothing down)`
why: `repo:notes/Research/Pieces/016 Minigame loss and retry.md:46-50` (ids `-1/-1/-1`, counter `0/0`); `repo:notes/Native Map/Systems/net.minigame.md:51` (the handler only forwards counters to the HUD).

5. old: `and `soccer.rs`'s `MINIGAME_ID = 42``
new: `and the `soccer.rs` pattern (it has no `MINIGAME_ID` constant; the only `MINIGAME_ID = 42` text is a basis string in `scripts/pieces/piece_015.py:507`)`
why: search of `prototype/osfr-tools/src/soccer.rs` for `MINIGAME|\b42\b` finds only `SetSoccerPlayerOneTimeStats { stats: [f32; 42] }` (soccer.rs:214); no `MINIGAME_ID` exists anywhere under `prototype/`.

6. old: `pattern; no op39 serializer exists in the crate today, so none was assumed.`
new: `pattern. op39 serializers do exist in the crate (`kart_gateway.rs:671` builds a 39/17 start frame; `kart_gateway.rs:449` accepts the 39/7 close; many `vec![39, 0, sub]` builders), and the 39/23 layout is documented in `restoration/piece_016.rs:18`.`
why: `repo:prototype/osfr-tools/src/kart_gateway.rs:447-449, 668-675`; `repo:prototype/osfr-tools/src/cooking.rs:936`; `repo:prototype/osfr-tools/src/restoration/piece_016.rs:18`.

**Checked and holding:** `kart_racing.rs` speedway id 39 / poi 39 (`kart_racing.rs:116-118`); the `kart_lobby_native.rs` 102/2 codec (`kart_lobby_native.rs:45-47`); "the current root has no speedway op150/147/57 content" (the POI reply encoder exists in `restoration/piece_077.rs:320`, but no speedway row turns up in it).

**Unsure:**
- The cited `lab/reports/kart-minigame-entry-20261009/` probe and `pre-register-window.json`, and the `lab/runs/` v2 run. The repo tip has no `lab/` directory, so I could not check the window table or the "v2 sends only 41/114 + 41/2 + op14" claim.
- The "69 ms later" register timing and the 37.x timestamps. These come from captures, not code.
- The `150/147/57` definition-block requirement. The tip has no op150 or op147 content; op57 is a POI reply encoder (`restoration/piece_077.rs:320`), so I could not confirm the blocker claim either way.
