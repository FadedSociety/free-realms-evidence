<!-- fleet job=pin-audit id=tests-cooking-rs status=done turns=7 usd=0.0026 tokens(read,write,in,out)=[31801, 10196, 16, 2021] model=claude-haiku-5-5 -->
# tests/cooking.rs

- **prototype/osfr-tools/tests/cooking.rs:316 six_ordered_rounds_create_fixed_recipe_intent_once_and_restore - pins `(35, 1)` from `prototype/osfr-tools/data/content/recipes.json` `recipes[key="chef.strong_arm_stew.sample"].output` (`definition_id` 35, `count` 1).** The grant is built in `src/cooking.rs:529` as `(recipe.product_definition_id, recipe.product_quantity)`, so it comes straight from that recipe row. The fixture loads the real `recipes.json` via `include_str!` (cooking.rs:51), so retuning the output count, or the output item, in the data would break this assertion while the code stays correct.
  **Fix:** read the expected grant from the recipe row, not from a literal. Load `recipes.json` in the test (or via the existing recipe loader used by `Cooking::load`), find the entry with key `chef.strong_arm_stew.sample`, and assert `t.grants == vec![(recipe.output.definition_id, recipe.output.count)]`. Keep the `vec![...]` shape check (one grant entry) as a separate count assertion.

Note: the same literal `vec![(35, 1)]` appears at cooking.rs:507 (not on the screened list). It has the same problem and should get the same fix.
