<!-- fleet job=note-refresh id=Pieces-035-Archer-progression status=nothing_found turns=10 usd=0.0104 tokens(read,write,in,out)=[188929, 37006, 22, 7829] model=claude-haiku-5-5 -->
# notes/Research/Pieces/035 Archer progression.md

**Verdict:** current. I found no false claim about our code or status in `035 Archer progression.md`. The note is dated 2026-10-09 and its status still matches the tip.

**Checked and holding:**
- **Module not registered:** `prototype/osfr-tools/src/lib.rs` has no `restoration` or `piece_0*` line, so "not registered in `lib.rs`" is still true. `tests/piece_035.rs:27-29` still includes the module by `#[path]`.
- **Artifacts exist:** `src/restoration/piece_035.rs` (597 lines), `tests/piece_035.rs`, `scripts/pieces/piece_035.py` and `tests/pieces/test_piece_035.py`.
- **Test counts:** `tests/piece_035.rs` has 15 `#[test]` functions, matching "15 integration vectors". `test_piece_035.py` has 14 `def test_`, matching "14 stdlib tests". `notes/Research/Suite Status 2026-10-13.md:144` also reports 15 passing.
- **Sub-opcodes:** the constants at `piece_035.rs:56-77` match the note (family 36, PlayerUpdate 35, 3, 14, 62, 1, 5, 10). The client constructors pass the same immediates: `FUN_00a2ed30` calls with 3, `FUN_00a2ee30` with 0xe, `FUN_008d0b10` with 0x3e.
- **Failure vocabulary:** `CodeStringMappings.txt` lists `NoCastNotEnabled^3079` (line 2218) and `NoCastTargeting^288` (line 2222). The locale table confirms id 280 and 3079.
- **Archer kit:** `piece_035.rs:87-103` has profile 35, wield 11, reach 30.0, bow 4266, abilities 1010/1011, damage 279/506, radius 10, energy 100. The pinned `Sanctuary/src/Resources/CombatJobs.json:4` says "Archer. Ranged; reach 30u ... Creation kit = 4266". Melee reach is 7 and the Wizard is 20 (`piece_035.rs:106-108`).
- **Wire shapes:** 36/10 is decoded at `piece_035.rs:210-232` (positional, `Target == 1` gives a float4 position, otherwise a guid, then `finish()`). 36/5 has the `Range` float at `piece_035.rs:245`, with the PR 121 comment at line 244.
- **Reconstructed policy:** `ReachGate` (line 366), `LineOfSight` with `Unchecked` (line 418), `admit_ranged_action` running reach then geometry (line 445) and `AmmoPolicy::NotRecovered` with `charges_items() == false` (line 493) all exist as described. The note says `LineOfSight` "defaults to" `Unchecked`. There is no `Default` impl, so this is wording only and I left it alone.
- **Gap claim:** no ranged payload or line-of-sight code exists in `src/`. The only `NoCastOutOfRange`/`NoCastLineOfSight`/`NoCastTooFar` references are the checker's forbidden-name list at `scripts/pieces/piece_035.py:379`.

**Unsure:**
- `notes/Build Guides/Gameplay/Combat and Abilities.md:257` and `:280` (outside this note) give partial field descriptions for 36/4 ("target array, ProjectileParameters, about 20 fields") and 35/62. That is not a full layout, so the note's "layout not recovered" is not contradicted. The gap row may still deserve a cross-link.
- The lab-side evidence cannot be read from these roots: the 65,810 corpus frames, the zero-frame family-36 count, the `evidence_sha256`, and the RED/GREEN log names under `../lab/reports/`. I did not verify them.
- The wiki and PR 121 citations (Archer traits, "auto-target radius" wording) were only partly checked. The `reach 30u` comment is confirmed in the pinned repos, and the wording in the reader comments was not checked line-for-line.
