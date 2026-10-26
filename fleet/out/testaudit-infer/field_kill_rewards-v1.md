<!-- fleet job=testaudit-infer id=field_kill_rewards-v1 status=done turns=3 usd=0.0044 tokens(read,write,in,out)=[29621, 23825, 8, 2304] model=claude-haiku-5-5 -->
# tests/field_kill_rewards.rs

{"file": "tests/field_kill_rewards.rs",
 "tests": [
  {"name": "a_solo_field_kill_pays_once_and_only_the_active_job", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the solo field-kill payout to the active job (exact 38/19 and 38/14 carriers), plus replay and corpse no-op checks. The similar shared_field_kill_quest_credit.rs tests assert quest credit, not coin/XP payout, so no equally strong duplicate was found."},
  {"name": "the_mid_level_farnum_camp_pays_the_kind_override_rate", "verdict": "keep", "covered_by": null, "reason": "Pins the definition-override-beats-level-band rule for the shipped MID-F1 camp (2 coins / 5 XP at level 5). Distinct from the synthetic override check in the shared-kill test; keep as a shipped-content canary."},
  {"name": "a_shared_kill_pays_each_credited_player_once", "verdict": "keep", "covered_by": null, "reason": "Multi-player once-only payout, job-at-claim rule (B switches job before the kill) and bystander no-credit. Unique reward-side coverage; keep."},
  {"name": "a_credit_expires_and_a_bad_row_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Expiry (TTL) refusal plus loader refusals for overlapping bands and duplicate overrides. Refusal and hostile-input checks; keep."},
  {"name": "an_overflowing_reward_refuses_one_player_without_stopping_the_field", "verdict": "keep", "covered_by": null, "reason": "Representability refusal (coin cap) that refuses one reward whole while the field continues; security-style refusal check with the fixed refusal line. Keep."},
  {"name": "an_overflowing_job_xp_refuses_the_whole_payout", "verdict": "keep", "covered_by": null, "reason": "Job-XP overflow refusal: no half-payout of coins. Refusal check; keep."},
  {"name": "a_field_kill_credit_survives_an_unrelated_content_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence-style check that a pending credit carries its pair across a content reload while a fresh engine reads the new table. Canary for reload semantics; keep."},
  {"name": "a_credit_survives_a_reconnect_and_expires_once", "verdict": "keep", "covered_by": null, "reason": "Reconnect persistence of a pending credit plus retain_casters TTL pruning. shared_field_kill_quest_credit.rs::the_credit_survives_a_reconnect checks quest advancement, not the reward pair; not a duplicate."},
  {"name": "a_battle_reward_at_the_coin_cap_is_refused_with_feedback", "verdict": "keep", "covered_by": null, "reason": "Only test of the non-field battle-win reward representability gate (F276), including the system line and the paid-below-cap control. Keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Reviewed the full file and the closest similar file (shared_field_kill_quest_credit.rs), which overlaps on kill-credit mechanics but asserts quest events rather than coin/XP payouts. I did not open the other similar files (miner_first_ore, fishing_entry, power_up_use, power_up_drops) or grep the whole suite for other coin/XP payout assertions, so a duplicate elsewhere in the suite could be missed; confidence is moderate for that reason. Every test here carries a refusal, persistence, canary or shipped-content assertion, so the conservative default is keep throughout."}
