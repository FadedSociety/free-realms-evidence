<!-- fleet job=bug-verify id=src-derby-rs-L801-f1 status=done turns=5 usd=0.0046 tokens(read,write,in,out)=[42307, 17712, 12, 3992] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/derby.rs:1322-1329

**Verdict:** confirmed

**Severity if confirmed:** medium. The bug changes in-match health and score only. It does not corrupt saves, crash the server, or grant items or coins. Completion reward is flat and independent of score (`derby_gateway.rs:8-14`, `:467-468`), so "low" is also defensible, but the flaw is a real rule bypass and the reviewer's medium rating holds.

**Evidence (checks in order):**

1. **Module tree.** `derby.rs` is live: `src/lib.rs:16` has `pub mod derby;` and `:17` has `pub mod derby_gateway;`. `derby_gateway::handle` (`derby_gateway.rs:373-387`) calls `staged.handle_client(owner, inner, now_ms)`. Only test-only uses of `derby` exist outside the library, so this is not test-only code.

2. **Input reaches it, with no upstream block.** `handle_client` (`derby.rs:1120-1121`) routes `VehicleHit(report) if report.reporter == sender` straight to `contact`. The only guards are sender identity (`reporter == sender`), so the client controls the report. Nothing in `handle` or `handle_client` checks attacker health.

3. **Failure is real.** The guard list in `contact` (`derby.rs:1322-1329`) covers phase, reporter, self-hit, `is_connected_human(sender)` and victim existence. There is no attacker-health check. Later guards cover impact, poses, freshness, radius, damage cap, victim alive (`:1383-1386`) and cooldown. The attacker's health is never read. A dead attacker's hit therefore passes and reaches:
   - the relay to other humans (`:1401-1404`), which happens before the shield return;
   - `damage_dealt` credit (`:1416`);
   - knockout scoring for the attacker (`:1430-1431`);
   - the victim's `respawn_at_ms` (`:1436-1437`).

   `relay_pose` (`:1293-1295`) also has no health check, so the dead car's pose stays fresh. The knockout-induced death is real: `:1421-1423` sets health 0 and `:1436-1437` sets the respawn timer. The respawn only resets health in `tick` (`:1684`, `ResetVehicle`), so the attacker stays at health 0 until then.

4. **Inconsistency confirmed.** `pickup_hit` refuses `self.drivers[&sender].state.health == 0` (`:1481`). `contact` does not check the attacker's health, although it checks the victim's (`:1383-1386`). No test covers a zero-health attacker: `tests/derby.rs:351-386` only checks that a duplicate hit within cooldown is empty (`:380`).

**Dropped-list items:** I did not re-verify them. The reviewer's reasoning there is consistent with what I read.

**Corrected fix:** The proposed fix is correct. Add `|| self.drivers[&sender].state.health == 0` to the guard list at `derby.rs:1322-1329`. The `drivers[&sender]` index is safe because `is_connected_human(sender)` is checked first in the same `||` chain. A regression test next to `tests/derby.rs:351` would cover it: knock out OWNER, then send a hit from OWNER and assert it is ignored.
