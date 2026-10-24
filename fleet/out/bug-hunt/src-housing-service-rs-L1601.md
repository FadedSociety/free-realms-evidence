<!-- fleet job=bug-hunt id=src-housing-service-rs-L1601 status=nothing_found turns=11 usd=0.0150 tokens(read,write,in,out)=[253908, 45027, 24, 13728] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/housing_service.rs lines 1601-2033 of 2033

No defect in `housing_service.rs` lines 1601-2033 that I could tie to a client-reachable input or a save. Lines read: 1601-2033 in full, plus the callers and helpers they depend on (`place`, `pickup`, `move_fixture`, `offer`, `handle`, `FurnitureStock`/`Inventory` impl, `housing.rs` `place_fixture`/`pickup_fixture`/`move_fixture`/`stage`/`restore`/`seed`, `validate_transform`).

Checked and cleared:

- **`pickup_all` (1604-1651):** all housing mutation happens on a `staged` clone and is committed only after `stock.return_instances` succeeds. That method clones the inventory and commits atomically (576-583). The `?` after commit (1644) re-reads the same lot that was just staged, so it cannot fail. Each `pickup_fixture` call checks `permission_for` and `locked`, and the shared ledger is updated per fixture, so a fixture cannot be returned twice.
- **`derive_ledger` (1671-1698):** the `let _ =` on `seed`/`stage` swallows errors. A failure needs a stock instance id that duplicates a placed fixture's id, which normal place/consume flow prevents, so I could not reach it from a packet.
- **`fixture_asset` (1871-1916):** the client's `selection_id` is only ever bound to an instance that `offer` verified is live, has count 1, and has a fixture row. `selections` is pruned to one entry per actor, so it stays bounded. The post-offer `?` lookups cannot fail because nothing changes in between.
- **`housing_transform` (2003-2033):** it rejects non-finite position, rotation and scale. `tilt` is not checked here, but both callers pass a server-side tilt (`IDENTITY_TILT` on place, the saved tilt on move). `validate_transform` in `housing.rs:1387-1413` then checks tilt finiteness, bounds, scale and unit quaternions on both the place and move paths.
- **Counts and casts (`house_info`, `instance_data`, `instance_info`):** `count` is clamped to `i32::MAX`. Fixture and permission keys use `u32::try_from`. `permission.level.max(0)` clamps negatives. The `name_id as u32` cast reads a server-side config value, not client input.
- **`fixture_item_list`, `fixture_update`, `placed_from_saved`, `fixture_definition_from_row`:** no panics or indexing on client data. Growth is bounded by server inventory or lot size.

Nothing in this window meets the bar for a finding.
