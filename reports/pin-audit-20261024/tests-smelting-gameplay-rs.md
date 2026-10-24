<!-- fleet job=pin-audit id=tests-smelting-gameplay-rs status=done turns=8 usd=0.0068 tokens(read,write,in,out)=[99741, 26997, 18, 4821] model=claude-haiku-5-5 -->
# tests/smelting_gameplay.rs

Checked the three screened lines against `data/content/recipes.json` row `miner.copper_bar.sample` (recipe_id 4, ingredients 2739×5 and 879×3, output 21785×5), and against the code paths that produce the counts.

- **prototype/osfr-tools/tests/smelting_gameplay.rs:275 private_mining_smelting_reward_atomic_once_restore_and_cancel - pins `3` (coal consumed, so 879 = 5 − 3 = 2) and `5` (bars granted) from `data/content/recipes.json` `records[key="miner.copper_bar.sample"]` `ingredients[definition_id=879].count` and `output.count`.**
  - **Fix:** read it through the recipe row. Load `data/content/recipes.json` (the pattern in `tests/smelting.rs:494` and `tests/cooking.rs:514` uses `include_str!`), find the row with key `miner.copper_bar.sample`, and compute the expected values as `mined_coal − row.ingredients[879].count` and `row.output.count`. The mined amount of 5 comes from the test's own loop and can stay as is.

- **prototype/osfr-tools/tests/smelting_gameplay.rs:327 private_mining_smelting_reward_atomic_once_restore_and_cancel - pins `5` (Copper Bar output per craft) from `data/content/recipes.json` `records[key="miner.copper_bar.sample"]` `output.count`.**
  - **Fix:** read it through the same recipe row, `assert_eq!(count(&g, 21785), row.output.count)`.

Not a finding:
- **smelting_gameplay.rs:198** `(5, 5)`: the ore and coal amounts are the test's own loop count (5 interactions). The per-interaction grant of 1 each is hard-coded in `src/gameplay.rs:4539`, not in a data file, so it is not a shipped data value.
