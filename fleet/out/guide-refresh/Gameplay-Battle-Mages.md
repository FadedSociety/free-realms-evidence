<!-- fleet job=guide-refresh id=Gameplay-Battle-Mages status=done turns=24 usd=0.0398 tokens(read,write,in,out)=[1323302, 93117, 52, 29790] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Battle Mages.md

**Verdict:** minor drift. The code-side claims hold at the tip. The asset claims are off, and some citations point at a file that is not in our tree.

**Corrections:**

1. `old:` has twelve files whose names start `test_bm_`
   `new:` has nineteen files whose names start `test_bm_`: the `.adr`, `.cdt`, `.dma` and `.dsk` set for each of the three flags (twelve files), plus `.dds` and `.dme` for each flag, and `test_bm_capflags_bbe.gr2`
   `why:` the asset manifest lists 19 `test_bm_` rows, `Assets_manifest.txt:46111-46129` and `:46117` (refs, osfr-asset-manifest). The "twelve" figure is correct only for the four-extension subset.

2. `old:` (the only asset names are `test_bm_*flag_bbe`, see Data and formats)
   `new:` (the asset names are `test_bm_*flag_bbe` plus `test_bm_capflags_bbe.gr2`, see Data and formats)
   `why:` `Assets_manifest.txt:46117`. The `*flag_bbe` glob does not match `capflags_bbe`, so the Overview's "only" is false.

3. `old:` The only other flag-like evidence is the `test_bm_*flag` assets.
   `new:` The only other flag-like evidence is the `test_bm_*flag` assets and `test_bm_capflags_bbe.gr2`, a capture-flag asset that sits closer to the "Capture The Flag Trophy" lead.
   `why:` `Assets_manifest.txt:46117`.

4. `old:** [Assets] ... manifests/rust-asset-catalog.tsv` (the citation in the Asset names paragraph)
   `new:` cite `osfr-asset-manifest/Assets_manifest.txt` (the copy in our refs), or keep the lab path and mark it as the author's copy.
   `why:` `rust-asset-catalog.tsv` is not in our refs or repo; only `Assets_manifest.txt` carries the `test_bm_` rows (`refs`, `Assets_manifest.txt:46111-46129`).

**Checked and holding (no change):** the processor roster size of 8 and the slot check `< 8` (`00b71200`, `00b71bd0`); `00b728a0` dispatch cases 2, 4, 6, 8, 0xb, 0xc, 0xd (no sub 5); `00b72f60` callers are only `0092f460` and `0093d180`; the bit-21 check at `+0x6f8` and the `+0x124` processor test in `0092f460`; `00af8df0` returns 0x11; `00b6f2b0` writes family 0x85; `00b70ad0` walks `+0x40` and `+0x30`; the `+0x29` barrier read in `00936d00`; `00cd5b90` registers `bm_reloaddata` (1) and `bm_camera` (2); the `00cd69e0` type-1 gate matches `00cd62c0`; the `00b72e80` caller is `00af9590`; `00cd51b0` gates on `+0x280`; the label confidences in the Key functions table and the generated section; the 88 / 36 / 13 / 25 / 14 counts (minigame.battlemages 48 plus net.battlemages 40, label table).

**Unsure:**
- The locale numeric ids in the note (`2035897657`, `2294936351`, `4286859379`, `313654616`, `1631681041`, and the Bixie ids) do not resolve in the locale tool ("no such id"). The tool resolves "Battle Mage" to 403033 and "Battle Mage Gear" to 403032, and only one "Battle Mage" entry appears, so "two entries" is unconfirmed. The note's ids may be a different hash scheme.
- "783 rows" in `MiniGameData.txt` could not be checked: no `MiniGameData` file was found under `client`.
- "251 matches for 'mage'" in `ScriptsBase.lua` was not counted. The `battlemage` and `bm_` no-match claim holds.
- Camera defaults from `0107b840`: the pitch multipliers read `DAT_01ba2de8` times three different constants (`_DAT_017f1d54`, `_DAT_01883774`, `_DAT_01883770`), not "30, -56.25, +56.25 times 0.0174533". I did not read the data bytes to confirm the constant values.
- Byte-level claims (`ret 4` in `00b72e80`, `DAT_017ea5a4` = negative zero, the 57.2958 constant) were not checked.
