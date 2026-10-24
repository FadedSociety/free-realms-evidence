<!-- fleet job=note-refresh id=Startup-Catalogues status=done turns=11 usd=0.0107 tokens(read,write,in,out)=[222776, 37629, 24, 7484] model=claude-haiku-5-5 -->
# notes/Research/Startup Catalogues.md

**Verdict:** minor drift. The builders, client addresses, byte layouts, and test counts check out. Two statements are false: the claim that the builders are not registered in the gateway, and the description of the test target. One citation has moved.

**Corrections:**

1. `old:` These builders are not registered in the shared startup gateway.
   `new:` These builders are registered in the shared startup gateway. `StartupSnapshot::build_packet` (`src/startup_snapshot.rs`) calls them for indices 00, 04-06, 35-37, 40, 42, and 44, and the gateway's startup path calls it for indices 5 and 8-45.
   `why:` repo:prototype/osfr-tools/src/startup_snapshot.rs:309, 313, 315, 344, 361, 363; repo:prototype/osfr-tools/src/gateway.rs:1898-1918 (`snapshot.build_packet(index, state.guid)`); repo:notes/Research/Startup Integration.md:3, 7-8 (W19 registration).

2. `old:` (`#[path]` includes the private builder module; no shared module registration)
   `new:` (imports the registered library module `osfr_tools::startup_catalogues`; `src/lib.rs` declares `pub mod startup_catalogues;`)
   `why:` repo:prototype/osfr-tools/tests/startup_catalogues.rs:1-4 (`use osfr_tools::startup_catalogues::{...}`; no `#[path]` attribute); repo:prototype/osfr-tools/src/lib.rs:89.

3. `old:` (`inventory.rs:319-336`, `inventory_v2_fixes.rs:34-90`)
   `new:` (`inventory.rs:607-625`, `inventory_v2_fixes.rs:35-90`)
   `why:` `Inventory::definitions_packet` is at repo:prototype/osfr-tools/src/inventory.rs:607 and calls `v2_fixes::encode_definition_batch_v2` at line 625. Lines 319-336 are now the `Content` struct and the `shared_content` cache. `encode_definition_batch_v2` starts at repo:prototype/osfr-tools/src/inventory_v2_fixes.rs:35; its doc comment begins at line 27.

**Checked and holding:**
- The builder file exists at `src/startup_catalogues.rs`, and the 10 builder functions the note names are all present (lines 113-259).
- The test target has 7 `#[test]` functions, one of them `#[ignore]` (the oracle). That matches "7 tests total, 6 passed".
- The 1,383 captured records and 1,329 unique IDs match the comment at `src/startup_catalogues.rs:109-110`.
- The item-batch reader contract (duplicates kept, ID-keyed cache) matches `src/startup_catalogues.rs:106-112`.
- The combat-flag layout (two zero dwords plus a bool, `src/startup_catalogues.rs:228-234`) and the settings body (three dwords, one byte, one float bit pattern, `src/startup_catalogues.rs:237-245`) match the note.
- The 06 tail is 62 bytes (`UNIDENTIFIED_193_2_CAPTURE_REST: [u8; 62]`, `src/startup_catalogues.rs:14`).
- Client addresses are present in the client database: `0092f460`, `009471a0`, `00a35cc0`, `00a40aa0`, `00c71510`, and `00c75fc0`.

**Unsure:**
- The `lab/reports/catalogues-20261013T204520Z/` and `lab/reports/startup-builders-20261013T191103Z/` paths are outside the readable roots, so I could not confirm that they exist.
- The capture counts (1,834 and 231 coin rows, eight kind-0 ability slots, 85-byte blobs with IDs 2 and 4, and the per-index lengths) are capture data that I could not verify against the private reference. The test assertions are consistent with them.
- The client reader details beyond the function addresses (for example, the 19-byte coin entry layout and the stat value-kind rule) were not decompiled line by line.
