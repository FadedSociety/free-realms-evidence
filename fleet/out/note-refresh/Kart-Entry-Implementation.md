<!-- fleet job=note-refresh id=Kart-Entry-Implementation status=done turns=14 usd=0.0205 tokens(read,write,in,out)=[463879, 60366, 30, 16667] model=claude-haiku-5-5 -->
# notes/Research/Kart Entry Implementation.md

**Verdict:** minor drift. The module, its typed refusals, reply order, phase machine and the `13 passed / 1 ignored` count all hold at the tip. The "Lead route" section describes wiring that has since been done one layer down, and one encounter-writer claim is wrong.

**Corrections:**

1. `old:` The test target includes the source with `#[path]` until then and uses real crate imports for everything else.
   `new:` The module is already registered in `src/lib.rs` (`pub mod kart_entry;`, line 41), and the test target uses `use osfr_tools::kart_entry;` with no `#[path]` include.
   `why:` repo:prototype/osfr-tools/src/lib.rs:41; repo:prototype/osfr-tools/tests/kart_entry.rs:17

2. `old:` 3. In `gameplay.rs::handle_in_world`, before the opening/quest/combat chain, mirror the lobby gate:
   `new:` 3. Routing already exists one layer down. `KartGateway` owns the handler (`kart_gateway.rs:158`), and `KartGateway::handle` sends subtypes 9 and 2 to `handle_entry`, which calls `handle_inner` (`kart_gateway.rs:626-634`, `677-679`). `gameplay.rs` reaches it only through its `kart_entry: Option<KartGateway>` field (`gameplay.rs:201`). The snippet below is no longer the route; do not add a second `33/0` hook in `handle_in_world`:
   `why:` repo:prototype/osfr-tools/src/kart_gateway.rs:158, 626-634, 677-679; repo:prototype/osfr-tools/src/gameplay.rs:201. No `handle_in_world` call to `KartEntryHandler` exists (grep finds none in `gameplay.rs`).

3. `old:` only from the launcher's explicit dev flag (`handler.set_gate(EntryGate::Enabled)`), and call
   `new:` by `KartGateway::open` on every opened entry (`kart_gateway.rs:522-524`, `entry.set_gate(EntryGate::Enabled)`, no dev-flag check), and call
   `why:` repo:prototype/osfr-tools/src/kart_gateway.rs:522-524 (also `:353` and `:571` enable race gates the same way)

4. `old:` which hard-codes rotation `w = 1.0`
   `new:` which writes `zone.rotation` verbatim but frames it with literal `1.0` floats (after the position and after the rotation, so its layout differs from the zone codec)
   `why:` repo:prototype/osfr-tools/src/encounter.rs:3111-3133 (rotation is written from `zone.rotation` at line 3120; the literal `1.0` values are at lines 3119 and 3121); repo:prototype/osfr-tools/src/zone_transition.rs:108 (zone codec writes position then rotation with no extra floats). The claim that the rotation `w` is hard-coded to 1.0 is not what the function does.

**Unsure:**

- `lab/reports/kart-entry-repair-20261009/` (the owned artifacts table, the `red.log` and `receipt.json` evidence, and the private capture gate). The `lab/` directory does not exist at the repo tip, so these paths could not be checked. They may be private and not committed.
- The verification counts for the reused codecs (`13+9+13+9 passed; 2 ignored`). At the tip, `tests/kart_progress_native.rs` has 9 passing plus 1 ignored, `tests/zone_transition.rs` has 10 plus 1 ignored, and `tests/kart_racing.rs` has 14 with none ignored. This is a dated run log from 2026-10-09 and may be history, not a current claim, so I left it alone.
- `handler.scene_frame()` has no callers in `src/` at the tip. The scene is still carried by the gateway's own path (`gameplay.rs:1660` uses `KartGatewayState::scene()`). Whether the op31 frame should go through `scene_frame()` is not settled by the code.
- The `33/11` `400.0` value and the `33/9` word meanings come from the private capture and could not be checked here.
