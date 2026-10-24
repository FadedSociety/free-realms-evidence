<!-- fleet job=test-audit id=tests-power-up-drops-rs-L1 status=done turns=11 usd=0.0127 tokens(read,write,in,out)=[245265, 37935, 24, 10948] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/power_up_drops.rs lines 1-765 of 765

Window: `prototype/osfr-tools/tests/power_up_drops.rs` lines 1-765 (read in full). Checked against `encounter.rs` (`bind_run_instance` 824, `reset_session` 1334, `enter_zone` 2110), `encounter/shared.rs` (`shared_effects` 490), `encounter/field_rewards.rs` (`claim_kill_credits` 288, `CREDIT_TTL_MS = 10_000`), and `bin/osfr-gateway.rs:1791` (the production caller passes `outcome.began_zoning`).

Most tests hold up. The lapse test at 608 is exact at the 10 000 ms credit boundary, and the bystander, participation-window, group-multiplier, and ttl tests each have a real canary. The findings below are the exceptions.

- **[medium] prototype/osfr-tools/tests/power_up_drops.rs:422 a_revive_or_same_instance_transfer_reload_discards_ground_pickups - the name and comment claim coverage of the revive and same-instance transfer (opcode 31) reload paths, but the body only calls `e.bind_run_instance(0, true)` directly.**
  - Why it cannot catch a regression: the gateway can stop mapping revive and transfer (opcode 31) to a scene reload, for example by passing `began_zoning` or `false` for those cases, and this test still passes. Nothing here drives the opcode-31 handler or the gateway's `outcome` mapping; the test only checks the engine's `scene_reload` flag.
  - Fix: rename the test to what it exercises (e.g. `bind_run_instance_with_scene_reload_clears_pickups`), or drive the real opcode-31 handler (revive and transfer) through the gateway and assert `pickup_count() == 0` afterwards. Also assert the boolean the reload returns.

- **[low] prototype/osfr-tools/tests/power_up_drops.rs:376 zoning_clears_pickups_but_not_the_held_power_up - the test never checks that the ground pickup existed before `reset_session`, so `removed(&out).is_empty()` can pass vacuously.**
  - Why it cannot catch a regression: the `kill` helper only asserts the enemy's removal, not that a pickup spawned. If the kill at line 381 stopped producing its guaranteed `t_shield` drop, the post-reset tick would still return no removals and the test would pass, even though it no longer tests clearing. The same gap exists in the second block of `pickups_do_not_follow_the_player_into_another_zone` (lines 724-732), which has no spawn assertion.
  - Fix: before `e.reset_session()`, assert `pickup_count() == 1` (or `pickups(&kill).len() == 1` for the second kill), so a reset that clears a pickup that was never there is caught.

No `#[ignore]`, no early-return skips, and no cannot-fail comparisons were found in lines 1-765.
