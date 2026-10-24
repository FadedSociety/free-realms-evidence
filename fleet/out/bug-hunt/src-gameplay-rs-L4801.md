<!-- fleet job=bug-hunt id=src-gameplay-rs-L4801 status=nothing_found turns=38 usd=0.0421 tokens(read,write,in,out)=[1725912, 78549, 80, 30071] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay.rs lines 4801-5475 of 5475

No reportable defects in `gameplay.rs` lines 4801-5475. I read the whole window and checked the callees that decide whether anything in it is reachable from a client packet. The tool budget ran out before I could finish every check, so this is a "not found in what I read" result, not a proof of absence.

Checked and dropped:

- **Mutation before `?` (`apply_identity`, 5237-5263; `enter_opening_cave`, 4993-5027; `stage_job_selection` path in `handle`, 5365-5373).** Partial mutation is followed by an error return. `gateway.rs` `handle_at` (around 1429-1430) clones gameplay state and commits only on success. The identity path (`osfr-gateway.rs` 1030, 1171) propagates the error before any save. I found no persisted partial state.
- **`apply_quest` (5408-5442).** Rewards are staged in clones and committed only on success. The `Err` branch keeps the reward pending as the message says.
- **`sync_world_stage` / `opening_dungeon_destination` / `completed_dungeon_replay` (4855-5069).** The `stages[&id]` indexing is safe: `opening.rs` load validation (around 262-300) requires a progress row for every content stage. The replay gate matches its doc comment.
- **`handle_item_bar` (5081-5112).** The heal percent comes from server item definitions (`item_bar.rs` 55-95, 226-445). Self-target and pending-confirm checks are present.
- **Client-controlled input in `handle` (5289-5375).** The `realm ` slicing is on an ASCII-lowercased copy of the same text, so the byte-5/6 slice is on a char boundary. The class-selection length check precedes `inner[4..8]`. Broadcast is gated by `developer_command_denied` (3675-3698).
- **Identity attachments.** Resolved server-side from a whitelist table (`identity.rs` 200-290), not taken from the client.
- **XP and coins.** `add_experience` and `grant_coins` use checked arithmetic, and `rank` is bounded (`profiles.rs` 228-329).

Possible but not reported: a knocked-out or already-active encounter reaching `enter_opening_cave` returns an error for that packet (5026 via `encounter.rs` 1362-1368). This is self-inflicted and not a remote crash, so I did not count it.
