<!-- fleet job=bug-hunt id=src-encounter-field-rs-L1 status=nothing_found turns=26 usd=0.0358 tokens(read,write,in,out)=[1206241, 72681, 54, 29343] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/field.rs lines 1-800 of 1101

No reportable defects in `prototype/osfr-tools/src/encounter/field.rs` lines 1-800. I read the whole window and checked the paths that reach it from client packets and saves.

What I checked and ruled out:

- **Client positions:** `battle_screen` (595-642) and `take_pending_battle` (566-573) take a player position. The caller (`encounter.rs:1566`) rejects non-finite or out-of-range positions before dispatch, so NaN cannot bypass the `> BATTLE_SCREEN_RADIUS` test in `battle_screen`.
- **Go path:** `handle_battle_go` (`gameplay/field_battle.rs:69-124`) consumes the pending battle via `take_pending_battle`, then re-opens the screen on refusal. The Go instance is ignored, but the battle id always comes from server-held pending state, so no client-chosen battle can start.
- **Reopen path:** `reopen_battle_screen` (511) has no `active()` guard, but it is only reached from `refuse_battle` after a consumed pending battle. I could not construct a reachable state where it sets pending during an active encounter.
- **Level gate:** `level_refusal` and `admit_battle` are consistent with their doc comments.
- **Load atomicity:** `load_field_enemies` and `load_field_battles` mutate before the fallible `rebuild_behaviours()`, but both developer reloads run inside `staged()`, which discards the clone on error. Startup (`gameplay.rs:899-919`) propagates errors and does not continue on a partial load.
- **Reload and quest sync:** `reload_field_enemies` resets quest-gated `present` flags, but `content_reload.rs:92` calls `sync_field_quests` afterward, so the gating is restored.
- **Arithmetic and indexing:** the level (1..=20), difficulty (1..=5), respawn, aggro, leash and radius values are all range-checked before `level_health`, `weapon_tier`, `difficulty_level`, `powi` and the `(to - coord) / left * step` division. `left > step >= 0` means the divisor is positive. Every collection is bounded by the 64/16/4 caps and the 128 KiB file limit.
- **Wander AI:** `tick_wanderers_for` (724-813) handles empty player lists and NaN distances without panicking. Its doc comments match the code.

Lines 800-1101 were outside the window and were only read as needed; I did not review them for findings.
