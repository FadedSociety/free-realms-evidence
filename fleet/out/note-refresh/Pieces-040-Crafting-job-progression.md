<!-- fleet job=note-refresh id=Pieces-040-Crafting-job-progression status=nothing_found turns=11 usd=0.0138 tokens(read,write,in,out)=[274793, 45074, 24, 10747] model=claude-haiku-5-5 -->
# notes/Research/Pieces/040 Crafting job progression.md

**Verdict:** current. Every checkable claim about our code at the tip matches; no corrections.

**Checked against the tip (all hold):**
- `prototype/osfr-tools/src/restoration/piece_040.rs` exists. It has `recipe_access`, `wiki_gate_access`, `UnknownRecipe`, `CRAFTING_JOBS`, `SHARD_CLASSES`, `RECIPE_ITEMS`, `LEVEL_TITLES`, `LEVEL_GATE_QUESTS` and `WIKI_GATES` (`repo:prototype/osfr-tools/src/restoration/piece_040.rs:120-150`, `:547`, `:630`, `:697`, `:788`, `:824`).
- Not registered: no `piece_040` or `restoration` reference in `src/lib.rs`. The owned test `#[path]`-includes the module (`repo:prototype/osfr-tools/tests/piece_040.rs:27-31`). The note's "not registered" claim holds.
- `prototype/osfr-tools/tests/piece_040.rs` has 11 `#[test]` functions (lines 41–412). The note says 11 tests.
- `tests/pieces/test_piece_040.py` has 5 test methods (lines 238–287). `scripts/pieces/piece_040.py` exists and points at the module path (line 49).
- Profiles: `src/cooking.rs:18` is `PROFILE = 45` and `src/forging.rs:18` is `PROFILE = 16`, matching the note. The checker's `accepted_services_preserved` check (`scripts/pieces/piece_040.py:617-627`) covers the drift claim.
- Shard classes: 58 Blacksmith Shards (name id 2561, owner 16) and 59 Chef Shards (name id 2562, owner 45) match `piece_040.rs:133-146`.
- Recipe counts: 49 `RecipeItem` entries (uniform 8-line blocks, lines 150–541). The test asserts 27 for class 58 and 22 for class 59 (`tests/piece_040.rs:83-93`).
- Rank ladders: the Blacksmith (4/5/10/15/15/20×4) and Chef (5×2, 10×2, 15×3, 20×2) vectors match the note's table (`tests/piece_040.rs:145-178`). Only 23872 has rank 0 (`tests/piece_040.rs:121-126`).
- Cross-class ids 869 and 2518 (`piece_040.rs:545`).
- Level title rows: 10 (5 per job, levels 4/8/12/16/20). Gate quests: 8 (levels 5/10/15/20 per job). Ids match the note (`piece_040.rs:547-695`).
- Wiki rows: Strong Arm Stew (minigame 46, difficulty 1, no rank) and Starnut Sundae (minigame 186, difficulty 3, required rank 10) (`piece_040.rs:697-718`).
- Validator policy: rank floor 1 (`rank_access`, line 775), cap 20 (line 776), and `UnknownRecipe` for unknown rows (lines 790/793/826). Matches the "Reconstructed" paragraph.
- Wiring: no `src/` file outside `piece_040.rs` references the module, so "the lead-owned wiring was not modified" still holds.
- Curve gap: `src/profiles.rs:2` and `:227` describe the reconstructed local 100-XP curve, matching the `job_rank_curve_missing` gap.
- The checker emits the two warnings the note reports: `wiki_gate_page_coverage` and `wiki_recipe_name_coverage` (`scripts/pieces/piece_040.py:601-683`).

**Unsure (not checkable from the repo):**
- Pass/warn counts in the evidence run ("14 pass, 2 warn"), the "59 passed / 10 ignored" cooking/forging run, and the evidence files under `../lab/reports/piece-040-20261009T035326Z/`. These live outside the `repo` and `refs` roots, and I did not run the tests.
- Wiki and locale facts (revisions 45318/46136/46062, the 25 vs 22 Chef row counts, the 23-of-25 empty `Where to find` cells, row ids 34060–34159, 387551–387641), and the 85,932-row locale count. These are data claims about external corpora, not our code.
- The "Chef name" / "Blacksmith name" attribution for 869 and 2518 is only partly verifiable from our code, which records only the names and class ids.
