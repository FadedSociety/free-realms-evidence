<!-- fleet job=bug-hunt id=src-gameplay-jobs-rs-L1 status=nothing_found turns=24 usd=0.0251 tokens(read,write,in,out)=[817250, 53640, 50, 20351] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/jobs.rs lines 1-225 of 225

No reportable defect in `prototype/osfr-tools/src/gameplay/jobs.rs` lines 1-225.

What I checked:

- **Panics on `unwrap` (lines 33, 34, 117, 123, 124, 130, 161-179, 192-209):** every `profiles.as_ref().unwrap()` is guarded by a caller or by an earlier check. `stage_job_selection` returns early when `profiles` is `None` (150-152). `learn_job` maps `None` to `Unavailable` (198-200). `begin_kart_race` and `begin_derby` both require profiles (npc.rs:864-867, derby_session.rs:106-109). `restore_job` is only reached with a `previous_job` recorded by those entries. The opening path that reaches the `26/13` branch at gameplay.rs:4379 requires profiles to load (gameplay.rs:683-685), so that unwrap is also unreachable with `None`.
- **Client-controlled job id:** the `26/13` handler passes the client id into `stage_job_selection` (gameplay.rs:4376, 5359). Line 153 rejects any id not in `profiles.state().unlocked`, and `activate` (profiles.rs:411-417) checks it again. `starter_items` uses `.get(..).unwrap_or_default()` (profiles.rs:199-205), so no panic.
- **Atomicity:** `stage_job_selection` (145-187) clones `self` and assigns back only on success. `learn_job` runs under `commit_if_changed` (npc.rs:58-68, 610), and a refusal leaves `changed` false. `restore_job` runs on the live state in the kart/derby exit paths (gameplay.rs:2683, derby_session.rs:164, 228). Its partial mutations are discarded only if the request-level gateway clone is dropped on `Err`. I did not verify that, and it is outside this window.
- **Swallowed equip error (line 47, `.ok()`):** a failed equip falls through to a fresh grant, but the second `equip_owned_definition` at line 56 uses the same first-match item and fails the same way, so the `?` returns `Err` and the staged copy is discarded. No duplicate persists.
- **Inventory-event double counting:** `give_starter_outfit` emits events itself (line 20). `learn_job` and the `26/13` path do not diff again, so events are emitted once.
- **Attachment checks:** `ensure_outfit`'s `starts_with(&0i32.to_le_bytes())` (77) correctly tests a zero attachment count. `has_required_profile_slots` (inventory.rs:678-685) is checked after the outfit repair in `stage_job_selection` (167-174).

Not reported: `reuse_owned=false` at npc.rs:876 and derby_session.rs:115 grants fresh starter copies on a job's first unlock. This is explicit in the code and comments, is one-time per job, and I could not show an exploitable gain.
