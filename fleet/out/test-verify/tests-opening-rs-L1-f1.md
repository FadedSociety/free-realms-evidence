<!-- fleet job=test-verify id=tests-opening-rs-L1-f1 status=done turns=10 usd=0.0102 tokens(read,write,in,out)=[120213, 26665, 22, 11295] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/opening.rs:498

**Verdict:** `refuted`

The narrow factual premise is right: the last check at `tests/opening.rs:499` is weak. Once `active_stage()` is `None`, `handle_command("opening turnin")` skips `on_interaction` and returns `status()` (`src/opening.rs:550-586`, `:541-546`), which never grants rewards. But the claim that the test "cannot catch" a re-grant-after-reload regression does not hold, for these reasons.

**Evidence**

1. **A post-reload replay of a completed turnin exists in the same test.** `engine` is reloaded at `tests/opening.rs:115`. Later, on that reloaded engine:
   - `:129-131`: stage 11's turnin (guid 3) completes the opening.
   - `:133`: `assert!(engine.on_interaction(3).unwrap().rewards.is_empty());`

   This replays the completing trigger of a finished stage after reload. `on_interaction` (`opening.rs:623`) routes to `on_event` (`:667/:669`). With no active stage, `on_event` returns at `:744-747` before any reward code. A regression that re-grants a completed turnin's reward would make `:133` fail.

2. **Reload-then-replay also happens earlier.** At `:117`, after the reload at `:115`, `on_interaction(1)` is replayed and asserted reward-free. At `:90`, after the reload at `:89`, the same pattern appears.

3. **Load rejects the `rewarded` regression the claim names.** `OpeningEngine::load` returns `Err` when `progress.rewarded != progress.completed` (`src/opening.rs:295-298`). A change that drops `rewarded` across load therefore fails the `.unwrap()` at `:89`, `:115` or `:481`. `:268-271` also pins that a corrupted `rewarded` flag is rejected.

4. **Private twin (`:367`, ignored with a stated reason).** This does not count against the gate. Within its loop, every reward goes through `assert!(rewarded.insert(reward.stage_id))` at `:460` and `:473`. Any duplicate re-grant emitted while a later stage is processed after a reload trips that assert. After the loop, `:494-497` also checks that exactly 17 stages are `completed && rewarded`.

**Caveat on the proposed fix.** `rewarded.len() == 17` is not safe as stated. Rewards are pushed only when `coins != 0 || !items.is_empty()` (`src/opening.rs:860-862`), so the set can hold fewer than 17 entries if any stage has an empty reward. The existing `:494-497` flag count is the correct check.

**Minimal fix (optional, not needed to refute):** replace the vacuous `:499` with an explicit replay of a completed turnin on the reloaded engine, e.g. `assert!(reloaded.on_interaction(<stage 10 turnin guid>).unwrap().rewards.is_empty())`, and assert `state` is unchanged before and after. Note that `:499` only checks something once `on_interaction` is actually called on a completed turnin, and `:133` already does this for stage 11.
