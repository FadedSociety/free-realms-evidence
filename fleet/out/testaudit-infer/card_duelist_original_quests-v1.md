<!-- fleet job=testaudit-infer id=card_duelist_original_quests-v1 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[19934, 11269, 8, 1678] model=claude-haiku-5-5 -->
# tests/card_duelist_original_quests.rs

{"file": "tests/card_duelist_original_quests.rs",
 "tests": [
  {"name": "shipped_card_duelist_bindings_load_and_stay_disabled", "verdict": "keep", "covered_by": null, "reason": "Only check that the shipped 3040011/3040034 giver and turn-in bindings load through the production engine, and that both quests refuse offers at every NPC with no state change. Refusal check; no equivalent test found elsewhere in the suite (tests/card_duelist_trainer.rs covers Sam's teaching menu, not these quests)."},
  {"name": "esther_the_brains_starts_at_dominic_and_meeting_esther_advances_it", "verdict": "keep", "covered_by": null, "reason": "Pins the recorded giver (Dominic, not Esther) and the objective-1 advance with no payout at accept or talk. No other test in the suite references quest 3040034 or the Esther chain, so it is the only check of this behaviour."},
  {"name": "poes_best_deck_is_offered_by_poe_with_its_xp", "verdict": "keep", "covered_by": null, "reason": "Checks the recorded 49/1 reward bundle (0 coins, 300 XP) and the Offered status for quest 3040011. No other test references this quest. The bundle values are recorded data, so keep."},
  {"name": "card_duelist_quests_need_the_job", "verdict": "keep", "covered_by": null, "reason": "Job gate for both quests (engine and in-world refusal without profile 120 active). The pack excerpt cuts off before the body, so it could not be fully checked; kept by the conservative rule (gate/refusal behaviour)."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "Each test covers quest IDs (3040011, 3040034) that no other test file in the repo references, so no superseded or duplicate verdicts are supported. Shared helpers (learn_card_duelist, card_duelist) overlap with tests/card_duelist_trainer.rs setup, but that is shared setup, not duplicated assertions. Could not read the file directly: the read tool returned 'not a file' for the path, so verdicts rest on the pack excerpt. The last test's body was truncated in the excerpt."}
