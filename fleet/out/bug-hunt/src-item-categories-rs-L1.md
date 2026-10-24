<!-- fleet job=bug-hunt id=src-item-categories-rs-L1 status=nothing_found turns=4 usd=0.0044 tokens(read,write,in,out)=[22936, 19433, 10, 3404] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/item_categories.rs lines 1-135 of 135

Reviewed `prototype/osfr-tools/src/item_categories.rs` lines 1-135 in full, plus the callers and evidence it depends on: `scripts/prepare-item-categories.py:45-58` (the producer of `categories.json`), `tests/item_categories.rs` (the layout and mutation tests), and the 2675-byte oracle note in MODLOG.md. I found no defect that meets the criteria.

What I checked:

- **Input source and reach (item 4).** `load` reads only `categories.json` from a server-side content directory. No client packet reaches it, so client-controlled panics and unbounded growth do not apply here.
- **Bounds and panics (items 1-2).** The file is read through `take(MAX_CONTENT + 1)` and then size-checked. Category count is capped at 512 and group count at 2048 before any loop. The `as i32` casts operate on those capped lengths. The O(n²) group scan is bounded by 2048. JSON errors are mapped to `Err`, not unwrapped. There are no unchecked indexes.
- **Atomicity (item 3).** `load` is pure: it builds a local `packet` and returns `Ok(Self { packet })` only after the SHA check passes. Nothing is mutated before a failing `?`.
- **Logic (item 5).** The wire layout matches the producer script and the comments. A category is written as key `id`, then `id`, `name_id`, `icon_id`, `unknown`, the bool byte, then `display`. A group is written as key `id`, then `id` and `category_id`. Groups are emitted by first-occurrence order of their ID, keeping content order within each ID. Validation rejects `<= 0` IDs and duplicate category IDs and duplicate (group, category) pairs. Byte arithmetic checks out: 8 + 25·N_cat + 4 + 12·N_group gives 98 for the test fixture and 2675 for the 71/74 real packet. The SHA check runs after validation and compares lowercase hex, which is the form the Python producer emits.

I found no issue that a remote player or a corrupted save could trigger through this file.
