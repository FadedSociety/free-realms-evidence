<!-- fleet job=bug-hunt id=src-quest-engine-rs-L2401 status=nothing_found turns=10 usd=0.0158 tokens(read,write,in,out)=[198967, 37368, 22, 18330] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/quest_engine.rs lines 2401-3000 of 3000

No defect I can tie to a line in `quest_engine.rs` 2401-3000 survives review. I read the whole window and checked the callers and upstream guards that matter.

What I checked, and why each candidate was dropped:

- **`validate_definition` (2427-2475):** `try_fold` overflow maps to `is_none_or` → error. Coins, item counts, XP total, and objective `required` are bounded. Duplicate or zero objective ids are rejected. Nothing here is client-controlled. Definitions come from content and are validated in `new_with_disabled` (1135).
- **`repair_counters` (2479-2535):** the early `return true` branches skip the pending/selected clearing. Unavailable entries are dropped unless completed, and then their counts are cleared. Nothing panics. Load order (1176-1177) runs repair before `validate_state`.
- **`validate_state` (2537-2599):** every path that indexes uses `get`/`zip`. The handshake checks are consistent with each other.
- **`validate_objective_kind` / `validate_event` (2601-2692):** bounds are applied to every client-reachable value. `ClientReported` ids are capped at `i32::MAX` and unique across definitions (1151-1159), so the duplicate-id concern in `ClientObjectives::update` cannot occur.
- **`event_matches` (2694-2794) and `on_event` (1789-1870):** the increment is `saturating_add(...).min(required)`. `counts` length is validated at load. `ReachPoi` and `EnterArea` go through the `location_quests` index, which includes both kinds (1198-1218). `self.definitions[&quest_id]` at 1807 is safe because an active quest without a definition is removed by repair or rejected by validation.
- **`decode_client_complete` (2800-2812):** the length check is exact, `try_into` returns an error rather than panicking, and zero and negative ids are rejected. Its only caller, `npc.rs:199`, maps the error. The id only selects an open goal of an active quest, through `current_objectives` (1321-1342), so a forged id changes nothing.
- **`ClientObjectives::update` (2856-2893):** the registered/armed logic re-arms closed-then-reopened goals with 45/9 and never re-registers. Duplicate ids are impossible per the uniqueness check above.
- **`within`, `is_complete`, `overall_progress` (2900-2919):** NaN and infinity produce `false` or NaN, not panics. Zero-objective quests are guarded at accept (1608, 1659, 1985), so the NaN path is unreachable in practice.
- **`encode_quest_reward_bundle` / `id_packet49` (2940-2996):** the 69-byte layout matches the comment. Sums are checked and conversions use `try_from`. Row count and body sizes are bounded. Reward data comes from server content, not the client.

Nothing was found that a remote player can trigger to crash the server, gain items or coins, corrupt a save, or otherwise break the rules above.
