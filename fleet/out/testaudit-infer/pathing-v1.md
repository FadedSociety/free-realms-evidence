<!-- fleet job=testaudit-infer id=pathing-v1 status=no_submit turns=3 usd=0.0041 tokens(read,write,in,out)=[28102, 18057, 8, 3072] model=claude-haiku-5-5 -->
# tests/pathing.rs

```json
{"file": "tests/pathing.rs",
 "tests": [
  {"name": "a_valid_request_gets_a_ground_following_path", "verdict": "keep", "covered_by": null, "reason": "Only pure-Pathing check of the ground-following path shape (21 points, echoed kind/aux, y follows terrain). The gameplay-level path test in src/gameplay/developer_teleport.rs checks only one interior y, so it does not cover this."},
  {"name": "the_longest_legal_request_stays_under_the_point_cap", "verdict": "keep", "covered_by": null, "reason": "Pins the 300 m limit and the MAX_POINTS cap, and includes a refusal canary for 305 m. No other test covers the cap."},
  {"name": "nearby_and_identical_points_give_a_short_path", "verdict": "keep", "covered_by": null, "reason": "Edge case for zero and short distances; no other test covers it."},
  {"name": "refusals_each_have_a_canary", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input canary covering TooFar, NotFinite, OutOfZone and Malformed. Must be kept."},
  {"name": "a_zone_without_a_grid_gets_the_failure_reply_not_a_path", "verdict": "keep", "covered_by": null, "reason": "Unknown-zone failure path; the gameplay tests do not exercise zone 99."},
  {"name": "refused_requests_leave_the_rate_budget_alone", "verdict": "keep", "covered_by": null, "reason": "Refusal check that refusals spend no rate budget. Security-relevant; the developer_teleport rate test does not check this."},
  {"name": "the_rate_cap_holds_and_resets_each_second", "verdict": "keep", "covered_by": null, "reason": "Rate-cap, window-reset and clock-regression checks. developer_teleport::path_requests_are_capped_per_second_and_refusals_are_silent covers only the cap count at gameplay level, so this one is stronger and is kept."},
  {"name": "missing_terrain_gets_the_clients_failure_reply", "verdict": "duplicate", "covered_by": "src/gameplay/developer_teleport.rs::path_request_without_terrain_gets_the_failure_reply", "reason": "Same no-terrain branch asserting the same 98/2 zero-node failure bytes, reached through Gameplay instead of Pathing::answer. Low-confidence duplicate: the lower-level test also pins the exact bytes, so keeping it is defensible."},
  {"name": "take_me_there_gets_the_breadcrumb_path_under_its_own_kind", "verdict": "keep", "covered_by": null, "reason": "Pins the kind-2 routing and aux echo at the Pathing level and compares against kind 1. The src test take_me_there_is_answered_like_the_breadcrumb checks the same idea through Gameplay, but this test is independent and stronger, so it is kept."},
  {"name": "take_me_there_is_refused_and_rate_capped_like_the_breadcrumb", "verdict": "keep", "covered_by": null, "reason": "Refusal and shared-budget check across kinds 1 and 2. No other test checks that kind 2 shares the same budget."},
  {"name": "other_packets_and_other_kinds_are_not_ours", "verdict": "keep", "covered_by": null, "reason": "Canary that other opcodes and kinds are ignored, and that truncated headers return None."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "The five 'most similar' files are unrelated (housing, coin store, kart, power-up, warpstone), so the real comparison is with src/gameplay/developer_teleport.rs, which has its own 98/1 tests: path_request_is_answered_from_the_terrain, path_request_without_terrain_gets_the_failure_reply, path_requests_are_capped_per_second_and_refusals_are_silent, and take_me_there_is_answered_like_the_breadcrumb. Those overlap in gameplay wiring, but this file tests the Pathing unit directly with stronger refusal, rate and cap canaries. Only one test is a plausible duplicate. Nothing is obsolete: the T404 Take Me There kind-2 routing is still live, as the T404 doc lines and developer_teleport's kind-2 test show. The file is not removable because it is the only unit-level suite for the refusal and rate-cap rules."}
```
