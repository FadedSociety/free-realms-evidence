<!-- fleet job=test-audit id=tests-bot-acceptance-1016-rs-L1201 status=done turns=6 usd=0.0064 tokens(read,write,in,out)=[66313, 22624, 14, 5804] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bot_acceptance_1016.rs lines 1201-1780 of 1780

Window reviewed: `bot_acceptance_1016.rs` 1201-1780 (read in full, plus the helpers it calls: `save_when`, `wait_log`, `log_outcomes`, `barrier`, `worn`, and the gateway quest-journal handler in `gameplay/npc.rs`). The objective-breadcrumb test (1301) and the handshake test (1747, `#[ignore]` with a reason) hold up: the objective tests compare full `gameplay` saves before and after each refusal, and the ignored test is labelled. Findings are below.

- **[medium] prototype/osfr-tools/tests/bot_acceptance_1016.rs:1624 neighbours_see_equipment_and_job_changes_live - "A replay changes nothing" (and the doc at 1569-1571 says a replay "leave[s] the saved state alone") is checked only for the absence of a broadcast.**
  - Why it cannot catch a regression: a server change that re-applies the equip on replay (for example a second `equipment` row write or a bumped counter, or a swap to a different row with the same item) and sends no 35/6 would still pass, because nothing reads the save after the replay.
  - Fix: take `let before = rig.save(0)["gameplay"].clone()` before `raw(&mut a, &equip)`, then after the 2 s wait and a barrier request (`ask(&mut a, "realm here", "Zone ")`, as `barrier()` does at line 640), assert `rig.save(0)["gameplay"] == before`.

- **[medium] prototype/osfr-tools/tests/bot_acceptance_1016.rs:1651-1664 neighbours_see_equipment_and_job_changes_live - the refused locked-job switch is said to leave the save alone, but only `profiles.active` is compared.**
  - Why it cannot catch a regression: a gateway change that refuses the profile switch but still writes equipment, inventory or other gameplay fields for profile 45 (or resets equipment rows) would pass, since only the active-profile field is read. The 2 s `is_err` check only covers broadcasts, not persisted state.
  - Fix: snapshot `rig.save(0)["gameplay"]` before `raw(&mut a, &refused)`, wait for a barrier, and assert full `gameplay` equality, as the objective test does at lines 1339-1343.

- **[low] prototype/osfr-tools/tests/bot_acceptance_1016.rs:1259-1267 quest_journal_selection_persists_across_relog - "A forged id changes nothing" checks only `selected_quest_id`.**
  - Why it cannot catch a regression: a forged 47/12 that adds or alters another quest (status, counts, or the active quest list) while still leaving `selected_quest_id` null would pass.
  - Fix: capture `save["gameplay"]["npc_quests"].clone()` before the forged `select(999_999)` and compare the whole `npc_quests` object after the "rejected" log line and a barrier.

- **[low] prototype/osfr-tools/tests/bot_acceptance_1016.rs:1282-1284 quest_journal_selection_persists_across_relog - the restored-selection wait matches the server's Debug-formatted request string (`format!("quest_id: {}", plan.quest)`).**
  - Why it matters: this is incidental log formatting. Any change to the request's Debug output (field order, spacing, or a rename) breaks the wait with a timeout unrelated to persistence, and the test then fails on churn rather than on the relog behaviour it claims to prove.
  - Fix: match on the structured fields the log already carries (the `outcome` plus the decoded quest id, if the event records one), or on `event` and `outcome` alone with the `selected_quest_id` save check that follows doing the real work.
