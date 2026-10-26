<!-- fleet job=testaudit-infer id=ninja_stealth_chain-v1 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[10095, 17578, 6, 1428] model=claude-haiku-5-5 -->
# tests/ninja_stealth_chain.rs

{"file": "tests/ninja_stealth_chain.rs",
 "tests": [
  {"name": "ty_offers_the_stealth_referral_after_stolen_away", "verdict": "keep", "covered_by": null, "reason": "Only test that drives the Ty offer of the stealth referral (3_110_004) through the 26/8 menu, 26/10 select, and 49/1 offer. It also carries refusal checks: a forged menu entry and a forged accept leave state unchanged, and a disabled-chapter reply is refused. quest_job_xp.rs covers the Ninja path 3_110_001 only, not this referral."},
  {"name": "three_mentors_are_required_in_order", "verdict": "keep", "covered_by": null, "reason": "Only test of the ordered three-mentor counter (Kosha, Chloe, Ty / Brendan) and its out-of-order refusal. Asserts exact counts at each step and that replays and unrelated NPCs change nothing. No other file exercises 3_110_004 counts."},
  {"name": "return_to_ty_settles_once", "verdict": "keep", "covered_by": null, "reason": "Covers the return-to-Ty turn-in: 49/13 end screen naming the NPC, forged end-reply refusal, a single coin payout of 5, and no double payment after replay and reload. Persistence and refusal checks with no equal test elsewhere."},
  {"name": "halted_mongo_chain_stays_hidden_and_save_reloads", "verdict": "keep", "covered_by": null, "reason": "Canary and persistence test: checks that the halted chapter 3_110_003 stays disabled in data/content/quests/ninja.json, is never offered, and that the full chain survives reconnects with the coin reward paid once. Removing it would lose the only check on the disabled-record gate."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All four tests cover the Ninja stealth referral chain (ids 3_110_002..004), which no similar file drives. The most similar files (archer_entry_chain.rs, brawler_job_chain.rs, starting_quest_chain.rs) test other job chains. quest_job_xp.rs touches only the Ninja path 3_110_001 and its XP. Each test has refusal, replay or persistence assertions, so none is removable. I did not read the similar files' bodies in depth; the verdicts rest on the test names, the shared constants and the grep for the stealth ids."}
