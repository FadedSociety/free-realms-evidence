<!-- fleet job=note-refresh id=Native-Mining-Shape-Parity status=done turns=7 usd=0.0061 tokens(read,write,in,out)=[69040, 21273, 16, 5426] model=claude-haiku-5-5 -->
# notes/Research/Native Mining Shape Parity.md

**Verdict:** badly stale. The generator parity error the note describes was repaired after the note was written. The note still reads as an open defect with a proposed fix, and the code and tests at the tip show that fix applied.

**Corrections:**

1. `old:` Rust `initialize_board` currently calls `random_tile(run,spec,true)` for both1 and2.
   `new:` Rust `initialize_board` now calls `random_tile(run,spec,false,…)` for shape1 (TILE_BUILDREGULAR, collectables excluded) and `random_tile(run,spec,true,…)` for shape2 (TILE_BUILDANY); the repair is applied.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1343-1346 (`1 => random_tile(run, spec, false, …)`, `2 => random_tile(run, spec, true, …)`); the receipt is in repo:notes/Research/Native Mining Dead Board.md:148-167.

2. `old:` Proposed narrow repair after the separate dead-board reshuffle repair:
   `new:` Narrow repair, applied after the separate dead-board reshuffle repair (receipt in [[Native Mining Dead Board]] §7):
   `why:` repo:prototype/osfr-tools/src/mining.rs:1343-1346 (the shape1 arm is `false`); repo:notes/Research/Native Mining Dead Board.md:157-158 and 162 record the applied patch and post-change source hash.

3. `old:` Test-first checks must force the collectable branch to prove shape1 refusal/shape2 acceptance and preserve refill availability.
   `new:` Test-first checks now exist in `tests/mining_shape_parity.rs`: `shape1_regular_cells_exclude_collectables_at_forced_percent` (line 243), `shape2_any_allows_collectables_at_forced_percent` (line 262), `gravity_refill_queue_still_allows_collectables` (line 278) and `mixed_seed_cases_keep_shape1_collectable_free` (line 297). They force 100% (and 50% over seeds 18-21) and pass GREEN per the Dead Board §7 receipt.
   `why:` repo:prototype/osfr-tools/tests/mining_shape_parity.rs:243-297; repo:notes/Research/Native Mining Dead Board.md:163-167.

**Unsure:**

- The original-script citations (`core/ServerGrid.as:357-361`, `core/ServerTileGenerator.as` 107-110 / 126-137) could not be checked: no `TILE_BUILDREGULAR`/`TILE_BUILDANY` text exists in the refs root. They match the citations in mining.rs:1344 and the test header, so I left them alone.
- The receipt path `../lab/reports/mining-shape-parity-lead-20261009T133418Z/receipt.json` lies outside the repo and could not be opened. The repair's bundle is cited as `lab/reports/mining-shape-parity-repair-20261009T133907Z` in the Dead Board note, and I could not confirm it either.
- The native125556 board details (ores at row10 cols 8/10, the six chains, the moved ore) and the claim that "native whole-round acceptance remains required" are historical or status claims that I could not check from the code.
- The module-contract claim that shape `1` is "regular random" and `2` is "any random" still holds (repo:prototype/osfr-tools/src/mining.rs:12), so I did not correct it.
