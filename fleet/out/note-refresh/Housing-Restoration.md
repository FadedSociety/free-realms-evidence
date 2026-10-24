<!-- fleet job=note-refresh id=Housing-Restoration status=done turns=18 usd=0.0225 tokens(read,write,in,out)=[626257, 58615, 38, 17856] model=claude-haiku-5-5 -->
# notes/Research/Housing Restoration.md

**Verdict:** badly stale on integration status. The state-machine facts (opcode numbers, `HOUSE_GUID_BASE`, FNV lot guid, snapshot schema check, `NotPropertyOwner`, the `restart_conservation_…` test, the 127/53 reader) still hold at the tip. The "not wired, no packet writer, not registered" statements do not.

**Corrections:**

1. `old:` | 2 | `ClientHousingPacketPlaceFixture` | server response |
   `new:` | 2 | `ClientHousingPacketPlaceFixture` | client to server |
   `why:` `client_sql` fn `00aa53f0` is the `ClientHousingPacketPlaceFixture` constructor, which calls `FUN_00aa4990(2)`. Fn `00abffb0` is the transport wrapper for the 127/2 commit, so it is a client send. Same finding in `notes/Build Guides/Gameplay/Housing.md:233` and `notes/Native Map/Shards/S0314 00aa2560-00aa90c0.md:21`.

2. `old:` - no packet writer for the housing family, so nothing in this module has been accepted by the native
  client;
   `new:` - typed packet codecs now exist in `src/housing_native.rs` (`PlaceFixture`, `InstanceData`, `InstanceList`, `FixtureUpdate`, `FixtureRemove`, `ZoneData`, `FixtureAsset`, `PlacementDenied`), and family 127 is routed through `Gameplay::handle_housing` (dormant unless `houses.json` exists). Nothing has been accepted by the native client, and the codecs use local length expectations (`housing_native.rs:1-24`);
   `why:` `prototype/osfr-tools/src/housing_native.rs:1-24` and `:215-860`; `src/gameplay.rs:2239`; `src/gameplay/housing.rs:14-15, 81-96`.

3. `old:` - the recovered `HousingPacketFixturePlacementDenied` body is unknown, so a denial reply cannot be serialized yet.
   `new:` - the recovered `127/53` denial reply is serialized: `HousingService::denial_reply` builds one string body, read by the client reader `FUN_00ab3030`, and `REPLY_PLACEMENT_DENIED = 53`.
   `why:` `prototype/osfr-tools/src/housing_service.rs:90, 705-712, 743`; `housing_native.rs:41` (`SUB_PLACEMENT_DENIED`).

4. `old:` - `HousingPacketFixtureAsset`, `HousingPacketFixtureItemList` and `HousingPacketZoneData` payload layouts outside the community model are undecoded.
   `new:` - `HousingPacketFixtureAsset`, `HousingPacketFixtureItemList` and `HousingPacketZoneData` now have local encoders and decoders, built from reconstructed layouts with `unknownN` fields. They are not verified against original captures.
   `why:` `prototype/osfr-tools/src/housing_native.rs:738-760` (`ZoneData` encode/decode), `:986-1003` (`FixtureAsset`), `:37` (`SUB_FIXTURE_ITEM_LIST`); `src/housing_service.rs:719-724` (`HousingReply` variants).

5. `old:` `prototype/osfr-tools/tests/housing.rs` includes the module by `#[path]` so it compiles before the lead registers `pub mod housing;` in `src/lib.rs`.
   `new:` `prototype/osfr-tools/tests/housing.rs` imports `osfr_tools::housing` directly, because `pub mod housing;` is registered in `src/lib.rs`.
   `why:` `prototype/osfr-tools/src/lib.rs:30` (`pub mod housing;`); `prototype/osfr-tools/tests/housing.rs:24-28` (`use osfr_tools::housing::{...}`, no `#[path]`). `grep '#\[path'` in that file returns nothing.

6. `old:` 1. Lead integration: register `pub mod housing;` in `src/lib.rs` and drop the `#[path]` include.
   `new:` 1. Lead integration: done. `pub mod housing;` is registered at `src/lib.rs:30` and the `#[path]` include is gone.
   `why:` `prototype/osfr-tools/src/lib.rs:30`; `tests/housing.rs:24`.

7. `old:` 2. Wire integration (item 025): decode or capture `PlaceFixtureRequest`, `SaveFixture`,
   `PickupFixture` and `HousingPacketFixturePlacementDenied` bodies, then answer from this state
   machine. Item 025 depends on this module's interfaces.
   `new:` 2. Wire integration (item 025): partly done. Family 127 is decoded by `housing_service::decode_request` and answered from this state machine through `Gameplay::handle_housing`. Still open: native capture of these bodies, since the codecs are unverified against original packets.
   `why:` `src/gameplay/housing.rs:9-12, 81-96`; `src/housing_service.rs:705-712`.

8. `old:` 3. Inventory integration (item 026): map `FixtureItemLedger` proposals onto the lead-owned inventory
   `new:` 3. Inventory integration (item 026): in progress. `Gameplay::handle_housing` stages a clone of the inventory with the housing request and commits both together, so the paired commit exists. The restart-restaging recipe is the test named below.
   `why:` `src/gameplay/housing.rs:92-96` (session and inventory cloned together); `tests/housing.rs:1306` (`restart_conservation_requires_restaging_the_captured_instances`).

**Unsure:**

- Test count. The note says the suite of **26** passes. `tests/housing.rs` carries 20 `#[test]` attributes at tip (lines 138–1102), and `src/housing.rs` has none. `notes/Autopilot/L030.md:72` and `L031.md:84` record "housing 26 passed" at an earlier tip. I could not reconcile 20 with 26, so I left the count unchanged. Running `cargo test --test housing` would settle it.
- `Build Ledger.md:109` ("registered, not routed") is also stale. It is not this note, so I did not correct it, but the same drift applies there.
- I did not check the 31 rows of `Houses.json` or the sha256.
- I did not check the 127/23, 127/14, 127/19 and 127/10 routing in detail.
