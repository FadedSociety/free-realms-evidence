<!-- fleet job=note-refresh id=Housing-Path status=done turns=21 usd=0.0253 tokens(read,write,in,out)=[732319, 62178, 44, 20331] model=claude-haiku-5-5 -->
# notes/Research/Housing Path.md

**Verdict:** badly stale in "Current integration blockers" and the Slice 0 step 3 text. Almost every integration claim there describes the tree before the 2026-10-20 housing slice 1 (`gameplay/housing.rs`). The asset arithmetic is internally consistent: the per-scene missing counts sum to 1,273, and the `.gcnk`/`.dds` splits match the 17-scene table. Those asset numbers could not be re-run here (the `lab/` tree is not in this checkout).

**Corrections:**

1. `old:` "- The client list path (`127/23`, `127/14`, `127/39`) is not implemented by
  the service, so a UI-driven My Houses screen cannot yet discover the test
  lot."
   `new:` "- The client list path is implemented: `127/23` grants the starter lot once and answers with the `127/39` owner list, and `127/14` lists one owner's houses. A UI-driven My Houses screen can discover the test lot."
   `why:` repo:prototype/osfr-tools/src/housing_service.rs:1410-1411 (127/23 grant plus 127/39 list), repo:prototype/osfr-tools/src/housing_service.rs:1432 (127/14); `REPLY_INSTANCE_LIST` = 39 at housing_service.rs:82.

2. `old:` "3. Route `127/23` to a house-list response, then `127/19` for the single test
   house. The list response is needed for a UI-driven flow and is not present
   in the current service."
   `new:` "3. Route `127/23` to the house-list response (already emitted by the service), then `127/19` for the single test house."
   `why:` repo:prototype/osfr-tools/src/housing_service.rs:1410-1411 and :1432.

3. `old:` "- `gateway.rs::application_handler` has no family 127 branch. Its final
  fall-through sends family 127 to `gameplay.handle_in_world`, which has no
  housing branch; a probe from the prior housing review saw zero replies and
  `changed=false`."
   `new:` "- `gateway.rs::application_handler` has no family 127 branch. Its final fall-through sends family 127 to `gameplay.handle_in_world`, which dispatches to `handle_housing` (family 127 prefix check) before the mount, matchmaking and soccer handlers."
   `why:` repo:prototype/osfr-tools/src/gateway.rs:464-553 (no `127` arm; `_ => "gameplay.handle_in_world"` at :553); repo:prototype/osfr-tools/src/gameplay.rs:2239-2240 (`handle_housing`); repo:prototype/osfr-tools/src/gameplay/housing.rs:86 (`FAMILY = [127, 0]` prefix check). The "zero replies" probe is historical and no longer describes the tip.

4. `old:` "- `Gameplay` has no housing service field. `HousingService` has a tested
  callable API, but no production caller."
   `new:` "- `Gameplay` holds the housing session: `housing: Option<housing::HousingSession>` owns a `HousingService`. `HousingService` is called from `handle_housing` on every family 127 request."
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:262 (field); repo:prototype/osfr-tools/src/gameplay/housing.rs:18-19 (`service: HousingService`) and :94-96 (`session.service.handle(...)`).

5. `old:` "- `game_store.rs` has an optional housing payload and load/save helpers, but
  the gameplay snapshot does not carry the service state."
   `new:` "- `game_store.rs` has an optional housing payload and load/save helpers. The gameplay snapshot carries the service state (`GameplayState.housing`), restored on load."
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:139 (`pub housing: Option<HousingServiceState>`), :607 (restore), :1147-1151 (`HousingSession::load`), :1377 (`housing: self.housing.as_ref().and_then(|h| h.state())`).

6. `old:` "- `HousingContent::bundled()` exists but `osfr-gateway` does not load
  `houses.json` or construct a `HousingService` for a login."
   `new:` "- `HousingContent::bundled()` exists. The gateway loads `houses.json` from the `--content` directory on login: `Gameplay::load(content, ...)` builds a `HousingSession` (which constructs the `HousingService`) when the file is present, and family 127 stays dormant without it."
   `why:` repo:prototype/osfr-tools/src/gateway.rs:817 and :1080 (`Gameplay::load(content/directory, ...)`); repo:prototype/osfr-tools/src/gameplay.rs:1147-1151; repo:prototype/osfr-tools/src/gameplay/housing.rs:6-7 and :36-50.

7. `old:` "The modules are registered but not in the production route:"
   `new:` "The housing modules are routed for family 127 through gameplay, but the slice is partial:"
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:2239; repo:prototype/osfr-tools/src/gameplay/housing.rs:1-4 (slice 1: 127/23, 127/14, 127/19, 127/10 bound to the session).

8. `old:` "1. Route the already-built housing service through the gateway and use one"
   `new:` "1. Keep the already-built housing service on its current route (family 127 reaches `handle_housing` through gameplay, not a gateway arm) and use one"
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:2239; repo:prototype/osfr-tools/src/gateway.rs:553 (no 127 arm). The "route it" step is already partly done, so the wording should not imply it is missing.

**Unsure:**

- "The current 21 enabled property rows" (line ~366) and "enabled_lots=21" (Evidence commands). A grep for `"enabled": true` in `repo:prototype/osfr-tools/data/content/houses.json` returned 20 lines (58 to 1167). The file has at least 31 `property_id` records. The note's 21 comes from the checker run dated 2026-10-17, which may count differently. I could not settle the count from the tip.
- The `lab/` asset claims (per-scene `.gcnk`/`.dds` counts, `sg_random_encounter_clearing` "4 of 4 `.gcnk`, 23 of 25 `.dds`", "16 of 64" tile textures for Seaside). `lab/` is not reachable from this checkout; the sums are internally consistent.
- `scripts/check-asset-delivery-scenes.py` exists at `repo:scripts/check-asset-delivery-scenes.py`; the note's "run from `project/`" path could not be checked.
- The `127/28` question: the enter path does emit `REPLY_INSTANCE_DATA` = 28 (`repo:prototype/osfr-tools/src/housing_service.rs:81`, `:1384`), so the note's "keep it in the first implementation" is already satisfied. The note's statement that 28 is "not present in the captured fragment" is about the capture and is not contradicted.
- Not this note, but related: `notes/Design/Build Ledger.md:109` still says housing is "registered, not routed"; the ledger row needs the same update.
