<!-- fleet job=note-refresh id=Repeat-Crafting-Control-Preparation status=nothing_found turns=22 usd=0.0234 tokens(read,write,in,out)=[747736, 67249, 46, 15079] model=claude-haiku-5-5 -->
# notes/Research/Repeat Crafting Control Preparation.md

**Verdict:** current. I found no claim about our code or status that is now false, and no citation that has moved.

**Corrections:** none.

**Checked and holding:**
- **Forging rules.** Quota 5 and 180 seconds match `scripts/prepare-forging.py:65` (`"duration_seconds": 180, "quota": 5`). The 14x14 board (`SIDE = 14`) and the minimum three-tile orthogonal, same-colour chain are at `prototype/osfr-tools/src/forging.rs:20` and `:847-875`. Hammers sit outside the chain colours 401-405 (`forging.rs:25`, `:865`).
- **Planner snapshot field.** `gameplay.forging.active` is correct: the snapshot is `{"character","gameplay"}` (`restoration/piece_017.rs:37-41`), `gameplay.rs:1360` writes `forging`, and `ForgingState.active` is at `forging.rs:90`.
- **Planner arguments.** `plan-forging-chain.py` takes `--limit`, `--anchor` and `--step` as the note uses them (matches `notes/Reviews/Remaining Opening Preflight.md:41`).
- **Helper script.** `project/scripts/drive-local-game.py` is `scripts/drive-local-game.py` at the repo root (same convention as other notes). It takes `--run` plus free commands and appends `external-inputs.jsonl` (`scripts/drive-local-game.py:17-44`).
- **Smelting phases.** Four stages, 101 to 104 (`restoration/piece_013.rs:206-211`).
- **Cooking phases.** Six phases (`cooking.rs:1`, `:517`).
- **Coordinate arithmetic.** The A and B mappings are consistent with each other and with `Forging Native Control Geometry.md:36` (anchor 492.24/232.53 times 1.2 = 590.69/279.03). The Cooking and Forging half-shot conversions (x0.6 of 1280-space) check out.
- **Status.** `notes/Current Progress.md:106` (14/17 rewarded, stage 15 unaccepted) and `:134` (next gates: repeat stage 13 Cooking, stage 14 mining, stage 15 at the relocated anvil) match the note's framing. `notes/Tasks.md:88` supports Forging 181715 with 5 hammers.
- **Linked notes.** All linked notes exist under `notes/Research/`.

**Unsure:**
- `lab/tools/plan-forging-chain.py`, `navigate-local-game.py` and the `lab/reports/...` evidence are outside the repo tip, so I could not read them. Their behaviour rests on the other notes that cite them (`Native Forging Controls.md:11`, `Native Navigation Helper.md`).
- `SmeltingGameClient.as` lines 422-435, the `RoundPour` mapping and the phase-104 gap are client-side. The decompiled client DB has no `Smelting` rows, and the only repo mention is `Native Smelting Controls.md:19` (cites lines 407-436). Not verifiable here.
- The "13 prior input-logged runs" count and the "began with size 1280 960" claim sit in lab logs outside the repo.
- Cooking and Smelting control coordinates (round clicks, bucket and bellows positions) come from accepted lab logs, not from repo code.
- The header date is October 8, but the evidence folder is `...20261009T001532Z`. This is a dating inconsistency, not a code claim.
