<!-- fleet job=pin-audit id=src-bin-osfr-gateway-t458-world-events-rs status=nothing_found turns=2 usd=0.0010 tokens(read,write,in,out)=[1827, 4623, 6, 857] model=claude-haiku-5-5 -->
# src/bin/osfr_gateway/t458_world_events.rs

No finding for `t458_world_events.rs:377` (`t458_stop_removes_every_live_actor_and_a_restart_uses_a_fresh_guid`).

- The `POOF` in `removal(first, POOF)` is a local test constant (`const POOF: i32 = 21;`, line 19). It is the effect id used in the test's own inline `show()` timeline fixture (lines ~33 and ~35: `remove` and `spawn` ops with `effect_id: POOF`). It is not read from `prototype/osfr-tools/data/content/*.json`, so retuning shipped data cannot break it.
- The `T0 + 500` is a test-clock offset passed to `rig.tick`, not a timeline or data value. The poof is emitted on the removal tick, and the test does not assert any duration or timer from data.

Nothing to change for this line.
