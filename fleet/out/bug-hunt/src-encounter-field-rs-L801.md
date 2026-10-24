<!-- fleet job=bug-hunt id=src-encounter-field-rs-L801 status=done turns=10 usd=0.0142 tokens(read,write,in,out)=[160954, 36109, 22, 16236] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/field.rs lines 801-1101 of 1101

Window `encounter/field.rs:801-1101` (end of `WanderNotice`/wander code, `tick_field`, `heading`, `advance`, `stand`, `walk`). I found one low-severity logic defect. I also checked and ruled out the candidates listed at the end.

- **[low] prototype/osfr-tools/src/encounter/field.rs:1021 - solo mode accumulates the uncapped `attack_damage` into `total_damage`, so the fight log's "taken" amount (encounter.rs:2506) overstates the damage the player actually lost.**
  - **Failure scenario:** the player has 60 HP and three field enemies in solo mode each have a 50-damage attack that hits in the same tick. Enemy A's reply shows `damage=50`. Enemy B's reply shows `damage=10`, because `left = 60-50 = 10`, and enemy C's reply shows `damage=0`. The shared-mode branch at line 1019 pushes the capped `damage`, but the solo branch at line 1021 adds `attack_damage`, so `total_damage` ends at 150. Line 2506 then logs `taken 150`. Only 60 HP was lost; the final `dealt = min(total, health)` at encounter.rs:2514 is correct, so the player's HP is not affected.
  - **Reach:** `tick_field` is called from encounter.rs:2489 with `&mut total_damage` and `None` participants (solo). The uncapped sum also comes from the earlier loop at encounter.rs:2485. The enemy damage is server-computed (`actor.damage * mitigation`), so a remote player does not control the amount. The impact is a wrong fight-log entry; it is not an exploit.
  - **Fix:** in the solo branch, add `damage` (the capped value) instead of `attack_damage`, matching the shared branch. Keep the encounter.rs:2485 caller consistent with it, or log only the amount actually applied.

Ruled out after reading callers:
- `field.rs:998` `player.expect(...)`: the only ways an actor enters `Chasing` are `field.rs:893` (after `delta <= aggro_range`) and `encounter.rs:1930` (on a player hit). If `player` is `None`, `delta` is `f32::MAX`, so line 886 forces `Returning` before the attack block. `aggro_range` is validated to `(0, 40]` at `field.rs:109` and `:187`. The expect is unreachable.
- `field.rs:1008` `(damage as f32 * mitigation).round() as u32`: `mitigation` is server-side (`skills.mitigation()`, or 0 in god mode). Rust float-to-int casts saturate, so there is no panic.
- `field.rs:1081` division by `left`: the caller guards `left > 0.001` at line 937, and `heading` guards at line 1062.
- `FieldParticipant.position`/`health`: `health` comes from server state (`encounter.rs:858`). Positions pass `valid_position`, and shared participants pass the `known_npcs` gate (`field.rs:852-859`). The respawn index at line 1026 is stable because the vector is not resized inside the loop.
- Saturating arithmetic is used on the time and HP sums.
