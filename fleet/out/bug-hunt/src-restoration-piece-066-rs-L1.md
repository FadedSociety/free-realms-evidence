<!-- fleet job=bug-hunt id=src-restoration-piece-066-rs-L1 status=done turns=10 usd=0.0086 tokens(read,write,in,out)=[166673, 28112, 22, 6794] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_066.rs lines 1-662 of 662

Window reviewed: `prototype/osfr-tools/src/restoration/piece_066.rs` lines 1-662. No panic, overflow, unbounded-growth, atomicity or trust-the-client defect is reachable. The module is a read-only loader and validator for the checked-in `notes/Research/original-quest-coverage.json`. It takes no client packet input, and nothing in production code calls it. `lib.rs` does not declare `restoration`, and the only consumer is `tests/piece_066.rs`, which includes the file via `#[path]` with `#[allow(dead_code)]`. Every finding below is therefore low severity, with no remote reach.

- **[low] prototype/osfr-tools/src/restoration/piece_066.rs:44 - `MISSING_REGION_ONE_STICKERS` is documented as guarding against a later edit silently dropping the three optional stickers, but nothing reads it.**
  - Failure scenario: someone deletes the `notes/Research/original-quest-coverage.json` entries for 2572, 2573 or 2587 from `missing_originals`. `validate()` (lines 618-625) reports no error or warning for the drop, and the constant is never compared against the data. The "cannot silently drop them" guarantee does not hold.
  - Reach: no production path. The only reference in the repo is this definition (a search for `MISSING_REGION_ONE_STICKERS` returns only line 44). The test target includes the file with `#[allow(dead_code)]` and does not import the constant (`tests/piece_066.rs:32-35`).
  - Fix: in `validate()`, push an error for each id in `MISSING_REGION_ONE_STICKERS` that has no matching `missing_originals` entry with `quest_id`, or correct the doc comment to say the constant is informational only.

- **[low] prototype/osfr-tools/src/restoration/piece_066.rs:541-549 - the duplicate-id check keys on `QuestId::display()`, so `Int(n)` and `Text("n")` in the same corpus are reported as duplicates even though `QuestId`'s `Eq`/`Ord` treat them as distinct.**
  - Failure scenario: a corpus row with numeric id 2513 and a text row with id "2513" in the same source yields `duplicate quest id 2513` as an integrity error, although `quest(source, &id)` (line 416) would distinguish them. The same display-keyed grouping at lines 549 and 584-590 would also mislabel them as a shared id.
  - Reach: the checked-in catalogue has no such collision, and the module is not on any server path, so this is a false-positive error only. The inconsistency with `QuestId`'s own equality is real.
  - Fix: key `seen` and `shared` on the `QuestId` itself (e.g. `BTreeSet<(String, QuestId)>`) rather than on its display string.

No medium or high findings.
