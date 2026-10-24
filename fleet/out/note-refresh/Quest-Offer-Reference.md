<!-- fleet job=note-refresh id=Quest-Offer-Reference status=done turns=21 usd=0.0324 tokens(read,write,in,out)=[1022568, 89870, 44, 21857] model=claude-haiku-5-5 -->
# notes/Research/Quest Offer Reference.md

**Verdict:** Moderate drift. The W65–W74 packet-layout and test-inventory claims mostly hold, but the central W67 Talk-to-offer policy is no longer what the code does, and three content/code facts in the W65 audit and the differences list are stale.

**Corrections:**

1. `old:` selecting Talk offers the first eligible quest for a quest-giver and suppresses the ordinary 26/3 response for that interaction.
   `new:` selecting Talk opens a dialogue (26/3) whose first row is the eligible quest's title (response 301, reconstructed); the 49/1 offer is sent only when the player picks that row (26/6). Talk itself sends no 49/1, and when no offer is eligible Talk keeps its dialogue response.
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:1034-1051 (Talk sets `quest_choice` from `offerable_quest_for_talk`), :1059-1063 (`quest_dialogue_choice` row prepended), :1071-1073 (26/3 pushed unless outcome is "offer"); repo:prototype/osfr-tools/src/gameplay/npc.rs:129-168 (26/6 with response 301 or 0 → `engine.offer` → 49/1); repo:prototype/osfr-tools/src/npc_interaction.rs:1156-1163; repo:prototype/osfr-tools/src/quest_engine.rs:1901-1926 (`TalkToNpc` only emits 49/13 turn-in, never an offer).

2. `old:` Our quest 3000021 has `title_string_id` 4206471822, which isn't a locale row.
   `new:` Our quest 3000021 has `title_string_id` 94247, the verified "Introduce Yourself" row (the W65 audit replaced the invalid ID).
   `why:` repo:prototype/osfr-tools/data/content/quests/adventurer.json:1627-1628 (`"title_string_id": 94247`); repo:prototype/osfr-tools/data/content/npcs/cobblestone_village.json:8069-8071; no occurrence of 4206471822 remains under prototype/osfr-tools.

3. `old:` Quest 3000020 (C1, giver key 9000000002, area Highroad Junction)
   `new:` Quest 3000020 (C1, giver key 9000000402, area Highroad Junction; the 9000000002 alias was replaced by 9000000402 in W110)
   `why:` repo:prototype/osfr-tools/data/content/quests/adventurer.json:1548 (`"giver_npc_id": 9000000402`) and :1617 (alias 9000000002 replaced with 9000000402).

4. `old:` Its giver name remains unresolved (candidate names Merigold/Raina Rush), but the unresolved NPC row records Highroad Junction;
   `new:` Its giver is Merigold (NPC 9000000402, name locale 103722, Highroad Junction), and the record lists quest 3000020 under `quests_given`;
   `why:` repo:prototype/osfr-tools/data/content/npcs/highroad_junction.json:6553-6558 (npc_id 9000000402, name "Merigold", name_string_id 103722) and :6586-6592 (quests_given 3000020).

5. `old:` We send 26/3 with the NPC name as the body and one close choice.
   `new:` We send 26/3 with the NPC greeting locale as the body (empty when no greeting is verified) and the Goodbye choice; on Talk with an eligible quest, the quest-title row is added first.
   `why:` repo:prototype/osfr-tools/src/npc_interaction.rs:1181 ("it is never the NPC name"), :898 (`body_string_id: npc.greeting_string_id`); repo:prototype/osfr-tools/src/gameplay/npc.rs:1059-1063.

**Unsure:**

- Test expectation at `repo:prototype/osfr-tools/tests/gateway_npc_offer_runtime.rs:314-323` asserts that a Talk selection sends 49/1 and no 26/3. Per correction 1, current code sends 26/3 with a quest row on Talk, so that test would now fail. I did not run it. The note's line "It asserts a one-option menu and 49/1 without 26/3" and the W67 "`npc_select` outcome `offer`" result describe the older behaviour. Those historical run results can stay, but the W67 policy text should not.
- Quest-start visual and NPX-guard claims (W68–W73) are client-side and not checkable from the server tree. I left them alone.
- W74 `w74_quest_runtime` test file and the per-message rejection behaviour (line 299) are not confirmed. I found `tests/w74_quest_runtime` absent from the first 300 test entries and only found a related comment in `src/bin/osfr_gateway/tests.rs:584`. Not settled.
- Locale-row provenance claims (`lab/reports/locale-id-to-text.json`, the 651-record audit counts) point to lab files outside this repo and could not be verified here.
- Test names and file paths cited in the note all exist (`tests/npc_interaction.rs:415`, `tests/gateway_npc_offer_runtime.rs:167`, `src/gameplay/w64_regional_quest_tests.rs:1093`, `src/gameplay/developer_teleport.rs:502/517`, `tests/startup_selfdata.rs:603`). `realm npx off` and `developer_quest_offer` are in `src/gameplay.rs:3954` and `:3985` as cited. The 49/14 10-byte decoder (`src/npc_interaction.rs:1186`) and 49/3 login restore (`src/quest_engine.rs:1457-1470`) also match.
