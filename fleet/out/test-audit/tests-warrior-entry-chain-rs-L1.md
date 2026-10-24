<!-- fleet job=test-audit id=tests-warrior-entry-chain-rs-L1 status=done turns=7 usd=0.0085 tokens(read,write,in,out)=[123384, 31492, 16, 6733] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/warrior_entry_chain.rs lines 1-1200 of 1311

Window reviewed: `prototype/osfr-tools/tests/warrior_entry_chain.rs` lines 1-1200 (plus the support helpers `tests/support/npc_quest_chain.rs` 160-220 and 640-740, and `src/gameplay/npc.rs` 11-31 for `update_npc_visibility`). Most tests check real production output against content files and the 26/49/35 packet bytes, so they are not circular. The findings below are the gaps I could confirm.

- **[medium] tests/warrior_entry_chain.rs:1069 `the_new_spawns_are_visible_to_a_second_session` - the "second session" never presents its own character to the visibility call.** Lines 1072-1080 build `at` from `first_character` (guid `CHARACTER`) and pass that same `at` to both `first` and `second`. `second_character` is used only for the final ledger-id check at 1106-1109.
  - Why it cannot catch a regression: `Gameplay::update_npc_visibility` (`src/gameplay/npc.rs:11-18`) reads only `character.zone_id` and `character.position`, not the guid. A change that makes a second session draw from the first session's guid, or share visibility state across sessions, still passes, because the second session's guid never reaches the call.
  - Fix: build `at` per session from that session's own character (e.g. `CharacterState { position: ..., ..second_character.clone() }` for `second`), and assert the second session's packets come from its own ledger/guid, or rename the test to say it checks the shared NPC view from zone 0.

- **[medium] tests/warrior_entry_chain.rs:1015-1024 `progress_survives_a_reload` - the doc comment claims an ordering that is never checked.** The comment says the held 49/13 is re-sent "after Dewey's 35/2, exactly as the client's ShowQuestEndScreen path expects". The body only does `packets.iter().find(has_family(49,13,W1))` and never checks where the 35/2 for Dewey sits, or that the 49/13 comes after it.
  - Why it cannot catch a regression: a change that emits the 49/13 before the 35/2 AddNpc, or drops the 35/2 for Dewey, still passes as long as a 49/13 for W1 is present.
  - Fix: find the index of the Dewey 35/2 (`parse_add_npc(..).actor_id == DEWEY`) and the index of the 49/13, and assert `end_index > add_npc_index`. Otherwise drop the ordering claim from the comment.

- **[low] tests/warrior_entry_chain.rs:765 `the_two_spawns_and_quests_load_with_real_targets` - exact provenance count pinned.** `assert_eq!(sources.len(), 5, "five provenance entries")` locks the number of provenance entries on each spawn row. This is incidental to whether the spawn is bound correctly, so adding or merging a source citation churns the test without any behavior change.
  - Fix: keep the Legacy-tag and non-empty-evidence checks (lines 766-779) and drop the exact count, or assert `sources.len() >= 1`.
