<!-- fleet job=bug-verify id=src-bin-osfr-gateway-rs-L2401-f2 status=done turns=8 usd=0.0082 tokens(read,write,in,out)=[100828, 25380, 18, 8029] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/bin/osfr-gateway.rs:3134-3140

**Verdict:** confirmed

**Severity if confirmed:** medium. The trigger is a server-side write error (ENOSPC, permissions). A remote player cannot cause it directly, so it does not meet the high bar.

**Evidence**

1. **In the real server.** `tick_shared_instance` (`prototype/osfr-tools/src/bin/osfr-gateway.rs:3015`) and `tick_shared_fields` (`:2984`) are in the `osfr-gateway` binary, not a test-only module. The `save` at `:3136` is `osfr_tools::game_store::save` (import at `:9`).
2. **Reachable from the tick.** `tick_shared_fields` calls `contain(|| self.tick_shared_instance(instance, now_ms))` at `:3006`. On error it inserts into `faulted_fields` (`:3007`). The tick is server-driven; no client packet is needed.
3. **Partial write.** The loop at `:3135-3137` runs `save(&self.sessions[key].state_path, &staged[key].snapshot())?` once per changed session. Each file is replaced atomically (`character_store.rs:106-123`, temp file then rename), so a failure on the second session leaves the first session's save on disk with the reward.
4. **Memory stays pre-kill.** Gateways are cloned into `staged` (`:3094`, `:3107`) and the field is cloned (`:3020`). Installing `staged` (`:3138-3140`) and the field (`:3141`) happens only after the loop, so an error skips both. The enemy stays alive in the field and A's live session keeps the pre-kill snapshot.
5. **Later overwrite and re-claim.** A's next save of that pre-kill snapshot erases the reward. The field is not persisted: its only source is `field_seeds` (`world.rs:826`, `:915`, `:931`), so a restart re-spawns the enemy.
6. **Comment does not cover it.** The comment at `:3134` ("publish only after affected saves") is true per file, but says nothing about the set of saves being all-or-nothing.
7. **Fix pattern exists.** `commit_trade_parties` (`:2579`, journal at `:2609-2638`) and `recover_trade_journals` (`:2656`) implement the journal approach.

**Caveats**

- The write can also fail deterministically: `save_document` calls `snapshot.character.validate()?` (`game_store.rs:80`) and `write_document` rejects snapshots over `MAX_SNAPSHOT_BYTES` (`game_store.rs:180`). I did not check whether a player can push a snapshot over the 1 MiB limit. If they can, the defect becomes player-triggerable and its severity should be raised.

**Corrected fix**

The claimed fix is correct. Add:
- A startup replay for any field journal, the same way `recover_trade_journals` replays trade journals. Otherwise a crash mid-write leaves the split state.
- Writing all temp files and then renaming them one by one is not atomic across files. Only the journal sequence (write journal, rename it into place, save each session, remove journal, then install) gives whole-or-absent behaviour.
