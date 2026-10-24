<!-- fleet job=test-verify id=tests-piece-093-rs-L1-f1 status=done turns=7 usd=0.0080 tokens(read,write,in,out)=[84799, 29274, 16, 6952] model=claude-haiku-5-5 -->
# high: tests/piece_093.rs:185

**Verdict:** `confirmed`, with a correction to the mechanism the claim gives. The test does not catch a `menu_parent` mapping change for categories 129-134. The claim's second clause, that a change to the row's category also passes, is wrong.

**Evidence**

- The only parent assertion for a category row is `tests/piece_093.rs:185-188`: `assert_eq!(emote_action(145).unwrap().parent_id(), EmoteCategory::Dramatics.menu_parent());`. `parent_id()` is `self.category.menu_parent()` (`src/restoration/piece_093.rs:106-108`). Changing the Dramatics arm of `menu_parent` (line 73) or swapping two arms moves both sides together, so this assertion still passes.
- No other assertion in the test file or in `tests/emotes.rs` or `tests/mount_routing.rs` pins a category parent value. `grep` for `parent`/`menu_parent` in those files finds only the lines above. The literal `130` in lines 200-206 is passed as an argument to the pure function `emote_visible_in_menu` (`piece_093.rs:869-875`). It does not read the mapping, so it cannot detect a change to `menu_parent`.
- `EMOTE_CATEGORIES` (lines 84-91, asserted at 94-100) pins locale ids, not parent ids. Lines 101-111 pin `locale_id()` and the row categories, not `menu_parent()`.
- Nothing in the Rust crate reads `parent_id()` outside this module. `emote_visible_in_menu` receives `parent_id` as a plain argument. So the claim's statement that the column-5 parent "drives" gating is overstated in this repo: no code or test connects a row's parent to the gating function.

**Where the claim's reasoning is wrong**

- Changing row 145's `category` in `EMOTE_ACTIONS` does not move both sides. `parent_id()` changes, but `EmoteCategory::Dramatics.menu_parent()` stays 130. For example, moving 145 to `Basics` gives 129 ≠ 130 and fails at line 186. The claim is therefore only right for mapping changes, not for row-category changes.
- The `TopLevel` check at line 184 (`emote_action(143).parent_id() == TOP_LEVEL_PARENT`) does catch a change to the `TopLevel` mapping, because `TOP_LEVEL_PARENT` is a separate constant.

**Minimal fix:** add literal parent assertions that do not go through `menu_parent()`, for example `assert_eq!(emote_action(145).unwrap().parent_id(), 130);` and one literal per category row (129-134). Better, compare them to the recovered column-5 values from the `QuickChatData` payload.
