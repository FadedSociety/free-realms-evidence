<!-- fleet job=test-audit id=tests-medic-level-five-chapter-rs-L1201 status=nothing_found turns=13 usd=0.0090 tokens(read,write,in,out)=[165144, 29305, 28, 7452] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/medic_level_five_chapter.rs lines 1201-1236 of 1236

No findings in `repo:prototype/osfr-tools/tests/medic_level_five_chapter.rs` lines 1201-1236.

What I checked:
- **1201-1214 (second player's Achieve Level 5 turn-in):** `second_coins` is captured at line 1173, before the second player's pills and vitamins, so the expected `second_coins + PILL_COINS + VITAMIN_COINS + LEVEL_COINS` is a real independent expectation. `second_xp` is captured after `set_medic_xp(..., 400)`, so `second_xp + LEVEL_XP` is correct. `finish_quest` (`support/npc_quest_chain.rs:529`) also checks state, but these window asserts add the cross-chapter coin sum, which that helper does not check.
- **1218-1235 (first player's session stays usable):** `before_state` and `before_bytes` are taken after the refused turn-ins and the stale 49/14 (lines 1111-1170), and nothing mutates `first` in between. The interact asserts compare the full serialized state and save. The 26/9 menu check matches the helper's own detection (`support/npc_quest_chain.rs:395`). `pending_turnin == Some(PILLS)` at 1235 is redundant with the state equality, but it is not wrong.

Not a finding, but relevant: the enclosing test is `a_failing_quest_event_for_one_player_does_not_stop_the_other` (line 1087). The wallet and profile refusals are asserted at 1111-1156, outside this window. The window's own assertions match the name.
