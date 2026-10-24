<!-- fleet job=note-refresh id=Client-Runtime-Dependencies status=done turns=6 usd=0.0091 tokens(read,write,in,out)=[81748, 36916, 14, 7308] model=claude-haiku-5-5 -->
# notes/Research/Client Runtime Dependencies.md

**Verdict:** minor drift. The dependency facts, the Launcher `d3dx9_31.dll` check, the Sanctuary launch arguments, and the CRC/size identity still match the tip. Two status sentences lag behind the baseline work that is now recorded in the repo.

**Corrections:**

1. `old:` The parent runner is testing a loopback HTTP service that supplies a matching CRC/size pair for the preserved archive manifest and records actual HTTP requests. Its outcome remains to be verified.
   `new:` The native harness runs a loopback HTTP service that answers `/manifest.crc` with the preserved archive manifest's own CRC/size pair and records actual HTTP requests. It ran in `client-baseline-20261008T020205Z` and `client-baseline-20261008T020419Z`, each with one HTTP 200 for `/manifest.crc`. In `client-baseline-20261021T193008Z`, 7 of 339 asset requests returned 200, including `manifest.crc`.
   `why:` `scripts/run-local-baseline.py:152-169` (the `/manifest.crc` responder built from `Assets_manifest.txt`); `notes/Research/Client Baseline.md:12-14`; `launcher/README.md:138`; `notes/Autopilot/T445.md:89`. The outcome is recorded, not pending.

2. `old:` Parent analysis is collecting actual executable import and Windows event evidence.
   `new:` Executable-import analysis identified the missing x86 `d3dx9_31.dll`. An official signed copy was then added only to disposable baseline copies, and the client reached World Ready after that step.
   `why:` `MODLOG.md:179-181`; `scripts/run-local-baseline.py:93-96` (copies `tools/directx-june2010/x86/d3dx9_31.dll` into the run copy).

**Unsure:**

- All `lab/...` artifacts cited in the note (`lab/manifests/*.json`, `lab/references/*`, `lab/runs/client-baseline-20261008T015537Z`) are outside the repo and the readable roots, so the presence table, the run exit code (27 after 51.235 s), the SHA/size figures and the `Launcher-runtime-evidence.json` copy were not verified. The repo has `refs/Launcher-runtime-evidence.json` and `refs/osfr-asset-manifest/SOURCE.json`, which exist but were not compared line by line.
- The pinned Sanctuary commit (`4f028dcc…`) cannot be checked. The unpinned copies in `refs/Sanctuary/src/Sanctuary.WebAPI/appsettings.json:9` and `refs/Sanctuary/run_client.py:26` do carry `AssetDelivery:IndirectServerAddress=http://osfr.editz.dev/assets`, as the note says.
- The community probe results (HTTP 200, `3387611285,9479368`; DNS failure for `osfr.editz.co.uk`) are dated observations. `refs/asset-cache/metadata-probes.json` exists but I did not re-read its results.
- Our own launcher's `offline_urls` point `IndirectServerAddress` at `127.0.0.1:9` (`launcher/README.md:138`). This does not contradict the note, which is about the community launcher, but it means a launcher-started client is expected to exit with code 27.
