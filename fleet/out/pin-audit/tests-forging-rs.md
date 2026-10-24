<!-- fleet job=pin-audit id=tests-forging-rs status=nothing_found turns=6 usd=0.0032 tokens(read,write,in,out)=[35321, 12938, 14, 2421] model=claude-haiku-5-5 -->
# tests/forging.rs

No findings in `prototype/osfr-tools/tests/forging.rs` for the three screened lines.

- **tests/forging.rs:409 chain_gravity_matches_right_to_left_bottom_to_top_queue_order - not a finding.** `400` is the base chain score, `CHAIN_SCORE = 400` in `src/harvesting.rs:70`, applied by `chain_score()` (`harvesting.rs:120`). It is a code constant, not a value in any `data/content` file. The data-free constant is pinned in `tests/harvesting.rs:166` too, which is outside this file. The forging path does not read a tunable score from data. If the team wants it live-tunable, that is a code change, not a test fix here.
- **tests/forging.rs:455 quota_then_native_next_level_awards_fixed_recipe_once_even_after_reload - not a finding.** `(30280, 1)` is a grant of item definition id 30280 (`data/content/recipes.json:3424`). Per the audit rule, an id is not a tunable value. The same test already reads the recipe row from `recipes.json` (lines 456-483) and checks `tx.grants[0]` against `output.definition_id` and `output.count`, so the hard-coded pair is a redundant id check, not a tuning pin.
- **tests/forging.rs:545 playable_generated_board_reaches_five_hammer_pieces_through_real_messages - not a finding.** Same as 455: id `30280` from `recipes.json`, an id rather than a tunable number.
