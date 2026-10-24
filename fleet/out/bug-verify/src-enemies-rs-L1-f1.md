<!-- fleet job=bug-verify id=src-enemies-rs-L1-f1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[9033, 9002, 8, 2184] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/enemies.rs:264-266`

**Verdict:** refuted (on reach, step 2). The code fact is real, but no remote input can reach it.

**Evidence**

1. **Module tree (step 1 passes).** `prototype/osfr-tools/src/lib.rs:20` has `pub mod enemies;`, so the file is compiled into the library. It is not test-only.

2. **Reach (step 2 refutes).** `EnemyEngine` is referenced only at its definition (`src/enemies.rs:163`, `impl` at `:169`). A search of `prototype/osfr-tools/src` for `EnemyEngine|enemies::` finds nothing else. `enter_instance` is called only from `tests/enemies.rs` (lines 219, 259, 315, 341, 363, 393, 394) and `tests/content_enemies.rs` and `tests/field_battle_roster.rs` import the type. The gateway and login binaries and the gameplay dispatch never construct an `EnemyEngine`. The world's `World::enter_instance` (`src/world.rs:1275`) is a different function. The claim itself concedes "No caller exists yet."

3. **Early return is documented design, not a silent drop.** `src/enemies.rs:264-266` returns `Ok(EnemyOutcome::default())` when the key already exists. `notes/Research/World Enemies.md:48` says: "Enter/activate stage-gated groups after the client-ready gate. Send the current live enemy snapshot to late joiners; `enter_instance` itself is idempotent." The stage-gated activation is therefore meant to be handled by a separate step in the integration plan, not by re-entry. The reviewer's failure scenario relies on a re-entry path the design has not built.

4. **The failure is conditional on a future caller.** The stated bug (`enter_instance(key, Some(910007))` after an earlier `enter_instance(key, None)`) cannot be triggered by a player packet today. Even if a caller were added, the fix would be a design choice (key on `(key, stage)` or add a spawn-missing-groups path), not an exploit.

Because the defect cannot be reached by a remote player, it does not meet the high-severity bar (crash, save corruption, item/coin gain). At most it is a latent API-contract gap for a future integration step, i.e. low severity. I would not file it as a current medium-severity bug.

**Severity if confirmed:** n/a (refuted); at most low, as a latent contract note.
