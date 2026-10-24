<!-- fleet job=test-audit id=tests-scavenger-hunt-quest-rs-L1201 status=done turns=8 usd=0.0061 tokens(read,write,in,out)=[80558, 22054, 18, 5082] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/scavenger_hunt_quest.rs lines 1201-1257 of 1257

Window `tests/scavenger_hunt_quest.rs` 1201-1257 (helpers `npc_row`, `Scratch`, `copy_split_content`, and the tail of `a_quest_that_no_job_lists_is_rejected_by_the_split_loader` at 1193-1213). The mutation logic is sound: `QUEST` (3_000_200, from `support/scavenger_hunt.rs:40`) is present in the shipped `jobs.json` (line 74), and the loader's union rule at `quest_engine.rs:899-908` does reject a quest no job lists. The helpers are used. Two weaknesses remain in the test's assertions:

- **[medium] tests/scavenger_hunt_quest.rs:1193 a_quest_that_no_job_lists_is_rejected_by_the_split_loader - no control load on the untouched copy before the mutation, unlike the sibling `a_malformed_hunt_record_is_a_load_error` (lines 1173-1176).** 
  Why it cannot catch a regression: if the shipped `jobs.json` ever stops listing `QUEST`, or `copy_split_content` produces a copy the loader rejects, the loader already fails at `quest_engine.rs:904-907` before the test's own mutation takes effect. The test then gets the same `InvalidData` and the same "jobs" substring and passes without exercising the rule it names.
  Fix: before line 1196's mutation, assert `QuestEngine::from_split_content(&scratch.0, 1, eligibility(), None).is_ok()` with a message such as "the untouched copy must load", as 1173-1176 does.

- **[low] tests/scavenger_hunt_quest.rs:1208-1211 a_quest_that_no_job_lists_is_rejected_by_the_split_loader - the error check is kind plus a bare substring "jobs", not the specific rule.** 
  Why it cannot catch a regression: any `InvalidData` error whose text contains "jobs" passes, including a jobs.json parse or schema failure, or a different future jobs-related message. The doc comment says the error "names the jobs.json union rule", but the loader's message (`split jobs reference missing quest definitions`, `quest_engine.rs:907`) is never matched.
  Fix: assert `error.to_string().contains("missing quest definitions")`, or the exact message from `quest_engine.rs:907`, so only the union rule satisfies the check.</result>
