<!-- fleet job=bug-hunt id=src-restoration-piece-077-rs-L801 status=nothing_found turns=15 usd=0.0192 tokens(read,write,in,out)=[407996, 50193, 32, 17637] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_077.rs lines 801-1346 of 1346

No reportable defects in `prototype/osfr-tools/src/restoration/piece_077.rs` lines 801-1346. I read the whole window and the call sites that feed it (`gameplay.rs` `handle_warp` 3559-3600, `on_location` 1806-1830, `warp_context` and `recover_login_pose` 3230-3249, `apply_relocation` 3213-3228; `terrain.rs` `height_at` 102-105). Candidates I checked and dropped:

- **`handle` (1142-1143):** `inner.get(..2)?` guards the opcode and `&inner[2..]` is safe after it.
- **Atomicity in `zone_teleport`, `safe_teleport`, `friend_teleport` (1172-1215, 1271-1283):** every `last_*_ms` write happens after the last fallible check, so a refusal changes nothing. The one leftover is in `gameplay.rs` `apply_relocation`, which can return `Err` after `warp.handle` has already stamped the cooldown. That cooldown is session-only and the error is server-side, so it has no player-visible effect.
- **`safe_teleport` (1192-1215) and `recover_login_pose` (1236-1259):** the fall test and the stuck cooldown agree with the doc comments and with `tests/warpstone_travel.rs:481-532`. The unattuned nearest-warpstone pick is deliberate and tested (test comment "allowed once (R)").
- **Trusting the client:** the 90 destination is looked up in the server table and must be an attuned warpstone. The 122 body is decoded and must be empty, and its target comes from the server position. The 58 friend view is server-supplied (`|_| None` in production). Position for `visit` comes from `character.position`, which the gateway validates before calling.
- **`recover_login_pose` NaN handling:** `TerrainGrid::height_at` returns `None` for non-finite x/z. A NaN `y` cannot come from a save, since serde_json cannot store NaN.
- **`WarpRules::checked` (870-884):** bounds reject NaN and oversized cooldowns. `WarpRegistry::default()` takes the custom `WarpRules::default()` (12 m, 5 s, 300 s, 3 m, 250 m), so it does not start with zero rules.
- **Arithmetic and collections:** `check_cooldown` uses `saturating_sub`, `total_cmp` handles the nearest-warpstone sort, and the visit and definitions collections are bounded by the nine-row CURATED table.
- **Unused public API:** `attune` (1055) is not called from any client path. `restore` (1077) filters saved ids to warpstones in the table.
