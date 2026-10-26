<!-- fleet job=testaudit-infer id=weapon_bar-v1 status=blocked turns=6 usd=0.0037 tokens(read,write,in,out)=[62249, 14628, 14, 2396] model=claude-haiku-5-5 -->
# tests/weapon_bar.rs

{"file": "tests/weapon_bar.rs",
 "tests": [
  {"name": "equip_relabels_the_basic_attack", "verdict": "keep", "covered_by": null, "reason": "Could not locate the file or any test with this name in the repo snapshot, so no duplicate or superseded match could be verified. Its assertions (basic slot named by equipped weapon name_id, reconnect rebuild, no-op replay sends no bar) look like a unique check of the T521 path. Kept by default."},
  {"name": "unarmed_bar_is_empty_and_rearm_restores_it", "verdict": "keep", "covered_by": null, "reason": "Pins the R/OSFR #124 unarmed-combat-job empty-bar behaviour. No same-named test was found in the repo, and the only related helpers (bar_ids in common/job_playtest.rs, job_ability_bars.rs, job_trainers.rs) were not shown to drive the unequip-to-empty-bar path. Kept by default."},
  {"name": "unrelated_or_refused_equip_sends_no_bar", "verdict": "keep", "covered_by": null, "reason": "Refusal check (wrong-class and locked-profile equips change nothing and send no bar). Refusal tests are never removed without a named equal test, and none was found. Its body was not visible in the pack excerpt, so it could not be compared further. Kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.2,
 "notes": "BLOCKED: prototype/osfr-tools/tests/weapon_bar.rs is not present in the repo snapshot. read returns 'not a file', and searches for the test names, the t521-weapon-bar fixture prefix, the OSFR #124 comment and the ARMED_BAR constant return nothing. The briefs root has no T521 entry. The excerpt also cuts off mid-way through unarmed_bar_is_empty_and_rearm_restores_it and never shows the body of unrelated_or_refused_equip_sends_no_bar. Verdicts are therefore conservative keeps, not analysis. The similar-file list (coin_store_siblings, bot_acceptance_1016, station_cash, sc_earnings, quest_offer_reward) is unrelated to weapon equip, and none of its test names match. Nearby equip-related files exist (tests/equip_eligibility.rs, tests/job_ability_bars.rs, tests/job_trainers.rs, tests/opening_abilities.rs, tests/piece_035.rs) and may overlap the equip-to-basic-slot and empty-bar checks. Those should be compared once the file is available."}
