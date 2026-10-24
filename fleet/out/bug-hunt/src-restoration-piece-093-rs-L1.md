<!-- fleet job=bug-hunt id=src-restoration-piece-093-rs-L1 status=nothing_found turns=5 usd=0.0071 tokens(read,write,in,out)=[65301, 26542, 12, 6278] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_093.rs lines 1-800 of 952

Window `prototype/osfr-tools/src/restoration/piece_093.rs` lines 1-800 is static data (consts and enum helpers, no parsing, indexing of client input, allocation, or mutation). I found no defect that a remote client can trigger.

What I checked:
- **Array sizes:** `EMOTE_COMMANDS` (72), `EMOTE_ACTIONS` (73), `EMOTE_ANIMATIONS` (72) and the flag arrays match their declared lengths. Rust enforces this at compile time anyway.
- **Command coverage:** every winning quick-chat id in `EMOTE_COMMANDS` (including the second `curious` → 148 binding) has an `EMOTE_ACTIONS` row. 2469 is absent from `EMOTE_ACTIONS`, as `DEAD_EMOTE_BINDINGS` says.
- **Animation coverage:** every `animation_id` in `EMOTE_ACTIONS` has a name in `EMOTE_ANIMATIONS`, or is the documented group 3200. No slot is unreferenced except 3351, which is documented as such.
- **Restriction flags vs. shipped data:** checked against `client/Resources/AnimationTypes.xml`. `freezeMovement` on 3001 and 3351 matches (lines 996, 1242). `disableBoneMasking` on 3329 matches (line 1240). `priority="1"` on 3101, 3201 and 3211-3214 matches. The `hideSlotType` exception list [3001] matches: 3001 is the only emo_ slot without `hideSlotType` in the surveyed Emotes block (lines 996-1020), and 3002-3007 carry priority 0 consistently with the PRIORITY_ONE list.
- **Locale ids:** `locale_id()` and `EMOTE_CATEGORIES` agree on all six categories. `menu_parent()` values are consistent with the `EmoteCategory` doc comments.
- **Callers:** `social_chat.rs:461-473` (`authorize_emote`) converts the animation and phrase ids with `try_from` and passes them into `validate_emote_phrase`, which is outside this window. Nothing in lines 1-800 consumes client input, so no client-controlled value reaches these tables unchecked.

Out of scope: `validate_emote` and `validate_emote_phrase` (lines 801-952) are not in my window. Nothing here depends on them.
