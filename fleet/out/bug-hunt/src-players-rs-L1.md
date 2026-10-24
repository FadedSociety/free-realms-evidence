<!-- fleet job=bug-hunt id=src-players-rs-L1 status=nothing_found turns=7 usd=0.0173 tokens(read,write,in,out)=[125980, 43521, 16, 21230] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/players.rs lines 1-800 of 873

No reportable defects in `prototype/osfr-tools/src/players.rs` lines 1-800. I read the whole window and checked the callers that feed it.

What I checked and why each is not a defect:

- **Panics on client input.** Coordinates and heading are rejected unless finite (`validate_pose`, 654-659; `nearby_sessions`, 222). Cell keys use saturating `as i64` casts (`cell`, 427), and neighbour offsets use `checked_add` (`nearby`, 457-463), so huge finite positions do not overflow. `distance_squared` and `radius_squared` stay finite in f64. `select_nth_unstable_by(cap)` runs only when `len > cap` (497). `self.sessions[id]` indexing (474, 491, 573) is safe because every cell occupant is also in `sessions` on every join, leave and move path.
- **Attachment wire parsing** (`validate_attachment_wire`, 698-732; `read_attachment_i32`, 734-746). Negative counts and lengths are rejected by `usize::try_from`. Offsets use `checked_add` with an upper-bound filter. The row count is capped by `available_rows` (≥24 bytes per row), so the loop is bounded by the 64 KiB input cap. `bytes.len() - 4` (731) is safe because a successful parse implies at least 4 bytes.
- **Unbounded growth.** Presentation size is capped at `MAX_ADD_PC_MESSAGE_BYTES` (691). Per-viewer views are capped by `max_visible_count`. `put_string`'s `expect` (854) cannot fire because `validate` bounds each string first.
- **Atomicity.** `join_with_presentation` runs every check (identity, pose, presentation, duplicate session, GUID ownership) before any mutation (271-285). `update_pose_with_state` validates before mutating and has no fallible step after mutation. `set_presentation` validates before its single write (354-355, where the `unwrap` is on a session just confirmed to exist).
- **Visibility bookkeeping.** I traced the `rerank` and cutoff-refresh logic (506-590) for join, move, zone change and leave, including the removed-subject case. Membership, cutoff and Spawn/Despawn/Position emission stay consistent. Ties use session id as the documented tiebreak, and the radius boundary is inclusive as documented.
- **Trusting the client.** The client-supplied position is accepted as-is by `update_pose_with_state`. The gateway applies `MovementDecision::RejectAndSnapBack` before calling it (`gateway.rs:1547`), so this is not a defect at this layer. `state`/`unknown` are opaque relay bytes by design (377). `set_presentation` and `join` validate `character_guid` against the authenticated snapshot, and the gateway sets it from `state.guid`.

Nothing in the window reaches a panic, unbounded allocation, a half-applied save, or a trusted client value through a path I could demonstrate.
