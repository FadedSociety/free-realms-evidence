<!-- fleet job=note-refresh id=Pieces-074-Collections-and-collectibles status=done turns=15 usd=0.0162 tokens(read,write,in,out)=[416731, 46141, 32, 12613] model=claude-haiku-5-5 -->
# notes/Research/Pieces/074 Collections and collectibles.md

**Verdict:** minor drift. The Rust module, its test counts, the category table, the error set and the exactly-once completion all match the tip. The two "remaining gates" about integration and the server-side packets are out of date, because `progression_extras.rs` now wires the ledger in and encodes the collection packets.

**Corrections:**

1. `old:` Lead integration: register `piece_074` in `prototype/osfr-tools/src/lib.rs` and drop the `#[path]`
   include from `tests/piece_074.rs`. Nothing else in the shared crate needs to change.
   `new:` Lead integration: the module is already compiled into the crate through `prototype/osfr-tools/src/progression_extras.rs`, which has its own include (`#[path = "restoration/piece_074.rs"] mod collection_ledger;`) and re-exports `CollectionLedger`, `CollectionCatalogue` and related types. `src/lib.rs` still has no `piece_074` entry. The remaining step is to drop the `#[path]` include from `tests/piece_074.rs` and import from the library. Whether `lib.rs` also gets a direct registration is for the lead to decide, but the shared crate already depends on this module.
   `why:` repo:prototype/osfr-tools/src/progression_extras.rs:21-25 (the `#[path]` include and re-export); repo:prototype/osfr-tools/src/lib.rs:71 (only `pub mod progression_extras;`, no piece_074 entry); repo:prototype/osfr-tools/tests/piece_074.rs:35-40 (the test still includes the file by `#[path]`); repo:notes/Research/Collections Achievements Titles.md:70 (says progression_extras reuses the Piece 074 ledger).

2. `old:` but no server-side sender and no
   `new:` but the only server-side encoder is `CollectionMessage::encode` (family 38, subtypes 8–11), which lives in `progression_extras.rs` and is called only from `CollectionProgression::collect`, and no routed sender reaches it; and no
   `why:` repo:prototype/osfr-tools/src/progression_extras.rs:410-463 (encoder for Start, Remove, AddEntry, RemoveEntry), 533-542 (AddEntry packet built into `collection_packets`); a search of `prototype/osfr-tools` finds `CollectionMessage` and `CollectionProgression` only in `progression_extras.rs` and its test, and the Build Ledger row for this system reads "Not routed" (repo:notes/Design/Build Ledger.md:97).

**Unsure:**

- `Interface: collection progress has no owner yet for the character save document.` `progression_extras.rs` has a `CollectionProgression` that holds the catalogue and ledger and exposes `ledger_bytes()` and `from_ledger_bytes()` (lines 489-513). Its comment says "Caller saves the ledger and RewardState in the same character transaction" (line 554). I found no character-save caller in `src/`, so the claim may still hold. I could not settle it.
- Checked and consistent: the seven `#[test]` functions in `tests/piece_074.rs` (the note says 7 passed); the 20 `def test_` functions in `tests/pieces/test_piece_074.py` (the note says 20 passed); `scripts/pieces/piece_074.py` and `tests/pieces/test_piece_074.py` exist; the `Ninja Dolls` exception is in `scripts/pieces/piece_074.py:157`; the category table rows, the error variants, the `MAX_LEDGER_*` bounds and the exactly-once `completed.insert` logic match `src/restoration/piece_074.rs:34-339`. The client-side claims for `FUN_009fce20` (returns 3), `FUN_009fce30` (three column names) and `FUN_009fd050` (`% 10`) match the decompile, and `DS_COLLECTIONS = 30` / `DS_COLLECTION_REWARD_ENTRIES = 33` match `ui:ScriptsBase.lua:4824,4827`. The `lab/reports/...` artefacts, the wiki counts (240 names, 100 sets, 44 cascade notes) and the RED log are outside the repo, so I did not check them.
