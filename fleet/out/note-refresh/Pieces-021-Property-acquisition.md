<!-- fleet job=note-refresh id=Pieces-021-Property-acquisition status=done turns=18 usd=0.0180 tokens(read,write,in,out)=[497655, 46515, 38, 14466] model=claude-haiku-5-5 -->
# notes/Research/Pieces/021 Property acquisition.md

**Verdict:** minor drift. Most code claims hold: the file and test paths, the 13 + 1 ignored Rust tests, the 13 Python tests, the `lib.rs` non-registration, the ZoneManager lines, the `Type == 16` line, the check order and the client constructor addresses. Three statements are false: the housing gate and the deed-gap counts.

**Corrections:**

1. `old:` `src/housing.rs` currently refuses a second owner of the same property id, while the
   `new:` `src/housing.rs` already accepts a second owner of the same property id (the lot guid is derived from owner and property id), so the
   `why:` repo:prototype/osfr-tools/src/housing.rs:637-653 derives `lot_guid` from `(owner_guid, property_id)`. repo:prototype/osfr-tools/src/housing.rs:673-685 looks up existing grants by that `lot_guid` and returns `PropertyAlreadyOwned` only when the same lot guid is held by a different owner. A second owner of the same property therefore gets its own lot.

2. `old:` The lead must widen that
   `new:` The lead need only confirm that
   `why:` The per-owner rule is already in place (repo:prototype/osfr-tools/src/housing.rs:637-685, as in correction 1). The "widen" instruction in gate 4 is no longer needed.

3. `old:` and 1 property row (`Snowhill Lodge`) has no deed.
   `new:` and 6 property rows (`Castle Test Lot`, `Chromakey Zone`, `Snow Days Lot`, `Snowhill Lodge`, `Sunstone Valley Lot`, `Sunstone Dam`) have no deed.
   `why:` repo:tests/pieces/test_piece_021.py:133-135 asserts 31 property rows and 25 rows that join a deed by `NameId`, so 6 rows have none. This also matches the top section of the note ("six rows have no deed item at all"). The Gaps bullet contradicts it.

4. `old:` a house row and a 950/855 price with **no** deed item in the dump.
   `new:` a house row and a 950/855 price with **no** deed joined by `NameId`. The Snowhill Lodge deed (12117) is in the dump but has no house row.
   `why:` repo:tests/pieces/test_piece_021.py:142-143 asserts deed 12117 is in `deeds_without_property_definition` ("the Snowhill Lodge deed has no Houses.json row"). The note's own 10-deed list also names Snowhill Lodge.

**Unsure:**
- The lab-only facts (`Houses.json`, `ClientItemDefinitions.json`, the wiki revisions, the 31/36/19/26/10 counts) were not re-derived, because `lab/` is not in the roots. I checked only the counts as asserted in the repo tests.
- The cargo and unittest result counts in the Verification table were not re-run. I checked the test declarations only: 13 `#[test]` plus one `#[ignore]` in `tests/piece_021.rs`, and 13 test methods in `tests/pieces/test_piece_021.py`.
- Outside this note: `src/restoration/piece_021.rs:8` cites `FUN_00aa8700` for the 49 constructor. The client shows `FUN_00aa86d0` (`fn` table, `0x31`), which this note has right. The Rust doc comment may need fixing.
- The Station Cash channel lists and wiki quotes were not checked. They are not code claims.
