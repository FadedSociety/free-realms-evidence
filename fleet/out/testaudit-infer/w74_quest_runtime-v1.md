<!-- fleet job=testaudit-infer id=w74_quest_runtime-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[7845, 8654, 6, 1121] model=claude-haiku-5-5 -->
# tests/w74_quest_runtime.rs

{"file": "tests/w74_quest_runtime.rs",
 "tests": [
  {"name": "saved_regional_quest_syncs_on_world_entry_and_bad_application_messages_are_dropped", "verdict": "keep", "covered_by": null, "reason": "Single end-to-end test that chains several behaviours no other visible test in this set combines: a saved regional quest replayed as a 49/3 record on world entry (quest_add_packet bytes compared to the entry replies), malformed 49/2 and unknown 49/99 application messages rejected with trace entries while pending_turnin is left unchanged (refusal/hostile-input check), and a 49/14 turn-in completing the quest with persisted state. Partial overlap with npc_interaction.rs quest_reply_49_2_reads_the_client_id_and_accept_flag and quest_end_reply_49_14_uses_six_byte_header_and_quest_id, and quest_engine.rs quest_add_packet use, but those are unit-level and do not cover the gateway world-entry sync or the trace-rejection assertions. Being conservative, keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The only test is #[ignore]d and needs private lab/references checkouts, so it does not run in the public suite; that is a cost/coverage note, not a removal reason. I did not read the similar files' bodies in depth; the verdict rests on test names and a grep for quest_add_packet/trace-reason strings, so the overlap judgement is moderate-confidence. Possible follow-up: confirm whether npc_interaction.rs's 49/2 and 49/14 tests assert the trace reason strings used here."}
