<!-- fleet job=test-audit id=tests-crafting-stations-route-rs-L1 status=done turns=5 usd=0.0066 tokens(read,write,in,out)=[53704, 22277, 12, 6570] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/crafting_stations_route.rs lines 1-630 of 630

Window reviewed: `crafting_stations_route.rs` lines 1-630. Most tests in this window are sound. The movie and station assertions compare against pre-state values and fixed expected constants, and `station::write_placements(None)` does remove the forge, so the "moved or removed" case really covers removal. The wrong-job test is no longer `#[ignore]`d, and the "Switch to Chef" and "Move closer" texts match `recipe_book.rs:250-253`. Three findings:

- **[medium] crafting_stations_route.rs:622-629 `the_farm_cooking_table_keeps_its_tutorial_menu_until_the_tutorial_craft_is_done` - the pending-craft check passes on any 26/9 menu in the reply, not on the menu for the opening table's GUID.**
  - Why it cannot catch a regression: `.any(|packet| inner(packet).starts_with(&[26, 0, 9, 0]))` ignores the actor GUID. If an unrelated actor or a stray 26/9 is sent during the interact, the test still passes. The 26/9 menu builder is `opening_world.rs:86-99`, which writes the actor guid at bytes 4..12, so the guid is available to check.
  - Fix: require `inner(packet)[4..12] == OPENING_TABLE.to_le_bytes()` in the same `any` predicate, and optionally assert that the first 26/9 reply is the only 26/9 reply.

- **[low] crafting_stations_route.rs:550 `a_world_station_spawn_offers_the_x_prompt_at_the_station_radius` - `assert_eq!(packet.len(), 334)` pins the whole AddNpc packet length.**
  - Why it cannot catch a regression: it is not what the test is about (the interactable flag and the prompt reach). Any unrelated trailing AddNpc field added or removed fails it, so the failure is churn and says nothing about the prompt.
  - Fix: drop the total-length assertion, or keep only the byte-224 and byte-237 checks, which test the claim directly.

- **[low] crafting_stations_route.rs:206 and :209 `smelting_rounds` - exact reply counts `replies.len() == 2` and `== 6` on the movie lifecycle.**
  - Why it cannot catch a regression: these counts are incidental to the crafting completion the test checks. A harmless extra or merged reply packet fails the helper, and the test that calls it then reports a movie-count failure rather than a crafting failure.
  - Fix: assert the specific reply the movie protocol needs (for example, that a reply starting with the expected opcode is present), not the total.
