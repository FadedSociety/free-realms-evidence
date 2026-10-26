<!-- fleet job=testaudit-infer id=quest_offer_gates-v1 status=no_submit turns=4 usd=0.0046 tokens(read,write,in,out)=[43984, 20306, 10, 3183] model=claude-haiku-5-5 -->
# tests/quest_offer_gates.rs

```json
{"file": "tests/quest_offer_gates.rs",
 "tests": [
  {"name": "objective_less_quest_is_hidden_and_skipped_by_the_talk_offer_path", "verdict": "keep", "covered_by": null, "reason": "quest_engine.rs::empty_objective_quest_cannot_be_offered_or_turned_in covers the engine refusal (offer/accept/turn-in unchanged), but not the NpcInteraction talk-path skip (offerable_quest_for_talk returning the next valid quest) or the Unavailable denial. The talk-skip is a distinct behaviour, so it is kept."},
  {"name": "under_level_offer_is_refused_without_mutation_then_qualifies", "verdict": "keep", "covered_by": null, "reason": "quest_save_tolerance.rs::split_level_and_job_gates_use_supplied_levels_and_recheck_accept and quest_engine.rs (around line 413) check the Level denial on offer and the later qualification. Neither asserts the full state is unchanged after a refused offer, which is this test's atomicity check. Overlap is high, so it is a candidate for merging, but it is not clearly superseded."},
  {"name": "job_requirement_uses_the_matching_job_level_and_refusals_are_atomic", "verdict": "keep", "covered_by": null, "reason": "quest_save_tolerance.rs::split_level_and_job_gates_use_supplied_levels_and_recheck_accept covers the Job denial for a wrong job and an under-level matching job. This test adds the atomic-state assertions and the qualified accept, so it is kept. Overlap is high."},
  {"name": "denied_accept_preserves_pending_offer_for_requirement_and_limit", "verdict": "keep", "covered_by": null, "reason": "Pins that a refused accept (Level or Limit, with QuestLimit message) keeps the pending offer unchanged. No other test found that checks the pending offer survives a refused accept on both gates."},
  {"name": "limit_refusal_preserves_the_developer_offer_for_a_retry_after_the_cap_rises", "verdict": "keep", "covered_by": null, "reason": "Unique check that a developer override survives a Limit refusal and still accepts after the cap rises. Not found in the similar files."},
  {"name": "a_declined_developer_offer_cannot_bypass_a_later_ordinary_offers_gate", "verdict": "keep", "covered_by": null, "reason": "Security-style check: a spent developer override must not bypass a later level gate. Not found elsewhere, so it is kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The file overlaps heavily with quest_save_tolerance.rs::split_level_and_job_gates_use_supplied_levels_and_recheck_accept and quest_engine.rs (offer Level/Job denials, empty-objective refusal). The overlap is on denial results; the atomicity and developer-override checks are unique to this file. I did not read the full talk-path tests in npc_interaction.rs or quest_giver_rows.rs, so the talk-skip verdict is the least certain. If merging is wanted, the two level/job tests could fold into the split-gate test without losing coverage. Nothing here is obsolete."}
```
