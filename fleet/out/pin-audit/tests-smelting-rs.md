<!-- fleet job=pin-audit id=tests-smelting-rs status=done turns=6 usd=0.0035 tokens(read,write,in,out)=[46927, 15659, 14, 2239] model=claude-haiku-5-5 -->
# tests/smelting.rs

**prototype/osfr-tools/tests/smelting.rs:316 four_round_win_is_single_server_recipe_intent_and_survives_restart - pins `5` from `prototype/osfr-tools/data/content/recipes.json` `output.count` (row `miner.copper_bar.sample`, `recipe_item_definition_id` 381, `job` miner, `ingredients` 2739x5 and 879x3, output `definition_id` 21785).**

- The test's expected grant `(21785, 5)` is the shipped output quantity of the smelting recipe that `begin(14)` loads. The test's own fixture (`Fixture::new`, lines 46-47) copies the shipped `recipes.json` into a temp dir, so the grant is the data value, not a number the fixture sets. The matching `consumes` assertion on line 317 is already read from the requirements, and the grant path in `src/gameplay/crafting.rs` is `recipe.product_quantity`, which comes from `row.output.count`.
- Retuning that data row would break this assertion while the code is still correct, so it is a finding.
- **Fix:** read it through the loaded row. Load `data/content/recipes.json` in the test (or the fixture's copied file), find the entry whose `ingredients` match the `requirements()` result, and compare `transaction.grants` to `vec![(output.definition_id, output.count)]`. Alternatively, bound it as `assert_eq!(transaction.grants.len(), 1)` and `assert!(transaction.grants[0].1 >= 1)`. I found no existing helper under `tests/common/` for recipe rows, so the row read is the direct route.

The other lines I checked are not findings in this sense: line 317 derives from the requirements, and the remaining 21785 counts are in other test files outside the screened list.
