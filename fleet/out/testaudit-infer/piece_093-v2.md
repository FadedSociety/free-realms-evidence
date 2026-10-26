<!-- fleet job=testaudit-infer id=piece_093-v2 status=done turns=3 usd=0.0035 tokens(read,write,in,out)=[27693, 16831, 8, 2176] model=claude-haiku-5-5 -->
# tests/piece_093.rs

{"file": "tests/piece_093.rs",
 "tests": [
  {"name": "recovered_command_table_matches_the_client_lua", "verdict": "keep", "covered_by": null, "reason": "Pins the 72-row command table and shared quick-chat ids (hi/hey, boo/scare) to the client Lua. No similar file asserts the command-to-id table."},
  {"name": "repeated_command_binding_resolves_last_and_the_old_id_is_a_dead_binding", "verdict": "keep", "covered_by": null, "reason": "Canary for BindCommandToLua last-row-wins ordering and the dead 2469 binding. Nothing else checks it."},
  {"name": "quick_chat_rows_carry_the_recovered_animation_ids", "verdict": "keep", "covered_by": null, "reason": "Pins display, say and animation columns of recovered quick-chat rows. No equivalent in the similar files."},
  {"name": "emote_menu_categories_match_the_recovered_locale_ids", "verdict": "keep", "covered_by": null, "reason": "Pins menu root 13 and category locale ids. Not covered by the similar files."},
  {"name": "animation_names_cover_every_referenced_id", "verdict": "keep", "covered_by": null, "reason": "Checks every action's animation id resolves to a named slot or group and that names are unique. No equivalent elsewhere."},
  {"name": "restriction_flags_come_from_the_animation_block", "verdict": "keep", "covered_by": null, "reason": "Pins freezeMovement, hideSlotType, boneMasking and priority flags from AnimationTypes.xml. Restriction data is not checked directly elsewhere."},
  {"name": "menu_gating_matches_the_client_lua_filters", "verdict": "keep", "covered_by": null, "reason": "Pins ChatLog quick-chat menu filters (emote vs canned mode). No similar file tests emote_visible_in_menu."},
  {"name": "validation_accepts_recovered_emotes_and_rejects_restricted_requests", "verdict": "keep", "covered_by": null, "reason": "Downgraded from superseded. The mounted and moving refusals are covered by tests/emotes.rs::mounted_actors_cannot_emote_but_can_still_use_plain_chat and moving_blocks_only_the_freeze_movement_slot. But this test also asserts the resolved animation ids returned by validate_emote (wave 3354, cheer 3306, dance 3200 standing). Grep finds no other test asserting 3354 or 3306 through validate_emote, and emotes.rs checks only Ok/refused lists. Keep, or split out the refusal lines and drop only those if the duplication matters."},
  {"name": "an_animation_id_with_neither_a_slot_nor_a_group_is_still_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal check: id 3899 has no name and cannot ride the Dance phrase; foreign id 99999 is refused; 184/3200 is accepted. emotes.rs covers 184/3899 only through the catalog wrapper, so this direct validate_emote_phrase check is kept under the refusal rule."}
 ],
 "whole_file_removable": false,
 "confidence": 0.7,
 "notes": "No test is removable with confidence. The previous answer marked validation_accepts_recovered_emotes_and_rejects_restricted_requests as superseded; the critique was right that emotes.rs does not assert the resolved animation ids (3354, 3306, 3200), so that verdict is withdrawn. Possible reduction: split that test and remove only the Mounted/Moving refusal lines, which emotes.rs already covers. The module path osfr_tools::social_chat::piece_093 was not needed for these verdicts."}
