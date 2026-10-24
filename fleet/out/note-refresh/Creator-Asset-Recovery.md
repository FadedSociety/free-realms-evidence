<!-- fleet job=note-refresh id=Creator-Asset-Recovery status=done turns=16 usd=0.0161 tokens(read,write,in,out)=[486271, 47564, 34, 10603] model=claude-haiku-5-5 -->
# notes/Research/Creator Asset Recovery.md

**Verdict:** minor drift. Nearly every checkable figure and path in the note still holds at the tip. Only the closing status sentence is stale, because creation was later verified natively.

**Corrections:**

- `old:` Complete native creation and appearance persistence remain pending.
  `new:` Native creation now succeeds and saves an identity through the native creator (runs `client-baseline-20261008T065152Z` and `072258Z`). Matching appearance in the opening world and restoration after restart remain pending. See [[Native Creator Delivery Proof]].
  `why:` notes/Design/Build Ledger.md:36 marks character creation "Native-verified" from runs 20261008T065152Z and 072258Z. notes/Research/Native Creator Delivery Proof.md:3 says that run "successfully created and selected" the character and proves "creation, persistence and delivery". notes/Research/Character Creation Audit.md:3 and :26 leave only opening-world appearance and restart restoration pending.

**Checked and holding (no change):**
- Launcher pin `e6a2674c516fe6062698440a1f37163132b4abca`: refs/asset-cache/cache-index.json:5 and refs/Launcher/SOURCE.json:3.
- `Server.cs` lines 465–466 download `<host>/client/<path>/<filename>` into `Client/<path>/<filename>`: refs/Launcher/src/Launcher/ViewModels/Server.cs:465-466.
- 19 custom files (one GZNE, nine GCNK, nine GCK2) under `custom/`: scripts/bundle/client_overlay.py:47-66; launcher/README.md:271.
- All 19 `http_status` 200 and `xxhash64_valid` true; none differ: refs/asset-cache/cache-index.json.
- Sizes sum to 8,070,260 bytes (the 19 `"size"` entries at cache-index lines 23–323).
- custom0_0 GCNK: 524,099 bytes / CRC 1383523233, original row 15,301 / CRC 3617083543, `original_manifest_match: false`: cache-index.json:37–50.
- `Assets_manifest.txt` CRC 123886846 / 9,479,368 bytes / SHA256 935bc0d9…: cache-index.json:12–16; notes/Research/Client Baseline.md:14. Community CRC 3387611285: cache-index.json:18.
- Flat cache and documented install path `Client/custom/`: cache-index.json:21–29 and :43.
- `[[Character Creation Audit]]` link resolves to notes/Research/Character Creation Audit.md. Its line 7 confirms the zero-row starting-set resource, and its line 9 confirms the populated community resource (413 bytes).

**Unsure:**
- The run ID `Run063016` does not match any run directory in the repo. The only match is `client-baseline-20261008T063016Z` in notes/Research/Character Creation Audit.md:7. That run is described there as the stock run that failed with `startingSetId=-1`, while line 13 says the custom files are what let zone loading reach `StartUi`. The note's sequence (custom overlay, then StartUi, then stall on the header-only starting-set table) is plausible but I could not confirm it from the repo.
- `Run061543` (HTTP 404 for the nine GCNK tiles) appears nowhere else in the repo. notes/Research/Movement Validation.md:77 has a timestamp `20261008T061543Z` in an unrelated context.
- The launcher's "Client directory as working directory" claim and the "403 on direct CDN paths" claim are about external software and traffic. I could not check them in the repo.
