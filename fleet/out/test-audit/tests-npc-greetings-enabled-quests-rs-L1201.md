<!-- fleet job=test-audit id=tests-npc-greetings-enabled-quests-rs-L1201 status=done turns=5 usd=0.0036 tokens(read,write,in,out)=[21073, 11648, 12, 3768] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_greetings_enabled_quests.rs lines 1201-1330 of 1330

Window 1201-1330 reviewed. The helpers (`in_world_talk` 627-662, `body_dword` 664, `binding_for` 668) and `npc_interaction.rs` (greeting_string_id only feeds the 26/3 body at line 898, not the option list) were read to confirm the test's premises.

- **[medium] prototype/osfr-tools/tests/npc_greetings_enabled_quests.rs:1218 the_greetings_add_no_quest_or_menu_change - the "no quest or menu change" claim has no baseline, so the menu checks compare the code with itself.**
  - Why it cannot catch a regression: lines 1244-1247 compare `first.interact(...)` with `second.interact(...)`. Both come from the same builder, so any change to the option list passes as long as it is deterministic. The 1260 check only fails if the greeting dword appears as an option `string_id`. Line 1254 (`len() >= min_options`, with min 1) does not pin the option list at all. A change that drops the quest option, adds an option, or alters an action for these three NPCs still passes. The 1276 check (`menu_packet[12..] == menu.packet[12..]`) is also self-referential, since the in-world 26/9 is built by the same service.
  - Fix: pin each NPC's expected 26/9 option list as literals (action kind and string_id, for example Talk, then the quest option with its title id), and assert equality with `menu.options`. Alternatively, snapshot the packet from before the greeting feature and compare against that.

- **[low] prototype/osfr-tools/tests/npc_greetings_enabled_quests.rs:1253-1256 the_greetings_add_no_quest_or_menu_change - the assertion message says "Talk remains the menu's first option" but the condition checks only the option count.**
  - Why it cannot catch a regression: the first-option property is checked at 1248-1252. The 1253 check only asserts `options.len() >= min_options`, so the message misdescribes what it protects, and a reader would believe first-option ordering is covered twice.
  - Fix: change the message to "NPC {npc_id}: the 26/9 menu has at least {min_options} option(s)", or replace the check with an exact expected option count per NPC, which also serves the finding above.

- **[low] prototype/osfr-tools/tests/npc_greetings_enabled_quests.rs:1226-1230 the_greetings_add_no_quest_or_menu_change - the `min_options` values (1, 1, 1) are a weak, incidental pin.**
  - Why it cannot catch a regression: a value of 1 is satisfied by a Talk-only menu, so the table implies a quest-giver check that the threshold does not enforce. The data is also unrelated to the greeting feature, so unrelated option work can shift it without changing the test's purpose.
  - Fix: replace the threshold with exact expected option lists per NPC (see the first finding).
