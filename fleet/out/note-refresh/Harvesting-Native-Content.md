<!-- fleet job=note-refresh id=Harvesting-Native-Content status=done turns=11 usd=0.0127 tokens(read,write,in,out)=[170807, 34959, 24, 13310] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Native Content.md

**Verdict:** minor drift. The core claims hold at tip: `harvesting::write_content(dir, game_id)` exists (`repo:prototype/osfr-tools/src/harvesting.rs:1044`), the `harvesting.json` values match the tip copy (game 111, profile 45, outputs `[2885, 2887, 2890, 2877]`, quota 15 / per_reward 5, `reconstructed_rules: true`; `repo:prototype/osfr-tools/data/content/harvesting.json:3-9, 195-224`), and the conflicting-duplicate refusal still exists. Four citations or wordings are stale.

**Corrections:**

1. `old:` `` `src/inventory.rs:170` ``
   `new:` `` `src/inventory.rs:404` `` (in `Inventory::parse_content`, reached from `Inventory::load` at `src/inventory.rs:365`)
   `why:` `repo:prototype/osfr-tools/src/inventory.rs:403-405` holds the `conflicting inventory definition` check. Line 170 no longer contains it.

2. `old:` `37 identical / 1 modified (`content/inventory.json`) / 3 added; all 38 frozen source files re-hashed unchanged`
   `new:` `41 content files plus the `STAMP.txt` marker (42 files): 37 identical / 1 modified (`content/inventory.json`) / 4 added (`STAMP.txt`, `content/harvesting.json`, `harvesting-content-proof.json`, `harvesting-receipt.json`); all 38 frozen source files re-hashed unchanged`
   `why:` `repo:notes/Reviews/Harvesting Native Content Review.md:35` and `:64-68`. The review's re-derivation found 42 candidate files with 4 added, and says the builder's `file-proof.json` records `added: 4`. The note's count leaves out `STAMP.txt`.

3. `old:` `exactly as
the cooking and forging supplements were built.`
   `new:` `with `IconData` normalized to `{Id, TintId: 0}`, because the stock `prepare-opening-base.py legacy_definition` path raises `KeyError: 'TintId'` on these catalog rows. The cooking row 35 precedent reproduces under the same normalization.`
   `why:` `repo:notes/Reviews/Harvesting Native Content Review.md:69-74`. The note implies an unmodified helper ran, but the invoked chain normalizes `IconData`.

4. `old:` `stores `MinProfileRank=1`/`ResellValue=0`, while the supplied sibling rows carry`
   `new:` `yields `MinProfileRank=1` and no stored `ResellValue` (it defaults to 0), while the supplied sibling rows carry`
   `why:` `repo:notes/Reviews/Harvesting Native Content Review.md:79-82`. `ResellValue` is not a stored catalog value for 2885/2890. Searching `repo:prototype/osfr-tools/src` finds no `ResellValue` at all.

**Unsure:**

- **Commands (line 70):** `cargo run --bin write-harvesting-content` and `cargo test --test package_preflight` do not exist in `repo:prototype/osfr-tools`. `src/bin/` holds only `osfr-*.rs`, `soe-probe.rs` and `osfr_gateway/`, `Cargo.toml` declares no `[[bin]]`, and `tests/package_preflight.rs` is absent. The review says the builder's 4-test probe lives under `lab/reports/harvesting-native-content-20261009T132512Z/probe` (`notes/Reviews/Harvesting Native Content Review.md:46-49`), so these commands may point at a lab-only crate. I could not check the lab tree.
- **"goals 601..604" (line 53):** the tip copy `data/content/harvesting.json` has goal values 411/413/416/403 (lines 165-194) and no 601..604 anywhere. The review says 601..604 are the collectable tile ids in the package copy. The package copy is outside the repo, so the tip copy cannot confirm the package's `harvesting.json` byte count (3734) or sha256 (`280f5cd7…`).
- **Frozen source hashes (lines 6-8):** I did not hash the repo files. They are history at freeze time, and `harvesting.rs` has moved since (e.g. `notes/Research/Harvesting Native Launch Preflight.md` cites `4e5196ba35ab99c6`). I left them alone.
- **Superseding note:** `notes/Research/Harvesting Native Content v2.md` and `notes/Reviews/Delegated Task Readiness.md:9` describe v2 package `opening-harvesting-native-20261009T142624Z` (11x11 padded, 90 playable cells, drop row 10). This note does not mention it. That is a missing pointer, not a false claim, so I did not record it as a correction.
