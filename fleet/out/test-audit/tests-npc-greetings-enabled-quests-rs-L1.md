<!-- fleet job=test-audit id=tests-npc-greetings-enabled-quests-rs-L1 status=done turns=6 usd=0.0111 tokens(read,write,in,out)=[119131, 37828, 14, 10293] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_greetings_enabled_quests.rs lines 1-1200 of 1330

Window: `prototype/osfr-tools/tests/npc_greetings_enabled_quests.rs` lines 1-1200. Read in full, plus `src/npc_interaction.rs:479-560`, `tests/common/npc_greetings.rs:100-200`, and the Petra quote in `notes/Build Guides/Content/Jobs/Brawler.md:131`. The first three findings are in the window. The fourth is a low-severity name issue.

- **[medium] tests/npc_greetings_enabled_quests.rs:1154-1161 an_unbound_row_still_sends_the_existing_empty_body - "a refusal must leave the menu exactly as it was" is checked by calling `interact` again, which rebuilds the menu, so the comparison cannot see the open menu's state.**
  - Why it cannot catch a regression: `NpcInteraction::interact` (`src/npc_interaction.rs:479-505`) recomputes `options` from content and overwrites `self.active` on every call. `reopened.options` and `before` are therefore two fresh builds of the same content. A refusal that mutates the active menu (for example, drops or reorders a non-Talk option, or sets `shop_open`) would still pass. The earlier successful Talk select at 1142 only shows that Talk survives.
  - Fix: after the refusals, do not re-run `interact`. Compare the active menu through an accessor, or re-select each `before` option id and assert it still resolves to the same action (for example `Ok(NpcSelection::Talk(..))` for Talk, and `InvalidOption` for an id not in `before`). Alternatively, assert that a refused `select` leaves `interaction.active` byte-equal to a snapshot taken before it.

- **[low] tests/npc_greetings_enabled_quests.rs:1104-1109 an_unbound_row_still_sends_the_existing_empty_body - the zero-greeting check is a constant assertion inside the per-NPC loop.**
  - Why it cannot catch a regression: it checks only that `BINDINGS` greetings are nonzero, which is already asserted at line 785 in `each_bound_greeting_is_the_npcs_own_first_person_line`. It does not depend on `file`, `npc_id`, or the row, so no change to the control rows can trip it.
  - Fix: remove it from the loop, or replace it with an assertion on the control row, such as `body_dword(&dialogue) == 0` together with `service_talk_body(...) == None` for the same row. The existing assertions at 1093-1103 already do that.

- **[low] tests/npc_greetings_enabled_quests.rs:1191-1194 two_players_see_the_same_greeting - the 26/4 close is only `.expect`ed and its effect is never observed.**
  - Why it cannot catch a regression: the test passes if the 26/4 call returns any `Ok`, including an empty reply that changes no session state. The body check at 1195-1200 then passes whenever the body comes from the static row, so it does not test the claim "closing A's dialogue cannot blank B's next Talk" in the stated way.
  - Fix: assert that the 26/4 outcome is what the production code produces (for example, that A's `26/3` state is cleared, or that a second `26/4` reply is returned). Alternatively, assert that A's next Talk returns the greeting again, which proves the close was processed.

- **[low] tests/npc_greetings_enabled_quests.rs:983 clicking_a_bound_quest_npc_returns_its_greeting_body - the name says "quest NPC", but the loop runs over all 13 `BINDINGS`, including rows with `quest: None` (for example Greyli at 9500000488, Therin, Petra, and Burt).**
  - Why it cannot catch a regression: the test passes for ambient or non-quest bindings, so the name claims a narrower scope than the body covers. This is a naming issue, not a missed failure.
  - Fix: rename it to something like `clicking_a_bound_npc_returns_its_greeting_body`, or filter to `binding.quest.is_some()` if the quest-only path is what matters.

Checked and not reported: the `enabled_quest_targets` loader cross-checks (lines 384-429), the `speaker_proof` negative cases (lines 951-979; the Petra objective is correctly classified as third-person by the `Petra would...` prefix rule), the Hrugagu control at 9500000309 (matches the blank list at line 300), and the refusal-error checks at 1125-1141.
