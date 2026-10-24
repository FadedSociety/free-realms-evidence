<!-- fleet job=bug-hunt id=src-restoration-piece-036-rs-L1 status=done turns=4 usd=0.0072 tokens(read,write,in,out)=[29036, 25122, 10, 7516] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_036.rs lines 1-432 of 432

Read `piece_036.rs` lines 1-432 in full, plus the tests at `tests/piece_036.rs` 150-290 and the callers of `WizardCastState::cast`. I found no panic, overflow, or atomicity defect. Checks that came out clean:

- `regenerate` (323-332): `saturating_sub`, `whole_seconds * 1000` cannot overflow, and the i64 widening is safe. A backwards timestamp grants nothing.
- Denial ordering in `cast` (349-424): the only mutation before a `?`/`Err` is `regenerate`, which is time-driven and harmless. Energy, `last_basic_ms` and `lock_until_ms` are written only after every check has passed, so a denied cast leaves no trace.
- Guid path (361-386): guid 0, self-target, unresolved target, non-finite position, dead, non-hostile and reach checks are all present. The reach boundary is inclusive, as documented.
- `squared_distance` on finite inputs can overflow to `inf`. That is still `> 400`, so it is refused and does not panic.
- The existing tests for lock, recast and energy (`tests/piece_036.rs` 202-281) agree with the code.

Only one finding, and it is a documented gap that I am reporting because the code does not check the value against server state:

**[low] prototype/osfr-tools/src/restoration/piece_036.rs:387-391 - a `CastTargeting::Position` request is accepted with no range check against `caster_position`, so a client-chosen ground point of any finite magnitude is accepted.**
- Failure scenario: a caster at `[0,0,0]` sends a Lightning Blast (slot Special, energy 100) with `Position([1.0e30, 0.0, 0.0, 0.0])`. Only `is_finite` runs on the position. The call returns `Ok(WizardCast { targeting: Position(..), .. })` and spends the 100 energy, and the caller plays the effects at that point.
- Reach: the wire path is `[36][10]` with target flag 1 and a `Vector4` payload, as the module doc describes. `cast` is the only gate. No non-test caller of `WizardCastState::cast` exists yet, so this is not live today. The module doc (lines 43-44) says positional resolution is unrecovered and that the request "carries no actor checks", so this may be intended policy. The reason to report it is that the request is still trusted without any server-side bound.
- Fix: before wiring this module to a live caller, reject `Position` targets whose distance from `caster_position` exceeds a bound (for example the 20-unit reach), or document the Position path as "not yet valid for play" and make the caller refuse it.
