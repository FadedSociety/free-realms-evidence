<!-- fleet job=note-refresh id=Pieces-049-Character-appearance-coverage status=done turns=15 usd=0.0173 tokens(read,write,in,out)=[368258, 51477, 32, 14330] model=claude-haiku-5-5 -->
# notes/Research/Pieces/049 Character appearance coverage.md

**Verdict:** current. The code-facing claims all hold at the tip; one command path is wrong.

**Checked and holding (repo evidence):**
- `src/restoration/piece_049.rs` exists and is not registered: no `restoration` module line in `prototype/osfr-tools/src/lib.rs`, and the module is only pulled in via `#[path]` in `tests/piece_049.rs:35-37`.
- `skin_tone_exclusion` returns `SkinTextureAbsent` for ids 7/8 (`EXCLUDED_SKIN_TONE_IDS = [7, 8]`, `piece_049.rs:423`, `:459-463`). `head_exclusion` returns `NotOfferedByPublicTables` for ids 5-8 (`EXCLUDED_HEAD_IDS = [5, 6, 7, 8]`, `piece_049.rs:427`, `:467-471`). The note's "four China head ids" holds only if read as ids 5-8; the note says exactly that elsewhere.
- Twelve excluded rows: `EXCLUDED_CREATOR_ROWS: [_; 12]` (`piece_049.rs:285`). Eight SkinTone rows (mappings 272 and 1, definitions 78090/78091) and four FaceType rows (mappings 268-271, definitions 78086-78089, indexes 5-8) at `piece_049.rs:297-417`. These match the note's per-type split.
- Counts: 223 offered / 49 unreachable mapping rows (`piece_049.rs:430-432`); FRC range 78037-78066 (`:434`); family count 36 (`:436`). The 253 → 241 arithmetic per character type (67-3, 61-3, 63-3, 62-3) also matches the excluded rows.
- Checker `scripts/pieces/piece_049.py` exists. It has `RustModuleDrift`, `ExcludedRowSetDrift`, `PublicTableDrift`, a sha256 per input, six gap strings (`:781-797`), `coverage ok` output (`:915`), and exit 2 on evidence errors (`:904-909`).
- Python test file `tests/pieces/test_piece_049.py` has 8 test methods (matches "Ran 8 tests"). Rust `tests/piece_049.rs` has 6 `#[test]` functions (matches "6 passed").
- Native-failure evidence (`client-baseline-20261008T065152Z`, `human_m_head_caucasian_08.dds` 404) is cited consistently in `notes/Research/Character Creation Audit.md:30` and `notes/Research/Native Asset HTTP Delivery.md:21`. The mapping 1 → 78091 → skin 8 "Pearl" chain is in `Character Creation Audit.md:41`.

**Corrections:**

1. `old:` `& scripts\cargo.ps1 test --test piece_049`
   `new:` `& ..\..\scripts\cargo.ps1 test --test piece_049`
   `why:` The wrapper lives at repo-root `scripts/cargo.ps1`. `prototype/osfr-tools/` has no `scripts/` directory (checked), so the command as written, run from `prototype/osfr-tools` per the note's own comment, does not resolve. Other notes call it as `../../scripts/cargo.ps1` or `./scripts/cargo.ps1` from the repo root (`prototype/osfr-tools/README.md:10`, `notes/Design/Debug Harness.md:14`).

**Unsure:**

- Gap "EyeColor guid 1000013 (Human Female) resolves to definition 77605 whose `GENDER_USAGE` is 1". The 77605 and `GENDER_USAGE` facts are not in the repo; the only copy is the checker's gap text (`scripts/pieces/piece_049.py:787-789`), and the `lab/` source tables are not reachable from here. Also, the checker's own `EXCLUDED_ROWS` reuse guid 1000013 for two different rows (SkinTone Human Male, `piece_049.py:78`, and FaceType Human Female, `:85`; the Rust table does the same at `piece_049.rs:334` and `:411`). That is consistent with guids being per-category, but I could not confirm it from source.
- Per-category option counts (for example FacePaint 12 female / 7 male, Clothes 9, HairColor 10) and the "18 scanned public packs" and "Pearl" locale claims rest on `lab/` inputs that are not in the repo, so I did not verify them.
- The 49 unreachable-row breakdown and the 253 row total match the Rust constants, but the underlying tables could not be re-derived from here.
- No native client run was checked; the note already says none was made.</result>
<parameter name="status">done
