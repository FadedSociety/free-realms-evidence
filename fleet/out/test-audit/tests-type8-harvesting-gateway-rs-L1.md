<!-- fleet job=test-audit id=tests-type8-harvesting-gateway-rs-L1 status=done turns=5 usd=0.0091 tokens(read,write,in,out)=[65225, 33152, 12, 8623] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/type8_harvesting_gateway.rs lines 1-1155 of 1155

Reviewed `tests/type8_harvesting_gateway.rs` lines 1-1155 (read in full). No `#[ignore]` or silent early-return skips in this window; the fixture paths fail loudly rather than skipping. Six findings, ordered by severity:

- **[medium] prototype/osfr-tools/tests/type8_harvesting_gateway.rs:841-847 authoritative_timer_pause_loss_and_results_close - the "paused run keeps its remaining time" check cannot fail if the timer never runs.**
  - Why it cannot catch a regression: `remaining_before` is an `Option<u64>` read from JSON. If `active.remaining_ms` is missing or renamed, both sides are `None` and `assert_eq!` passes. Also, nothing shows the clock would advance without the pause, so a server that never decrements `remaining_ms` (or ignores `tick_at` entirely) passes. The only control is the later `Lost` phase, which is a separate path.
  - Fix: assert `remaining_before.is_some()` and that it is positive. Then add a control: on a second, unpaused run (or after `FRServer_Pause\tfalse`), `tick_at(+N)` must strictly reduce `remaining_ms`. Keep the paused equality check.

- **[medium] prototype/osfr-tools/tests/type8_harvesting_gateway.rs:1154 fixture_definitions_exist_in_the_private_campaign - `assert!(FIRST_MINING_INSTANCE > 0)` is a constant-versus-literal check that cannot fail.**
  - Why it cannot catch a regression: `FIRST_MINING_INSTANCE` is `pub const ... = 18_000_001` (src/mining.rs:94). Changing it to any positive value still passes, and the line has nothing to do with the test's claim that fixture definitions are mintable from the manifest.
  - Fix: delete the line, or replace it with an assertion that touches harvesting behaviour, such as `Gameplay::load` on the fixture succeeding and the mining namespace not colliding with `harvesting::FIRST_INSTANCE_ID`.

- **[medium] prototype/osfr-tools/tests/type8_harvesting_gateway.rs:779 save_reconnect_cancel_and_restart_rebind_the_run - the name says the run is rebound, but the body asserts the run is released.**
  - Why it cannot catch a regression: at lines 800-801 the test asserts `active_instance(&restored).is_none()` after reload, with the comment "(R) Reconnect releases the run". Nothing checks that a restored run can resume or keeps its instance, phase or remaining time. A change that rebinds the run on reload, or drops the restore entirely, would not be distinguished beyond the release check.
  - Fix: rename to match what is proven (e.g. `save_reconnect_releases_run_and_restart_grants_nothing`), or add an assertion on the restored state that matches the stated rule. Either way the name and the body must agree.

- **[medium] prototype/osfr-tools/tests/type8_harvesting_gateway.rs:1082-1087 harvesting_content_loads_fail_closed_and_binds_region_111 - the reconstructed quota check passes vacuously on an empty goal list.**
  - Why it cannot catch a regression: `spec.goals.iter().all(|goal| goal.quota == 25 && goal.per_reward == 5)` is true when `goals` is empty. Dropping every goal from the recovered content would pass, even though the message says "the reconstructed quotas stay unchanged".
  - Fix: also assert `spec.goals.len() == 4` (or `!spec.goals.is_empty()`) before the `all`, and assert the goal values/indexes, not only the quotas.

- **[medium] prototype/osfr-tools/tests/type8_harvesting_gateway.rs:1093-1096 harvesting_content_loads_fail_closed_and_binds_region_111 - "missing reward definitions must refuse the gateway load" only checks `is_err()`.**
  - Why it cannot catch a regression: any load failure passes, including a malformed JSON, a wrong game/profile binding, or a future bug in `Gameplay::load`. The test therefore does not prove the refusal is about the reward definitions it names. The same `is_err()`-only pattern is used for the wrong-game, wrong-job, wrong-asset and orphan cases at lines 1033-1057, so the "fail-closed binding" claim is only checked for refusal, not for which rule refused.
  - Fix: capture the error and assert its message names the rule (e.g. contains "unknown reward definition" for 2885/2887/2890/2877, and the game/profile/asset/orphan messages for the other cases). Otherwise a regression that breaks one binding check but still errors elsewhere passes.

- **[low] prototype/osfr-tools/tests/type8_harvesting_gateway.rs:439-447 older_snapshots_default_absent_harvesting_state - the message says "byte-identical" but the body compares `serde_json::Value`s.**
  - Why it cannot catch a regression: `Value` equality ignores key order, whitespace and number formatting, so a serializer change that reorders or reformats keys (but keeps the same values) would pass while the claim "stays byte-identical" is false.
  - Fix: compare `serde_json::to_vec(&state)` against `serde_json::to_vec(&old)` (or the raw source bytes) for the byte-identical claim, or reword the message to "value-identical".
