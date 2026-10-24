<!-- fleet job=test-audit id=tests-housing-rs-L1201 status=done turns=5 usd=0.0050 tokens(read,write,in,out)=[31707, 18915, 12, 4643] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/housing.rs lines 1201-1378 of 1378

**[medium] prototype/osfr-tools/tests/housing.rs:1251 a_guest_with_edit_permission_can_edit_but_a_stranger_cannot - the name says a permitted guest can edit, but the guest only places a fixture; every move is performed by OWNER.**
- Why it cannot catch a regression: `permission_for` (src/housing.rs:851-859) accepts a level >= `PERMISSION_CAN_EDIT`, and `move_fixture` (src/housing.rs:1028-1037) calls it. If `move_fixture` were changed to check only `owner_guid` (or to skip the permission check for guests), the test would still pass: the owner's move at line 1282 still succeeds, and the final `Err(NotPropertyOwner)` at line 1293 for OTHER after the level is reset to 0 would still be returned, because the owner-only check also rejects a non-owner. So the guest's granted edit right is never shown to work on a move.
- Fix: after the grant at line 1267 and the placement at line 1270, add `housing.move_fixture(OTHER, HOUSE, placed.fixture_guid, transform(401.5, 4.0, 410.0), &mut inventory).expect("a guest with edit level may move")`, and check the stored transform (e.g. via `saved_fixtures(HOUSE)`) shows that position. Keep the post-revocation denial at line 1293 as the stranger/revoked check. Then a move path that ignores the guest's permission fails the test.

No other problems in lines 1201-1378 that I could confirm:
- 1201-1234 (`saving_an_existing_fixture_keeps_the_build_area_bound`) checks both the `OutsideBuildArea` error and that the stored transform is unchanged. That matches the existing-fixture branch at src/housing.rs:1098-1104.
- 1237-1248 (`a_rejected_seed_leaves_the_ledger_unchanged`) is meaningful. Without the validate-before-mutate step at src/housing.rs:378-385, the retry `seed(CHAIR, 0, [1])` would return false and fail.
- 1305-1378 (`restart_conservation_requires_restaging_the_captured_instances`): the pre-restage pickup error, the restocked counts (3 and 1), and the final count of 4 after pickup together catch a pickup that mints stock or fails to restore it.
- No `#[ignore]`, no early returns, no fixture-dependent passes in the window.
