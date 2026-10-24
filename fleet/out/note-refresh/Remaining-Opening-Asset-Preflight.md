<!-- fleet job=note-refresh id=Remaining-Opening-Asset-Preflight status=done turns=10 usd=0.0178 tokens(read,write,in,out)=[284892, 64229, 22, 13859] model=claude-haiku-5-5 -->
# notes/Research/Remaining Opening Asset Preflight.md

**Verdict:** minor drift. Most checkable claims hold at the tip. The one stale status line is the migration sentence. Most of the note's evidence lives in `../lab`, which is outside the repo and cannot be read from here, so those claims are listed as Unsure rather than checked.

**Corrections:**

- `old:` Cooking integration owns that combined new version and its separately reviewed migration.
  `new:` Cooking integration owns that combined new version. Its separately reviewed migration has already run: the farm checkpoint was migrated into the NEW file `lab/state/opening-cooking-character.json`, and only the opening content hash changed, to `3e6f4228efc76460b8b4ff5c9ecefb36264e2caf308da7d0cc7fc3ea8e34229e`.
  `why:` MODLOG.md:259 (migration entry, opening hash 3e6f…, source SHA `ab8588…`). MODLOG.md:251 (the same opening hash is the final variant, prepared before the migration). Its native Cooking win and Mae turn-in on that content are at MODLOG.md:307–319. The sentence reads as a pending future step, but the migration is already done.

**Checked and consistent (no change needed):**

- Actor count and split: `scripts/prepare-opening-content.py:79-111` defines 27 actors. The Gloam Creature is model 3933 (line 101). Artifacts are model 3934 with GUIDs 920021–920023 (lines 104–107). Copper ore is model 607 (line 97). Twenty-three actors pass, and the four remaining are the creature and three artifacts, which matches the note's split.
- Original artifact Y: the shared Y of -51.3 is at `scripts/prepare-opening-content.py:104`. The corrected Y values -51.17, -54.47 and -46.92 are at `scripts/cooking_campaign_proof.py:13-14`, and X/Z are unchanged.
- The corrections are Y-only: `scripts/cooking_campaign_proof.py:36-39` rejects any change other than Y, and the artifact goals keep `required` = 1 (`prepare-opening-content.py:142`).
- Interaction radius of 12 units: `prepare-opening-content.py:73`, and the 3D `within` check at `prototype/osfr-tools/src/opening.rs:595`.
- Repair manifest SHA `824722567c6ef6b91890a063f65fde0af4c5772162e4eee1a32e2bb10892a423`: `cooking_campaign_proof.py:11` (REPAIRS_SHA). The `rust-opening-cooking-original-assets` directory is the default output at `scripts/prepare-cooking-campaign.py:16`.
- Pinned toolkits: fr-adr-toolkit `5acfdf8d6006fa6f43d1d3605f076a6be7393e72` is in `recovery-manifest.json:101`. ForgeLightToolkit `9c06714c5d79d9152c322814bc904abad944e06e` appears in `scripts/pieces/piece_079.py:40`.
- Delivery cache: `scripts/asset_delivery.py:67-82` loads `references/asset-cache/http-raw/index.json` only in `__init__`, so new entries are seen on the next initialization, as the note says. `AssetDelivery.get` exists at line 116.
- Alternate artifact1579 (`gw_precursor_artifact_01.adr`) is referenced in `scripts/check-cooking-migration.py:73`, consistent with the "preserved as history" wording.

**Unsure:**

- "Ended native run093305 still explicitly reports unavailable artifact collision/textures." I found no `093305` run reference in the repo beyond an unrelated `20261008T093305Z` row in `notes/Research/Movement Validation.md:92`. It may live in `../lab` or the reviews.
- Every `../lab/reports` figure: the 52-file and 25-file closures, cache counts of six and 16, footprint gaps 2.67/9.04/14.56, CRCs and sizes, and the artifact floor JSON. None can be verified from the repo.
- Line 11 says "goal counts ... remain unchanged". That holds for the artifact objectives. The combined variant does change four Chef gather goals from 3 to 4 (`scripts/cooking_campaign_proof.py:52-53`). Line 3 does admit the combined version, so this may be intentional, but the wording could mislead.
- `notes/Research/Artifact3 Native Interaction Approach.md:17` gives a render Y of -47.924015 for an approach target. It is a different point from the artifact positions, so I see no contradiction, but I did not confirm it.
