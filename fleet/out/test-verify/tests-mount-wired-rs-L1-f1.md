<!-- fleet job=test-verify id=tests-mount-wired-rs-L1-f1 status=no_submit turns=7 usd=0.0076 tokens(read,write,in,out)=[94256, 27587, 16, 6433] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/mount_wired.rs:205-208

**Verdict: confirmed.** The claim is narrower than the reviewer's wording, but its core holds: no test in the repo fails if the binary's zone derivation breaks.

**Evidence**

- **The zoning case passes the flag in directly.** `tests/mount_wired.rs:205-208` is `mounted_game()` then `game.settle_mounts(&who(), true)`, asserting `has(&out, 168, 4) && removes_ride(&out)`. No zone change happens anywhere in the test. This assertion does catch a regression inside `settle_mounts` (if it ignored `zoned`, the early return at `gameplay.rs:2061` would fire and the assert at line 207 would fail), but it says nothing about how `zoned` is computed.
- **The gateway-level test doesn't zone either.** `mount_wired.rs:306` calls `gateway.settle_rides(false)` after a knockout. `Gateway::settle_rides` (`gateway.rs:1371`) takes `zoned` as a parameter, so the derivation can't be reached from there.
- **The derivation is only in the binary.** `src/bin/osfr-gateway.rs:1730` is `let zoned = outcome.began_zoning || previous.zone_id != staged_gateway.state().zone_id;`, feeding `settle_rides(zoned)` at line 1731. Replacing it with `false` changes nothing observed by `mount_wired.rs`, because that file never runs the binary path.
- **No other test covers it.** `mount_routing.rs:277-310` ("zoning" as a trigger) calls `service.dismount_request(...)` directly, which is the same call for every trigger, so it doesn't exercise zone detection. A case-insensitive search of `src/bin` for `mount|ride_|rides|168, 0` finds no ride test that changes zone (the only ride-related test is `osfr_gateway/tests.rs:558`, a fanout check). The `began_zoning` tests in `field_battle_roster.rs` and `dungeon_stone_heart.rs` never mount a ride.

So the regression "the binary drops `began_zoning` or the zone-id comparison" passes the whole suite. The module doc's "zoning ends the ride" is true only at the `settle_mounts(zoned=true)` level, which this file does pin.

**Minimal fix:** add a binary-level test in `src/bin/osfr_gateway/tests.rs` that mounts a ride, then drives a zone-changing staged request through the path at `osfr-gateway.rs:1700-1731`. Assert a `168/4` reply and a `35/3` removal, and that `ride_view` is `None` afterwards. Alternatively, rename the gateway-level zoning case so it doesn't claim the derivation.
