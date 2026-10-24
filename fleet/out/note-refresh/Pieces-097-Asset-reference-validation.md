<!-- fleet job=note-refresh id=Pieces-097-Asset-reference-validation status=done turns=19 usd=0.0247 tokens(read,write,in,out)=[665813, 72542, 40, 17916] model=claude-haiku-5-5 -->
# notes/Research/Pieces/097 Asset reference validation.md

**Verdict:** minor drift. The counts, file paths, test counts (8 passed / 1 ignored; 11 Python tests), the reconstructed rules and the "not registered in `src/lib.rs`" status all match the tip. One citation points at the wrong note, and two phrases overstate what the code and tests show.

**Corrections:**

1. `old:` four character-creation rows in [[Character Creation Audit]]
   `new:` four `IS_VALID_FOR_PC = 1` rows in [[049 Character appearance coverage]] (`Models.txt` ids 1, 2, 60, 61)
   `why:` `notes/Research/Pieces/049 Character appearance coverage.md:34-37` lists the four creator character types bound to `human_m.adr`, `fairy_m.adr`, `human_f.adr`, `fairy_f.adr`. `notes/Research/Character Creation Audit.md:34-41` has no four-variant table; it covers the SkinTone and FaceType resources and the Human male Caucasian heads. The same wrong citation sits in the module doc at `prototype/osfr-tools/src/restoration/piece_097.rs:22-23`, which should be corrected alongside.

2. `old:` The five `hsg_` entries and the two `_complete.agr` pool rows match the furniture findings of
   `new:` The five `hsg_` entries (the two `_complete.agr` pool rows among them) match the furniture findings of
   `why:` `notes/Research/Pieces/024 Furniture catalogue.md:55-59` lists exactly five missing furniture models (9046, 16872, 16874, 18112, 18136). The note's list of 21 contains those same five, so the two pool rows are not extra entries. As written, the sentence reads as seven.

3. `old:` anchors, locale, class, category and model lookups are case-insensitive
   `new:` asset-name lookups are case-insensitive (names are lowercased in `asset_names` and `classify_model`)
   `why:` `prototype/osfr-tools/src/restoration/piece_097.rs:274` and `:329-337` lowercase asset names and model names. The only case test is `asset_and_locale_lookups_are_case_insensitive` (`prototype/osfr-tools/tests/piece_097.rs:314-323`), and it checks asset names only. Class, category and locale keys are integer ids, and the code has no "anchor" lookup at all.

**Unsure:**

- **Test status after the run in the note.** The note's GREEN lines were recorded before a later problem. `MODLOG.md:448` says SmartAppControl blocked the `piece_097` executable in a broad gate run, with eight ordinary tests and the private gate unexecuted. `notes/Tasks.md:170` still lists "Resolve OS-blocked piece_097 test execution" as open. `notes/Research/Suite Status 2026-10-13.md:206` shows `tests/piece_097.rs | 8 | 0 | 1`, so the count is consistent. I did not change the note, because the 8/1 result is reported elsewhere, but the GREEN section should not be read as a post-block re-run.
- **Numeric claims I could not check.** The `Param1` figures (2,867 / 2,525, the per-type resolve-all list, and the 3,533 / 7 / 16 description counts) rest on the `lab/` bundle, which is not in the repo. The one figure I could test, type 12 at 541/541 (`tests/piece_097.rs:383-391`), is consistent with the note's list. The `lab/` report paths are also not checkable here.
- **Module registration.** `src/lib.rs` has no `restoration` or `piece_097` reference, which matches the note. No `src/restoration/mod.rs` exists either, so the registration step is still open, as the note says.
