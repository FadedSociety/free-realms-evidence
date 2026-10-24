<!-- fleet job=note-refresh id=Toolbox status=nothing_found turns=9 usd=0.0064 tokens(read,write,in,out)=[126386, 23764, 20, 4270] model=claude-haiku-5-5 -->
# notes/Research/Toolbox.md

**Verdict:** current. Every claim about our code in `notes/Research/Toolbox.md` checks out at the tip. The rest of the note describes the author's private machine (skill packs, app versions, `C:\Users\...` and `lab/tools` installs, checksums) and cannot be checked against the repo, so I left it alone.

**Checked against the tip (all hold):**
- Rust gateway crates (last paragraph): `prototype/osfr-tools/Cargo.toml:11-13` declares `serde` (derive), `serde_json`, and `sha2 = "0.10"`. `Cargo.lock` at `prototype/osfr-tools/Cargo.lock:248, 278, 291` locks `serde`, `serde_json`, and `sha2`.
- `sha2` is used for template integrity in `prototype/osfr-tools/src/combat.rs:9` and `:111`, where `template_sha256` is compared.
- `serde`/`serde_json` are used for character-save documents in `prototype/osfr-tools/src/character_store.rs:14, 76, 98`, and for bounded reference content in `src/content.rs:4-5`.
- `scripts/run-local-baseline.py:37-38` defines `--rust-reference` and `--state-file`. Line 117 points at `target/release/osfr-gateway.exe`, which matches "against the release Rust binary".
- `scripts/check-gateway-session.py` exists. It needs `--run` (line 81) and launches `osfr-gateway.exe` (lines 84, 124), not the game. Its checks cover rejected replacement and different-seed replacement sessions (lines 166-185). That matches "without launching the game".
- `project/scripts/cargo.ps1` maps to `scripts/cargo.ps1`. It sets `CARGO_HOME` and `RUSTUP_HOME` under `lab/tools` (lines 3-5).
- `setup-manifest.json` exists at the repo root.
- The linked notes `Rust Gateway Milestone`, `Universal Modder Assessment`, and `Community Asset Validation` all exist in `notes/Research/`.

**Unsure:**
- `lab/manifests/client-directx-runtime.json` and `lab/references/SOURCE.json` live in the private `lab/` tree, which is not in this repo, so I could not verify them.
- The skill and app version counts (Ponytail six skills, Caveman 22, Universal Modder eleven) and the tool versions are not visible from the repo.
