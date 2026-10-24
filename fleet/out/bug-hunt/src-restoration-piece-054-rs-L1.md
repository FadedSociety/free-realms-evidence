<!-- fleet job=bug-hunt id=src-restoration-piece-054-rs-L1 status=nothing_found turns=7 usd=0.0054 tokens(read,write,in,out)=[67165, 16633, 16, 5270] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_054.rs lines 1-268 of 268

No reportable defects in `prototype/osfr-tools/src/restoration/piece_054.rs` lines 1-268.

What I checked:

- **Input handling in `resolve_melee_attack` (lines 233-268):** non-finite coordinates are refused at 242-246 before any arithmetic. Finite but huge coordinates overflow to `inf` in the distance, which then fails `distance > reach` at 252 and is refused. No NaN path reaches the comparison. `target_health <= 0` is refused at 247. The repeat gate at 255-263 uses `saturating_sub`, so a backwards clock cannot underflow. There is no indexing, slicing, unwrap, or division on client values anywhere in the window.
- **Boundary and doc agreement:** the `> reach` refusal at 252 matches the doc comment at 228-229. The repeat gate `< 600` at 257 matches the doc at 230.
- **Callers:** `resolve_melee_attack` is called only from `tests/piece_054.rs` (lines 59, 177) and not from `src/encounter.rs`, so no packet field reaches it in production today. The window has no atomicity issue, because it mutates nothing.
- **Wield table versus its doc comment:** the module doc (lines 11-12) and `notes/Research/Pieces/054 Melee attacks.md:26` say job wield types "9..19" play 1099. The `WIELD_MELEE_ANIMATION_GROUPS` table (lines 124-132) has rows 9-17 only. I checked the preserved original `client/Resources/WieldTypeAnimationMappings.txt`, which has no 18 or 19 rows at all. The code is therefore correct and the "9..19" wording in the doc and notes is a documentation slip. It is not a behavioural defect, so I did not report it.
- **Player attacks with wield types that map to group 0** (0, 6, 20, 27, 28, or unlisted ids): these are accepted with `swing_animation = 0`. The original data has no melee group for those types, so this matches the recovered contract and is not a defect.

Nothing in the window meets the five defect categories with a reachable failure.
