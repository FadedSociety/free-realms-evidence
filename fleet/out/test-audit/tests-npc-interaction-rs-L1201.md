<!-- fleet job=test-audit id=tests-npc-interaction-rs-L1201 status=done turns=15 usd=0.0088 tokens(read,write,in,out)=[236889, 29921, 32, 5367] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/npc_interaction.rs lines 1201-1213 of 1213

**[low] prototype/osfr-tools/tests/npc_interaction.rs:1206-1211 a_two_session_refusal_does_not_change_the_other_players_state - the "first session's menu still answers" check only matches the 26/3 family prefix, not that the reply is the Samantha dialogue.**
- **Why it cannot catch a regression:** `talked.replies.iter().any(|packet| packet.starts_with(&[26, 0, 3, 0]))` passes for any 26/3 packet in the reply list. A change that answers the select with a 26/3 whose actor bytes (12..20, set by `patch_npc_actor` in `src/gameplay/npc.rs:1156-1159`) name a different NPC, or a dialogue for a different menu row, would still pass. The window also never checks `talked.changed`, so a select that answers but commits nothing is not detected either.
- **Fix:** Assert the reply's actor, e.g. `packet.len() >= 20 && packet[12..20] == SAMANTHA.to_le_bytes()` on the matching 26/3, and/or assert `talked.changed` (or that `saved(&first)` moved past `first_before` to match the Talk outcome, as `talk_step` in `tests/support/npc_quest_chain.rs:419-420` does).

No other problems in the window: `send` (`tests/support/npc_quest_chain.rs:290-298`) panics on a refused packet, so the select is genuinely accepted, and the final `second` state check is a real comparison. No `#[ignore]`, no early return, and no over-pinned counts.
