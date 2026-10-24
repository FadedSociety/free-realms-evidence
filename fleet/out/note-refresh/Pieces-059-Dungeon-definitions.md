<!-- fleet job=note-refresh id=Pieces-059-Dungeon-definitions status=nothing_found turns=14 usd=0.0144 tokens(read,write,in,out)=[362637, 49369, 30, 9189] model=claude-haiku-5-5 -->
# notes/Research/Pieces/059 Dungeon definitions.md

**Verdict:** current. Every code, file, count and status claim I could check at the tip matches the repo, and I found no false statement that needs a correction.

**Checked and holding:**
- Artifacts exist at the cited paths: `prototype/osfr-tools/src/restoration/piece_059.rs`, `prototype/osfr-tools/tests/piece_059.rs`, `scripts/pieces/piece_059.py`, `tests/pieces/test_piece_059.py`. The Rust test file uses a `#[path]` include (`tests/piece_059.rs:18-20`), and `src/lib.rs` does not register the module, which matches the "lead owns registration" text.
- Rust acceptance tests: 11 `#[test]` functions (`tests/piece_059.rs`, lines 28-209).
- Python checker tests: 10 `test_` methods, including the four hard-failure cases (`tests/pieces/test_piece_059.py:205, 223, 236, 251`).
- Checker error names `DeclaredZoneMissing` and `ObjectiveNameMismatch` exist (`scripts/pieces/piece_059.py:425, 492`).
- Roster: 43 rows, 2 removed, difficulty membership `[8, 8, 9, 9, 9]` (`piece_059.rs:39, 137-180`).
- Entry rule: 1 open, 2 recommends level 3, 3/4/5 require levels 5/9/13 (`piece_059.rs:261-285`).
- Achievement block: ids 30439-30475 with 37 bound rows. The gaps are Bixie Hive, Cursed Graveyard!, Sandscale Oasis and Precursor Ruins, plus the two removed rows (`piece_059.rs:138-180`).
- Entrance gaps: Precursor Ruins and Treeleaf's Retreat have no entrance, so 41/43 (`piece_059.rs:170, 177`).
- Zone table: all 14 `Z(...)` rows match the note's stems, `*.gzne` bytes, chunk counts and chunk bytes (`piece_059.rs:138-179`). Den of Secrets is a stub (`piece_059.rs:148`).
- `REGIONS` has 13 entries (`piece_059.rs:119-133`).
- `ZONE_STUB_LIMIT = 84` (`piece_059.rs:29`).
- Terrain: `Resources/ObjectTerrainData.xml` has 34 rows, and only id 87 `DenOfSecrets` is a dungeon (`client:Resources/ObjectTerrainData.xml:34`).
- Locale spot-check: the "Complete the" rows match the roster names, including the doubled-article `The Bat Cave!` at 30449 and the doubled space at 30456 (`locale` tool).
- Cross-links resolve: `notes/WorkItems/059.md` and `notes/Research/Starting Dungeon Audit.md`, `Original Activity Coverage.md` and `Wiki Research Database.md` all exist. (`Research/Pieces/` is a directory of its own, so the `../` links from the note resolve as written.)
- No Autopilot report changed piece_059 after the note was written. `notes/Autopilot/L030.md:42` only cites `piece_059::ZONE_STUB_LIMIT`, which still exists.

**Unsure:**
- The lab bundle `../lab/reports/piece-059-20261009T054317Z/` (`dungeons.json`, `provenance.json`, `red-evidence.txt`, `checker.log`, `python-tests.log`, `rust-tests.log`) lies outside the readable roots, so I could not confirm it exists. The `piece 059 evidence ok: 43 dungeons, 14 recovered zone maps, 29 zone gaps` and `Ran 10 tests` / `11 passed` outputs are also unverified: I did not run them.
- The note's Verification paragraph calls the fourth hard-failure case "an unreadable evidence file". The checker test at `tests/pieces/test_piece_059.py:251` is named `test_missing_evidence_file_is_a_hard_failure`. This is only a wording difference, and I did not read the test body to settle which case it exercises.
- Wiki page facts (the 43-row roster, the "(removed)" marks, the entry sentences) and the pack catalogue byte counts are original-data claims that I did not re-check against the refs corpus.
