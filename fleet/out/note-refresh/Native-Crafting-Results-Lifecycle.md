<!-- fleet job=note-refresh id=Native-Crafting-Results-Lifecycle status=done turns=15 usd=0.0158 tokens(read,write,in,out)=[419932, 49348, 32, 10854] model=claude-haiku-5-5 -->
# notes/Research/Native Crafting Results Lifecycle.md

**Verdict:** minor drift. One sentence is stale because a later change (and its acceptance record) landed after the note was written. The rest of the code claims hold at the tip.

**Corrections:**

- `old:` Ui.QuitMiniGame instead has a separately proven39/6 path; adding and accepting ordinary pre-win Quit remains a next cancellation task.
  `new:` Ui.QuitMiniGame instead has a separately proven39/6 path; ordinary pre-win Quit is now handled: a pre-win run is cancelled on 39/6 without a transaction, while terminal Won/Lost runs wait for the 26/42 Close. Native Cooking Playing Quit was accepted (see Reviews/Native Crafting Quit 005748).
  `why:` repo:prototype/osfr-tools/src/cooking.rs:386-399 (sub 6 calls `self.cancel()` for Offered/Playing runs only, with no transaction); repo:prototype/osfr-tools/src/gameplay/ordinary_quit_routing.rs:39 (test `ordinary_cooking_quit_cancels_atomically_and_malformed_replays_roll_back`); repo:notes/Current Progress.md:118 (Native Cooking Playing Quit accepted).

**Checked and holding (no change needed):**
- Cooking and Smelting terminal win send `OnGameWonMsg`, then `results()` = 39/18, 39/47 (one `scoreTotalScore` row), 39/19; stars sent as 0 (`repo:prototype/osfr-tools/src/cooking.rs:533-534, 751-776`; `smelting.rs:518-519, 701-716`).
- Forging keeps its delayed `FRServer_GameOver` callback before sending the terminal sequence (`repo:prototype/osfr-tools/src/forging.rs:641-651`).
- `results_presented` is a service field, not part of the state, and suppresses duplicate presentation and the second 39/19 on Close (`cooking.rs:342-347`, `smelting.rs:330-335`, `forging.rs:655-658`).
- 39/7 is a no-op while terminal state is retained (`cooking.rs:381-385`).
- Terminal Smelting ScoreSet replay cannot change the score (`smelting.rs:484-490`).
- The 26/42 Close requires exactly four bytes (`repo:prototype/osfr-tools/src/gameplay.rs:4277-4278`; the exact match `[26,0,42,0]` in `minigame.rs:372`).
- Forging's "thirty crafting tests" count matches the independent-review record (`repo:MODLOG.md:313`).

**Unsure:**
- "Thirty ordinary crafting tests pass": the per-file `#[test]` counts are 4 in cooking, 4 in smelting and 4 in forging, and the 30 figure rests on the MODLOG record. I did not run the suite.
- "Current Cooking variant has six hidden completion actors": I found no test in the tree that asserts six; the three-actor fire-only expectation is confirmed by `notes/Reviews/Native Crafting Results Independent Review.md:27`.
- "Native acceptance of the new finish sequence remains pending": `notes/Current Progress.md:106` records a fresh native Cooking run with the results Close and Mae turn-in accepted. The pending gate is the new branch, so this may still be correct, but I could not confirm it.
- The `../lab/reports/...` proof paths and SHA256 values are outside the repo, so I could not check them.
