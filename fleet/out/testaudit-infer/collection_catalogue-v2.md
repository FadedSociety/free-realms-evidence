<!-- fleet job=testaudit-infer id=collection_catalogue-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[11848, 12940, 6, 1752] model=claude-haiku-5-5 -->
# tests/collection_catalogue.rs

{"file": "tests/collection_catalogue.rs",
 "tests": [
  {"name": "committed_catalogue_holds_every_captured_collection", "verdict": "keep", "covered_by": null, "reason": "Whole-catalogue totals and link/note invariants; no similar file performs this check (collection_coins.rs covers a different file format)."},
  {"name": "collection_10_matches_the_capture", "verdict": "keep", "covered_by": null, "reason": "Field-by-field pin of one captured collection and entry row; not repeated in the similar files."},
  {"name": "exploration_sets_carry_their_captured_rows", "verdict": "keep", "covered_by": null, "reason": "Pins reward items, tokens, collection_add and name ids for specific captured sets; not found elsewhere."},
  {"name": "entry_for_item_answers_only_unique_links", "verdict": "keep", "covered_by": null, "reason": "Refusal check: an item linked by two entries and a negative id must answer None."},
  {"name": "every_bound_item_has_a_runtime_definition", "verdict": "keep", "covered_by": null, "reason": "T630 cross-source gate (catalogue bindings vs runtime item catalogue); no similar test performs this join."},
  {"name": "loader_refuses_bad_files", "verdict": "keep", "covered_by": null, "reason": "Loader refusal suite for this loader. collection_coins.rs has a same-named test but for CollectionCoins, so it does not supersede it."},
  {"name": "meta_map_drops_a_chain_whose_source_is_another_target", "verdict": "keep", "covered_by": null, "reason": "Not present in the current file (grep finds no meta_map test in tests/collection_catalogue.rs). The pack's test list is stale; nothing to remove. Conservatively kept as a refusal-type check if it exists in another revision."},
  {"name": "meta_map_dedupes_repeats_and_refuses_two_targets", "verdict": "keep", "covered_by": null, "reason": "Not present in the current file (no such test in the tree). Pack list is stale; no removal proposed. Refusal-type behaviour, so kept conservatively."},
  {"name": "regenerate_or_check_collection_catalogue", "verdict": "keep", "covered_by": null, "reason": "Ignored generator/drift oracle; the only drift check for the committed file. Costs no batch time while ignored."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Verified on disk: the file has loader_refuses_bad_files (line 251) and regenerate_or_check_collection_catalogue (line 623), and the first five tests match. The two meta_map tests named in the pack and in the previous answer do not exist in the tree (the pack's 725-line count and doc lines are from a different revision), so their verdicts are unverified against code. The previous answer's claim that its read covered only 639 lines is consistent with the file on disk being shorter than the pack. Re-pack from the current tree before relying on the meta_map entries. No removal is proposed; the file is kept whole."}
