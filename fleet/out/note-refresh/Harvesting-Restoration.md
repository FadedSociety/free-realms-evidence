<!-- fleet job=note-refresh id=Harvesting-Restoration status=done turns=15 usd=0.0179 tokens(read,write,in,out)=[390884, 52346, 32, 14923] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Restoration.md

**Verdict:** badly stale. The module, tests and contract names still exist, but the integration status, the reconstructed board/quota numbers, the profile binding and the goal tile values were all changed after this note was written.

**Corrections:**

1. `old:` Nothing is registered in `lib.rs`, no gateway/content integration was performed and no native client run happened: the shared game window is lead-controlled.
   `new:` `harvesting` is registered in `lib.rs` and bound by the gateway as an opt-in Harvesting111 candidate under Chef45. A native baseline run was captured (`client-baseline-20261009T202011Z`), but whole-round native acceptance remains open because the shared game window is lead-controlled.
   `why:` repo:prototype/osfr-tools/src/lib.rs:29 (`pub mod harvesting;`); repo:prototype/osfr-tools/src/gameplay.rs:977-992 (`Type8Engine::load` with `HARVESTING_GAME_ID`, Chef profile check); repo:prototype/osfr-tools/src/harvesting.rs:85-87 (native run `client-baseline-20261009T202011Z`); repo:notes/Design/Build Ledger.md:105 ("native round unverified").

2. `old:` No native client run and no gateway/door binding: harvesting cannot yet be launched in the actual client, and `harvesting.rs` is not registered in `lib.rs` (root integration).
   `new:` Harvesting is gateway-bound and registered (`lib.rs` and `gameplay.rs`, opt-in Chef45 candidate). Open gates: whole-round native acceptance (type-8 `39/5` start, `39/14` payloads, `39/17`, `39/19`) and recovery of the original `Minigames/MatchThree/*.txt` server tables.
   `why:` repo:prototype/osfr-tools/src/lib.rs:29; repo:prototype/osfr-tools/src/gameplay.rs:977-999; repo:prototype/osfr-tools/src/harvesting.rs:85-87.

3. `old:` The module encodes a 10x10 staircase shape (76 playable cells, rows 4/6/8/10/10/10/10/8/6/4) from the screenshot, 180 seconds, quota 15 tiles per goal with 5 tiles per bundle, wildcard 5%, collectable 12%, no blockers or powerups, and one bundle granted per completed goal.
   `new:` The module emits an 11x11 padded grid: a 10x9 playable rectangle (`RECONSTRUCTED_PLAYABLE_ROWS` = 9, `RECONSTRUCTED_BORDER` = 1) plus one dropzone row. The screenshot's 4/6/8/10/10/10/10/8/6/4 staircase is kept only as the unlaunched `diamond_shape` record. Values: 120 seconds, quota 25 tiles per goal, 5 tiles per bundle, wildcard 5%, collectable 0%, no blockers or powerups, one bundle per completed cluster.
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:762-798 (board, duration, quota, percent constants); repo:prototype/osfr-tools/src/harvesting.rs:800-809 (`RULE_NOTICE` fidelity gap); repo:prototype/osfr-tools/src/harvesting.rs:872-921 (`diamond_shape` vs `padded_engine_shape`); repo:prototype/osfr-tools/src/harvesting.rs:999-1010 (`collectable: Vec::new()`, `meter_id`, `reconstructed_rules`).

4. `old:` `profile_id` mirrors `game_id` because no job-profile evidence exists;
   `new:` `profile_id` is the recovered Chef binding `CHEF_PROFILE_ID = 45` (a local binding; the original profile gate is still uncaptured), and `validate_content` refuses any other profile.
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:62-64 (`CHEF_PROFILE_ID`), :1026 (`profile_id: CHEF_PROFILE_ID`), :1070-1075 (validate refuses other profiles).

5. `old:` Goal tiles are `601+slot` per the original `TILE_COLLECTABLE + spawn type`;
   `new:` Goal tiles are selectable produce values `400 + type` (`TILE_SELECTABLE_CATEGORY` = 400; region 111 uses 411/413/416/403). The 600 block is not used, because the client ships no `farmingValue60x` names for it;
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:81-93 (selectable category and `FIRST_PRODUCE_VALUE`), :82-88 (`TILE_COLLECTABLE_CATEGORY` never used by harvesting), :941-973 (`board_spec` goal and tile values).

6. `old:` undefined harvesting variants emit empty goals/outputs rather than invented produce.
   `new:` undefined harvesting variants (58 and 110/112/114/116/118/120/217) refuse to build a board or content at all (`board_spec` and `content` return `HarvestError`), rather than emitting empty goals/outputs.
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:926-929 (doc: "refuse to propose a board at all"), :976-987 (`board_spec` error for non-region ids), :1016-1022 (`content` error).

7. `old:` `content(game_id)` returns `{schema_version, game_id, profile_id, name_id, description_id, icon_id, spec}`
   `new:` `content(game_id)` returns `{schema_version, game_id, profile_id, name_id, description_id, icon_id, preload_file, launch_movie, spec}`. `preload_file` is `FarmingAssets.txt` and `launch_movie` is `game_farming.gfx`.
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:1023-1033 (`HarvestContent` literal); :43, :47 (the two constants).

**Unsure:**

- Artifact SHA-256 values (module `cdb451aefada…`, tests `b6fa910a…`) could not be recomputed with the tools available. `harvesting.rs` has changed since the note was written: repo:notes/Research/Harvesting Native Launch Preflight.md:70 and repo:notes/Research/Harvesting Native Mouse Driver.md:17 cite different revisions (`272711da0e6b72fc…`, `4e5196ba35ab99c6…`). Treat the note's full hashes as stale and recompute them before citing.
- `old:` "`harvesting.rs` is self-contained ... no `crate::` imports" holds: there are no `crate::` matches in `harvesting.rs`. However, the file now declares `#[path = "harvesting_lifecycle.rs"] pub mod lifecycle;` (harvesting.rs:33-34). The note's claim that the module "does not contain a board engine, network envelope, tick loop or inventory transaction" was not checked against `harvesting_lifecycle.rs`, which may hold grant or runtime logic.
- Test count: 17 `#[test]` functions in `tests/harvesting.rs`, which matches "17 tests". Pass/fail status was not re-run.
- Client-side `ConfigServer.GAME_ID=60`, the Lakesfield screenshot and the wiki hash are outside the repo and were not checked.
- The `rule_notice` and `reconstructed_rules=true` claims hold (harvesting.rs:800, :1011), but the note's phrase that "the tests assert both" was not verified.
