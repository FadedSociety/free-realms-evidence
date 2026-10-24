<!-- fleet job=bug-hunt id=src-kart-racing-rs-L1 status=nothing_found turns=11 usd=0.0138 tokens(read,write,in,out)=[252305, 38678, 24, 12798] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_racing.rs lines 1-724 of 724

No defect found in `prototype/osfr-tools/src/kart_racing.rs` lines 1-724 that I can tie to a line and show is reachable from a client packet or a save.

What I checked:

- **Frame decode (196-231):** the length gates (`len < 7`, `inner.len() < 4`) come before every index and slice, and `declared == available` is enforced. Nothing panics on short or odd input.
- **Subtype-11 name (238-255):** `payload.len() < 8`, then `checked_add` and `end > len` before slicing. NUL and UTF-8 are rejected. No unwrap on client data.
- **`TrackLayout::validate` (325-353):** bounds checks run before the O(n²) duplicate scan, so the scan is capped at 512 entries. Laps are bounded by `MAX_LAPS`.
- **`on_checkpoint` (517-565):** the checkpoint id is matched against the server's `expected` value. In the service caller (`kart_service.rs:2585-2590`) `got = expected`, so the client does not choose the id. The counters (`next_index`, `laps_completed`) stay bounded because phase becomes `Finished` at `laps`. Each branch mutates state only on the accept path, with no error after mutation.
- **Timing:** `now_ms` is server-side (`kart_service.rs` passes the gateway clock), so clients cannot forge lap time or move the clock backwards. The `<` comparisons match their doc comments.
- **`observe_racer_state` (570-577):** `saturating_add`, no progress change.
- **`finish` / `abandon` / `claim_reward` (582-613, 706-723):** `claim_reward` is gated on `Finished` and full laps, and `reward_claimed` is set only on the priced grant path. `abandon` cannot overwrite `Finished`. The grant path in `kart_rewards.rs:273-337` (outside my window) restores a staged copy and commits it only after every grant succeeds, so a refusal leaves the live session untouched.
- **`restore` (639-698):** `next_index` and `laps_completed` are range-checked before `checkpoints[...]` indexing. `checkpoints.len() >= 1` is guaranteed by `validate`, and `next_index - 1` cannot underflow because `next_index != 0` on that branch. The coherence rules line up with what `on_checkpoint` and `abandon` can produce. The only snapshot shapes they accept but normal play never produces (for example `Abandoned` with `reward_claimed`) cannot reach a grant, because `claim_reward` requires `Finished`.
- **`LobbyGameDefinition::encode` (152-164):** the capacity and field count match the doc (5 × i32 per entry plus 16 trailing zero bytes). The `as i32` cast is on a server-built list, not client input.

Possible concern, not reported: a one-checkpoint track would let every pass count as a lap. The track layouts come from lead-supplied content (`kart_service.rs:1340`), not from clients, so I did not treat it as a defect.
