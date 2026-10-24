<!-- fleet job=bug-hunt id=src-housing-native-rs-L801 status=nothing_found turns=10 usd=0.0111 tokens(read,write,in,out)=[195911, 36962, 22, 9097] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/housing_native.rs lines 801-1258 of 1258

No defects found in `prototype/osfr-tools/src/housing_native.rs` lines 801-1258. I read the whole window and the helpers it depends on (`Reader`/`Writer` at lines 55-209, `FixtureInstanceInfo`, `FixtureDefinition`, `FixtureUpdate` at 386-600, and `PlayerHousingInstanceInfo`/`ZoneData`/`InstanceList` at 655-800).

What I checked:

- **Bounds and panics.** `Reader::take` uses `checked_add` and a length check. `HousingPacket::decode_inner` (1204) checks `len < 4` before `inner[..2]`. `HousingPacket::decode` (1244) checks `len < 2` before `payload[..2]`. Counts are capped at `MAX_COUNT` (4096) and strings at `MAX_STRING` (4096). Every `Vec::with_capacity` is capped at 64. Every element consumes at least 4 bytes, so loops are bounded by input size. No `unwrap` runs on client data.
- **Encode/decode symmetry.** `InstanceData` (encode 860-905, decode 907-980), `FixtureAsset` (1002-1056), `FixtureItemList` (1069-1112), `PositionUpdate`, `PlacementDenied`, `HouseInfo`, and `ZoneData` field order matches on both sides. The trailing factory bool (written as `false` at 903, required to be `false` at 975) is consistent. Struct-literal fields that call the reader are evaluated in source order, so the reads line up.
- **Reachability.** `HousingPacket::decode`, `InstanceData::decode`, `FixtureAsset::decode`, `FixtureItemList::decode`, `PositionUpdate::decode`, and `PlacementDenied::decode` have no callers in `src/`. They are only exercised by `tests/`. The production client-input path in `housing_service.rs` uses `WirePlaceFixture::decode` (line 447) and the `piece_025` `wire::decode` (line 485), which are outside this window.

Minor observations I did not report because they are not defects: the `MAX_COUNT` doc comment says counts "must fit the remaining input", but `Reader::count` does not check that. Nothing is harmed because the preallocation is capped and every element consumes bytes. `HousingPacket` also omits subtype 39 (`InstanceList`), which is consistent with it being a separate list type.
