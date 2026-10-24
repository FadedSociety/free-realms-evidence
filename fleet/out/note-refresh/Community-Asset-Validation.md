<!-- fleet job=note-refresh id=Community-Asset-Validation status=nothing_found turns=9 usd=0.0122 tokens(read,write,in,out)=[180172, 51478, 20, 7873] model=claude-haiku-5-5 -->
# notes/Research/Community Asset Validation.md

**Verdict:** current. Every checkable claim I could reach matches the tip. No corrections.

**What I checked (all hold):**
- `scripts/check-community-assets.py` exists. It imports `AdrFile`, `DmaFile`, `DmeFile`, `DskFile` from the pinned toolkit (line 18). It maps references through `catalog.tsv` (lines 21-27). It asserts finite positions and in-range indices (line 39). It renders a static textured preview (lines 40-62). Output goes to `lab/extracted/community-asset-check` (line 23). `output.mkdir()` without `exist_ok` refuses to overwrite (line 24), which matches "deliberately protected against overwrite". The `report.json` limitations say "Static pose preview; animation not tested" and "No new binary format parser written" (lines 78-79).
- Toolkit pin `5acfdf8d6006fa6f43d1d3605f076a6be7393e72` matches `recovery-manifest.json:101` and `MODLOG.md:560`. The toolkit `LICENSE` is AGPL-3.0 (`refs:fr-adr-toolkit/LICENSE:1`, `fr-adr-toolkit/README.md:118`).
- Chatdy numbers (4,256 vertices, 6,317 triangles, 92 bones, 32 slots) match `MODLOG.md:560` and `notes/Research/Edenfps Toolkit and Sanctuary Branch Review.md:21`. Warpstone 998 vertices / 978 triangles also match those two sources. "DMOD v3" matches the Edenfps note.
- Actor dependencies `treeble.dsk`, `chatdy_lod0.dme`, `chatdy.dma` match `refs:fr-adr-toolkit/ASSET_FORMATS.md:28-31`. `CHATDY.DDS` matches `notes/Research/Pieces/098 Rust rendering/client feasibility.md:86-87`.
- 52-byte vertex stride is the toolkit's supported ClrNrmUVSkin layout (`refs:fr-adr-toolkit/fr_formats/dme.py:94`, `dme.py:29`).
- Pack claims: `scripts/check-community-pack.py` runs the DbgPack/ForgeLight Toolbox extractor, compares names, offsets, lengths, CRC-32 and SHA-256 with the Rust catalog, and writes `lab/manifests/community-pack-check.json` (lines 34-92). `prototype/osfr-tools/README.md:106` says all 24 supplied packs were extracted and CRC-checked. `MODLOG.md:174` gives 6,074 entries / 45,765,884 bytes.
- `AGENTS.md:26` is the project instruction the note cites ("search existing community tools and XeNTaX/ZenHAX/QuickBMS research").
- The `[[Universal Modder Assessment]]` link resolves to `notes/Research/Universal Modder Assessment.md`. The `..\lab\tools\universal-modder-env\Scripts\python.exe` reproduction command follows the convention used across `notes/Research/Recovery Commands.md:55`.
- "No GZNE reader ... established" does not conflict with `notes/Current Progress.md:198`, which says no custom GZNE parser is needed for scene loading. That is a separate claim.

**Unsure:**
- Line 13 says "Only source/documentation was fetched." `MODLOG.md:560` says the full toolkit was downloaded and inventoried later, and the Edenfps review says "Downloaded templates and script bundles stay lab-only." That is a later fetch, so the original claim may still be accurate for the 2026-10-08 session. I could not verify the fetch history from the repo alone.
- The BMS host "was unavailable" and the XeNTaX/ZenHAX citations are external history. I could not check them here.
- The `chatdy-preview.png`, `report.json`, and "default completed output already exists" are in the lab, outside the repo. I could only confirm them through `MODLOG.md` and the code, not the files themselves.
