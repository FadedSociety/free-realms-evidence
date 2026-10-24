<!-- fleet job=pin-audit id=tests-piece-013-rs status=nothing_found turns=2 usd=0.0011 tokens(read,write,in,out)=[1997, 5001, 6, 967] model=claude-haiku-5-5 -->
# tests/piece_013.rs

No findings in `prototype/osfr-tools/tests/piece_013.rs`. All five screened lines pin values from Rust constants in `prototype/osfr-tools/src/restoration/piece_013.rs`, not from a shipped data file under `data/content/`:

- Line 47 (`copper.measure_percent == 65`) and line 51 (`ORES[4].measure_percent == 85`): `ORES` table literals at src/restoration/piece_013.rs:53 and :81.
- Line 55 (`FURNACE.spill_data == 2.5`): src/restoration/piece_013.rs:107. The generator `scripts/pieces/piece_013.py:145` also sets it, but that is a script, not a data file.
- Line 56 (`HEAT_FURNACE.gain_max == 30.0`): src/restoration/piece_013.rs:123.
- Line 58 (`GAME_WON_QUANTITY_LITERAL == 10`): src/restoration/piece_013.rs:31.

A repo-wide search found none of these fields or values in `data/content/*.json`. These are recovered-definition constants in code, so they are outside the rule that gameplay tunables live in data files. Retuning them would not break the test while the code is still right by the team's data rule. Whether they should move into data is a separate question, not a finding here.
