<!-- fleet job=bug-hunt id=src-housing-rs-L801 status=nothing_found turns=8 usd=0.0193 tokens(read,write,in,out)=[182252, 50137, 18, 22402] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/housing.rs lines 801-1500 of 1500

No reachable defect in `prototype/osfr-tools/src/housing.rs` lines 801-1500.

Checked and ruled out:
- **Mutation before fallible steps:** `place_fixture` (893-973), `pickup_fixture` (977-1024), `move_fixture` (1028-1068) and `restore_lots` (1213-1264) all do their fallible work on clones or staged values and commit with no `?` after the live write. `save_state`/`replace_bytes` (1270-1282, 1424-1449) leave the old file in place on failure.
- **Client-controlled sizes and indices:** `load_state` (1285-1300) caps the read at `MAX_SNAPSHOT_BYTES + 1`. `rebuild` (1302-1350) checks count, duplicate guid and `max_fixtures`. No slice or index is taken from client data in this window. Float paths are NaN/inf-guarded in `validate_transform` (1387-1413) and `is_unit_quaternion` (1415-1418), and there is no integer overflow or division.
- **Trusting the client on placement:** the service path (`housing_service.rs` 1504-1566) takes instance and tint from the server-side `stock` and `config`, and `housing_transform` (2003-2033) takes tint and tilt from the existing placement. `stock.consume` runs before the staged housing state commits, so a second placement of the same instance is refused by the real inventory.
- **Permissions and locks:** `permission_for`, `can_visit` and `set_permission` compare guid and level correctly. Owner and level checks use `>=` against the intended thresholds.

Latent, not reachable from a client packet today (not reported as findings):
- `save_fixture_placement` (housing.rs:1072-1160) creates a fixture without any `FixtureItemLedger` or stock check and accepts a client-supplied non-zero `fixture_guid` without a namespace check. Nothing calls it: a grep of `prototype/osfr-tools` finds only the definition, and the `SaveFixture` request returns `UnresolvedRequest` (`housing_service.rs:1294`). It becomes a gain-items and state-corruption path if wired to the wire without the ledger.
- `rekey_tint` (housing.rs:411-442) does not check owned units at the destination tint. The wire `Move` path (`housing_service.rs:1304-1331`) keeps the existing tint, so it is unreachable from a client packet today.
