<!-- fleet job=bug-hunt id=src-quest-engine-rs-L801 status=nothing_found turns=11 usd=0.0158 tokens(read,write,in,out)=[252310, 43984, 24, 15487] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/quest_engine.rs lines 801-1600 of 3000

No reachable defect found in `prototype/osfr-tools/src/quest_engine.rs` lines 801-1600. I read the whole window, plus the callees it depends on (`repair_counters` 2479, `validate_state` 2537, `validate_definition` 2427, `overall_progress` 2912, `offer_denial` 1653, `accept`/`decline` 1698-1785, `quest_journal::breadcrumb`, and the `pending_turnin_actor` callers). Items I checked and cleared:

- **Index panics in `active_login_packets` (1468-1469, 1485, 1501) and `quest_add_packet` (1437):** `self.definitions[&quest_id]`, `self.state.quests[&quest_id]` and `progress.counts[index]` are safe. `validate_state` (2549-2567) rejects any non-Completed save entry whose quest is unavailable, and it requires `counts.len() == objectives.len()` for available quests. Active entries are therefore always available and correctly sized.
- **`offer` indexing (1585):** `offer_denial` (1654) returns `Unavailable` for a missing definition before the index is reached.
- **Division by zero in `overall_progress` (2916):** `validate_definition` (2466) rejects `required == 0`, and `validate_state` caps counts at `required`, so no NaN path is reachable.
- **Split loader objective reorder (975-986):** the `expect` only fires if content is inconsistent. The content is authored on disk, not supplied by a client.
- **Split loader decline at 1009-1015:** `repair_counters` has already removed disabled or unavailable pending offers, so the path is consistent.
- **Client inputs (`select_quest` 1540, `set_auto_switch_selected` 1561, `offer` 1573):** each is checked against server state (Active status, pending/Offered state, giver match, limits).
- **Casts and encodings (`quest_id.try_into`, `name_id`, `put_i32`):** bounded or validated; the one `id as u32` at 1356 operates on content-only values.

One possible issue sits outside my window and needs a corrupt save to trigger, so I did not report it: `repair_counters` (2500) can reset an Active quest's counts while `pending_turnin` still points at it, and `validate_state` (2587-2592) would then fail the whole load.
