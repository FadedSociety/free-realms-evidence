<!-- fleet job=testaudit-infer id=content_jobs-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[29026, 14572, 10, 1543] model=claude-haiku-5-5 -->
# tests/content_jobs.rs

{"file": "tests/content_jobs.rs",
 "tests": [
  {"name": "job_batch_loads_and_npc_references_resolve_or_are_declared", "verdict": "keep", "covered_by": null, "reason": "Mostly overlaps tests/content_npcs.rs::regional_npc_batch_and_resolved_job_references_validate (same 17-job count, same trainer_npc_ids resolved-or-unresolved check, same ContentDb::load over a scratch package, same db.jobs.len()==17). Not a clean duplicate, though: it is the only test here that checks quest talk-objective npc_id references (Call the Crew!: Shakey) against the NPC set, and it asserts the newer 23-file quest layout (T500-T502 zone slices). content_npcs.rs still asserts 19 quest files and 660 quests, so the two files disagree on the current batch. Kept because it is the only check of the objective-NPC path and the newer quest-file snapshot; the overlap is a candidate for consolidation rather than removal."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Single test, so the file is one binary's worth of time. Its job-count and trainer-reference checks duplicate content_npcs.rs (created T247, last changed F710); the stale quest-file count (19) there versus 23 here is a maintenance issue worth fixing in content_npcs.rs rather than deleting this test. I did not inspect content_dungeons.rs or content.rs in depth; they appear to cover dungeon and generic ContentDb validation, not job/NPC batch references."}
