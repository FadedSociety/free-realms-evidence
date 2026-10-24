<!-- fleet job=bug-hunt id=src-soccer-service-rs-L801 status=nothing_found turns=15 usd=0.0205 tokens(read,write,in,out)=[359307, 54014, 32, 20221] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soccer_service.rs lines 801-1063 of 1063

No reportable defect in `prototype/osfr-tools/src/soccer_service.rs` lines 801-1063.

What I checked, and why each path is clean:

- **`handle_client` (919-978):** the sender is checked against `sessions` first. `apply_state_request` requires `sender == request.player` (270), and `apply` refuses a mismatch before any state read (soccer_match.rs:598). Kick power, direction, and aux are bounded by `state_request_intent` and by `authority.apply` (soccer_match.rs:690-693). The probe clone is validated before the live match is touched, and `unit()` runs on the probe before any live mutation. Both `apply` and `apply_state_request` mutate nothing before their error returns, so the "refusal leaves the match untouched" claim holds. `pass_target` is always `None` from the only caller (soccer_entry.rs:432), so the pass path is refused rather than trusting client input.
- **`tick` (846-909):** `advance` is the only fallible step before the runs and relay bookkeeping, and it rejects `dt` outside `(0, max_tick]` before mutating. The caller clamps `dt` to 0.25 s (soccer_entry.rs:452), which equals `max_tick` (soccer_match.rs:129), so it is accepted. The Goal, Restart, and Possession branches are mutually exclusive and do not index client-sized data.
- **`start`, `second_half`, `timeout`, `disconnect` (804-840):** each has a guard, and the mutation that follows (`kickoff`, `start_second_half`) is the last fallible step. The `sessions.is_empty()` case is handled.
- **`unit`, `entry_scene`, `entry_frame` (1002-1040):** the length and finiteness checks run before division, and the scene is validated by `zone_transition::encode`. All scene values are constants.
- **`wire_from_inner` (1046-1060):** the length check precedes the byte indexing, and the `u32` length conversion is checked. The output header matches `soccer::encode` and what `decode` accepts (`outer` 5, `flag`, `u32` length, body).
- **`restore`/`snapshot` (980-990):** these only delegate. `SoccerService::restore` has no callers in `src`, so it is not reachable from a client packet or a save.

Weaker observations I did not report because they are not clear defects: `second_half` does not reset `last_holder`, so the next Possession event can carry a stale `previous`. This is consistent with the documented "last reported holder" semantics. Also, `soccer_entry.rs` passes gateway `now_ms` as f32 seconds, which loses ms precision after about 4.6 hours of uptime. That is outside this window and does not affect the match logic.
