<!-- fleet job=testaudit-infer id=opening_world-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[7126, 12058, 6, 670] model=claude-haiku-5-5 -->
# tests/opening_world.rs

{"file": "tests/opening_world.rs",
 "tests": [{"name": "native_prompt_radius_with_utf8_name_matches_full_community_packet_and_preserves_menu", "verdict": "keep", "covered_by": null, "reason": "The only test that drives OpeningWorld::load, spawn, menu and initialization. It byte-compares the spawn packet, menu_npc/menu_prop and the initialization packets against the community fixture, and checks the float radius and UTF-8 name-length offsets. No other test in the suite exercises the opening_world writers; the similar files (npc_interaction, players, station_cash) test other packets and only mention opening_world in passing. Its doc is empty, but the name states the behaviour clearly."}],
 "whole_file_removable": false, "confidence": 0.9, "notes": "Single-test file that is the sole coverage for src/opening_world.rs byte layouts (spawn, menu, initialization). Its fixture is synthetic and the test is a canary for the native 237-offset radius write. Nothing to remove."}
