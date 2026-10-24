<!-- fleet job=bug-hunt id=src-restoration-piece-034-rs-L1 status=done turns=7 usd=0.0122 tokens(read,write,in,out)=[115045, 35733, 16, 13214] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_034.rs lines 1-682 of 682

Window reviewed: `prototype/osfr-tools/src/restoration/piece_034.rs` lines 1-682. No panic, unbounded-growth, or client-authority defect is reachable from a client packet today. The module is not registered in the crate (`notes/Research/Pieces/034 Ninja progression.md:157`, "Lead integration") and its only callers are in `tests/piece_034.rs`, so the findings below are latent or low-impact.

- **[low] `prototype/osfr-tools/src/restoration/piece_034.rs:604` - `cast` runs `regenerate` before its refusal checks, so a refused cast can still change state, contradicting the doc at line 577 ("a refusal leaves the state untouched").**
  - Failure scenario: energy is 50, `last_energy_ms` is 0, and the basic is on recast. `cast(.., Basic, 1_100)` after a cast at 1_000 calls `regenerate(1_100)`. That sets `last_energy_ms` to 1_000 and raises energy to 54. The call then returns `NotReady`, but the state has changed.
  - Reach: `cast` is the only entry point for ability use. Any caller that compares state before and after a refusal, or persists on error, sees the change. The energy credited is legitimate time accrual, so no coins or items are gained. `a_refused_cast_does_not_change_the_state` (`tests/piece_034.rs:322-330`) passes only because energy is already full there.
  - Fix: either move `self.regenerate(now_ms)` after the recast check and apply it on the success path, or correct the doc comment to say that time accrual is applied on refusal too.

- **[low] `prototype/osfr-tools/src/restoration/piece_034.rs:410` and `:505` - the equipped-weapon rank gate is enforced only in `equip`. `from_json_with_state` (`:302`, `:407-412`) and `set_rank` (`:482`) can leave a weapon equipped above the acting rank, and `cast` (`:580-639`) never re-checks it.**
  - Failure scenario: a saved state `{rank: 1, weapon_definition_id: 75119}` (`MinProfileRank` 16 per the doc at `:16`) passes `parse`, because the only weapon check at `:410` is `contains_key`. `cast(2, Basic/Special, now)` then uses the rank-16 weapon's abilities at rank 1.
  - Reach: a save restored through `from_json_with_state`, or a lowered `set_rank`. Both are server-side (lead-owned persistence and rank), not client packets, so the impact depends on how the lead persists and edits state. No client packet sets rank or weapon directly.
  - Fix: in `parse`, reject `state.weapon_definition_id` when `weapons[id].min_profile_rank > state.rank`. Optionally repeat the same check at the top of `cast`.

Considered and dropped:
- `regenerate` (`:563-573`): the `i64` product can overflow only if `now_ms` is near `u64::MAX` and the catalogue regen rate is in the billions. Neither happens with server-clock values or the catalogue's rate of 4.
- `cast` (`:580`) accepts `now_ms` with no monotonic clamp, so a caller that forwarded a client timestamp could skip recasts and refill energy. No such caller exists in the crate, so I am not reporting it as a finding. The lead integration should source `now_ms` from the server clock.
- Parse-time validation (`:306-423`) covers ability/weapon references, energy bounds, and damage. `NinjaProgression::cast`'s index paths all go through validated maps, and no slice or `unwrap` is reachable from packet bytes (`denial_payload`, `start_casting_packet`).
