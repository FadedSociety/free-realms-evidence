<!-- fleet job=testaudit-infer id=opening_cave_replay-v1 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[38858, 15035, 10, 2327] model=claude-haiku-5-5 -->
# tests/opening_cave_replay.rs

{"file": "tests/opening_cave_replay.rs",
 "tests": [
  {"name": "post_campaign_ordinary_guide_can_start_the_cave_again", "verdict": "keep", "covered_by": null, "reason": "Only test that starts the bound dungeon again from a completed post-campaign save via the ordinary guide interaction; asserts run identity, full enemy health, zoning, and no inventory/stage change. No similar-file test names a post-campaign replay."},
  {"name": "replay_requires_a_real_exit_before_another_run", "verdict": "keep", "covered_by": null, "reason": "Refusal check: a second interaction during an active run must not start another, and only the real 'realm exit' yields a fresh instance. Not matched by encounter.rs names, which cover first-run lifecycle."},
  {"name": "wrong_giver_selection_or_range_never_starts_a_replay", "verdict": "keep", "covered_by": null, "reason": "Refusal/hostile-input bundle: other guide, non-start menu choice, and out-of-range interaction all refused. Security-style check; keep."},
  {"name": "partial_chain_or_missing_reward_proof_never_replays", "verdict": "keep", "covered_by": null, "reason": "Refusal check for unfinished chain and missing reward proof gates. Keep."},
  {"name": "replay_grants_no_duplicate_economy_or_stage_progress", "verdict": "keep", "covered_by": null, "reason": "Economy/persistence canary for replay clears (inventory, stage progress, rewarded set unchanged). The first-run reward test in encounter.rs (save_restart_win_and_exit_preserve_reward_exactly_once) covers a different path, so not a duplicate."},
  {"name": "each_cave_clear_pays_the_dungeon_station_cash_once", "verdict": "keep", "covered_by": null, "reason": "Could not verify: no test with this name exists in the repository copy of the file (it has 452 lines, the pack says 519, and the pack's last test is absent). Cannot judge overlap with a station_cash test, so kept conservatively. The pack's source revision may differ from the repo tip."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "No test is clearly superseded or duplicated by the similar files; the most similar file (encounter.rs) covers first-run encounter lifecycle and reward once, not the post-campaign replay gate. Discrepancy: the pack reports 519 lines and a sixth test each_cave_clear_pays_the_dungeon_station_cash_once, but the repo file is 452 lines and ends at replay_grants_no_duplicate_economy_or_stage_progress. Re-check against the correct revision before acting on that test."}
