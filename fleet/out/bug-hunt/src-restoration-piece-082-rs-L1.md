<!-- fleet job=bug-hunt id=src-restoration-piece-082-rs-L1 status=nothing_found turns=6 usd=0.0038 tokens(read,write,in,out)=[44728, 14772, 14, 2952] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_082.rs lines 1-353 of 353

Reviewed `prototype/osfr-tools/src/restoration/piece_082.rs` lines 1-353 in full, and checked the Python mirror of `canonical_fingerprint` (`scripts/pieces/piece_082.py:331-354`). No defect in the window that I can tie to a line and show is reachable.

What I checked:

- **Reach:** the module is not compiled into the server. Nothing in `src/` registers `piece_082` (no `mod`/`pub mod` line; `src/restoration/` has only other pieces, and the piece_082 header says it awaits lead registration). Its only callers are `tests/piece_082.rs`, which includes it via `#[path]`. No packet handler constructs `InventorySearch`, `ContentIndex` or `OwnedInstance`, so no client packet or save reaches it.
- **Panics (1):** no indexing, slicing, `unwrap`, or `from_utf8` on external data. `resolved_rows()` (`:215-217`) subtracts `missing_definitions.len()` from `rows.len()`. `report()` pushes exactly one row per instance and at most one missing entry per instance, so it cannot underflow. Fingerprint formatting cannot panic.
- **Unbounded growth (2):** `add_instance` (`:236-248`) has no cap, but no client path reaches it.
- **Atomicity (3):** `insert_definition` (`:86-112`) validates before it mutates, so no half-applied state.
- **Trusting client (4):** the only validations are `id == 0` and `category < 0`, and they run before any insert. Conflicting definitions are refused (`:102-105`), matching the doc comment.
- **Logic (5):** the doc comments match the code: rows are in instance-id order via `BTreeMap`, `definitions_missing_category` counts definitions per category, and `definitions_missing_name` skips `name_id == 0` and is sorted and deduplicated. The Rust and Python fingerprint formats match field for field.

Nothing to report.
