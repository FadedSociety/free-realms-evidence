<!-- fleet job=note-refresh id=Pieces-069-Quest-turn-in-transactions status=done turns=12 usd=0.0129 tokens(read,write,in,out)=[238894, 37658, 26, 11549] model=claude-haiku-5-5 -->
# notes/Research/Pieces/069 Quest turn-in transactions.md

**Verdict:** minor drift. The file paths, test counts (9 Rust vectors, 11 Python tests), bounds, `consider` order, opcode constants and the "not wired into gameplay.rs" status all hold at the tip. Two statements about how the legacy quest path grants rewards are now false, and the wiring caveat that depends on them is stale.

**Corrections:**

1. `old:`
```
`quests.rs::enemy_defeated` sets `completed`
and `rewarded` in the same step as the reward, so the lead must pass the pre-turn-in progress
(or split "ready" from "rewarded") for `consider` to see a first request.
```
`new:`
```
`quests.rs::enemy_defeated` sets `completed` and queues the reward but leaves `rewarded` false. `gameplay.rs::apply_quest` flips `rewarded` through `acknowledge_reward` only after the inventory grant succeeds, so a first turn-in request reaches `consider` as completed and unrewarded. The lead only needs to pass the progress resolved by `quest_id`; no ready/rewarded split is required.
`why:` `repo:prototype/osfr-tools/src/quests.rs:463-504` (`enemy_defeated` sets `progress.completed = true` at 492, pushes the `QuestReward`, and never touches `rewarded`); `repo:prototype/osfr-tools/src/quests.rs:344-356` (`acknowledge_reward` is the only writer of `rewarded = true`); `repo:prototype/osfr-tools/src/gameplay.rs:5413-5420` (`apply_quest` calls `acknowledge_reward` after `grant_bundle` succeeds).

2. `old:`
```
`gameplay::apply_quest` and `gameplay::apply_opening` grant the
coins first and then each item one at a time, so a failure or a crash in the middle leaves a quest
that says `rewarded = true` with a partial or missing reward
```
`new:`
```
`gameplay::apply_quest` and `gameplay::apply_opening` both hand the bundle to `Inventory::grant_bundle`, which stages the coins and then each item on a clone and commits them all or nothing. `apply_quest` sets `rewarded` only after that succeeds, so an in-process failure leaves no `rewarded = true` with a partial reward.
`why:` `repo:prototype/osfr-tools/src/inventory.rs:1045-1059` (`grant_bundle` clones state, grants coins then each item, and assigns `*self = staged` only at the end); `repo:prototype/osfr-tools/src/gameplay.rs:5416-5420` (`apply_quest`); `repo:prototype/osfr-tools/src/gameplay.rs:5196-5208` and `4838-4839` (`grant_reward` and `apply_opening` both route through `grant_bundle`).

3. `old:`
"Both quest engines in this crate flip the quest's completion flags and hand back a reward bundle in
the same step that they apply it."
`new:`
"Both quest engines in this crate flip the quest's completion flag and hand back a reward bundle. The legacy quest engine (`quests.rs::enemy_defeated`) does not set `rewarded`; `gameplay::apply_quest` sets it after the grant."
`why:` `repo:prototype/osfr-tools/src/quests.rs:492-497` and `repo:prototype/osfr-tools/src/quests.rs:354`. This is the premise behind correction 2.

**Checked and holding (no change):**
- `src/restoration/piece_069.rs` exists; `tests/piece_069.rs` has 9 `#[test]` functions and includes the module by `#[path]` (`tests/piece_069.rs:27`).
- `tests/pieces/test_piece_069.py` has 11 test methods; `scripts/pieces/piece_069.py` exists.
- Bounds match `piece_069.rs:96-102` (262,144 bytes, 4,096 records, 16 items, `i32::MAX` coins, 10,000,000 XP).
- The `consider` order matches `piece_069.rs:330-384`.
- The opcode constants match the note's list (`piece_069.rs:74-91`).
- The module is not registered in `lib.rs` and not referenced from `gameplay.rs` (the note's "not wired" status holds).

**Unsure:**
- `scripts/cargo.ps1 test --lib` "24 passed" and the checker's "26 checks" could not be verified without running them. I counted 9 cooking check IDs in `scripts/pieces/piece_069.py` but did not count the Bartle checks.
- The `lab/...` evidence paths and the decompiled `BaseQuestPackets.cs` could not be confirmed; `lab/` is not in the readable roots.
- `Notes/Reviews/...` in the note's text is capitalized differently from the actual `notes/Reviews/Native Cooking Finish and Mae 171251.md`. That is cosmetic, so I did not correct it.
