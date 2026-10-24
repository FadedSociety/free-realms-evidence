<!-- fleet job=bug-hunt id=src-soccer-entry-rs-L1 status=nothing_found turns=32 usd=0.0309 tokens(read,write,in,out)=[1158581, 62504, 66, 22916] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soccer_entry.rs lines 1-511 of 511

## Window: `prototype/osfr-tools/src/soccer_entry.rs` lines 1-511

No defect I could tie to a line in this window survives the checks below. Every fallible step either runs on a clone of `SoccerService` that is committed only on success, or validates its input first.

### Candidates checked and dropped

- **`Content::validate` (228-257) / `load` (132-144):** `game.id` is bounded to `1..=i32::MAX`, `encounter_id > 0`, ids are unique, and there are 1..=8 games. The file is capped at 1 MiB. `reward.coins` is capped at `i32::MAX`, and `job_xp` keys must be positive with non-zero amounts. The content is server-side, not client input.
- **`Session::begin` (305-341):** `game.id as i32` is safe because validation bounds it. `join`, `fill_bots_for_solo`, and `offer_minigame` run on a local clone, so a failure leaves nothing changed. `activity_id` comes from `activities.admit`, which resolves it against the same content.
- **`handle_client` (420-436):** `sequence` uses `checked_add`, and `self.sequence` is written only after success. `now_ms as f32 / 1000.0` cannot panic.
- **`handle_lifecycle` (388-415):** all work is on a clone. `last_tick_ms` is set with no `?` after it. A double Cancelled cannot reach `leave()` twice, because `exit_soccer` removes the session first.
- **`tick` (443-485):** `saturating_sub` and `min(250)` bound the elapsed time. Restart and HalfTime transitions run on a clone. The `settled` flag stops repeat settlement.
- **`settle` (492-506):** it has no `settled` guard, but the doc's "duplicate call is inert" still holds. `MinigameRuns::finish_inner` (minigame.rs:548) returns a default outcome unless the run is `Playing`. `finish_minigame` returns a default outcome unless the authority phase is `Finished`. Win and loss grant consistency is enforced (`SoccerActivity::finish` derives `won` from the same `winner == team` check used for the settlement).
- **Re-entering Play during a live match:** I checked this at gameplay.rs:3253-3266 and gameplay/occupation.rs:63-114. `Soccer` sets `gates.warp = true`, so `warp_blocker` returns `Busy`, which blocks the second `begin_soccer` that would otherwise capture the arena pose as the return location.
- **Locked job XP (`job_xp`) causing a per-tick settlement error:** real in principle, since `apply_grant` refuses locked profiles (rewards.rs:111-113) and `Session::begin` does not pre-check. But the shipped `data/content/soccer.json` has `"job_xp": {}`, so it needs an authored config change to trigger. Not reported.
- **Possible gateway-side issue, outside this window:** `exit_soccer` (gameplay.rs:3375-3380) takes the session before checking `self.encounter`, so a `None` encounter drops the match without zoning the player back. This needs a deployment without an encounter. Not reported because it is outside my window and I did not confirm reachability.

No `unwrap`/`expect`, indexing, or unchecked arithmetic on client-controlled values appears in lines 1-511.
