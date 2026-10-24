<!-- fleet job=note-refresh id=Pieces-096-Typed-world-initialization status=done turns=16 usd=0.0204 tokens(read,write,in,out)=[564836, 63963, 34, 13595] model=claude-haiku-5-5 -->
# notes/Research/Pieces/096 Typed world initialization.md

**Verdict:** minor drift. The status, file paths, test counts, the slot registry and the "not registered" claim all hold at the tip. Two statements about the gateway are stale.

**Checked and holding:**
- `src/restoration/piece_096.rs` (1169 lines), `tests/piece_096.rs` (465 lines, `#[path]` include at line 34), `scripts/pieces/piece_096.py` and `tests/pieces/test_piece_096.py` all exist.
- Registry: `INIT_SLOTS` (`piece_096.rs:182-229`) has typed slots 0-7 and 42-45, 12 in total. Captured slots 8-41 are 34 in total. The Python checker's `TYPED_SLOTS` (`tests/piece_096.rs:57`) matches.
- Test counts: 9 hermetic `#[test]` functions (lines 190-384) plus one `#[ignore]` oracle (line 406). Python has 7 test methods (lines 55-127).
- `verify_captured` exists (`piece_096.rs:1148`). The module is not registered: no `mod piece_096` or `restoration/piece_096.rs` path appears in `src/`.
- The `frame` layout (`piece_096.rs:462-469`) is u16 5, u8 1, u32 length, payload, as the note says.
- Captured-emitter attribution (`piece_096.rs:240-257`) gives 6 + 14 + 3 = 23 op35 slots, as the note says.

**Corrections:**

1. Line 119 (Remaining gates, item 2)
   - `old:` `` `wrapped`/`initial_zone` pair duplicates two of these writers and should be replaced by ``
   - `new:` `` `wrapped` (gateway.rs:690) duplicates `frame`, and no `initial_zone` function exists at the tip; replace `wrapped` by `frame` so the copies cannot drift ``
   - `why:` `repo:prototype/osfr-tools/src/gateway.rs:690` defines `wrapped`, which writes `[5,0,1,len,inner]` like `piece_096.rs:462-469`. A search of `prototype/osfr-tools` finds no `initial_zone` function. The only mention is a stale comment at `tests/world.rs:176`, plus the module doc itself at `piece_096.rs:38`.

2. Line 117 (Remaining gates, item 2)
   - `old:` `` `Gateway::load_reference` could call `verify_captured` for the 12 typed slots ``
   - `new:` `` `load_reference` (a free function at `gateway.rs:312`, not a `Gateway` method) could call `verify_captured` for the 12 typed slots ``
   - `why:` `repo:prototype/osfr-tools/src/gateway.rs:312` is `fn load_reference(directory: &Path)` at top level. The `impl Gateway` block starts later, at line 697.

**Unsure:**
- The "lib test: 24 passed" figure, and the other lab-side results (RED/GREEN logs, the private oracle run, `piece-096.json`). I did not run them, and they sit outside the repo.
- Recovered-source claims that cite `lab/decompiled/...` (for example the `HandlePacketClientIsReady` send order and the 1383-row / 263 893-byte item payload). The capture is not in the repo, so I could not confirm them. A search for `1383` and `263893` found no match in `prototype/osfr-tools`.
- The Rust field-level layouts (for example `ZoneDetails` values `FabledRealms`/type 2/id 5/geometry 5) match `tests/piece_096.rs:59-72`. I did not check the encode bodies byte by byte.
