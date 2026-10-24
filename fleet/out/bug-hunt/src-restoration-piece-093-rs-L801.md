<!-- fleet job=bug-hunt id=src-restoration-piece-093-rs-L801 status=nothing_found turns=9 usd=0.0078 tokens(read,write,in,out)=[106650, 22580, 20, 7761] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_093.rs lines 801-952 of 952

Window `prototype/osfr-tools/src/restoration/piece_093.rs` 801-952 (emote transition/restriction tables, `emote_command_id`, `emote_action`, `emote_animation_name`, `emote_restrictions`, `emote_visible_in_menu`, `EmoteContext`, `validate_emote`, `validate_emote_phrase`). I found no defect I could show reachable from a client packet or save.

What I checked:
- **No panics or unbounded growth.** Every function is a bounded linear scan over `const` tables or a `contains` on a fixed array. No indexing, `unwrap`, division or arithmetic on client values exists in the window.
- **Client input stops at the catalog.** The only client-controlled value that reaches `validate_emote_phrase` is the phrase id, via `social_chat.rs:461-473` (`QuickChatCatalog::authorize_emote`). The animation id comes from the server's startup catalog (`gateway.rs:1310-1318`, from `startup_snapshot.rs:512`), not from the packet. Negative ids are mapped to `u32::MAX` and then refused as foreign (`social_chat.rs:469-471`).
- **Mount and movement state are server-derived.** `gateway.rs:1322-1324` takes `mounted` from gameplay and `moving` from the server's `last_movement_ms`. `social_chat.rs:485-491` applies the 500 ms window with `saturating_sub`. The client cannot set either flag directly.
- **Doc and test agree.** `emote_command_id` keeps the last binding (`curious` → 148), as its doc and `tests/piece_093.rs:67` state. `emote_visible_in_menu` matches its doc and tests at `tests/piece_093.rs:190-210`. `validate_emote` checks the command's winning row, so the dead 2469 binding is never used.

Considered and dropped:
- `validate_emote_phrase` (piece_093.rs:942) skips the `AnimationMismatch` check when the phrase id has no recovered `EMOTE_ACTIONS` row (`is_some_and`). This fails open, but the animation still comes from server catalog data and is still checked for block range, mount state and freeze. I could not construct a client-reachable harm, so I did not report it. Reviewers may want to know that the mismatch check is data-dependent.
- The 500 ms moving window is a design limitation (opcode 125 carries no velocity), not a defect in this window.
