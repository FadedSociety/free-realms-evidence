<!-- fleet job=note-refresh id=Cave-Results-Score-Binding status=done turns=8 usd=0.0099 tokens(read,write,in,out)=[110946, 34263, 18, 8923] model=claude-haiku-5-5 -->
# notes/Research/Cave Results Score Binding.md

**Verdict:** badly stale in its diagnosis sections (Verdict, Original versus reconstructed, Exact suspected fields, Options). The bug it describes is fixed at the tip. The note's own "Implemented repair" section (lines 58-68) is current and matches the code. The Lua binding, the 39/47 field layout and the test file claims all hold.

**Corrections:**

1. `old:` The panel is bound correctly; one server field carries the wrong value.
   `new:` The panel is bound correctly; in the captured run one server field carried the wrong value. That is fixed at the tip (see "Implemented repair").
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2944-2972` (`end_scores` now passes `won`; `total = if won { OBJECTIVE_AWARD_SCORE } else { 0 }`).

2. `old:` `encounter.rs::end_scores` writes that field as a literal `0` for every run (`for value in [-1, score_type, count, -1, 0]`), so the native panel shows 0 even though the same run sends a 5000-point completed objective in `45/3`.
   `new:` In the captured build `encounter.rs::end_scores` wrote that field as a literal `0` (`for value in [-1, score_type, count, -1, 0]`), so the native panel showed 0 even though the same run sent a 5000-point completed objective in `45/3`. The tip now writes `OBJECTIVE_AWARD_SCORE` on a win and `0` on a loss.
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2960-2967`; the old literal loop no longer exists. `repo:prototype/osfr-tools/tests/encounter_score.rs:180-213` covers the win and loss totals.

3. `old:` - **Current reconstruction.** `encounter.rs::end_scores` deliberately reports zero points ("the current combat rules award no score, so report real defeats without inventing points"), while `objective_complete` sends a local `5000` objective value. The result is the panel's internal contradiction: a 5000-point completed goal and TOTAL SCORE 0.
   `new:` - **Current reconstruction.** `encounter.rs::end_scores_packet` reports the won total from the same local constant that `objective_complete` sends (`OBJECTIVE_AWARD_SCORE = 5000`), and a loss reports 0. The earlier zero-points wording ("the current combat rules award no score") is gone, and the contradiction between the 5000 goal and TOTAL SCORE 0 no longer occurs on a win.
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:112-115` (constant and comment), `:2956-2960` (comment and `total`), `:2980-2983` (`objective_complete`). `grep "award no score"` in `src/` returns nothing.

4. `old:` 1. **`encounter.rs::end_scores`, `scoreTotalScore` row, 5th i32** — hardcoded `0`; this is what must carry the run total.
   `new:` 1. **`encounter.rs::end_scores_packet`, `scoreTotalScore` row, 5th i32** — now `OBJECTIVE_AWARD_SCORE` on a win and `0` on a loss (fixed; this was hardcoded `0` at capture time).
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2960-2963`.

5. `old:` 2. **`encounter.rs::objective_complete` 4th i32** — local `5000` objective value; either it should be summed into (1), or the scoreless policy must drive it to 0 so the panel is self-consistent.
   `new:` 2. **`encounter.rs::objective_complete` value i32** — local `5000` objective award (`OBJECTIVE_AWARD_SCORE`), sent after the objective id and a `0` value. It is the third i32 of the `45/3` body, not the fourth. The same constant now feeds the won total in (1), so the panel is self-consistent on a win.
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2980-2984` (`objective(3, id, 0)` then `extend(OBJECTIVE_AWARD_SCORE)`); the native table in this note shows the same order (objective, extra 0, value 5000).

6. `old:` - **A (consistent non-zero total):**
   `new:` - **A (consistent non-zero total; implemented at the tip: won = `OBJECTIVE_AWARD_SCORE`, loss = 0):**
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2960` and the "Implemented repair" section of this note.

7. `old:` - `src/encounter.rs` `9c0123fe…`-era change (`68cfc114b65ae9f8…` after formatting)
   `new:` - `src/encounter.rs` change (`68cfc114b65ae9f8…` after formatting); the regression file `tests/encounter_score.rs` is `9c0123feebda5efb…`
   `why:` `repo:notes/Reviews/Cave Results Score Repair Review.md:12-13` (the hash table assigns `68cfc114…` to `encounter.rs` and `9c0123fe…` to `tests/encounter_score.rs`).

**Unsure:**
- The `lab/` artifacts (`writer-probe.log` sha256s, `native-results-vectors-v4` hashes, `decode-cave-score-row.ps1`, `ScriptsBase.lua` line numbers under `lab/decompiled`) are outside the repo tip, so I could not verify their hashes. The Lua lines do match: `ui:ScriptsBase.lua:48393` (`setTotalScore`) and `:48401-48409` (`GetTotalScore`, column 5 where column 2 == 4).
- The `tests/encounter.rs` ignored test is named `native_results_close_and_terminal_packets_match_compiled_community_writers` (`repo:prototype/osfr-tools/tests/encounter.rs:777-778`). The note's `native_results_close` filter is a substring of it, so it still selects the test.
- Test counts (`encounter_score` 3/3) match the three `#[test]` functions in `tests/encounter_score.rs`. I did not run the suites.
- The `39/47` handler `009bb030` is cited consistently in the repo notes and `minigame.rs:745`. I did not re-check the disassembly.
