<!-- fleet job=testaudit-infer id=warrior_trainer-v2 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[36983, 13999, 10, 2203] model=claude-haiku-5-5 -->
# tests/warrior_trainer.rs

{"file": "tests/warrior_trainer.rs",
 "tests": [
  {"name": "dewey_is_drawable_and_has_a_warrior_trainer_row", "verdict": "keep", "covered_by": null, "reason": "Content canary for Dewey (POI record, extra spawn, drawn AddNpc, Warrior trainer row). Overlaps job_trainers::trainer_rows_match_the_job_and_spawned_npc_content in part, but the drawn-AddNpc check was not verified elsewhere, so keep."},
  {"name": "warrior_requires_brawler_rank_5", "verdict": "keep", "covered_by": null, "reason": "The previous verdict (superseded by job_trainers::service_refusals_change_nothing) is not supported. I checked job_trainers.rs lines 464-500: that test only exercises the Wizard (profile 12) and Ninja (profile 2) rows for NeedsRank, plus a Ninja 400-XP boundary. It never drives the Warrior row (profile 32), and it does not check the active job staying unchanged or the single-unlock rule for Warrior. Only the Warrior rank-5 path in job_trainers near line 1595-1613 touches profile 32, and that is an ability-slot check, not a learn refusal. Keep."},
  {"name": "dewey_learns_warrior_through_the_npc_menu", "verdict": "keep", "covered_by": null, "reason": "Drives the real 26/8 to 26/10 path including busy-gate, out-of-range, peer-under-rank and repeat refusals. warrior_entry_chain::dewey_offers_becoming_a_warrior_only_to_warriors covers only the happy path, so the refusals are not duplicated."},
  {"name": "refused_learn_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input test (under-rank, forged option id, wrong-NPC selection, busy and range gates), asserting byte-identical save. Refusal checks are kept by policy."},
  {"name": "warrior_unlock_survives_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence check through a real save/load and fresh login; no equivalent Warrior-specific reload test was identified."},
  {"name": "non_warrior_trainers_do_not_offer_warrior", "verdict": "keep", "covered_by": null, "reason": "Negative canary that a non-Warrior trainer never offers Become a Warrior and gains no Warrior unlock. Not clearly covered by job_trainers, which checks each trainer's own job."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "All six tests kept. The prior removal of warrior_requires_brawler_rank_5 rested on a mis-read: job_trainers::service_refusals_change_nothing never exercises the Warrior row (profile 32), so the critique's objection holds. Not verified: warrior_entry_chain.rs and the full job_trainers.rs learn tests beyond the lines read, and the NpcVisibility drawn-AddNpc tests. Several file reads failed with tool errors on the first attempt; the retry on job_trainers.rs 464-500 succeeded, and the warrior_trainer.rs read still failed, so my check of that file's own test bodies is limited to the excerpt and the previous pack."}
]}
