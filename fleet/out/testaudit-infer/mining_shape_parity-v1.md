<!-- fleet job=testaudit-infer id=mining_shape_parity-v1 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[23845, 17440, 8, 1825] model=claude-haiku-5-5 -->
# tests/mining_shape_parity.rs

{"file": "tests/mining_shape_parity.rs",
 "tests": [
  {"name": "shape1_regular_cells_exclude_collectables_at_forced_percent", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the shape-1 (TILE_BUILDREGULAR) collectable-free pool at forced 100%. Other mining test files set collectable_percent to 0 (mining.rs, mining_dead_board.rs, mining_powerups.rs, mining_review.rs fixtures), so they never exercise the collectable pool and cannot cover this refusal."},
  {"name": "shape2_any_allows_collectables_at_forced_percent", "verdict": "keep", "covered_by": null, "reason": "Only check that shape 2 (TILE_BUILDANY) still draws collectables; no other test file drives the shape-to-pool dispatch with collectables enabled. Its positive assertion is the counterpart guarding against over-restriction."},
  {"name": "gravity_refill_queue_still_allows_collectables", "verdict": "keep", "covered_by": null, "reason": "Only test that checks the refill queue after a chain keeps the collectable-enabled pool (random_tile(true) path, src/mining.rs ~1539). Unique coverage of that path among the mining tests."},
  {"name": "mixed_seed_cases_keep_shape1_collectable_free", "verdict": "keep", "covered_by": null, "reason": "Different from the single-seed tests: it sweeps four seeds at 50% and asserts both the shape-1 refusal and a refill-queue assertion. Its shape-2 tail (seed 19, 100%) repeats shape2_any_allows_collectables_at_forced_percent with a different seed, so it is a partial overlap, but the multi-seed shape-1 sweep is not covered elsewhere. Kept conservatively."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "The four tests are the only ones in the suite that set a non-zero collectable_percent and check the shape-to-pool dispatch in Type8 (mining.rs random_tile, shape codes 1/2). The similar files (mining_idle, mining_review, mining_move_detection, kart_service, quest_turnin_feedback) do not touch the collectable pool. The only possible trim is the trailing shape-2 block of mixed_seed_cases_keep_shape1_collectable_free, which duplicates shape2_any_allows_collectables_at_forced_percent with a different seed; I did not mark it removable. Fixtures are synthetic temp files and are cleaned up on drop."}
