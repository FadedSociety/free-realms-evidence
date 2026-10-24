<!-- fleet job=test-audit id=tests-piece-066-rs-L1 status=done turns=6 usd=0.0080 tokens(read,write,in,out)=[60661, 29755, 14, 7319] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_066.rs lines 1-348 of 348

Window: `prototype/osfr-tools/tests/piece_066.rs` lines 1-348 (read in full), checked against `src/restoration/piece_066.rs` (`validate`, `prerequisite_links`, `local_binding`) and `notes/Research/original-quest-coverage.json`.

- **[high] prototype/osfr-tools/tests/piece_066.rs:340 prerequisite_links_expose_the_wiki_chain - the test pins a known-truncated extractor token, `"Quest:Your"`, as the correct prerequisite.**
  - Why it cannot catch a regression: the JSON (`original-quest-coverage.json:1375-1376`) stores `"Quest:Your"` because of a whitespace-split extraction defect. The page's real prerequisite is `Quest:Your First Weapon` (the same row's `previous` field, json:1378, and `notes/Research/Pieces/066 Historical quest catalogue.md:54-57` say so). The assertion locks in the wrong value, so the test passes on the bug and would fail on the fix. A repair that extracts the full title would turn this test red, and it gives no signal that the value is wrong.
  - Fix: assert `link.prerequisite == "Quest:Your First Weapon"` (and the `Quest:Learn to Mine & Smelt Ore` link for page `Quest:Your First Weapon`), and make the test fail until the extractor is repaired. Until then, mark it `#[ignore = "truncated prerequisite token, see notes/Reviews/MMO Dispatch Ledger.json 066 entry"]` rather than pinning the defect. The dispatch ledger already records this defect as open ("repair falls to lead").

- **[high] prototype/osfr-tools/tests/piece_066.rs:224 validator_reports_gaps_without_fabricating_errors - the expected warning `unresolved wiki prerequisite "Quest:Learn"` pins the same truncated token.**
  - Why it cannot catch a regression: once the prerequisite is extracted in full (`Quest:Learn to Mine & Smelt Ore`), `validate()` (src lines 643-657) resolves it through the `previous` chain and no longer emits this warning. The test then fails on a correct fix and passes on the broken state. It checks for a warning that exists only because of the defect.
  - Fix: remove the `Quest:Learn` entry from the expected list and assert the warning set is empty for wiki prerequisites, or assert that every wiki prerequisite resolves (`page_titles` or `chain` contains it). Keep the `errors.is_empty()` check at line 212.

- **[low] prototype/osfr-tools/tests/piece_066.rs:335 prerequisite_links_expose_the_wiki_chain - the name says it exposes the wiki chain, but the body checks one prerequisite link and one start NPC; `previous`/`next` are never asserted.**
  - Why it cannot catch a regression: a change that drops the `previous`/`next` chain (or breaks `chain` in `validate()`, src 634-642) still passes, because only one `prerequisite` string and the NPC are checked.
  - Fix: assert `previous`/`next` for `Quest:Fighting off the Pack` (`Quest:Your First Weapon` / `Quest:Eviction Notice`), or rename the test to say it checks the prerequisite link and start NPC.

- **[low] prototype/osfr-tools/tests/piece_066.rs:254 objective_and_reward_rows_aggregate_with_source_labels - the name promises aggregation, but the test only uses `find` and `any` on single rows.**
  - Why it cannot catch a regression: `objective_rows()` or `reward_rows()` could drop rows, duplicate them, or stop grouping them, and the test still passes as long as one matching row exists.
  - Fix: assert the exact row count per source (for example, the total number of objective rows equals the sum of `objectives.len()` across quests), or rename the test to `objective_and_reward_rows_carry_source_labels`.

Not flagged: the count and totals assertions (lines 42-70), the local-stage binding checks, and the fabricated-binding and duplicate-id mutation tests (lines 281-333). Those mutations do change the outputs the tests check, and `validate()` emits the matching errors.
