<!-- fleet job=testaudit-infer id=piece_057-v1 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[10029, 15074, 6, 1869] model=claude-haiku-5-5 -->
# tests/piece_057.rs

{"file": "tests/piece_057.rs",
 "tests": [
  {"name": "loot_event_opcode_is_the_original_client_sub_packet", "verdict": "keep", "covered_by": null, "reason": "Pins the recovered loot-event sub-packet id (29). No other Rust test in the repo references PLAYER_UPDATE_LOOT_EVENT; the only other references are the Python oracle, which checks the source constant rather than a Rust test."},
  {"name": "loot_prop_models_are_recovered_asset_rows", "verdict": "keep", "covered_by": null, "reason": "Recovered model ids for loot props; no other Rust test covers LootProp::model_id or these constants."},
  {"name": "loot_toast_locale_ids_are_recovered", "verdict": "keep", "covered_by": null, "reason": "Recovered locale ids for loot toasts and coins name; unique to this file."},
  {"name": "documented_drop_lists_are_recorded_verbatim_with_gaps", "verdict": "keep", "covered_by": null, "reason": "Verbatim check of five wiki-documented drop lists including explicit gaps (missing name ids); the data exists only in this module. Not a duplicate of any other test."},
  {"name": "documented_lists_refuse_to_become_weighted_tables", "verdict": "keep", "covered_by": null, "reason": "Refusal check: documented lists must not gain invented probabilities. Refusal checks are kept; no equivalent test elsewhere."},
  {"name": "pinned_weighted_selection_matches_community_semantics", "verdict": "keep", "covered_by": null, "reason": "Pins weighted selection and out-of-range roll behaviour of DropTable; unique to this module."},
  {"name": "weighted_tables_reject_the_invalid_shapes_the_pinned_loader_rejects", "verdict": "keep", "covered_by": null, "reason": "Hostile/invalid input refusal for empty, zero-weight, non-positive quantity and amount tables; kept as a refusal check."},
  {"name": "a_kill_is_registered_once_and_granted_once", "verdict": "keep", "covered_by": null, "reason": "Once-only kill registration and grant contract (idempotence/persistence-style check); no other test drives LootLedger."},
  {"name": "grants_require_the_killer_and_a_registered_defeat", "verdict": "keep", "covered_by": null, "reason": "Security/eligibility refusal check (unregistered kill, non-killer claimant); kept."},
  {"name": "invalid_tables_are_refused_without_consuming_the_kill", "verdict": "keep", "covered_by": null, "reason": "Refusal check that an invalid table does not spend the kill; kept."},
  {"name": "loot_prop_policy_is_labelled_reconstruction", "verdict": "keep", "covered_by": null, "reason": "Pins which loot props are used for which case (chest vs bags/coins); unique to this module."}
 ],
 "whole_file_removable": false,
 "confidence": 0.85,
 "notes": "The five most similar files (piece_056, kart_racing, station_cash, piece_084, piece_072) are unrelated domains (effects, racing, cash shop, selling, objectives). A repo-wide search for LootLedger, DropTable, PLAYER_UPDATE_LOOT_EVENT, weighted_from_documented and COMMUNITY_DOCUMENTED_DROPS found no other Rust test using them; only the src module, this test file, and the Python oracle (scripts/pieces/piece_057.py, tests/pieces/test_piece_057.py) reference them. No superseded, duplicate or obsolete verdicts apply. Caveat: the constants-only tests are cheap, but they are the only pins of recovered evidence, so they are kept per the conservative rule. Overlap with the Python oracle is across languages and not counted as duplication."}
