<!-- fleet job=note-refresh id=Pieces-082-Inventory-search-crash status=done turns=9 usd=0.0144 tokens(read,write,in,out)=[196410, 49458, 20, 12491] model=claude-haiku-5-5 -->
# notes/Research/Pieces/082 Inventory search crash.md

**Verdict:** minor drift. The repo-side claims hold: all four cited files exist, the test counts match, and the Rust constants and the nine pinned hashes match the code. One original-client attribution is wrong and is repeated in the Rust module header.

**Corrections:**

1. `old:` (`FUN_00a6e7b0`, `1341392`), copy the applied text, clear the pending flag.
   `new:` (the loop `FUN_00a6e7b0`, `1341392`, calls it through vtable slot `+0x3c`; the slot target is not re-proved here, and the vault's shard reading in `Build Guides/Gameplay/Items and Inventory.md` names `FUN_00a6d9b0` for it), copy the applied text, clear the pending flag.
   `why:` In the client decompile, `FUN_00a6e7b0` is the rebuild loop, not the predicate. It contains `cVar2 = (**(code **)(*piVar5 + 0x3c))(*piVar4);` and copies the accepted row's `+0x10` id into the result array. `FUN_00a6e910` (the refresh path, client_sql `fn` row `00a6e910`) calls `FUN_00a6e7b0`, and `Items and Inventory.md:279` records the same correction. The same misattribution appears in `prototype/osfr-tools/src/restoration/piece_082.rs:16-17` and `prototype/osfr-tools/tests/piece_082.rs:9-10`, and those headers should be fixed with it.

**Checked and holding:**
- Files exist: `src/restoration/piece_082.rs`, `tests/piece_082.rs`, `scripts/pieces/piece_082.py`, `tests/pieces/test_piece_082.py`.
- Test counts: `test_piece_082.py` has 15 test methods, matching "Python `15 passed`". `tests/piece_082.rs` has 7 `#[test]` functions plus 1 `#[ignore]`d oracle, matching "7 passed, 0 failed, 1 ignored".
- The Rust constants `0x2e8`, `0x2f0`, `0x2ec`, `0x2d0` and slot `0x3c`, plus the names `BaseClient.SearchInventoryItemsData` and `BaseClient.InventoryItemsData` and the query `Wheeler`, are in `src/restoration/piece_082.rs:39-53` and pinned by `tests/piece_082.rs:201-216`.
- `scripts/pieces/piece_082.py:76-86` lists nine pinned input hashes, and the crash manifest hash `644cd786…` matches.
- The client's constructor path agrees: `ClientPlayerItemManager` (`009918d0`) sets `*(param_1[0xdf]+0x2e8)=1` after building the search source, and `FUN_00a6deb0` clears `+0x2e8`, sets `+0x2f0` and the `IString<char>` at `+0x2ec`. `FUN_00a6e910` clears `+0x2d0` after the rebuild.

**Unsure:**
- The `1341483` / `1341392` / `1170126`-series pseudocode line numbers and the `../lab` fault evidence (exit code, last frame at 21.593 s, the 1386/1329/71/74/63 counts, the `Wheeler` match list and the fingerprint `72260f1c…`) live outside the repo or in the private bundle, so I could not verify them. The `0xC0000005` value does equal `3221225477`.
- I did not run the Python or Rust suites. The counts above come from static inspection.
- The identity of the slot `+0x3c` target (`FUN_00a6d9b0` per the vault's shard reading) is not confirmed by a vtable lookup.
- `src/restoration/` has no `mod.rs`, and no restoration piece is registered in `lib.rs`. The note's lead-registration step is a future gate, so I did not treat it as a false claim.
