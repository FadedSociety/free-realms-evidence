<!-- fleet job=testaudit-infer id=harvesting_runtime_tiles-v1 status=no_submit turns=2 usd=0.0024 tokens(read,write,in,out)=[9126, 12607, 6, 1396] model=claude-haiku-5-5 -->
# tests/harvesting_runtime_tiles.rs

```json
{"file": "tests/harvesting_runtime_tiles.rs",
 "tests": [
  {"name": "malformed_persisted_harvesting_configs_are_refused_without_mutation", "verdict": "keep", "covered_by": null, "reason": "Refusal and no-mutation check for four malformed tile registrations (missing produce 411, duplicate 411, wrong category, out-of-set kind 505). The border file only covers the border gate, not the tile gate, so nothing else checks these tile refusals."},
  {"name": "valid_four_kind_content_loads", "verdict": "keep", "covered_by": null, "reason": "Positive load check that also asserts the four-tile count and that the harvesting engine is kept. The closest twin, harvesting_runtime_border.rs::padded_content_mining_and_legacy_stay_permissive, loads the same writer output but does not assert the four-tile count, so this is not strictly superseded. It is near-duplicate in spirit and could be merged, but it is kept conservatively."},
  {"name": "missing_content_legacy_and_mining_stay_permissive", "verdict": "keep", "covered_by": null, "reason": "Permissive-contract canary. The legacy no-content branch is also in harvesting_runtime_border.rs::padded_content_mining_and_legacy_stay_permissive, so that branch is a duplicate. The mining branch and the Chef profile/game-id assertions add coverage the border file lacks, so the test is kept whole. Trimming the legacy branch would be a safe follow-up."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Closest file is tests/harvesting_runtime_border.rs (same fixture pattern, border gate instead of tile gate). Its padded/legacy/mining test overlaps this file's third test on the legacy and writer-load paths. The tile-refusal test is unique to this file. I did not read the other similar files (type8_gateway, type8_harvesting_gateway, kart_service, npc_interaction) in depth; they test mining/harvest gateway and other features and do not appear to drive Gameplay::load tile refusals. Task metadata (created_by/last_changed_by) is null, so no obsolescence by task was found."}
```
