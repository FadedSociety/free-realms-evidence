<!-- fleet job=note-refresh id=Original-Activity-Coverage status=done turns=11 usd=0.0121 tokens(read,write,in,out)=[204444, 33310, 24, 11830] model=claude-haiku-5-5 -->
# notes/Research/Original Activity Coverage.md

**Verdict:** minor drift. Most checkable claims hold at the tip (receipt-bound rows 46/77/139, `forging.rs` binding `GAME = 139`, `cooking.rs`/`smelting.rs` game ids, the 24-test count in `tests/test_minigame_coverage.py`, the status totals in the committed JSON, the review evidence files, and the TYPE 8/9 row mixes). The one false area is the "leftover wording" item, which the repo has already fixed.

**Corrections:**

1. `old:`
```
`prototype/osfr-tools/src/restoration/piece_018.rs:156` still calls the forging
entry "TYPE 9 mimic anvil movie" (its own records already carry
`original_type: 8`). Piece 015 does not edit that file; the record is listed in
`findings.leftover_wording_outside_ownership` for the owning piece to retire.
```
`new:` The forging entry at `prototype/osfr-tools/src/restoration/piece_018.rs:156` now reads `family: "TYPE 8 MatchThree (Forging row 139)"`, and no "mimic anvil" wording remains under `prototype/`. The `findings.leftover_wording_outside_ownership` record in `scripts/audit-minigame-coverage.py` (lines 1086-1096) is stale and still quotes the retired text.
`why:` repo:prototype/osfr-tools/src/restoration/piece_018.rs:156 (`family: "TYPE 8 MatchThree (Forging row 139)"`, `original_type: 8` at :159); a search for "mimic anvil" under `prototype/` returns no matches; the stale record is repo:scripts/audit-minigame-coverage.py:1086-1096.

2. `old:`
```
Known leftover outside
this piece: `src/restoration/piece_018.rs:156` still says "TYPE 9 mimic anvil
movie" (listed in `findings.leftover_wording_outside_ownership`, not edited).
```
`new:` No leftover from this piece remains outside its ownership: `src/restoration/piece_018.rs:156` now reads "TYPE 8 MatchThree (Forging row 139)", so the old "TYPE 9 mimic anvil movie" wording is gone from `prototype/`. Only the stale finding record in `scripts/audit-minigame-coverage.py` still quotes it.
`why:` repo:prototype/osfr-tools/src/restoration/piece_018.rs:156-159; no "mimic anvil" match under `prototype/`; repo:scripts/audit-minigame-coverage.py:1086-1096.

**Unsure:**
- The "24 stdlib tests" count matches the file (20 `test_*` methods in `ParseTests`/`DetectionTests`/`OutputTests`/`RealSourceTests` plus 4 in `NativeReceiptTests`, lines 260-410). I counted by reading the file because the search tool capped its output at 20 hits.
- The status totals (3 / 195 / 511 / 74), the 783-game count, and the TYPE 8 and TYPE 9 row mixes match the committed JSON (`notes/Research/original-activity-coverage.json`, around lines 16932-16937). I did not recompute the lab bundle hashes or the SHA-256 of the catalogue, because the lab files are outside the repo.
- MiniGameData rows 46 (`^9^`), 77 (`^9^`) and 139 (`^8^`) match the note's type assignments (client:Resources/MiniGameData.txt lines 47, 78, 140).
- The status line's "runtime lookup module" has no obvious match in the owned-artifacts table. The closest candidate is `prototype/osfr-tools/src/restoration/piece_015.rs`, which I did not inspect in depth.
- I did not verify the "60 other TYPE 8 Forging rows" or the "entry 139000001/score 6600" frame details, because they need the lab captures.
