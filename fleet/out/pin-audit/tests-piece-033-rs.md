<!-- fleet job=pin-audit id=tests-piece-033-rs status=nothing_found turns=4 usd=0.0021 tokens(read,write,in,out)=[16486, 10300, 10, 1319] model=claude-haiku-5-5 -->
# tests/piece_033.rs

No findings in `prototype/osfr-tools/tests/piece_033.rs`. All four screened lines (225, 230, 235, 240) compare `rank_damage` against literal arrays, but those arrays are not read from `prototype/osfr-tools/data/content/*.json`.

- The values come from the `WARRIOR_SKILLS` const in `prototype/osfr-tools/src/restoration/piece_033.rs` (lines 359-382: `rank_damage: &[133, 150, 167, 183, 200]`, `&[50, 56, 63, 69, 75]`, `&[83, 94, 104, 115, 125]`, `&[50, 56, 63, 69, 75]`). The header of that file says they were recovered from the client, so they are code constants, not data-file rows.
- A search of `prototype/osfr-tools/data` for these arrays and the skill ids (24540, 4908, 24694, 24706) found only the unrelated name-id rows in `job_abilities.json` and `stores.json`. No shipped data file carries the rank damage ladders.

The tests here check the code constant, so retuning a data file would not break them. They do pin the recovered numbers, and if those constants are meant to be live-tunable, that is a separate question for the code side, not a data-file finding for this test.
