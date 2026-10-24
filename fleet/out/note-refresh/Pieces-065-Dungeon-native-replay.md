<!-- fleet job=note-refresh id=Pieces-065-Dungeon-native-replay status=done turns=23 usd=0.0307 tokens(read,write,in,out)=[1054728, 82979, 48, 19457] model=claude-haiku-5-5 -->
# notes/Research/Pieces/065 Dungeon native replay.md

**Verdict:** minor drift. The file paths, module wiring, wire table, gate rules, test names and checker flags all match the tip. One sentence about how gates report missing rows is overbroad and is wrong for several gates.

**Corrections:**

1. `old:`
   recovered. A gate fails on contradictory rows and reports `NotEvidenced` when the rows are
   absent, so a missing capture cannot pass.
   `new:`
   recovered. A gate reports `NotEvidenced` when the capture lacks the rows or snapshots its rule reads from the start (no `31` into the cave, no `41/114`, no `41/107`, no `41/2`, no session snapshot). It reports `Failed` when a row its rule needs is missing after the event that requires it: no voluntary `26/10` start or attack after the zone-ready, no enemy movement before the trigger, no `39/47` rows after a win, no close request after the results. A missing capture still cannot pass, because every gate needs its rows.
   `why:` `prototype/osfr-tools/src/restoration/piece_065.rs:575-579` (no voluntary trigger returns `failed`), `:645-657` (no enemy motion returns `failed`), `:775-779` (no `39/47` rows returns `failed`), `:822-826` (no close request returns `failed`), versus `:509-562` (absent zone, launch, ready and enter rows return `not_evidenced`). The test at `prototype/osfr-tools/tests/piece_065.rs:330-339` asserts `Failed` for missing score rows.

**Checked and current** (no change needed):
- Module path `src/restoration/piece_065.rs` exists. It is not registered in `src/lib.rs` (`lib.rs` has no restoration or piece_065 entry). The owned test includes it via `#[path = "../src/restoration/piece_065.rs"]` (`tests/piece_065.rs:30`).
- Wire table: all 41/x, 39/x, 32/7, 32/9, 35/5, 26/10, 125, 38/1, 31, 10 and 13 rows match `REPLAY_WIRE` (`piece_065.rs:85-219`), including the PR 74/76/77 source attributions. `41/109` is recorded as a client-to-server capture row, and its body `29006d000000000001000000` decodes to `[41,0,109,0, 0, instance 1]`.
- Selections 101 exit, 103 attack and 104 start match `SELECTION_*` (`piece_065.rs:56-58`) and `src/encounter.rs:116-119`.
- Gate order and rules match `piece_065.rs:502-922`: fresh entry, combat, boss (exactly one tallest enemy, 32/9 display, 0 HP), rewards (last `39/18` must be a win, every enemy dead, `39/47` equal to the enemy count, 411 in the rewarded set), exit (41/109 or 101, then a world return, session ends in zone 0 with no encounter), and reconnect (same fingerprint, rewarded set unchanged, starts in the world).
- The retry rule (grade the last `39/18`) is at `piece_065.rs:486-494`.
- Test names exist: `an_earlier_loss_does_not_invalidate_the_winning_attempt` (`tests/piece_065.rs:212`), plus the wire, synthetic, per-gate and preserved-transcript tests (`:68-515`). Python tests `test_end_to_end_bundle_for_the_v2_results_run` and `test_negative_control_rust_constant_drift_fails` exist in `tests/pieces/test_piece_065.py:148` and `:184`.
- Files exist: `scripts/pieces/piece_065.py`, `tests/pieces/test_piece_065.py`. The checker writes only its report directory (`piece_065.py:667-669`, `:575-642`) and never sends packets or launches processes. The `--connect-run` flag exists (`piece_065.py:653-658`). `analysis/gateway-decode-proof.json` is required for decoding (`piece_065.py:540-542`).
- Pinned references exist: `refs/Sanctuary-combat-pr-research/pr-76`, `pr-77` and `pr-74` contain the cited `.cs` files, and `SOURCE.json` is present.
- `notes/Research/Starting Dungeon Audit.md`, `Native Combat Results Lifecycle.md` and `Cave Results Score Binding.md` all exist.

**Unsure:**
- Limits bullet: "runs recorded without it (for example 20261009T013155Z) cannot be decoded and are reported as skipped." The skip reason is real (`piece_065.py:540-541`), but `20261009T013155Z` is not in `DEFAULT_RUNS` (`:51-58`). The Commands section passes it as `--connect-run`, and `connect_session` (`:453-468`) reads only the before/after snapshots and does not need the decode proof. So it is skipped only if passed to `--run`, not by default. I did not change this because the sentence is conditional rather than false.
- The grading table (6 runs, pass/fail per gate) and the "newest bundle" `lab/reports/piece-065-20261009T053857Z/` cannot be verified. `lab/` is outside the repo and `lab/reports` is not in this tree.
- The capture timings (105.344s, 106.750s, 115.657s and so on), frame numbers, the 50-coin reward and the loss times are capture facts I could not check here. The 411 zone and encounter ids are local assignments (`piece_065.rs:46-50`), as the note says.
