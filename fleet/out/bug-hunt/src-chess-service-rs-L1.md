<!-- fleet job=bug-hunt id=src-chess-service-rs-L1 status=nothing_found turns=14 usd=0.0220 tokens(read,write,in,out)=[443886, 51474, 30, 22283] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/chess_service.rs lines 1-705 of 705

No reportable defects in `prototype/osfr-tools/src/chess_service.rs` lines 1-705. I read the whole window and the callers and callees that matter: `chess.rs` `settle_player`, `game_over`, `handle_payload` and `settle_player` on `ChessTables`; `minigame.rs` `handle_client`, `offer`, `finish_inner` and `start`/`started`; and `gameplay.rs` `handle_chess`, `begin_chess`, `apply_chess`, `seed_chess`.

Candidates I checked and dropped:

- **Double payout on repeated terminal packets.** `handle_movie` (l.487-491) calls `settle` on every terminal table result. Chess `settle_player` returns nothing unless `game_over` has the player, then inserts into `settled` on acceptance. `finish_inner` (minigame.rs:548) also requires `RunState::Playing`, and `handle_movie` (l.468) only runs in `Playing`. Coins cannot be paid twice.
- **Coins paid without a ledger record, or the reverse.** `settle` records the ledger only when `settled.reward_state` is `Some`. A capped win takes the `finish_win_without_reward` path, which returns `reward_state: None`, so the ledger and the payout stay consistent.
- **Daily cap bypass.** `remaining` is computed from the ledger before the grant, and `grant.coins <= remaining` gates it. `coins` comes from validated content, not the packet.
- **Mutation before error.** `route` and `begin` stage on a clone and commit only on success. `route_inner` never mutates and then returns `None`.
- **Client-controlled authority.** `player_id` comes from the session. `row_id` is looked up in content. Difficulty, skill and coins come from content. `handle_payload` checks seat membership.
- **Panics.** The window has no `unwrap`/`expect` on client data. Slice access at l.418-419 is guarded by `len() >= 3`. `as u8` (l.512) and `as i32` (l.612, l.621) are preceded by content validation. `elapsed` uses `try_from(...).unwrap_or`. The ledger uses `saturating_add`/`saturating_sub`.
- **Instance-id collisions.** `MinigameRuns` ids are monotonic (minigame.rs:262-275), so a stale table cannot be reopened under the same id.
- **`reseed` (l.286-293) ignores `content.scoring` when `tables` is `None`.** It builds `ChessTables::with_seed` without `set_scoring`. This is only reachable through the test/fixture hook `Gameplay::seed_chess` (called only from `tests/chess_route.rs`), never from a client packet or the gateway. It is not a player-reachable defect, so I am not reporting it.
