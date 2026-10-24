<!-- fleet job=bug-hunt id=src-housing-service-rs-L801 status=done turns=22 usd=0.0315 tokens(read,write,in,out)=[837221, 68811, 46, 29019] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/housing_service.rs lines 801-1600 of 2033

Window reviewed: `prototype/osfr-tools/src/housing_service.rs` 801-1600 (plus the helpers it calls: `decode_request` 394-505, `fixture_asset` 1871-1916, `derive_ledger` 1671-1698, `housing_transform` 2003-2033, and `housing.rs` place/pickup/move/set_permission/set_locked/FixtureItemLedger/validate_transform). I found no panic, unbounded-growth, or item/coin-gain defect reachable from a client packet. The main paths hold up:

- `place` (1504-1566): all fallible housing and ledger checks run on a staged clone. `fixture_update` runs before `stock.consume(..)?`, and the live `self.housing` is replaced only after the consume succeeds.
- `pickup` (1568-1600): `row_for_fixture_definition(..)?` and `return_instance(..)?` both run before `self.housing = staged`.
- `request_grant` (1414-1430): the lot is granted on a clone, and the starter unit is returned before `*self = staged`.
- `move_fixture` (1304-1359): the fixture is looked up in the actor's own lot (`house_of`), and `housing.move_fixture` enforces build area, unit rotation, finiteness and tint preservation.
- `offer`/`fixture_asset`: `selections` holds at most one binding per actor (1880-1882), so the map cannot grow without bound. Bindings are re-resolved against live stock at place time.
- `from_state`: the fixture count is checked before `restore_lots`, and duplicate and still-owned placed instances are rejected.
- Permission and edit gates are checked on every mutating path (`can_enter`, `require_edit_mode`, `locked`).

Checked and dropped: the post-commit `saved_fixtures(..)?` calls in `place` (1557), `pickup` (1593) and `move_fixture` (1333-1339) sit after `self.housing = staged`. They contradict the comment at 1549-1550, but they cannot fail, because the same house_guid was just staged successfully. The `MAX_STATE_FIXTURES` (4096) cap versus per-lot `max_fixtures` from content is a configuration matter, not client-driven, so I did not report it.

**[low] housing_service.rs:1301-1303 - the `move_fixture` doc says the wire path cannot call it, but `handle` does (1277-1282), and the `Request::SaveFixture` error arm (1294-1297) is unreachable.**
- Failure scenario: a client sends an opcode-5 (OP_SAVE) housing packet. `decode_request` (housing_service.rs:457-483) returns `Request::Move` with a client-chosen `fixture_guid` and transform before `wire::decode` runs. `handle` then calls `move_fixture`, so the server applies a move that the doc says is unproven. The wire-level `SaveFixture` arm, which is meant to return `UnresolvedRequest`, never fires.
- Reach: `decode_request` (housing_service.rs:457-483) -> `handle` Move arm (1277-1282) -> `move_fixture` (1304). Authorization is intact: `house_of`, `can_enter`, `require_edit_mode`, and the fixture must exist in the actor's own lot (1314-1320). So this is a doc and dead-code mismatch, not an escalation.
- Fix: either update the doc at 1301-1303 to match the OP_SAVE routing, or route opcode 5 to `Request::SaveFixture` so the unresolved-request error is returned as the comment at 1294 intends.
