<!-- fleet job=test-verify id=tests-piece-066-rs-L1-f1 status=done turns=7 usd=0.0066 tokens(read,write,in,out)=[80893, 25166, 16, 5190] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_066.rs:340

**Verdict:** `refuted`

**Premise check (accurate):** The fixture really does store the truncated token. `notes/Research/original-quest-coverage.json:1375-1376` has `"prerequisites": ["Quest:Your"]` for `Quest:Fighting off the Pack`, and `previous` at line 1378 is `Quest:Your First Weapon`. The ledger records the defect at `notes/Reviews/MMO Dispatch Ledger.json:181` as open. The test loads this file through `QuestCatalogue::load_workspace()` → `CATALOGUE_RELATIVE_PATH = "notes/Research/original-quest-coverage.json"` (`src/restoration/piece_066.rs:40`). So the test does pin the bad value.

**Why the claim does not hold:** The claim says the test cannot catch the regression it names. Walking the test against plausible regressions of the code under test:

- `tests/piece_066.rs:339-341` is `links.iter().any(|link| link.page == "Quest:Fighting off the Pack" && link.prerequisite == "Quest:Your")`. If `prerequisite_links()` (`src/restoration/piece_066.rs:502-513`) returns an empty Vec, drops the link, swaps page and prerequisite, or emits a different string, the `any` is false and the test fails.
- Those are the regressions this test exists to catch, and it catches them.
- The one thing it does not flag is the data truncation. That is a known, ledgered data defect, not a regression. It is also not invisible: the same file already pins the full title in `wiki_pages_carry_pinned_revision_prerequisite_and_start_npc` (`tests/piece_066.rs:135`, `pack.previous == "Quest:Your First Weapon"`), so the full-title value is covered in another field.

What the claim actually describes is a characterization assertion that encodes a known-wrong expectation. If the extractor is repaired, this test goes red, and the correct response is to update the expected string as part of that repair. That is a stale-oracle hygiene issue, not a case where a regression slips through. Nothing a regression could do to `prerequisite_links` passes this test silently.

**Side note (does not change the verdict):** The proposed fix's second link, `Quest:Learn to Mine & Smelt Ore` for page `Quest:Your First Weapon`, is also not in the data. The `Quest:Your First Weapon` row at json:1401-1404 has `"prerequisites": ["Quest:Learn"]`, which is the same truncation, and `Learn to Mine & Smelt Ore` appears only in `previous`. So an assertion that the full title is present would fail today, which is expected for a known-open defect. Marking the test `#[ignore]` with a reason is a reasonable hygiene choice, but it is a separate question from whether the test can catch a regression.
