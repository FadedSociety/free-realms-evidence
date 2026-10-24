<!-- fleet job=note-refresh id=Native-Mining-Tile-Rendering status=done turns=6 usd=0.0067 tokens(read,write,in,out)=[58459, 21674, 14, 6772] model=claude-haiku-5-5 -->
# notes/Research/Native Mining Tile Rendering.md

**Verdict:** minor drift. The diagnosis is dated 2026-10-09 and is accurate as a snapshot, but its "Source side" and "Bounded recommendation" text still describes the pre-fix emitter as current, and the "Fix applied" section at the bottom has since moved the code.

**Corrections:**

1. `old:` So the second argument is `kind.category` (400/600), not the per-kind
   `new:` At the emitting revision (`a66073…`) the second argument was `kind.category` (400/600), not the per-kind index; the tip now sends `value - category` (see "Fix applied").
   `why:` repo:prototype/osfr-tools/src/mining.rs:1369-1378 (`kind.value.checked_sub(kind.category)` passed as the second field of `OnTileInfoMsg\t{}\t{}`).

2. `old:` `initialize_board` lines 1106-1114)
   `new:` `initialize_board` lines 1106-1114 at that revision; at the tip the emitter is `prototype/osfr-tools/src/mining.rs:1359-1379`)
   `why:` repo:prototype/osfr-tools/src/mining.rs:1359-1379 (`if !reshuffle { for kind in &spec.tiles { ... message(... OnTileInfoMsg ...) } }`); the 1106-1114 range no longer holds this emitter.

3. `old:` ## Bounded recommendation (no edits made)
   `new:` ## Bounded recommendation (applied 2026-10-09; see "Fix applied")
   `why:` repo:prototype/osfr-tools/src/mining.rs:1369-1377 already emits `OnTileInfoMsg(value, value - category)` for every configured kind, and the refusal for underflow is at mining.rs:1371-1372. The recommended bullet "Emit `OnTileInfoMsg(value, value - category)`" is therefore done.

4. `old:** No production source was edited.**`
   `new:** No production source was edited in the diagnosis itself; the narrow repair in "Fix applied" (2026-10-09) was made afterwards and is the current state.`
   `why:** repo:prototype/osfr-tools/src/mining.rs:1361-1377 (fix present) and repo:prototype/osfr-tools/tests/mining_tile_rendering.rs:1-9 (new regression test); the note's own "Fix applied" section contradicts the header.

**Checked and holding:**
- `prototype/osfr-tools/tests/mining_tile_rendering.rs` exists with exactly 3 `#[test]` functions (lines 126, 147, 162), matching the "3 passed" claim.
- `mining_spec()` carries 401..405 (category 400) and 601/602 (category 600) at mining.rs:968-1002, matching the 1..5 / 1..2 index claims.
- The `checked_sub` underflow refusal with the text "mining tile value below its category" is at mining.rs:1371-1372.
- Locale 117144 = "Iron" (confirmed through the `locale` tool).

**Unsure:**
- Frame inventory (`game_mining.gfx`: `SelectableTile1`–`SelectableTile5`, `Iron_LowQual/MedQual/HighQual`, gem frames) and the `CodeStringMappings.txt` ranges (601–603 Iron, 604–606 Tin, etc.) cite `lab/decompiled/...` and `Resources/` paths. The client index here has no `Iron_MedQual` or `SelectableTile5` hits, so I could not re-verify them.
- The `lab/reports/...` bundles, the SHA-256 prefixes and the `mining-board.png` hash are outside `repo`, so I did not check them.
- The "Remaining native verification" paragraph is a lead-owned action, not a code claim, so I left it as is.
