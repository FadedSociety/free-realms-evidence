<!-- fleet job=note-refresh id=Pieces-062-Boss-behaviors status=nothing_found turns=19 usd=0.0177 tokens(read,write,in,out)=[594884, 47407, 40, 11617] model=claude-haiku-5-5 -->
# notes/Research/Pieces/062 Boss behaviors.md

**Verdict:** current. Every checkable claim about our code, files, test counts and the locale/client/wiki citations I tested matches the tip. No corrections.

**Checked and holding (evidence):**
- Module and test files exist at the cited paths: `prototype/osfr-tools/src/restoration/piece_062.rs`, `prototype/osfr-tools/tests/piece_062.rs`, `scripts/pieces/piece_062.py`, `tests/pieces/test_piece_062.py`.
- The `#[path]` include and the open "lead registers `pub mod piece_062;`" gate are still accurate: `prototype/osfr-tools/tests/piece_062.rs:34-36` includes the module by path, and no `mod piece_062` registration exists in `src/`.
- Test counts: 8 `#[test]` in `tests/piece_062.rs` (matches "8 passed"); 11 test methods in `tests/pieces/test_piece_062.py` (matches "Ran 11 tests").
- `advance(phase, event)` exists as a pure lookup over `PHASE_TRANSITIONS` (`piece_062.rs:461-470`). The five `*_RECOVERED` / `GR2_CLIP_DURATION_DECODED` flags are all `false` (`piece_062.rs:434-442`), matching the gaps list.
- Attack timing table: seven rows with values matching the note's table (`piece_062.rs:163-206`), including `com_h2h_attack_02` having no interrupt. Eight abilities in `ABILITIES` (`piece_062.rs:226-299`). Two missing clips listed (`piece_062.rs:411-420`), so 29/31 resolved. Bark durations 1.392 / 2.136 / 3.552 match (`piece_062.rs:395-408`).
- Checker exits with code 2 on failure (`scripts/pieces/piece_062.py:1106,1109`). The locale export path points at `lab/reports/job-catalogue-20261009T022023Z/locale-en_us.json`, the same path other pieces use.
- Community and client identity: `Resources/Models.txt:3402` maps 4220 to `necronomicus_m.adr`; `Sanctuary/src/Resources/Npcs.json:11783` carries the same file name for Necronomicus.
- Locale ids: 5100650, 5100653, 5100686/5100688/5100690, 5100693/5100695, 5100666, 5100995, 442596, 442598 (level-20 group warning), 442600, 5101015/5101016 and 5101014 all resolve to the text the note quotes. The even portal ids (e.g. 5100670) are blank.
- Wiki: `freerealms-wiki/wikitext/16394-49285-9066384514a1.wiki:9` and `18431-48953-b00c074c7c7f.wiki:8` give "Difficulty 5 - ... level 13 or higher". `16877-50130-b385ebd250b0.wiki:10` supports "is a [[Fairies|fairy]] [[Non-Playable-Character|NPC]] [[Boss|boss]]", and lines 36 and 39 support the phase sentences and the two dialogue quotes.
- Lair assets: `Assets_manifest.txt` lists `mv_necronomicus.gzne`, `necronomicus_pixie_gloam_smoke.xml` and `necronomicus_chest_beam.xml`.
- No Autopilot report changes piece 062 after its dispatch; `notes/Research/Suite Status 2026-10-13.md:171` also shows `tests/piece_062.rs` with 8 passing.

**Unsure:**
- The lab-only items (the `ap_contact` seven-value monotonicity, the 4.633334 = 139/30 frame fraction, the ambient sphere at `193,-49,252` radius 35, the `DX_*` MP3 durations and the `EndTime` values) sit in the preserved lab and the pinned readers. I could only check their presence in the client manifest, not their values.
- The "Lead integration" and "Independent review" gates describe future work. I did not check whether they had been done outside the repo.
