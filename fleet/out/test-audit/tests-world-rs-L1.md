<!-- fleet job=test-audit id=tests-world-rs-L1 status=done turns=7 usd=0.0072 tokens(read,write,in,out)=[83286, 22979, 16, 7027] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/world.rs lines 1-433 of 433

Window: `prototype/osfr-tools/tests/world.rs` lines 1-433. Code under test read in `prototype/osfr-tools/src/world.rs` (NpcVisibility::load 244-386, update 580-627, exclude_actor_guids/content_key/teleport_targets 531-577).

- **[medium] prototype/osfr-tools/tests/world.rs:103 encounter_child_waits_for_zone_ready_callback - the name says the child "waits for zone ready", but the body never checks the not-ready state before the callback.**
  - Why it cannot catch a regression: `enter_instance` (line 109) is followed only by `instance_id`, `zone_id`, and `kind` checks, then `mark_zone_ready(10, child)` is asserted true. If `enter_instance` marked the player ready immediately, or the child skipped `awaits_client_ready`, `mark_zone_ready` would still return true and the test would pass. The sibling test at line 98 does check the pre-ready `false` for the two-player case, but this single-player encounter path has no such check.
  - Fix: after line 109, assert `entered.awaits_client_ready` is true and `!world.player_location(10).unwrap().ready`. Then keep the `mark_zone_ready` assertion.

- **[medium] prototype/osfr-tools/tests/world.rs:330-331 npc_visibility_loads_content_caps_the_view_and_respects_startup_exclusions - the "caps the view" claim rests on `additions.len() <= 64`, which is also true when the cap is never reached.**
  - Why it cannot catch a regression: the cap is `NPC_VISIBILITY_LIMIT` in `update` (world.rs:608, 619). The test picks the position of the first `legacy_data` row and never checks how many candidates fall within `NPC_VISIBILITY_RADIUS`. If the fixture has fewer than 65 NPCs in range, a regression that removes the `take(NPC_VISIBILITY_LIMIT)` calls would still pass, because the view would be under 64 anyway.
  - Fix: assert the in-radius candidate count is greater than 64 for the chosen position (or pick a position that has one), then assert `additions.len() == 64`. Alternatively, rename the test so it no longer claims a cap check.

- **[low] prototype/osfr-tools/tests/world.rs:364 npc_visibility_loads_content_caps_the_view_and_respects_startup_exclusions - exact count `unrenderable.len() == 3` pins the knocker row count in the content data.**
  - Why it is churn, not a missed bug: adding or removing a content row changes this count, and the test is about the knocker model being filtered out, not about the number of rows.
  - Fix: assert `!unrenderable.is_empty()` (so the loop is not vacuous) and drop the exact count, or keep the count in a separate data-integrity check.

- **[low] prototype/osfr-tools/tests/world.rs:411 and :420 zone_less_legacy_regional_npcs_spawn_in_the_open_world_and_teleport_index - exact counts of 50 zone-less legacy NPCs are pinned twice.**
  - Why it is churn: the test's purpose is that every zone-less legacy NPC is in the teleport index and spawns. The literal 50 breaks when content is added, even when the behaviour is correct. The `filter(...).count() == 50` at line 420 also only confirms the count, not the spawn.
  - Fix: assert `zone_less_ids` is non-empty and that `targets.iter().filter(...).count() == zone_less_ids.len()`. The spawn check at line 428-432 already covers one NPC.

- **[low] prototype/osfr-tools/tests/world.rs:302-303 npc_visibility_loads_content_caps_the_view_and_respects_startup_exclusions - `regional_anchors` is built and then discarded (`let _ = &regional_anchors;`), and `extra_zone` is just an alias of `zone_id`.**
  - Why it matters: the setup reads as if it checks nearest-anchor zone assignment, but no assertion uses it. The loader's nearest-anchor logic (world.rs:338-346) is only labelled "diagnostics only" (world.rs:365) and is not tested here.
  - Fix: either delete the anchor computation and the alias, or assert the extra spawns' zone through the public API if one exists. Do not leave dead setup that implies coverage.
