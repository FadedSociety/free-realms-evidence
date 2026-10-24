<!-- fleet job=pin-audit id=tests-piece-036-rs status=nothing_found turns=5 usd=0.0045 tokens(read,write,in,out)=[43053, 23772, 12, 2197] model=claude-haiku-5-5 -->
# tests/piece_036.rs

No findings in `prototype/osfr-tools/tests/piece_036.rs` for the six screened lines. None of the expected numbers is read from a shipped data file under `data/content/*.json`, and the test file does not pull them from one.

- **Lines 97-99** (`WIZARD_BASIC_RECAST_MS` 600, `WIZARD_ENERGY_MAX` 100, `WIZARD_ENERGY_REGEN_PER_SECOND` 4): these are `pub const` values in `src/restoration/piece_036.rs` (lines 71-75), tagged COMMUNITY-RECOVERED. The test imports them, so it reads the code constant, not a data row. No `data/content` file holds these fields. `scripts/pieces/piece_036.py` also compares against `WIZARD_ENERGY_MAX` in code.
- **Line 112** (`fallback.damage` 200): a literal in the `WIZARD_ABILITIES` table in `src/restoration/piece_036.rs` (line 121). It is code, not data. The same literal at line 181 is also not from data.
- **Lines 124** (`zap.damage` 279) and **133** (`blast.damage` 1143): these are assertions against `STUDENT_WIZARD_WAND_ZAP_DAMAGE` and `STUDENT_WIZARD_WAND_LIGHTNING_BLAST_DAMAGE` (code constants, src lines 89 and 91), with the literal repeated. The matching 279/1143 values in `data/reference/weapons.json` are other weapon rows and are not what this test reads. `data/content/combat_scale.json` mentions 279 only in evidence text.

These are code constants, which the test reads through the imported names. Retuning a `data/content` value would not break them. Whether these code constants should move into a data file is a separate question outside this audit.
