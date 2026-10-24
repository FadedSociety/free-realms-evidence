<!-- fleet job=bug-hunt id=src-encounter-rs-L1 status=nothing_found turns=11 usd=0.0149 tokens(read,write,in,out)=[246514, 42945, 24, 14079] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter.rs lines 1-800 of 3158

No reportable defects in `prototype/osfr-tools/src/encounter.rs` lines 1-800.

The window is almost entirely declarations, content structs, and small pure helpers. None of them parses client packet bytes, and none holds a mutation that can be left half-done. I read every line and checked the candidates against their callers.

Checked and cleared:
- `level_health` (45), `weapon_tier` (52), `difficulty_level` (86): inputs are clamped or matched with a catch-all, so no panic or overflow. `level` is clamped to 1..=20 before `level - 1`.
- `valid_position` (127), `distance`, `horizontal_distance`: finite and magnitude guards are present where client positions enter (for example 1566, 1822, 2331 call sites).
- `resolve_behaviour` (329-373): `merged[key]` only runs on an object produced by `to_value` of a struct. Unknown keys are rejected by `deny_unknown_fields`. Errors propagate with `?` to both callers (1155, field.rs:176). No error is swallowed.
- `Behaviour::check` (378): covers the distance fields and reach <= chase_limit. `attack_ms`, `run_ms` and `rest_ms` are unchecked, but they are content-authored, not client-reachable.
- `prize_bundle` (596): `quantity as i32` is safe. Battle prizes are range-checked to 1..=100 in `encounter/field.rs:339-348`, and `items.len()` is capped at 4 there. Dungeon prizes are content-only.
- `Ground::snap` / `snapped` (788-800): NaN and infinity are handled by `height_at`. An i64 overflow in `c + 1` needs coordinates around 1e18 or a near-zero grid cell. Callers only feed it positions at most 1e6 from validated input, or content positions, so this is not reachable.
- `FieldBattle`/`FieldActor`/`FieldSpawnGroup` field types: their bounds (`enemies.len() <= 16`, difficulty 1..=5, respawn 1..=3600, level 1..=20, level_band) are enforced in `encounter/field.rs:184-199` and `329-355`. Battle `required_combat_level` is enforced through `admit_battle` (field.rs:555). Content values (for example battle 12340 difficulty 3 needs 5, battle 12303 difficulty 5 needs 13) match the difficulty mapping.

Noted but not reported, because they are content tuning or intent rather than a code defect:
- The `level_health` doc (41-44) cites video health values (level 20 = 7116-9821) that the x1.75-per-4-levels formula from a 1000 baseline does not reproduce (about 14,270). The doc acknowledges the level-20 figure at line 38.
- `weapon_tier` doc ranges overlap at level 12 (P4 "8-12", P5 "12-20"). The code gives P5 at 12, which is consistent.
- `encounter/field.rs:155` overwrites each group member's `behaviour` and `level_band` from the spawn group. This is intentional content policy, not client input.
