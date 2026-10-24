<!-- fleet job=bug-hunt id=src-world-rs-L1 status=nothing_found turns=17 usd=0.0210 tokens(read,write,in,out)=[556301, 52063, 36, 17926] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/world.rs lines 1-800 of 1624

Window `prototype/osfr-tools/src/world.rs` lines 1-800: no defect I could tie to a client-reachable path. Read the whole window and the callers of its public entry points (`update`, `shared_view`, `hidden_view`, `replace_placements`, `add_static_actor`, `exclude_actor_guids`, `read_placements`).

Checked and dropped:
- **`update` / `shared_view` (world.rs:580, 171):** positions are checked finite before use, and non-finite candidates are filtered. Candidate lists are bounded by content rows and `NPC_VISIBILITY_LIMIT`. Client position only selects which content NPCs are sent, so it is not an authority question.
- **`unframe_tunnel` (world.rs:707-716):** the `len < 7` guard runs before `bytes[3..7]` and `bytes.len() - 7`, so there is no panic. Framing matches the `[5,0,1]` + u32 LE prefix used by `startup_world::tunnel`.
- **`load` expect (world.rs:346):** `anchors` is checked non-empty at 319 before the extras loop, and nothing shrinks it afterwards.
- **`exclude_actor_guids` (world.rs:531-535):** it drops `visible` entries without sending 35/3. Callers are startup (`gateway.rs:845`, visible empty) and `take_shared_fields` (`gameplay.rs:416`). After that, shared mode returns early from `update`, and `shared_view` removes known actors through the session-owned `known` set, so nothing is left stale.
- **`replace_placements` (world.rs:425-436):** a `?` after `placed` is taken and actors are removed. The only error source is `update`, which rejects non-finite positions before mutating and whose tunnel framing cannot fail for `build_add_npc` output. Callers re-read and retry (`placement_watch.rs:150`), and the apply-own path uses a clone. I judged this unreachable from a player.
- **Quaternion yaw (world.rs:291):** `[x,y,z,w]` with `2*atan2(y,w)` matches `wugachug.json` (`[0,-0.77,0,0.636]`).
- **Integer casts (`as i32`/`as u32`):** wrapping only, no panic. `revision` uses `wrapping_add`.
- **Non-finite heading/scale in authored placement or content files (world.rs:402-404, 292, 359):** `facing()` can yield NaN for a non-finite heading. This needs a bad world-builder file, not a remote player, so it is outside the defect scope.

Nothing reaches the high or medium bar from a remote player or a save.
