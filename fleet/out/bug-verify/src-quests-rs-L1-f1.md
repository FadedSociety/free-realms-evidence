<!-- fleet job=bug-verify id=src-quests-rs-L1-f1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[21094, 15022, 10, 4628] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/quests.rs:289-328

**Verdict:** confirmed (narrow, not remote)

**Severity if confirmed:** low. The defect is real, but it needs a content edit that lands exactly on the saved counts, or a hand-edited save. No remote packet can reach it, and it corrupts nothing. Its effect is that one character's login fails until someone fixes the save.

**Evidence:**
- **Module tree:** `quests.rs` is live. `src/lib.rs:74` has `pub mod quests;`, and `gameplay.rs:28` and `gameplay.rs:1154` use `QuestEngine::load(directory, quests)?` inside the `Gameplay` load path. `gateway.rs:817` and `gateway.rs:1080` call `Gameplay::load` with `?`, so a load error propagates.
- **The logic in the report holds.** For counts `[3]`, required `3`, `accepted: true`, `completed: false`:
  - The repair at `quests.rs:290-297` does not fire. `count > required` is false, and the `completed && count != required` clause needs `completed`.
  - Validation at `quests.rs:320-325` runs `progress.completed != all(count == required)`, which is `false != true`, so it returns `Err(invalid("saved quest progress is inconsistent"))` at line 327.
  - So the comment at line 289 ("Objective edits must not prevent login") is contradicted for this case.
- **Remote reachability: refuted.** The only writes to `counts` are the load-time repair (`quests.rs:299`) and the increment in `enemy_defeated` (`quests.rs:473-478`, guarded by `*count < goal.required`). The only write to `completed` is `quests.rs:492`, which runs when every goal is met inside `enemy_defeated`. Play therefore cannot produce "all goals met, not completed". The inconsistent state needs a content edit that lowers `required` to exactly the saved count, or a tampered save.
- **Tests:** `tests/quests.rs:293-308` covers counter drift and the rewarded-flag rejection. It does not cover the all-equal, not-completed case.

**Corrected fix:** the suggested fix is questionable. Adding `progress.completed != all_goals_met` to the repair at 296 would reset a quest whose goals are now all met to zero counts. That wipes progress the player earned. A better option is to treat the save as completed by the edit. That needs a deliberate decision about whether the reward is paid, because paying it on load risks paying twice. Either way, the validation at 320-325 should not hard-fail. Add a test for the all-equal, not-completed case.
