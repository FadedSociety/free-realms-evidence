<!-- fleet job=pin-audit id=tests-piece-066-rs status=nothing_found turns=6 usd=0.0031 tokens(read,write,in,out)=[39680, 14251, 14, 1755] model=claude-haiku-5-5 -->
# tests/piece_066.rs

No findings in `prototype/osfr-tools/tests/piece_066.rs` for the screened lines.

- **tests/piece_066.rs:117 wiki_pages_carry_pinned_revision_prerequisite_and_start_npc - `Some(16)` is not a tunable value.** The number comes from the recovered wiki record for `Quest:Your First Weapon`. `QuestCatalogue::load_workspace()` (src/restoration/piece_066.rs:391) reads `notes/Research/original-quest-coverage.json`, where that page's `coin_reward` is 16 (line 1412). It is a historical observed fact, not a gameplay value in `data/content/*.json`, and it is not produced by any code path the test could break by retuning. Leave as is.
- **tests/piece_066.rs:134 wiki_pages_carry_pinned_revision_prerequisite_and_start_npc - `Some(18)` is the same kind of value.** It comes from `Quest:Fighting off the Pack` in the same research file (`coin_reward` 18, line 1387). Leave as is.

Both assertions check the catalogue's recovered evidence, pinned by the file's own revision IDs (27815 / 28955). Neither reads a live data file that is meant to be tuned.
