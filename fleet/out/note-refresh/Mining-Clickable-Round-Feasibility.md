<!-- fleet job=note-refresh id=Mining-Clickable-Round-Feasibility status=done turns=14 usd=0.0160 tokens(read,write,in,out)=[329757, 43686, 30, 14485] model=claude-haiku-5-5 -->
# notes/Research/Mining Clickable Round Feasibility.md

**Verdict:** badly stale. The status line, the blocker section and the dependency section still describe the state before run 3 and the short-idle repair. Three code citations have also moved, and one stated engine behaviour is now false.

**Corrections:**

1. `old:` the clickable evaluation itself is **not yet run**
   `new:` the clickable evaluation has been run (run 3, reconstructed rates 10/25/50 %): no rate reached quotas, every attempted click was accepted, and the completion handshake was not driven
   `why:` the run 3 table (note lines 151-158) records trials; the status line is the first thing readers see.

2. `old:` Piece 028 is repairing it to min-1 idle / min-3 chain (RED/GREEN). New trials must wait for
   `new:` The short-idle repair has landed at `8b32d7c5…`, not under piece 028 (which is the housing save migration). Trials may now run against
   (Line 139 then reads "that accepted pin." and should stay as is.)
   `why:` `repo:prototype/osfr-tools/src/mining.rs:2267-2269` (`idle_points`, floor 2); `repo:notes/Research/Mining Short Idle Acknowledgements.md:1-6, 67-68`; `repo:notes/Reviews/Mining Short Idle Acknowledgement Review.md:64-72`; piece 028 is `notes/Research/Pieces/028 Housing save migration.md`.

3. `old:` the engine's `coordinates()` refuses an idle report carrying fewer than three tile pairs
   `new:` the engine's idle parser `idle_points()` accepts one or more tile pairs; only the chain parser `coordinates()` keeps the three-tile floor (this was the pre-8b32 behaviour)
   `why:` `repo:prototype/osfr-tools/src/mining.rs:2258-2269` (`coordinates` → `coordinate_list(list, 6)`; `idle_points` → `coordinate_list(list, 2)`); `mining.rs:801-802` uses `idle_points`.

4. `old:` a one- or two-tile `OnIdleMsg` therefore aborts with `malformed mining coordinate list`.
   `new:` a one- or two-tile `OnIdleMsg` is accepted since the short-idle repair; the `malformed mining coordinate list` refusal now applies only to odd, empty-interior or under-floor lists.
   `why:` `repo:prototype/osfr-tools/src/mining.rs:2249-2251, 2267-2269`; `repo:notes/Research/Mining Short Idle Acknowledgements.md:30-32`.

5. `old:` definitions `950..=953` at `mining.rs:1054`/`:1059`
   `new:` the constants at `mining.rs:73-76`; the definition validation at `mining.rs:1097-1098` (values outside 950..=953 refused) and `:1092-1095` (900..=949 refused)
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1054` and `:1059` are now the `write_content` game-id check and `profile_id`, not powerup definitions.

6. `old:` the refusal of a falling clickable at `:1523`/`:1530`
   `new:` the refusal of a falling clickable at `:1576`/`:1580` (in `collect_fall`, which starts at `:1554`)
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1576-1580` (`mining clickable powerup cannot fall`); `:1523`/`:1530` are now the gravity move code.

7. `old:` the `950..=953` handling at `:2002`
   `new:` the inbound click arm `["OnActionMsg", index, list]` at `:776`, dispatching through `apply_powerup_action` to the per-powerup handlers at `:1801-1806`; `:2002` is now inside `shatter`'s neighbour walk
   `why:` `repo:prototype/osfr-tools/src/mining.rs:776-790, 1789-1806, 1994-2002`.

8. `old:` The driver has no click input path yet, and the click-target generation must come from the recovered
   `new:` Runs 1-3 added a click input path to the private driver (run 3: every attempted click accepted); the click-target generation must still come from the recovered
   `why:` note run 3 table (lines 151-158); the sentence is in the blocker section that predates runs 1-3.

9. `old:` `4abe6b07f8edf52798ce810cde752a58fb959c30fcb639675371a041e463eb46`
   `new:` `8b32d7c5cf646f794d73b4f4426ecd053f5273f3cf63a419429e5512d625c83d` (current `src/mining.rs` pin; the 4abe pin is the superseded run 1/2 engine)
   `why:` `repo:notes/Research/Mining Short Idle Acknowledgements.md:67-68` and `repo:notes/Reviews/Mining Short Idle Acknowledgement Review.md:66`. I did not recompute the tip file hash myself (no hashing tool); this rests on those two notes.

**Unsure:**
- Run 3 counts, collected values, wall times, the `lifecycle-handshake.json` receipt and the `lab/reports/...` paths (note lines 151-166, 176-178) could not be checked: `lab/` is not in the repo.
- `fall row PLAYABLE_MAX = 10` (line 17): no `PLAYABLE_MAX` in `repo:prototype/osfr-tools/src/mining.rs`; it looks like a private-harness detail.
- "A parameter-bearing NextLevel is refused" (line 178) is consistent with the exact-match `["OnNextLevelMsg"]` arm at `mining.rs:870` and the default refusal at `:913`, so I left it as is.
- Line 133 (`stays disabled until root confirms the pin`) describes the run 2 script state; I could not check the script in the repo.
