<!-- fleet job=note-refresh id=Pieces-052-Enemy-patrol-and-idle status=done turns=17 usd=0.0274 tokens(read,write,in,out)=[748097, 82143, 36, 19225] model=claude-haiku-5-5 -->
# notes/Research/Pieces/052 Enemy patrol and idle.md

**Verdict:** minor drift. Almost every checkable claim holds at the tip: the files exist, the `piece_052.rs` bounds and constants match the code, the test counts match (8 `#[test]` in `tests/piece_052.rs`, 15 `def test_` in `tests/pieces/test_piece_052.py`), the module is still unregistered in `lib.rs`, and the animation mapping rows are correct. One sentence overstates what the checker does.

**Corrections:**

1. `old:` These functions, the preserved `native-motion-verification.json` record and the 13 compiled-serializer fixtures are re-verified by
the checker rather than restated.
`new:` The checker re-reads the preserved `native-motion-verification.json` record and the 13 compiled-serializer fixtures (`verify_native_evidence`, `verify_oracle_fixtures`). It does not re-check the native functions: `008e5940`, `0095dae0`, `00908a50` and `008b3180` are cited from the Native NPC Motion note only, and no address appears in the script.
`why:` `repo:scripts/pieces/piece_052.py:270-301` (`verify_native_evidence` only reads JSON fields and layout strings); `repo:scripts/pieces/piece_052.py:367-422` (fixture byte-diff check); a case-insensitive search of `repo:scripts/pieces/piece_052.py` for `8e5940|908a50|95dae0|8b3180|1030083|1093435` returns no hits.

**Checked and holding (no change):**
- `src/restoration/piece_052.rs` constants: opcode 125 / 36 bytes; opcode 35 subtype 8 / 21 bytes; waypoints 2–16; speed `0 < v <= 6.25` (`:65-67`, `:205`); arrival radius `<= 5` (`:69`, `:210`); dwell `<= 10 000 ms` (`:71`, `:225`); extent `<= 200` (`:73`, `:241`); tick 100 ms and step 250 ms (`:75-78`, `:371`, `:393`); guid `<= 1` refused (`:323`).
- Controller behaviour: run base (3, flag 1) on start and stand base (1, flag 1) on arrival (`:404-406`, `:423-427`); no overshoot past the arrival radius (`:415`).
- `tests/piece_052.rs:34` still has the `#[path]` include, so the lead-integration gate stands; no `piece_052` line in `src/lib.rs`.
- `Resources/CodeAnimationMappings.txt` (client root): `0^1^loc_stand`, `30^2^loc_walk`, `1^3^loc_run`, plus `1001^com_h2h_attack_01`.
- Sanctuary `Npc.Speed = 6.25f` default (`refs:Sanctuary/src/Sanctuary.Game/Entities/Npc.cs:96`).
- Template hash `602c66b1…` matches the `encounter-template.bin` hash cited in `notes/Autopilot/T026.md:55`.
- The Outdoor Wolf review covers chase/lunge pixels only, as the note says (`notes/Reviews/Native Outdoor Wolf Controls 183551.md:19`).
- The `008b3180` speed getter does read the entity speed field (`client_sql fn 008b3180`).

**Unsure:**
- The file offsets `1030083` (for `008e5940`) and `1093435` (subtype-8 dispatch) and the claim that `008e5940` consumes exactly those fields. The decompiled `008e5940` is a bounded 16-bit stream reader, which fits, but I did not verify the offset or the field list.
- The replay numbers (3299 frames, 256/2 movement, 100 animations, the 187.766 s transition, the 133/34 cross-check) and the 13-fixture count. These are in the `lab/` tree, which is outside the roots I can read. The test file does assert the 3299 / 256 / 2 / `{1:8, 3:8, 1001:84}` counts, so they are at least what the checker expects.
- The `lab/reports/piece-052-*` directories and the bundle path. Not readable from here.
- The "local spawn template still holds `0.0`, `(-1,-1,-1)`, `1`, `2`" claim. The script's expected values match, but I did not read the binary.
