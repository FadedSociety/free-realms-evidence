<!-- fleet job=testaudit-infer id=bixie_hive_dungeon-v1 status=done turns=2 usd=0.0032 tokens(read,write,in,out)=[11374, 13540, 6, 2770] model=claude-haiku-5-5 -->
# tests/bixie_hive_dungeon.rs

{"file": "tests/bixie_hive_dungeon.rs",
 "tests": [
  {"name": "the_start_screen_carries_the_instance_and_roster_count", "verdict": "keep", "covered_by": null, "reason": "Pins the 575-byte 41/114 layout and roster offset for the Bixie row (4 prizes, text dwords). bandit_hideout_dungeon.rs has a same-named test, but it checks a different row's bytes, so it is not the same assertion."},
  {"name": "a_level_one_character_can_start", "verdict": "keep", "covered_by": null, "reason": "Only check of the exact authored Bixie content row (ids, actors, positions, payout, arena, prize pool) and the level-1 start."},
  {"name": "the_marker_is_terrain_safe_and_clear_of_the_bixie_camp", "verdict": "keep", "covered_by": null, "reason": "Placement safety check for this marker (terrain disc, slope, clearance from field enemies). Bixie-specific data; not covered elsewhere."},
  {"name": "a_non_combat_job_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check on the non-combat gate; keep under the refusal rule."},
  {"name": "a_busy_character_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check for a live arena run (busy state); keep under the refusal rule."},
  {"name": "the_full_route_pays_sixty_eight_coins_and_one_prize", "verdict": "keep", "covered_by": null, "reason": "Full route with exact Bixie payout (68 coins, one prize, 50 XP) and replay-once check; bandit's full-route test pays 60 coins, so the assertions differ."},
  {"name": "refusals_leave_everything_unchanged", "verdict": "keep", "covered_by": null, "reason": "Multi-case hostile-input and refusal test (forged Go, forged portal, wrong marker, full bag). Keep under the refusal rule."},
  {"name": "every_previewed_prize_resolves_and_fits", "verdict": "keep", "covered_by": null, "reason": "Checks this row's prizes against the catalogue and bag capacity, plus a synthetic unresolvable-prize refusal. Bandit has a similar test for its own row only."},
  {"name": "guids_are_unique_across_shipped_content", "verdict": "keep", "covered_by": null, "reason": "Collision check covering the new GUIDs against the Bixie field actors and loader refusal. Bandit's version checks different GUIDs."},
  {"name": "a_second_player_runs_its_own_instance_and_is_paid_once", "verdict": "keep", "covered_by": null, "reason": "Two-session isolation and single-payout check. Near-identical to bandit_hideout_dungeon.rs::a_second_player_runs_its_own_instance_and_is_paid_once and a candidate for consolidation, but it drives this row's path, so it is kept conservatively."},
  {"name": "the_win_and_the_mid_fight_return_survive_a_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence/reload check (no second payout, no stuck busy state). Persistence tests are kept. Mirrors bandit_hideout_dungeon.rs::the_win_and_the_mid_fight_return_survive_a_reload; consolidation candidate only."},
  {"name": "the_portal_row_applies_the_same_gates", "verdict": "keep", "covered_by": null, "reason": "Checks the published 167/1/1 row and Play gates for this battle; the bandit equivalent checks level gates, not job gates."},
  {"name": "a_second_session_sees_the_marker_not_the_arena", "verdict": "keep", "covered_by": null, "reason": "Visibility check on the new marker's 35/2 AddNpc position and that arena actors are hidden. Mirrors bandit's test; consolidation candidate, not proven duplicate."},
  {"name": "a_live_change_before_the_close_survives_the_payout", "verdict": "keep", "covered_by": null, "reason": "Live-state delta survival through payout and Close. Mirrors bandit_hideout_dungeon.rs::a_live_change_before_the_close_survives_the_payout; consolidation candidate, not proven duplicate."},
  {"name": "a_failing_start_does_not_stop_the_other_session", "verdict": "keep", "covered_by": null, "reason": "Cross-session isolation after a refused start (non-combat job, full bag). Unique combination; kept."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Audit was light: I compared test names and doc lines against bandit_hideout_dungeon.rs (T353 sibling, same shape) and checked the names of a few tests there, not their bodies. Several engine-level tests (second player, reload, second session, live change, start-screen packet) look like row-substituted copies of bandit's. They are candidates for consolidation into a shared generic helper, but I did not verify identical assertions, so I kept them. Nothing is clearly redundant. The file is not removable as a whole: it holds the only checks of the Bixie row's content, terrain and payout."}
