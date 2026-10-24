<!-- fleet job=pin-audit id=tests-cooking-gameplay-rs status=done turns=15 usd=0.0072 tokens(read,write,in,out)=[196871, 22171, 32, 4925] model=claude-haiku-5-5 -->
# tests/cooking_gameplay.rs

Two of the three screened lines pin a number that ships in a data file. Line 339 does not.

- **prototype/osfr-tools/tests/cooking_gameplay.rs:340 cooking_gameplay test (`private_chef_gather_cooking_atomic_once_gates_restore_cancel`) - pins `1` from `prototype/osfr-tools/data/content/recipes.json` `output.count` (the Strong Arm Stew row, `output.definition_id` 35, `count` 1).**
  - **Fix:** read it through the recipe row. Look up the Strong Arm Stew recipe in `recipes.json` and assert `count(&g, 35) == recipe.output.count`, or bound it as `>= 1`. The test itself does not set the output.

- **prototype/osfr-tools/tests/cooking_gameplay.rs:345 private_chef_gather_cooking_atomic_once_gates_restore_cancel - pins `1` from `prototype/osfr-tools/data/content/recipes.json` `output.count` (same Strong Arm Stew row, item 35).** The `0` for item 2862 is an ingredient that is consumed, not a tunable value, so it is not a finding.
  - **Fix:** same as line 340. Read the expected output count from the recipe row and compare it to `count(&restored, 35)`. Keep the `0` for 2862.

Not a finding:
- **cooking_gameplay.rs:339 `count(&g, 14794) == 1`.** The reward count `[14794, 1]` comes from the stage 910004 `reward.items` in `tests/fixtures/quests/opening.json`, which is a test fixture. The test loads its content from `lab/references`, not from `data/content`, so no shipped data file holds this value. Leave it as is. If the team wants it live-tunable, move the expected value into that fixture row and read it there.

Note: the stage 910004 craft trigger uses `recipe_id` 2001, while the `recipes.json` Strong Arm Stew row is `recipe_id` 70. The 35 output in lines 340 and 345 is the same item either way, so the finding stands, but whoever writes the fix should confirm which recipe row the runtime actually uses.
