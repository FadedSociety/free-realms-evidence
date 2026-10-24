<!-- fleet job=bug-hunt id=src-encounter-shared-rs-L1 status=nothing_found turns=19 usd=0.0250 tokens(read,write,in,out)=[572219, 56830, 40, 24311] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/encounter/shared.rs lines 1-647 of 647

No reportable defect in `prototype/osfr-tools/src/encounter/shared.rs` lines 1-647. I read the whole window and the callers that matter: `gameplay.rs:470-570` (`handle_shared_field`), `gameplay.rs:2291-2297` (`shared_action` call site), `encounter.rs:1779-1800` (`enemy()`), `encounter.rs:1846-1990` (`strike_damage`), `encounter/skills.rs:116-200` (`job_ability`) and `432-470` (`tick_job_effects`), `encounter/field_rewards.rs:40-69` (`KillCredit::retain_after_leave`), and `npc_interaction.rs:1034-1042` (the 26/8 decoder).

Candidates checked and dropped:

- **`shared_action` Ability branch (`shared.rs:347-379`) skips `known(target)`, unlike the Interact/Select branches.** Not exploitable: `gameplay.rs:530` calls `restrict_to(known)` before any shared action, and `enemy()` (`encounter.rs:1785`) only returns `present` enemies, so an out-of-interest guid is never hit.
- **Length and index handling in `shared_action` (`shared.rs:347-402`).** Every slice is preceded by a length check, and the `inner[12]` read only happens when the length is already 13. The 26/8 layout matches `npc_interaction::decode_npc_interact_26_8`.
- **`with_shared_fields` (`shared.rs:406-453`) restore on error.** Restoration runs before `result` is returned and there is no `?` in between. The `gameplay.rs` callers also run `restore_presence` before propagating errors.
- **`take_shared_fields` keeps `attacks`, `moving` and `kills` on the engine (`shared.rs:300-320`).** This is deliberate and pinned by the test at `shared.rs:596-640` (the "selective transfer" assertion), so it is not a defect.
- **`retain_casters` (`shared.rs:165-192`) and `set_active_quests` (`shared.rs:213-223`).** The TTL, presence and departure rules match their doc comments. The `||`/`&&` precedence on line 217 is ambiguous but consistent with the "engaged enemies stay present" intent, so I did not report it.
- **`due`, `position`, `respawn_at`, `initialization`, `interest_candidates`.** No client-controlled index, unwrap or overflow reaches them.
- **Atomicity of job-ability and DoT errors.** `job_ability` returns Err only before any mutation (`valid_position`), and `strike_damage` always returns Ok, so the partial-mutation-then-error path is not reachable.
