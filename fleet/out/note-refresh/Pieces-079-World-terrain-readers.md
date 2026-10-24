<!-- fleet job=note-refresh id=Pieces-079-World-terrain-readers status=done turns=11 usd=0.0161 tokens(read,write,in,out)=[301755, 59302, 24, 11250] model=claude-haiku-5-5 -->
# notes/Research/Pieces/079 World terrain readers.md

**Verdict:** minor drift. The inventory counts, reader window, abort numbers, file paths, the "awaiting lead registration" status and the reproduce commands all match the tip. One statement is stale: the `.cdt` containers are no longer wholly unread in our code. A first-party prefix parser exists.

**Corrections:**

1. `old:` `and **2,743 `.cdt`** (all `CDTA`). No community reader for either was found`
   `new:` `and **2,743 `.cdt`** (all `CDTA`; the first-party `CdtaMesh::parse` reads the container prefix, tail undecoded). No community reader for either was found`
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_064.rs:80-96` defines `CdtaMesh` ("Parsed CDTA container prefix ... `tail_len` records the bytes this reader deliberately does not decode") and `CdtaMesh::parse` checks the `CDTA` magic and version 1. Its header (lines 1-34) states the bytes after the prefix stay unparsed.

2. `old:` `* Still-unread preserved world formats, header-triaged here:`
   `new:` `* Preserved world formats not decoded past the header, header-triaged here (the `.cdt` prefix is parsed first-party, see piece_064 below):`
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_064.rs:1-2,36-39,80-96` (prefix-only CDTA reader, `CDTA_VERSION = 1`).

3. `old:` `| GZNE (174) / CDT (2,743) containers | header triage only | unread; no community reader found |`
   `new:` `| GZNE (174) / CDT (2,743) containers | header triage only; CDT prefix parsed first-party by `piece_064.rs` `CdtaMesh::parse` (tail undecoded) | GZNE unread; CDT tail open; no community reader found |`
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_064.rs:80-96`. The GZNE part still holds: no GZNE parser exists in `prototype/osfr-tools/src` beyond the zone-header facts in `restoration/piece_059.rs:17-19`.

**Checked and holding (no change):**
- `src/restoration/piece_079.rs` exists. Its constants match the note: 2,344 chunks, 8 placeholders, histogram 2/51/35/1,122/1,126, pinned survey 2,277 ok and 67 failed, 59 aborts, 47 recovered (32 v3 + 15 v4), 2 complete v4, 12 residual, 15 short parses, 2 pinned-ok short parses (`piece_079.rs:47-87`). Pinned window 0..=6 is at `piece_079.rs:51-54`. `COLLISION_DECODED` and `DETAIL_MASK_DECODED` are false (`piece_079.rs:56-59`).
- `tests/piece_079.rs` exists and `#[path]`-includes `src/restoration/piece_079.rs` (lines 10-12, 18-19). Its header says the module is not yet registered in `src/lib.rs`. `lib.rs` has no `restoration` or `mod piece` reference, so "awaiting lead registration" is accurate.
- `scripts/pieces/piece_079.py` and `tests/pieces/test_piece_079.py` exist. The checker returns exit 2 on `EvidenceError` (`piece_079.py:927-929`).
- `notes/WorkItems/079.md` lists the same committed paths.

**Unsure:**
- The `../lab/...` artifacts (survey JSONs, sha256 values, `GcnkFile.cs` line numbers, `RuntimeObject.cs:70`, the variant recovery counts, and the 13/12 v4 splits) live outside the repo. I could not verify them. The chunk names `pack_10/000820.gcnk` and `pack_21/003752.gcnk` do appear in `tests/pieces/test_piece_079.py:202,259`, consistent with the note.
- I did not check whether the `ForgeLightToolkit` pin or the `soir20` and `psemu` community-tool claims hold. They are external.
