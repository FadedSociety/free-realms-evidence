<!-- fleet job=note-refresh id=Native-Asset-HTTP-Delivery status=nothing_found turns=13 usd=0.0143 tokens(read,write,in,out)=[331554, 48778, 28, 9863] model=claude-haiku-5-5 -->
# notes/Research/Native Asset HTTP Delivery.md

**Verdict:** current. Every checkable claim about our code and the pinned native and Sanctuary evidence I could reach still holds at the tip. No corrections.

**Checked and holding:**
- `scripts/check-native-asset-envelope.py` exists (line 13 defines `MAGIC`; `--expected-raw`, `--expected-crc` and `--self-test` are all present, lines 36-48).
- The self-test rejects exactly seven variants, matching the note's "seven invalid variants": bad_magic, wrong_decoded_length, truncated, trailing, bad_zlib_checksum, bare_zlib, raw_deflate (`scripts/check-native-asset-envelope.py:55-63`).
- The checker does not start a server or modify client files; it only reads its inputs (whole file).
- Wire format: `scripts/asset_delivery.py:150` writes `>II` magic + raw length + `zlib.compress(raw, 6)`, matching the note's construction. `tests/test_asset_delivery.py:30,50` checks the same header.
- Native functions the note cites exist in the client decompilation: `FUN_010ebd70` (requires `8 < len`, magic `0xA1B2C3D4`, returns bytes 4..7), `FUN_010ebee0` (passes `input+8` and `length-8`, zlib version string `"1.2.3"`), `FUN_010ee080` (calls the inflate init with window bits 0xf = 15), and `FUN_01099fd0` (DecompressJob). Checked via `client_sql` `fn.c`.
- Sanctuary `ZLib.cs` (`refs:Sanctuary/src/Sanctuary.Core/IO/ZLib.cs:55-92`) has the `0xA1B2C3D4` magic check, the big-endian length read, and the 8-byte skip.
- The 12-byte table value `0090A4C8` equals 9,479,368, the declared length.
- The row size equals the wire envelope length: `scripts/check-asset-delivery-scenes.py:82` asserts `manifest_wire_bytes == record["size"]`, consistent with the note's "row's size is the compressed response-envelope size."
- The failing `human_m_head_caucasian_08` request is still recorded as failing (`notes/Research/Character Creation Audit.md:30`, `notes/Research/Pieces/049 Character appearance coverage.md:75`). No Autopilot report resolves it.

**Unsure:**
- Line 59 says "serve through the existing loopback asset handler." There are two loopback handlers, and they differ in ways the note doesn't say:
  - `launcher/src/assets.rs:150-176` serves files from `<client>/indirect-assets/` byte for byte. It ignores the `?crc` query and does no CRC/SHA check, and it does no envelope wrapping. The wrapped `.z` must already be on disk, as its own doc comment says (`launcher/src/assets.rs:21-23`).
  - `scripts/asset_delivery.py:116-170` is the harness handler. It does what the note's recommendation on line 19 asks for: it allowlists manifest-CRC-matching catalog names, requires `query == expected CRC` (line 127), checks source SHA/CRC (lines 144-145), wraps raw to envelope (line 150), and records proofs with SHA256.
  - The note's "should resolve only allowlisted verified catalog names, check the requested CRC … retain SHA256 provenance" is a recommendation, not a status claim, so I left it. It is true of the harness but not of the launcher responder. If the integration step means the launcher, the note needs a qualifier.
- Not verifiable from the repo: the `lab/reports/*` evidence, the public-manifest probe values (timestamp, 2,229,472 bytes, SHA256s), the Python zlib 1.3.2 re-encoding claim, the 8921 → 8929 size arithmetic, and the exact pseudocode line numbers (2574099, 2574162, 2575309, 2508093). The `fn` table has the functions but not the external line numbering.
- The note's "CRC123886846" (line 42) is probably a missing space ("CRC 123886846"). It matches `notes/Research/Creator Asset Recovery.md:13`, so I left it alone.
