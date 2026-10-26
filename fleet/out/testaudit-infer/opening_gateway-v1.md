<!-- fleet job=testaudit-infer id=opening_gateway-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[7990, 10922, 6, 1052] model=claude-haiku-5-5 -->
# tests/opening_gateway.rs

{"file": "tests/opening_gateway.rs",
 "tests": [
  {"name": "private_all_opening_actions_dungeon_return_and_restarts", "verdict": "keep", "covered_by": null,
   "reason": "Only test in the file. It is a packet-driven, gateway-level run of all 17 opening stages (talk/interact, dungeon select and kills, win, restart, return to zone 0). It also carries refusal checks: a remote interaction with the guide and with the magic door must leave the snapshot unchanged, and a forged/remote entrance cannot zone the player. Those refusal and persistence assertions (coins and position survive restart) are not clearly matched by opening.rs::private_opening_every_stage_is_completable_through_typed_events_and_reward_once_after_reload, which works at the engine level with typed events rather than through the gateway packet path. Since it is ignored and needs private content, it adds no per-run cost unless the env vars are set."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "The pack lists a single test. Similar opening tests in tests/opening.rs (private_opening_every_stage_is_completable_through_typed_events_and_reward_once_after_reload, private_opening_content_loads_with_all_objectives_and_verified_actor_references) overlap the stage-completion and reward-once path but at the engine level, not through Gateway packets. The gateway-specific refusal checks are the reason to keep. Confidence is moderate because I did not read the full opening.rs assertions side by side with this file; if that comparison shows the stage loop is identical, the stage-walk portion could be judged superseded, but the refusal and restart checks would still need keeping."}
