<!-- fleet job=test-audit id=tests-common-station-rs-L1 status=nothing_found turns=4 usd=0.0023 tokens(read,write,in,out)=[17382, 12358, 10, 1209] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/station.rs lines 1-36 of 36

Reviewed `prototype/osfr-tools/tests/common/station.rs` lines 1-36 (the whole file). It contains no `#[test]` functions. It is a shared fixture module: two position constants (`NEAR`, `AWAY`) and `write_placements`, which writes a `PlacementFile` with either one live-world `sh_forge_02` placement or an empty record list.

Checks against the code under test:
- `write_placements` builds a `Placement` and serialises it with `serde_json`. It does not compare against its own output, so the cannot-fail pattern does not apply.
- Its callers are `tests/crafting_stations_route.rs:361-372` and `src/gameplay/t018_station_refresh.rs:121-192`. Those callers assert on the outcome of the refresh, not on the helper's own output.
- `PLACEMENT_GUID_BASE` is imported from `src/world.rs:56`, so the GUID is not hard-coded against a copy of the code under test.
- The header comment says the position is one "no shipped station occupies". A search of `data/content/crafting_stations.json` for `321` / `654` found no match, which is consistent with that claim. I did not check every coordinate in that file.

No findings in this window.
