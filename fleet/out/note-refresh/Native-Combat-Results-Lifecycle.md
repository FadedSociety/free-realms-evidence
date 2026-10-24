<!-- fleet job=note-refresh id=Native-Combat-Results-Lifecycle status=done turns=20 usd=0.0224 tokens(read,write,in,out)=[691299, 59229, 42, 16237] model=claude-haiku-5-5 -->
# notes/Research/Native Combat Results Lifecycle.md

**Verdict:** Moderate drift. The packet routing, close handling and terminal ordering match the tip. Two status/data statements are stale: the native v3 acceptance is now recorded as passed, and the won total row is no longer zero points.

**Corrections:**

1. `old:` The patch supplies two original labels: type0 enemies defeated with the actual zero-health enemy count and type4 total score. Both have zero points, matching the current scoreless combat rules/GameOver.
   `new:` The patch supplies two original labels: type0 enemies defeated with the actual zero-health enemy count and type4 total score. The defeat row has zero points. The total row carries `OBJECTIVE_AWARD_SCORE` (5000) on a win and zero on a loss, matching the local objective award; no per-kill points or historical score are invented.
   `why:` repo:prototype/osfr-tools/src/encounter.rs:115 (`const OBJECTIVE_AWARD_SCORE: i32 = 5000;`) and :2958-2963 (`let total = if won { OBJECTIVE_AWARD_SCORE } else { 0 };`, with the total row's points set to `total`). The Cave Results Score Binding note (repo:notes/Research/Cave Results Score Binding.md:62) records the same change.

2. `old:` supplies actual defeat counts and zero-point score rows before presentation.
   `new:` supplies actual defeat counts and score rows (won total 5000, lost total 0) before presentation.
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2944-2951 (`end_scores` passes the actual zero-health count and the win/loss flag) and :2953-2963.

3. `old:` Unit, compiled community writer and nearest gateway integration checks pass; native v3 modal acceptance remains pending.
   `new:` Unit, compiled community writer and nearest gateway integration checks pass; native v3 modal acceptance is recorded as passed in [[../Reviews/Native Combat Results v3]] (runs 163518 win and 163829 loss: a visible score page held about 59 s before the actual Close, then exact 39/18→39/47→39/19 ordering and a genuine 41/109 `[0,1]`).
   `why:` repo:notes/Reviews/Native Combat Results v3.md:3-10 (independent audit table and exact terminal order); repo:notes/Tasks.md:93 (marked done).

4. `old:** These gates are **pending** until the main agent runs the updated release.`
   Note: the exact old text is `These gates are **pending** until the main agent runs the updated release.`
   `new:` These gates were **met** by the v3 runs (see [[../Reviews/Native Combat Results v3]]); the 154226 failure below is the history that led to them.
   `why:` repo:notes/Reviews/Native Combat Results v3.md:10 and :14-16 (ignored39/7 ACK, genuine41/109 only after Close, no repeated reward, same-session journal).

5. `old:` The compiled C# oracle's102-byte Won and Lost row vectors are in `lab/reports/native-results-vectors-v3`; SHA256 `66559e6173093d9d3a42e07d18d4761187a8e20fc058d76e8f7348082b2db923` and `8e69efeb6e47f842a269cd91a6f6246e5dd3489d01d3164de535fd2262cf4820`.
   `new:` The compiled C# oracle's102-byte Won and Lost row vectors were first recorded in `lab/reports/native-results-vectors-v3`; the current bundle is `lab/reports/native-results-vectors-v4/`, which differs only in the won end-scores row's last i32 (the 5000 objective award). Use v4 for the won row.
   `why:` repo:notes/Research/Cave Results Score Binding.md:62-65 (v4 bundle, "identical to native-results-vectors-v3 except the won end-scores row"); repo:prototype/osfr-tools/src/encounter.rs:2960. The v4 hashes were not recorded in the sources I could read, so the SHA256 values are left for the author to update.

**Checked and current:**
- `encounter.rs` Won/Lost terminal path emits 39/18 (`game_over`, :2032, :2524), 39/47 and 39/19 (`present_results` :2570-2574); no zoning there (`out.zoning` is set only in begin :1406, knockout :2535 and retry :2632).
- Retained terminal encounter and `results_presented` suppression: `exit()` :2594 skips the duplicate Remove; reset in `reset_session` :1337, called by retry :2629, begin :1396, and exit :2599; `on_zone_ready` :1485.
- 41/109 acceptance (:1611-1626): length 12, first header 0 or the authored encounter id, and the exact current instance. Only 26/42 terminal close (:1592-1602), 41/109 and the guide exit reach `exit()`. 39/7 is only a comment in `encounter.rs:706` and `minigame.rs:779`; it does not exit.
- Close packet is 12 bytes (`close_packet(0, 1)` checked by `tests/encounter.rs:782-783`).
- Private test `native_results_close_and_terminal_packets_match_compiled_community_writers` exists (`tests/encounter.rs:776-778`, ignored unless `OSFR_NATIVE_RESULTS_VECTORS` is set). `tests/opening_gateway.rs:110-112` has one private test, ignored by design.

**Unsure:**
- `All14 ordinary encounter tests pass` (the line as written, with no space). `tests/encounter.rs` has 16 non-ignored `#[test]` functions plus 2 ignored private ones (lines 86 to 694 and the two ignored at 715 and 776). I did not find a source for a count of 14. The count may come from a different test run or may cover other modules, so I did not correct it.
- Locale lookups for `scoreEnemiesDefeated`→117298 and `scoreTotalScore`→117296 returned nothing, so I could not confirm the ids from the locale table. The Review (repo:notes/Reviews/Native Combat Results v3.md:12) does name the same two original labels.
- The `lab/` artifacts (trace scripts, fixtures `lab/state/native-combat-results-v3`, the vector hashes and the 154226 proof) are not in the repo, so I could not verify them.
- The client-side claims (for example `00c172c0`→`008d2730`→`009bd240`→`008a31a0`, the original Lua Logger default, `ScoreScreen:Hide2` in HUD.showMain) are client facts and I did not check them against the decompiled client.
