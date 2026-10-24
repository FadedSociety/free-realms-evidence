<!-- fleet job=test-audit id=tests-enemies-rs-L1 status=done turns=8 usd=0.0064 tokens(read,write,in,out)=[85753, 19068, 18, 6341] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/enemies.rs lines 1-416 of 416

Reviewed `prototype/osfr-tools/tests/enemies.rs` lines 1-416 (the whole file) and the `src/enemies.rs` code it exercises (`tick` 340-530, `use_ability_on_enemy` 560-600, `step_toward` 677-696). Most tests check real behaviour: the leash return, the aggro-radius cut-off, the kill/respawn timing, and the per-instance health split all have assertions that the current code would fail on a regression. Three weaker spots:

- **[medium] tests/enemies.rs:379 opening_wolf_messages_match_encounter_engine_byte_for_byte - `assert_eq!` on two message lists with no non-empty guard, so an empty-vs-empty result passes.**
  Why it cannot catch a regression: if `EnemyEngine::tick` stops emitting aggro/chase packets for the wolf (for example, aggro is broken), and `EncounterEngine::tick` also returns no replies (for example, the stage is not armed because `set_world_stage` or the encounter file changes), then `enemy_messages == encounter_messages` is `[] == []` and the test passes. The lab-file `assert!` at line 356 only checks that the file exists, not that the replies are produced.
  Fix: add `assert!(!enemy_messages.is_empty());` and `assert!(!encounter_messages.is_empty());` before line 379, and optionally pin the expected first packet prefix (for example `&enemy_messages[0][..2] == &[125, 0]`) so the comparison is anchored to a known packet.

- **[low] tests/enemies.rs:295 ability_damage_kills_once_and_respawns_after_its_timer - the duplicate-kill check only asserts `ability.failure.is_some()`.**
  Why it cannot catch a regression: any failure reason passes, including an unrelated one (for example, a caster cost or cooldown problem, or a broken target check). A change that made the dead enemy take the damage path but still return `kill: None` would also pass, because the test never compares the enemy's health or mode after the duplicate attempt.
  Fix: assert the specific failure kind (or the dead-target message) and assert that `engine.enemy(key, 17).unwrap()` still has `health == 0`, `mode == EnemyMode::Dead` and `respawn_at_ms == Some(600)` after line 292.

- **[low] tests/enemies.rs:237-248 nearby_player_aggroes_chases_and_attack_uses_exact_32_7_bytes - the attack step pins the full 0x20 attack packet byte-for-byte and the total message count (`len() == 5`, line 236).**
  Why it cannot catch a regression: this is not a defect in the test as such, but unrelated changes to the packet layout or to the number of animation packets (for example, adding a pose packet) would fail a test named for aggro and chase. The name claims only aggro, chase and the 32/7 packet, yet the test also pins the animation count and the health arithmetic.
  Fix: keep the byte check in a dedicated attack-packet test. In this test, check only the packet prefix and the `players[0].health == 75` result, and drop the exact `len() == 5` if it is not part of the claim.
