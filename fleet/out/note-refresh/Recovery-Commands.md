<!-- fleet job=note-refresh id=Recovery-Commands status=done turns=10 usd=0.0132 tokens(read,write,in,out)=[207885, 43814, 22, 11192] model=claude-haiku-5-5 -->
# notes/Research/Recovery Commands.md

**Verdict:** minor drift. Nearly every command, script, binary, test name and path in the note still exists and matches the code. One numeric bound is wrong.

**Corrections:**

- `old:` The harness now allows 10–900 seconds for gameplay checks.
  `new:` The harness now allows 10–3600 seconds (`--seconds` is validated against that range in `scripts/run-local-baseline.py`).
  `why:` `repo:scripts/run-local-baseline.py:57-58` reads `if not 10 <= run_options.seconds <= 3600: parser.error("--seconds must be between 10 and 3600")`. A search of that script for `900` finds nothing else. `repo:prototype/osfr-tools/tests/gameplay.rs` sets no duration bound. The 900 cap also appears in `repo:prototype/osfr-tools/README.md:51` ("The duration must be 10–900 seconds"), which is stale against the script too. The README is not the note, so it is not corrected here.

**Checked and holding:**

- `osfr-tools catalog|extract` usage and the refuse-to-overwrite behaviour: `repo:prototype/osfr-tools/src/main.rs:154-180` (`create_new(true)` for the catalog; `fs::create_dir` for extract).
- `scripts/cargo.ps1` (`-CargoArgs` as a remaining-args array), `scripts/verify-soe-capture.ps1` (`-CaptureDirectory`): exist.
- `ExportNative.java` takes an output directory; `InspectNative.java` requires one new JSON path and writes it with `CREATE_NEW`: `repo:scripts/InspectNative.java:13-21`.
- Decompiler timeout of 30 seconds: `repo:scripts/ExportNative.java:39`. The 900-second analysis budget is in `repo:recovery-manifest.json:50`.
- Counts: 153,423 internal functions and 545 external functions match `repo:recovery-manifest.json:56-64`.
- `--test gateway` with `actual_original_client_capture_when_explicitly_configured` (ignored, `#[ignore]`): `repo:prototype/osfr-tools/tests/gateway.rs:478-480`.
- `--test gameplay` with `OSFR_GAMEPLAY_CONTENT` and `OSFR_GATEWAY_CAPTURE`, ignored: `repo:prototype/osfr-tools/tests/gameplay.rs:64-68`.
- `--bin soe-probe`: `repo:prototype/osfr-tools/src/bin/soe-probe.rs`.
- Baseline options `--rust-reference`, `--state-file`, `--content`, `--drop-server-sequence` (16-bit check, first-transmission drop): `repo:scripts/run-local-baseline.py:37-60` and `:368-379`.
- 8-MiB receive buffers on both sockets: `repo:scripts/run-local-baseline.py:106-109`. D3DX9_31 copied from `lab/tools/directx-june2010/x86/d3dx9_31.dll`: `:94-96`. No input automation: `:255`.
- Refuse-existing-destination in the two community wrappers (`mkdir(exist_ok=False)` / `mkdir()`): `repo:scripts/check-community-pack.py:60`, `repo:scripts/check-community-assets.py:24`. Also `repo:scripts/check-gateway-session.py:99` and `--run` at `:81`.
- Content prep scripts (`prepare-gameplay-inventory.py`, `-quests`, `-combat`, `prepare-item-categories.py`) exist and use argparse.
- Every `[[...]]` link target exists under `notes/Research/`.

**Unsure:**

- "the seven `ilspy-*.log` files" and the `ilspycmd` invocation: the logs live under `lab/`, which is outside the repo, and `recovery-manifest.json` does not list them. Not settled.
- "backs up eight INI files": `run-local-baseline.py:100-101` globs every `*.ini` in the client copy, so the count depends on the client's contents. The code does not fix it at eight. Not settled.
- Lab-only artifacts (`lab/manifests/rust-gateway-milestone.json`, `lab/references/...`, the completed run directories, the 1-minute walking check authorisation) cannot be checked from the repo.
