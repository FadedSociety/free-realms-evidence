<!-- fleet job=bug-hunt id=src-matchmaking-rs-L1 status=nothing_found turns=11 usd=0.0188 tokens(read,write,in,out)=[310501, 54906, 24, 17740] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/matchmaking.rs lines 1-800 of 1601

No reportable defect in `prototype/osfr-tools/src/matchmaking.rs` lines 1-800.

What I checked:

- **Reachability.** The `Matchmaking<C, R>` state machine (`new`, `join`, `leave`, `disconnect`, `set_ready`, `tick`, `close_match`) has no caller outside `tests/matchmaking.rs`. The gateway path (`gameplay/matchmaking_route.rs`) only uses `handles`, `Listings` and `route`, and the adapter test `adapter_refuses_join_and_rejects_malformed_known_requests` shows 141/3 join is refused. No client packet reaches `join`, `set_ready` or `tick` today. Any finding here would be a latent issue, and I did not file one.
- **Panics on client input.** `unwrap`s at 319, 367, 477, 523 and 689 sit behind reservation or queue invariants that are maintained inside this window. `begin_ready_check` indexes `self.queues[&queue_id]` with a key taken from the queue map. `offered.replies[0]` is guarded by the `len() != 1` check at 703. `GroupLaunchPacket::header_only` (1356) is only called with sub-ops 14, 15 and 16, all in its accepted set, so its `?` never fails.
- **Atomicity.** `join` validates before it mutates. The `?` returns in `cancel_ready_and_requeue`, `take_formation` followed by `begin_ready_check`, and `start_match` after `ready.take()` only fire on `checked_add` overflow of i32 launch or instance ids, or on invalid configured `RunSpec`. Neither is client-triggerable in practice.
- **Logic against tests.** The ready-timeout requeue, ready-disconnect cancel, leave/disconnect split, team-capacity FIFO assignment and duplicate-join inertness all match the named tests in `tests/matchmaking.rs` (lines 386-538).

Latent observations, not filed because nothing reaches them today:

1. `unique_request_id` (line 750-760) inserts into `used_request_ids` on every `join` and every requeued member and never removes entries. Once `join` is wired to 141/3, a client that repeatedly joins and leaves would grow that set without bound. This is worth a cap or a per-session limit before the adapter is connected.
2. `join` (line 293-308) returns `Duplicate` for a solo entry whose session is already waiting inside a larger group. The test at tests/matchmaking.rs:485 asserts this, so it is probably intended.
3. `remove_session` (line 477-486) does not update `QueueEntry.leader` when the leader leaves a waiting party. Nothing in this window reads `leader`.
