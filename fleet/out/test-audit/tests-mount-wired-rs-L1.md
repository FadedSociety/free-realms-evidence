<!-- fleet job=test-audit id=tests-mount-wired-rs-L1 status=done turns=7 usd=0.0070 tokens(read,write,in,out)=[65500, 20351, 16, 7590] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mount_wired.rs lines 1-316 of 316

Window: `prototype/osfr-tools/tests/mount_wired.rs` lines 1-316. Two findings, one of them the header's zoning claim.

- **[high] prototype/osfr-tools/tests/mount_wired.rs:205-208 `a_knockout_a_chasing_enemy_an_instance_battle_and_zoning_each_end_the_ride` - the zoning case passes `zoned = true` straight into `settle_mounts`, so it never tests that a zone change ends a ride.**
  - Why it cannot catch a regression: the real zone detection lives in `src/bin/osfr-gateway.rs:1730-1731` (`let zoned = outcome.began_zoning || previous.zone_id != staged_gateway.state().zone_id; staged_gateway.settle_rides(zoned)`). The gateway-level test (lines 292-315) never changes zone either. So the binary could drop `began_zoning` or the zone-id comparison (always passing `false`) and every test here would still pass. The module doc (lines 7-8) says zoning ends the ride, which this file does not show.
  - Fix: at the gateway level, mount, then perform a real zone transition (a zone-change request or a state with a different `zone_id` run through `handle_at`/the staged path the binary uses), and assert `has`/`removes_ride` on the replies and `!emote_context(..).mounted`. Alternatively, rename the test to drop "zoning" and add a separate test for the binary's zone derivation.

- **[medium] prototype/osfr-tools/tests/mount_wired.rs:313 `the_gateway_reports_mounted_to_the_emote_rules_and_settles_rides` - the neighbour check only matches the removal prefix `[35,0,3,0,1,0]` and never checks the ride's guid.**
  - Why it cannot catch a regression: a `nearby` removal for any other actor (for example a pet, or the wrong guid computed from the owner) still satisfies `any(|r| r.starts_with(&[35,0,3,0,1,0]))`. The gameplay-level `removes_ride` helper checks `r[6..14] == ride_guid()`, but this gateway-level assertion does not.
  - Fix: `.any(|r| removes_ride-style check)`, i.e. `r.starts_with(&[35,0,3,0,1,0]) && r[6..14] == actor.to_le_bytes()`, with `actor` already computed at line 273.

- **[low] prototype/osfr-tools/tests/mount_wired.rs:307 `the_gateway_reports_mounted_to_the_emote_rules_and_settles_rides` - `r[7..10] == [168, 0, 4]` hard-codes the 7-byte gateway wrap header offset.**
  - Why it is churn, not a miss: a change to the outer framing (the `wrap`/`wrapped` layout at `src/gateway.rs:690` or the test's own `wrap` at line 220) would fail this test even though the mount removal is still correct, and it is not what the test is about.
  - Fix: find the reply by its inner bytes (for example `r.windows(3).any(|w| w == [168, 0, 4])` or strip the known header via a helper) instead of a fixed index.

Checked and fine: the `#[ignore]` and early-return paths (none present); the content fixture at line 245 is asserted with `is_file` rather than skipped, and the `round59` content directory is used by other tests; the knockout, chase and battle branches each assert removal of the ride through `removes_ride`, which would fail if the trigger did nothing (`ride_restrictions` reads `knocked_out` and `in_minigame`).
