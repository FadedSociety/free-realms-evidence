<!-- fleet job=note-refresh id=Pieces-054-Melee-attacks status=done turns=17 usd=0.0199 tokens(read,write,in,out)=[613033, 62573, 36, 11928] model=claude-haiku-5-5 -->
# notes/Research/Pieces/054 Melee attacks.md

**Verdict:** minor drift. The reviewed 3 m player reach, the wield and animation rows, the module and the test counts all hold at the tip. One checker cross-check is now false, which also means the checker itself would fail on the current encounter source. One call-site citation has moved.

**Corrections:**

1. `old:` the `600 ms` repeat gate and the `<= 2.5` enemy contact rule;
   `new:` the `600 ms` repeat gate and the enemy contact rule `distance(position, s.position) <= b.reach` (the `melee` preset default is `reach: 2.5`);
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:2457` now reads `if distance(position, s.position) <= b.reach {`, and the 2.5 default is data-driven at `repo:prototype/osfr-tools/src/encounter.rs:301` (`reach: 2.5,`). The literal `<= 2.5` no longer appears in `encounter.rs`. MODLOG.md:22-26 records the move to presets. `repo:tests/pieces/...` is not involved, but `repo:scripts/pieces/piece_054.py:67` still pins `PRODUCTION_ENEMY_CONTACT = "distance(position, s.position) <= 2.5"`, and `:295` uses it as `has_enemy_contact`. The checker therefore fails closed on the current tip. The Rust test `repo:prototype/osfr-tools/tests/piece_054.rs:107-111` already pins the new form. The "exit 2 ... GREEN" evidence in the Verification section is stale for the checker (see Unsure).

2. `old:` 600 ms checks in `encounter.rs::attack` with this gate
   `new:` 600 ms checks in `encounter.rs::strike_damage` (reached from `attack` through `strike`) with this gate
   `why:` `repo:prototype/osfr-tools/src/encounter.rs:1814` is `attack`, which calls `strike` (1835) and then `strike_damage` (1846). The inline `distance(position, s.position) > range` check and the `saturating_sub(last) < 600` check sit at `repo:prototype/osfr-tools/src/encounter.rs:1872-1877`.

**Checked and holding (no change):**
- `src/restoration/piece_054.rs` (268 lines), `tests/piece_054.rs` (8 `#[test]`s) and `tests/pieces/test_piece_054.py` (8 `def test_`s) exist. The Rust test still includes the module by `#[path]`, and `lib.rs` does not register `piece_054`, so the "lead integration" gate is still open.
- Production profile rows: `repo:prototype/osfr-tools/src/encounter.rs:2893-2904` (2/11/32/43 and fallback at 3.0; 35 at 30.0; 12 at 20.0).
- Wield table rows, including 13 = 1099 and hand-to-hand = 1000, match `piece_054.rs:114-141`.
- The `Any -> Combat` and `Combat -> loc_stand` timings match `piece_054.rs:207-224`.
- `Resources/AnimationTypes.xml:558` (com_h2h_attack_01 slot 1001) and `Resources/AnimationGroups.xml:635-639` (com_swing 1099, fallback 1000) are present.
- The review `notes/Reviews/Native Cave Completion 081219.md` exists and states 20 hits, 1.970–2.434 units, and the 150 ms bound.

**Unsure:**
- The lab bundle `lab/reports/piece-054-20261009T043758Z/` is not visible from the repo root, so I could not confirm the evidence files or the logged test counts (the Rust and Python 8-test counts match the source).
- The "GREEN: 15 passed; 2 ignored" for `tests/encounter.rs` could not be re-run. The named test `melee_requires_contact_and_enemy_motion_attacks_have_native_animation` exists at `repo:prototype/osfr-tools/tests/encounter.rs:571`.
- The exact `piece_054.py` exit behaviour after the enemy-contact string drift is inferred from the substring check at line 295, not run.</result>
