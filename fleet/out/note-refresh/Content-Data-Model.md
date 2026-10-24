<!-- fleet job=note-refresh id=Content-Data-Model status=done turns=15 usd=0.0183 tokens(read,write,in,out)=[464829, 61242, 32, 12018] model=claude-haiku-5-5 -->
# notes/Research/Content Data Model.md

**Verdict:** minor drift. The schema, file list, record fields, loader checks and startup citations hold. One closing limit is false: the schema is registered and has production consumers. The source-tag list is also incomplete.

**Corrections:**

1. `old:` The schema is not registered in shared `lib.rs` and has no production consumer yet; lead integration and gameplay/native gates remain separate.
   `new:` The schema is registered in shared `lib.rs` (`pub mod content;`) and has production consumers: `ContentDb` is imported and indexed by `World` (`World::new` takes a `ContentDb`; `world.rs` imports `content::{ContentDb, ...}`), the quest engine loads `Quest` and `Job` files through `content::VersionedFile` and `SCHEMA_VERSION`, and `Gateway::runtime_zone` builds `content::Zone`. Gameplay and native gates remain separate.
   `why:` repo:prototype/osfr-tools/src/lib.rs:14 (`pub mod content;`); repo:prototype/osfr-tools/src/world.rs:7 and :1082-1083 (`World::new(content: ContentDb, ...)`); repo:prototype/osfr-tools/src/quest_engine.rs:8, :854, :886-888; repo:prototype/osfr-tools/src/gateway.rs:998-1014. The consumers are in production modules, not only in tests.

2. `old:` Each tag is `{ "kind": "client" | "video" | "wiki" | "reconstructed", "evidence": "..." }`.
   `new:` Each tag is `{ "kind": "client" | "video" | "wiki" | "reconstructed" | "legacy-data", "evidence": "..." }`. `legacy-data` is accepted by the parser and is used in the data files (`legacy-data` tags in `tests/content_npc_spawns.rs` and `tests/field_enemy_level_camps.rs`). Only `reconstructed` requires the `(R)` prefix.
   `why:` repo:prototype/osfr-tools/src/content.rs:21-28 (`SourceTag` has `LegacyData`, serde rename `legacy-data`); content.rs:563-568 (only `Reconstructed` needs `(R)`).

**Checked and holding (no change):**
- `src/content.rs` strict serde records (`deny_unknown_fields` on `VersionedFile` and records), `SCHEMA_VERSION = 1`, and the eight required files (`content.rs:591-601`).
- Loader checks: NPC/POI zone links, NPC quest links, quest giver and prerequisite links, objective and reward validation, job trainer and quest links, dungeon entry requirements, and minigame-to-dungeon (`content.rs:607-838`).
- Job XP keys resolve to `profile_id` (`content.rs:698-703`, `:767`).
- `startup_catalogues::ItemDefinition { id: i32, serialized_record: &[u8] }` (`startup_catalogues.rs:52-55`).
- `startup_messages::ZoneDetails` fields (`startup_messages.rs:20-27`).
- `startup_world::NpcSpawn` (`startup_world.rs:599`) and `startup_world::PointOfInterest` (`startup_world.rs:212`).
- Reader `PlayerUpdatePacketAddNpc_ReadBody` at `00921a10` (Gateway and Transport.md:6043).
- Counts: 17 job pages, 17 NPC pages (excluding the index) and 74 dungeon pages (excluding `Dungeons.md`) under `notes/Build Guides/Content/`.
- The 783-entry minigame registry (MMO Work Queue row 015).
- The fixture uses the two startup rows (`tests/fixtures/content/npcs.json`, `pois.json`).

**Unsure:**
- POI reader `PoiDefinitionRow_ReadFields` at `00b98290`: the address matches Zones and Terrain.md:474 and the Native Map shard. I did not decompile it.
- The capture export `../lab/reports/worldcontent-20261013T203151Z/world-content.json` is outside the repo, so I could not check its values. The fixture rows cite the same path.
- The content index's provenance precedence (client, then video, then wiki) and the Build Ledger item 5 wording were not checked.
