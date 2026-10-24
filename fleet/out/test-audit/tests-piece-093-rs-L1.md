<!-- fleet job=test-audit id=tests-piece-093-rs-L1 status=done turns=6 usd=0.0076 tokens(read,write,in,out)=[54920, 24079, 14, 7986] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_093.rs lines 1-278 of 278

Window: `prototype/osfr-tools/tests/piece_093.rs` lines 1-278. Code under test read in `prototype/osfr-tools/src/restoration/piece_093.rs` (1-952). Findings, most serious first:

- **[high] tests/piece_093.rs:185 emote_menu_categories_match_the_recovered_locale_ids (menu-parent check) - the expected value is produced by the same code path as the value under test, so the parent check cannot fail.**
  - Why it cannot catch a regression: `EmoteActionRow::parent_id()` is defined as `self.category.menu_parent()` (src/restoration/piece_093.rs:106-108). The test compares `emote_action(145).parent_id()` with `EmoteCategory::Dramatics.menu_parent()`. Any change to the `menu_parent` mapping, or to the row's category, moves both sides together. Nothing checks the recovered column-5 parent from the `QuickChatData` payload, and that parent drives the menu-tree gating in `emote_visible_in_menu`.
  - Fix: assert literal parent ids for known rows, for example `assert_eq!(emote_action(145).unwrap().parent_id(), 130)`, `assert_eq!(emote_action(143).unwrap().parent_id(), u32::MAX)`, and one row per category (129-134). Better still, check them against the recovered payload column-5 values, not the code's own mapping.

- **[medium] tests/piece_093.rs:64-70 repeated_command_binding_resolves_last_and_the_old_id_is_a_dead_binding - the "dead binding" claim is checked only against a hand-written constant, not against the command table.**
  - Why it cannot catch a regression: `assert_eq!(DEAD_EMOTE_BINDINGS, [(2469, "curious")])` compares a constant with itself. The test never confirms that `EMOTE_COMMANDS` actually contains the earlier `("curious", 2469)` row. If that row were deleted, the test would still pass, because `curious` still resolves to 148 and 2469 still has no action row. The name's claim that the old id was a binding is therefore not exercised.
  - Fix: assert that `EMOTE_COMMANDS.iter().filter(|(c, _)| *c == "curious").map(|(_, id)| *id).collect::<Vec<_>>() == [2469, 148]`. That pins array order and the dead id together, so removing or reordering the first row fails.

- **[medium] tests/piece_093.rs:137-142 animation_names_cover_every_referenced_id - the comment says "no duplicate names and no duplicate ids", but only names are checked.**
  - Why it cannot catch a regression: a second `EMOTE_ANIMATIONS` row with an existing animation id but a new name (e.g., `(3317, "emo_no2")`) passes. The `dedup` check runs on names only. The duplicate-id claim is never tested, and an id collision would make `emote_animation_name` silently return the first match.
  - Fix: collect the ids from `EMOTE_ANIMATIONS`, sort, dedup, and assert the length is unchanged, in the same way as the names.

- **[medium] tests/piece_093.rs:146-176 restriction_flags_come_from_the_animation_block - the name says the flags come from the animation block, but the test never reads `AnimationTypes.xml`.**
  - Why it cannot catch a regression: the expected lists (`FREEZE_MOVEMENT_ANIMATIONS`, `HIDE_SLOT_TYPE_EXCEPTIONS`, `PRIORITY_ONE_ANIMATIONS`, `DISABLE_BONE_MASKING_ANIMATIONS`) are the same constants that `emote_restrictions` reads. The test checks code against code. A wrong flag value copied into both places, or a mis-recorded XML attribute, passes. The `AnimationTypes.xml:1156-1160` citation in the comments is never checked. The `hide_slot_type` result for every named slot is also computed by a rule in the code, not read from the data.
  - Fix: parse the `Emotes` block of `client/Resources/AnimationTypes.xml` (or check a generated fixture derived from it, with its hash pinned) and assert each slot's `hideSlotType`, `freezeMovement`, `disableBoneMasking` and `priority` against `emote_restrictions`. Alternatively, rename the test to say the flags are the recorded constants.

- **[low] tests/piece_093.rs:49, 74, 93, 118 (also 116-117 comment) - `len()` assertions on fixed-size arrays, and exact counts that churn.**
  - Why it cannot catch a regression: `EMOTE_COMMANDS`, `EMOTE_ACTIONS`, `EMOTE_CATEGORIES` and `EMOTE_ANIMATIONS` have array types `[_; N]` with the same `N`, so `.len()` equals the declared size at compile time. These asserts cannot fail on any data change. The counts also restate the array sizes and churn when unrelated rows are added.
  - Fix: remove these asserts. Pin the content instead (for example, the sorted command set or the set of quick-chat ids against the payload), which fails when a row is dropped or swapped.

- **[low] tests/piece_093.rs:259-278 an_animation_id_with_neither_a_slot_nor_a_group_is_still_refused - the doc says the id is refused "outside the Emotes block", but 3899 is inside it.**
  - Why it cannot catch a regression: `EMOTE_ANIMATION_BLOCK` is 3001..=3900 (src:913), so 3899 passes the block check. It is refused only by `AnimationMismatch` (src:942), because row 184 carries 3200. The test does not exercise the block-range check it describes. A change to the block bounds that still rejects 3899 by mismatch would pass unnoticed.
  - Fix: add an assertion with an id just outside the block (e.g., 3901 with a row-184 request, expecting `ForeignAnimation`), and reword the doc to say the id is refused by animation mismatch.

No `#[ignore]` or early-return skips in this window. The `#[path]` include target (src/restoration/piece_093.rs) exists.
