<!-- fleet job=note-refresh id=Fishing-Service status=done turns=25 usd=0.0284 tokens(read,write,in,out)=[997106, 64712, 52, 20764] model=claude-haiku-5-5 -->
# notes/Research/Fishing Service.md

**Verdict:** badly stale. The file, API and content claims mostly hold, but the scope, interface and integration statements describe a state before the service was wired into gameplay (W160 and later). Those are the misleading parts.

**Corrections:**

1. `old:` This implements a callable service seam. It does
   `new:` This started as a callable service seam and is now wired into gameplay: NPC entry calls `FishingService::enter`, and every in-world packet goes through `route`. It does
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:925 (`self.fishing.enter(`); repo:prototype/osfr-tools/src/gameplay.rs:2600 (`.route(character.guid, inner, now_ms, ...)`); repo:prototype/osfr-tools/src/fishing_service.rs:17-29 (module doc, ordinary entry W160); repo:notes/Design/Build Ledger.md:107 ("Wired, never run natively").

2. `old:` need lead-owned integration.
   `new:` need only the operator's exact area/game/encounter choice confirmed. The gateway has no fishing route (`osfr-gateway.rs` only reads `HOUR_WINDOW_MS`), but the activation flag is already emitted by `route`: `STATUS_FISHING` on start and `STATUS_NORMAL` on any end (fishing_service.rs:626-629, 676-678). Gameplay calls `route` from gameplay.rs:2600, and gameplay.rs:1868 calls `supervise`.
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:55-56, 600-634, 666-681; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1794 (only the HOUR_WINDOW_MS constant is used there).

3. `old:` 2. Route the shared minigame lifecycle to `handle_minigame_lifecycle`.
   `new:` 2. Route the shared minigame lifecycle through `route`, which calls `handle_minigame_lifecycle` for 39/5, 39/6 and 41/109 and then `mark_started` (sends the 39/17 status when the round starts). Calling the lower-level methods directly still works.
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:326-354 and 611-633.

4. `old:` Every server-selected value lives in `data/content/fishing.json` with a source tag.
   `new:` Every server-selected timing, probability, registration, school, species and weight value lives in `data/content/fishing.json` with a source tag. The per-grade payout rows, the optional catch cap (disabled by default) and the item-id table live in `data/content/fishing_spots.json`.
   `why:` repo:prototype/osfr-tools/data/content/fishing_spots.json:4-34 (`payout.by_grade`, `catch_cap.enabled: false`) and :91 (`items`); repo:prototype/osfr-tools/src/fishing_service.rs:17-20 and 112-116.

5. `old:` layer must call `bind_item_definition(species_key, size_grade, id)` first.
   `new:` layer must call `bind_item_definition(species_key, size_grade, id)` first on the low-level `begin` path. The ordinary `enter` path binds every non-zero id from the `items` table in `fishing_spots.json` itself. The client still does not supply these ids.
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:584-591 (`enter` loops over `spots.items` and calls `bind_item_definition`); repo:prototype/osfr-tools/data/content/fishing_spots.json:91-97.

6. `old:` `QuestEvent::CollectItem` for the granted item definition and quantity one;
   `new:` `QuestEvent::CollectItem` for the granted item definition and quantity one, plus `QuestEvent::FinishMinigame { minigame_id: game_id }` (one paid catch is one minigame completion);
   `why:` repo:prototype/osfr-tools/src/fishing_service.rs:1007-1014.

**Checked and holding (no change):** `src/fishing_service.rs` and `tests/fishing_service.rs` exist; `lib.rs:22` exposes `pub mod fishing_service`; `begin` signature matches (fishing_service.rs:222-230); `handle_minigame_lifecycle`, `mark_started`, `disconnect` (drops state, returns sub-12 despawns, no reward), `set_lure` and `tick` exist; cast distance is validated against the anchor (`validate_cast`, fishing_service.rs:1234-1248); a bad reel before hook or after the deadline escapes with a kind-0 result (`escape`, fishing_service.rs:870-883); a valid hooked reel settles a kind-5 result with `apply_grant` staged on a clone and committed only on success (fishing_service.rs:941-1018); reply order is sub 14, then reward packets; `fishing.json` has 6 areas, 40 species and 13 lures, with catch_chance 1.0 and line_snap_chance 0.0 (fishing.json:7-12; the species and lure counts were confirmed from the block layout and the 13 `bonus_percent` entries); the 10% lure bonus is applied to listed weights (fishing_service.rs:1263-1267).

**Unsure:**
- The verification record (note lines 176-184) says the W34 test run is "blocked by shared compile errors" in `src/soccer_match.rs`. That file no longer contains `unknown_word`; it uses `state_counter` and `steering_vector` (soccer_match.rs:262-334). I could not confirm whether the build compiles now, so I did not change the record. It reads as a historical run log.
- The client-side addresses and byte-count claims (`00b6a400`, `00b66be0`, `00cd0150`, and so on) were not re-verified against `client_sql`.
- Notes/Autopilot shows later fishing tasks (F120, F153, F186, F210, F270, T029, T244) that changed `fishing_service.rs` heavily. This note's line counts and the 1623-line file were not compared against those reports.
