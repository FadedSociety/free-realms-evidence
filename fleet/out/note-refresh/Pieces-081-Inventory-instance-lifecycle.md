<!-- fleet job=note-refresh id=Pieces-081-Inventory-instance-lifecycle status=done turns=12 usd=0.0160 tokens(read,write,in,out)=[275571, 45447, 26, 15124] model=claude-haiku-5-5 -->
# notes/Research/Pieces/081 Inventory instance lifecycle.md

**Verdict:** badly stale. The "gap" section, the test paragraph and the integration contract describe the pre-integration tree. The lead has since wired the counter into `Inventory::grant_with_tint`, so production no longer allocates `max(id) + 1`. The module itself (schema, floor-on-open, burn-before-hand-out, verify, `Exhausted`) still matches the code.

**Corrections:**

1. old:
```
Production allocates a new instance inside `Inventory::grant_with_tint` as
`max(existing item id) + 1` (`src/inventory.rs`), and `Inventory::consume` deletes a row when its
count reaches zero. Retiring the highest row therefore frees its id: the next grant hands the same
id out again. A restart repeats the same derivation because nothing durable records the id.
```
new:
```
`Inventory::grant_with_tint` now takes a new row's id from `instance_ids::allocate_from_snapshot` (the `piece_081.rs` module, included by `#[path]` at `src/inventory.rs:40-41`). It returns `max(stored next_instance_id, highest live id + 1)` and stores the following value in `InventoryState.next_instance_id`. `Inventory::consume` still deletes a row when its count reaches zero but does not lower that mark, so retiring the highest row does not free its id. The mark is saved with the items (`src/inventory.rs:83-85`), so a restart keeps it.
```
why: repo:prototype/osfr-tools/src/inventory.rs:1012-1016 (`instance_ids::allocate_from_snapshot(staged.state.next_instance_id, &live_ids)`, then `staged.state.next_instance_id = Some(next)`); :83-85 (field, serde default, skip if none); :1062-1103 (consume never touches the mark); repo:prototype/osfr-tools/src/restoration/piece_081.rs:63-75.

2. old:
```
Two characterisation tests pin both halves: `production_reward_reuses_a_retired_top_instance_id`
shows the current allocator reusing id 3 after it was consumed, and
`counter_supplied_ids_close_the_production_reuse_gap` shows the counter agreeing with production on
the first grant and diverging exactly at the reuse.
```
new:
```
Two characterisation tests pin both halves: `production_reward_never_reuses_a_retired_top_instance_id` (`tests/piece_081.rs:356`) asserts that production does not reuse id 3 after it is consumed, and `counter_supplied_ids_close_the_production_reuse_gap` (`tests/piece_081.rs:372`) shows the counter and production agreeing on ids 3 and 4.
```
why: repo:prototype/osfr-tools/tests/piece_081.rs:356-367 (test is renamed and asserts `reused > first`); :372-390 (asserts `production_reused == 4 == second`, no divergence).

3. old: `tests the lead should retire when `inventory.rs` takes its id from the counter.`
new: `tests guard the integrated call site. `inventory.rs` already takes its id from the allocator, so both run as regression guards against reuse.`
why: repo:prototype/osfr-tools/src/inventory.rs:1012-1016 (the call-site change has landed).

4. old: `2. In `Inventory::grant_with_tint`, replace the `max(id) + 1` derivation with `counter.allocate()`.`
new: `2. Done. `Inventory::grant_with_tint` takes its id from `instance_ids::allocate_from_snapshot` (`src/inventory.rs:1012-1016`) instead of `max(id) + 1`. The staged clone, merge, `fits_one_stack` check (`src/inventory.rs:982`) and 38/2 reply (`src/inventory.rs:1032`) are unchanged.`
why: repo:prototype/osfr-tools/src/inventory.rs:982, 1012-1016, 1032. `InstanceCounter::allocate` is not called from `src/` outside `piece_081.rs`.

5. old:
```
1. Open the counter once per character where gameplay state loads, passing every id the build can
   observe: the live rows plus the prepared content's own `initial_state` ids. The current content
   starts at 7, the live campaign at 35, so the counter opens at 36.
```
new:
```
1. Not used as written. `inventory.rs` does not open an `InstanceCounter`. At each new-row grant it floors the stored mark against the character's live rows only (`src/inventory.rs:1012-1014`). The prepared content's `initial_state` ids are not passed in.
```
why: repo:prototype/osfr-tools/src/inventory.rs:1012-1014 (`live_ids` built from `staged.state.items` only). `InstanceCounter::open` appears only in `src/restoration/piece_081.rs` and `tests/piece_081.rs`.

6. old: `module already owns or folded into the version 2 gameplay snapshot by its owner.`
new: `module already owns. It was folded into the gameplay snapshot instead: `InventoryState.next_instance_id` is an optional field saved with the items (`src/inventory.rs:83-85`). The inventory path does not write the sibling document.`
why: repo:prototype/osfr-tools/src/inventory.rs:83-85; MODLOG.md:428 ("integrated piece081 pure allocator into optional InventoryState.next_instance_id saved with items").

7. old: `before the lead retires them.`
new: `while the call site stays on the allocator. Both assert the integrated behaviour (`tests/piece_081.rs:356-390`).`
why: repo:prototype/osfr-tools/tests/piece_081.rs:356-390 (the tests now assert non-reuse and agreement, so they do not fail on the current tip).

**Unsure:**
- The "no shared `lib.rs` was touched" claim (line 11-12 of the note). `src/lib.rs:36` now has `pub use inventory::instance_ids as inventory_ids;`, and the shared `src/inventory.rs` was changed to call the module. I cannot tell from the tree whether that was this piece or the lead. The note's claim covers only this piece's own commits, so I did not correct it.
- "version 2 gameplay snapshot" (step 4): I found no source for the "version 2" label in `src/inventory.rs`. I did not correct the label itself.
- The test counts and log results (RED 8 failed, GREEN 12 passed, ordinary suite 1338 passed) are in `lab/` and were not re-run. The test names and assertions I read are consistent with a passing suite, but I did not confirm the numbers.
- "The `fits` stack check" in the integration contract: the function is `fits_one_stack` (`src/inventory.rs:193`). This is a naming nit and I left it out of the corrections.
- Reading `grant_with_tint` by hand, I believe the second test now yields `4` for production, but I did not run it.
