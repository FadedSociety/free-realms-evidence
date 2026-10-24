<!-- fleet job=note-refresh id=Pieces-093-Emotes-and-social-actions status=done turns=15 usd=0.0212 tokens(read,write,in,out)=[462893, 56788, 32, 18854] model=claude-haiku-5-5 -->
# notes/Research/Pieces/093 Emotes and social actions.md

**Verdict:** Badly stale on one thread, minor drift elsewhere. The recovered tables, client citations (ScriptsBase.lua, AnimationTypes.xml, AnimationTransitionRules.xml) and the restriction flags all hold at the tip. What is false is the Dance / animation 3200 gap, which L038 closed, and the "remaining integration" section, which predates the gateway wiring.

**Corrections:**

1. `old:` carries animation id 3200, which has no `AnimationSlot` row in `AnimationTypes.xml` and no `CodeAnimationMappings.txt` row. (wrapped over lines 98-99; join with single spaces)
   `new:` carries animation id 3200, the `emo_dance` AnimationGroup (`AnimationGroups.xml:874-880`) that plays one of slots 3201 and 3211-3214; `piece_093.rs` names it (`EMOTE_ANIMATIONS`, line 718).
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_093.rs:717-718` names 3200 as `emo_dance`; `repo:client:Resources/AnimationGroups.xml:874` defines the group; `repo:notes/Autopilot/L038.md:1-11` records the change.

2. `old:` No motion is invented for it; `validate_emote` rejects it as unrecovered. (wrapped, line 99-100)
   `new:` `validate_emote_phrase` accepts it standing and refuses it while mounted.
   `why:` `repo:prototype/osfr-tools/tests/piece_093.rs:243-247` (mounted refusal) and `:277` (`validate_emote_phrase(184, 3200, standing) == Ok`); `repo:prototype/osfr-tools/src/restoration/piece_093.rs:939-951` has no unrecovered-name rejection.

3. `old:` `Dance` (3200) cannot be accepted until the slot is recovered.
   `new:` `Dance` (3200) is accepted standing and refused mounted in code; the native check is that it plays `emo_dance` (one of 3201, 3211-3214).
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_093.rs:717-718`, `repo:prototype/osfr-tools/tests/piece_093.rs:277`.

4. `old:` 4. Recovery still open: animation id 3200, the trigger for `emo_spraycan` (3351), and any historical
   `new:` 4. Recovery still open: the trigger for `emo_spraycan` (3351), and any historical
   `why:` same as item 2. The `emo_spraycan` gap itself still holds: `piece_093.rs:785-787` says no quick-chat row reaches 3351.

5. `old:` each; `validate_emote` is the intended entry point, not a replacement for the packet writer.
   `new:` each. The refusal gate is already live: `route_quick_chat` calls `QuickChatCatalog::authorize_emote`, which calls `piece_093::validate_emote_phrase`, and refusals are silent drops. `validate_emote` has no production caller yet.
   `why:` `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2302-2310`; `repo:prototype/osfr-tools/src/social_chat.rs:461-474`; `grep validate_emote\(` in `src/` finds only `piece_093.rs:916`.

6. `old:` 8 behavioral tests;
   `new:` 9 behavioral tests;
   `why:` `repo:prototype/osfr-tools/tests/piece_093.rs` has nine `#[test]` functions (lines 47, 63, 72, 90, 114, 145, 178, 213, 263). L038 also reports "piece_093 9 passed".

7. `old:` Not registered in `src/lib.rs` (lead-owned).
   `new:` Not registered in `src/lib.rs` (lead-owned). `src/social_chat.rs:16-19` includes it with `#[path]` and re-exports it as `social_chat::piece_093`, which is how the gateway reaches it.
   `why:` `repo:prototype/osfr-tools/src/social_chat.rs:16-19`; `repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:444`.

8. `old:` 1. Lead registers the module in `src/lib.rs` and drops the `#[path]` include (shared file, lead-owned).
   `new:` 1. Lead registers the module in `src/lib.rs` and drops the `#[path]` includes in `src/social_chat.rs:17` and `tests/piece_093.rs:34` (shared files, lead-owned).
   `why:` `repo:prototype/osfr-tools/src/social_chat.rs:16-18`; `repo:prototype/osfr-tools/tests/piece_093.rs:31-36`.

9. `old:` 124: test animation_names_cover_every_referenced_id_except_the_recorded_gap ... ok
   `new:` test animation_names_cover_every_referenced_id ... ok
   `why:` `repo:prototype/osfr-tools/tests/piece_093.rs:114` (renamed by L038). This is a pasted log line, so it is minor.

**Unsure:**
- The Python checker still reports 3200 as unrecovered (`repo:scripts/pieces/piece_093.py:321, 418-424`). L038 did not touch it (`repo:notes/Autopilot/L038.md:132-133`), so the quoted checker output and `dance-animation-unrecovered` finding are still what it prints. The note should say the checker is pre-L038 if it keeps that output.
- The Rust module doc says column 5 is the menu parent (`repo:prototype/osfr-tools/src/restoration/piece_093.rs:15-17, 105`). The note says column 1, and the client Lua agrees: `ScriptsBase.lua:10152` passes `GetData(i,1)` as the parent. The note is right; the Rust comment looks wrong.
- The reconstruction paragraph says the Open Free Realms server decompile "does not carry an emote restriction model". I did not check the refs decompile, so I cannot confirm or refute that sentence.
- `social_chat.rs:483` says callers pass `mounted=false`, but `gateway.rs:1322-1325` now reads `Gameplay::is_mounted`. This is not in the note; it is only relevant if the note is later edited to describe mount wiring.
- `notes/Design/Build Ledger.md:44` still says "Dance (3200) refused". That contradicts L038 and `tests/piece_093.rs:277`, but it lives in another note.
