<!-- fleet job=note-refresh id=Pieces-012-Cooking-recipes-content status=done turns=15 usd=0.0205 tokens(read,write,in,out)=[551569, 65527, 32, 13519] model=claude-haiku-5-5 -->
# notes/Research/Pieces/012 Cooking recipes/content.md

**Verdict:** minor drift. The file paths, module status, test names and checker claims all hold at the tip. One recorded test count no longer matches the test sources.

**Corrections:**

- `old:` Sibling evidence that the integrated gameplay layer agrees: 13 passed, 1 ignored;
  `new:` Sibling evidence that the integrated gameplay layer agrees: 14 passed, 4 ignored at the tip (`cooking` 11 passed / 1 ignored, `cooking_gameplay` 1 passed / 2 ignored, `piece_012` 2 passed / 1 ignored);
  `why:` `repo:prototype/osfr-tools/tests/cooking.rs:80-578` has 12 `#[test]` functions, one of them `#[ignore]` at `:495`; `repo:prototype/osfr-tools/tests/cooking_gameplay.rs:15` is the only non-ignored test, with `#[ignore]` at `:124` and `:352`; `repo:prototype/osfr-tools/tests/piece_012.rs` has two plain tests and one `#[ignore]` at `:152`. The same counts appear in `repo:notes/Autopilot/F289.md:191` and `:194` (`cooking` 11/1, `cooking_gameplay` 1/2). The cargo command in the note does not pass `--ignored`, so all four ignored tests are counted.

**Checked and holding:**

- `prototype/osfr-tools/src/restoration/piece_012.rs` exists, and `lib.rs` has no `restoration` module, so "not yet registered in `lib.rs`" is still true (`repo:prototype/osfr-tools/src/lib.rs:1-102`).
- `tests/piece_012.rs` uses the `#[path = "../src/restoration/piece_012.rs"]` include (`:6-7`).
- The production `osfr_tools::cooking` service exposes `Cooking::load`, `begin`, `begin_recipe`, `state`, `requirements` and `CookingTransaction` (`repo:prototype/osfr-tools/src/cooking.rs:129-272`). The audit uses them as described.
- The materials and product constants (2862/2875/2884/2900 x4, 35 x1), the stage types `[1,2,3,6,17,7]` and the ingredient art ids `[10,24,40,49,46,46]` match `repo:prototype/osfr-tools/src/restoration/piece_012.rs:20-24` and `repo:prototype/osfr-tools/src/cooking.rs:22-23`.
- The audit flow (replay, reload replay, `FRServer_GameClose`, six groups of four round statistics and four final statistics) matches `piece_012.rs:179-214`.
- `scripts/pieces/piece_012.py` and `tests/pieces/test_piece_012.py` exist. The Python file has 8 test methods (6 synthetic, 2 real-source), matching "8 tests OK" (`repo:tests/pieces/test_piece_012.py:163-228`).
- The checker's reviewed hashes and CLAIMED_RECIPE_ID 55824 are reported as unverified, as the note says (`repo:scripts/pieces/piece_012.py:34-39`). The always-on gaps number five (`:314-333`), and a missing `reconstructed_phase_values` label is a mismatch (`:311-313`).
- Locale checks: 1232 = "Strong Arm Stew", 386023 = "Cooking: Strong Arm Stew", 20520 = the minigame description, 3172 = the food's health/size text, 993 = unrelated (Elite Pink Anguish Aid Cap).

**Unsure:**

- The product definition 35 (`class_id` 9, `max_stack` -1), the material definition blobs, the wiki revision 45318 text ("Where to find: Tutorial") and the SHA-256 values cite `../lab` or the wiki corpus. Neither is in the readable roots. `refs` has no `List_of_Recipes` page to compare against.
- The checker run outputs (`../lab/reports/piece-012-20261009T025212Z/`) and the "no mismatches" result were not re-run.
- "Unmodified production service": `cooking.rs` has changed over the period, and I did not diff it against the state the audit was written against.
- "The gateway-level once-only recipe settlement is covered by the reviewed private gameplay tests": the relevant tests are the ignored private ones, which I did not run.
