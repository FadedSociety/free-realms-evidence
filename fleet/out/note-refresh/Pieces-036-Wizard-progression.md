<!-- fleet job=note-refresh id=Pieces-036-Wizard-progression status=done turns=20 usd=0.0232 tokens(read,write,in,out)=[848614, 68029, 42, 12426] model=claude-haiku-5-5 -->
# notes/Research/Pieces/036 Wizard progression.md

**Verdict:** current, with one minor drift in the lead-integration gate. Every checkable code and file claim holds at the tip. The gate's module path is the only wording that no longer matches the tree.

**Corrections:**

- `old:` register `pub mod piece_036;` under `src/restoration/`
- `new:` add `pub mod restoration;` to `src/lib.rs` and register `pub mod piece_036;` in it
- `why:` `prototype/osfr-tools/src/restoration/` has no `mod.rs`, and `src/lib.rs` has no `restoration` module (search for `mod restoration` in `src/lib.rs` returns nothing). The shared-module pattern is in `notes/Reviews/Delegated Task Readiness.v1.md:41`. The `#[path]` include the note says to drop is still live at `prototype/osfr-tools/tests/piece_036.rs:34-36`.

**Verified as current (no change needed):**

- The module, owned test, checker and Python test exist at the cited paths: `src/restoration/piece_036.rs` (432 lines), `tests/piece_036.rs` (16 `#[test]`s, matching "16 passed"), `tests/pieces/test_piece_036.py` (12 tests, matching "Ran 12 tests"), `scripts/pieces/piece_036.py`. The checker's exit-2 path is at `scripts/pieces/piece_036.py:551-554`.
- `src/combat.rs:205-213` is the `(36, 10)` parse with the `if target == 1 { 32 } else { 24 }` length check, as cited.
- Module policy matches the note's rules: the cast order is profile, slot, caster finite, guid target checks (self, dead, hostile, reach with `20.0` inclusive via squared distance), position target checked only for finite values, `CastInProgress` lock, 600 ms basic recast, energy spent once, regen 4/s with partial seconds carried and saturating at 100 (`piece_036.rs:339-424`). `AbilityEffect` has only `SweepDamage`, and `CastDenial` carries no string id (`piece_036.rs:96-98, 249-276`).
- Community values in `piece_036.rs` match the pinned Sanctuary data at `refs:Sanctuary/src/Resources/`: `CombatJobs.json:76-98` (profile 12, reach 20, wield 10, slots 4895/4899, recast 600, fallback 4010, energy 100/4, wand 4914 → 4011/4028); `CombatAbilities.json:113-142+` (4010 200 dmg; 4011 279; 4028 1143, energy 100, cast 16305); `ClientItemDefinitions.json:92998-93018` (4914 Class 10, slot 7, NameId 11056, DescriptionId 1114, icon 3158/234, category 207, power rating 1, NoTrade, MinProfileRank 1); `Profiles.json:479-490` (profile 12 Type 2, NameId 2280, DescriptionId 2281, icon 1343, badge 12, MembersOnly false, Trial true).
- The Native Combat Controls cross-reference holds: `notes/Research/Native Combat Controls.md:20` carries Disposition 0 at +0x178 and the dead flag at +0x6f8 bit 7.
- The cited link targets exist (`notes/Research/Native Combat Controls.md`, `notes/MMO Work Queue.md`, `notes/Design/MMO Worker Contract.md`).

**Unsure:**

- `lab/` is not part of the repo tree, so I could not check the `lab/decompiled/.../BaseAbilityPackets.cs` claims directly: the "18 ability packets" count, the 36/5 literal's 44-byte length, and the `lab/reports/piece-036-20261009T033448Z/` evidence. The in-repo test fixture (`tests/pieces/test_piece_055.py:181-193`) shows only an excerpt of that enum, so the count is neither confirmed nor refuted.
- The wiki claims (Student Wizard Wand revision 26356 stating 279 / 1143; Wizard revision 46067 level list) could not be checked. `freerealms-wiki/raw` has no `revid` 26356 or 46067 match, and `wiki.sqlite` is not reachable from these roots.
- The pinned revision `4f028dcc…` is cited consistently across the repo, but I did not verify the `sha256` values the note's checker enforces.
