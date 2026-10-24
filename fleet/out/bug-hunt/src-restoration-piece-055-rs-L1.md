<!-- fleet job=bug-hunt id=src-restoration-piece-055-rs-L1 status=nothing_found turns=5 usd=0.0038 tokens(read,write,in,out)=[34786, 15288, 12, 3013] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_055.rs lines 1-326 of 326

Reviewed `prototype/osfr-tools/src/restoration/piece_055.rs` lines 1-326 in full. No reachable defect found.

What I checked:
- **No client input reaches this code.** The only references to `RangedEnemyAttack`, `EnemyCastProfile` and `begin_cast` are in this file, its own test `tests/piece_055.rs` (pulled in via `#[path]`; the file header says it is "not yet registered" in the crate), and the research note. No server handler, packet decoder or save path calls into it, so no remote player can supply `distance_units`, `now_ms`, the profile fields or a `CombatResolution`. Client-controlled panic and resource findings do not apply.
- **Arithmetic and overflow:** `begin_cast` and `advance` use `checked_add` and return `Invalid` on overflow. Both return before any state is written, so there is no half-applied state. The `u32`→`u64` widening is lossless. No division or indexing exists.
- **Validation order:** `begin_cast` rejects non-finite or negative distance, bad range, and `ability_id <= 0` before the `Busy` check. It sets `state` only after the range check and the `checked_add`, so a refused cast never starts.
- **Lifecycle matches the design note** (`notes/Research/Pieces/055 Ranged enemy attacks.md` lines 101-120): cast → `36/3`; `advance` emits `35/62` when flight is positive and `36/14` when it is zero; detonation fires once; `resolve` fires once and returns `NotDetonated`/`AlreadyResolved` otherwise; `interrupt` is only legal while casting.
- **Constants:** `PROJECTILE_PARAMETERS_DWORD_UNIT_A/B` = 8/9 correspond to byte offsets 0x20/0x24 as the doc says.

Non-defect observations (not reportable as bugs):
- A `Resolved` caster cannot cast again (`begin_cast` returns `Busy`), because nothing returns the state to `Idle`. This looks like intended single-use behaviour, and the module is not wired in, so I did not report it.
- If `advance` jumps past both milestones in one call, it emits only the launch and the detonation waits for the next call. The doc says milestones are crossed once per call, so this is by design.
