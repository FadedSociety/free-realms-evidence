<!-- fleet job=note-refresh id=Pieces-034-Ninja-progression status=done turns=28 usd=0.0274 tokens(read,write,in,out)=[1079839, 65495, 58, 16878] model=claude-haiku-5-5 -->
# notes/Research/Pieces/034 Ninja progression.md

**Verdict:** minor drift. Most claims hold at the tip: the module, test and script paths exist, the 15 Rust and 15 Python tests are present, `lib.rs` still has no `pub mod restoration`, and the job, weapon, reach, recast, energy and locale facts match the cited sources. Two statements are now incomplete or false.

**Corrections:**

1. `old:` `` `src/combat.rs` and `src/encounter.rs` still answer 36/10 themselves, so the validator is only ``
   `new:` `` `src/combat.rs` and `src/encounter.rs` still answer 36/10 themselves, and since T010 the gameplay route also answers Ninja's basic 36/10 (job basics for six jobs, including Ninja weapon 75091) with its own reach and 600 ms gate, not this module; so the validator is only ``
   `why:` `repo:prototype/osfr-tools/src/gameplay.rs:4634-4637` (the 36/10 branch; slot 0 is the displayed basic); `repo:prototype/osfr-tools/tests/job_basic_attacks.rs:247` (`starter_test!(ninja_starter_weapon_kills_cave_enemy, 2, 75091, 6)`, which sends the real 36/10 basic through `Gameplay`); `repo:notes/Autopilot/T010.md:14-20, 36`. None of these call `restoration::piece_034`. The sentence "today … still answer 36/10 themselves" is accurate about combat.rs and encounter.rs but omits the route that now serves Ninja.

2. `old:` `Refusals mutate nothing: every check runs before the first write, which the vectors assert.`
   `new:` `Refusals spend and stamp nothing: the energy regeneration tick runs before the checks and can advance the energy clock even when the cast is refused; the spend and recast stamp happen only after every check passes.`
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_034.rs:604` calls `self.regenerate(now_ms)`, which writes `state.energy` and `state.last_energy_ms` (lines 563-572), before the energy check at 605 and the recast check at 613. The first spend is at 625, after all refusals.

**Unsure:**

- The evidence paths `lab/reports/piece-034-20261009T034148Z/`, `lab/references/…`, `lab/decompiled/…`, `lab/extracted/…` do not exist under the repo root (`repo` has no `lab/` directory). `notes/WorkItems/034.md:13` cites them as `../lab/reports/…`, so they are probably a sibling workspace. I could not confirm the emitted report, the RED/GREEN logs or the `.json` checker output.
- The run counts in the Verification table (71 weapons, 6 tiers, 3 abilities, 10 refusals, 25 icons, 7 gaps, 1 discrepancy; "15 passed" and "12 passed, 3 failed") could not be re-run. The 15 test functions in each file match the stated totals. I did not confirm the 6-tier and 10-refusal counts in `scripts/pieces/piece_034.py`.
- The wiki-sourced damage ladder (254/889 through 2372/8302, page revisions) and the "21 power attacks" figure were not checked against `wiki.sqlite`. The 254/889 pair is consistent with `piece_034.rs` header comments.
- Native acceptance (gate 7) cannot be checked from a read-only tree.
