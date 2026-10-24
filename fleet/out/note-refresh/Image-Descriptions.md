<!-- fleet job=note-refresh id=Image-Descriptions status=done turns=8 usd=0.0107 tokens(read,write,in,out)=[99949, 41147, 18, 9070] model=claude-haiku-5-5 -->
# notes/Research/Image Descriptions.md

**Verdict:** minor drift. The pipeline, layouts, UI-name rule, search flags and counts match the tip. Two statements about file locations are wrong, plus one detail about icon selection.

**Corrections:**

1. `old:` Each `*.txt` lists the cells.
   `new:` `index.json` (one file for the whole run) lists each sheet's cells, with the source path of every cell.
   `why:` `repo:scripts/image_sheets.py:6` (docstring: "Writes sheets plus index.json (sheet -> cells -> source file)"), and `repo:scripts/image_sheets.py:97` writes `out / 'index.json'`. The script writes no per-sheet `.txt` files.

2. `old:` 1. `fl_pack.py` (with `lab/references/dbg-pack` on `PYTHONPATH`) unpacks all 22 packs to `lab/extracted/named/` (3.0 GB).
   `new:` 1. `lab/references/forgelight-toolbox/FLUtils/fl_pack.py` (with `lab/references/dbg-pack` on `PYTHONPATH`) unpacks all 22 packs to `lab/extracted/named/` (3.0 GB).
   `why:` `repo:scripts/check-community-pack.py:28` (`toolbox = lab/references/forgelight-toolbox`), `:61` (`tool = toolbox / "FLUtils" / "fl_pack.py"`), `:63` (`PYTHONPATH` = dbg-pack). `lab/extracted/named` is the path in `repo:scripts/build_asset_graph.py:39`. The "22 packs" claim holds: the client root has `Assets_000`–`Assets_009` (10) plus `AssetsW_000`–`AssetsW_011` (12), i.e. 22 `.pack` files (`client` root listing).

3. `old:` Each icon appears once, at its largest size variant (`_32/_64/_128` are merged).
   `new:` Each icon appears once, at its largest file (by bytes) among its size variants (`_32/_64/_128` and other size suffixes are merged).
   `why:` `repo:scripts/image_sheets.py:18` (SIZE_SUFFIX covers 16 to 512) and `:42-45` (the keeper is chosen by `path.stat().st_size`, not pixel size).

**Checked and holding:**
- Icon layout 4×4 at 192 px, UI 2×2 at 384 px (`repo:scripts/image_sheets.py:20`).
- UI name rule `^(ui|hud|loading|emblem|portrait|enc|minigame|notification)|_notification|loading` (`repo:scripts/image_sheets.py:19`).
- Search script path, index file name and the `--kind`, `--masks` flags, with mask/silhouette hidden by default (`repo:scripts/image_search.py:7-9, 29`).
- Coverage arithmetic: 552 + 12,761 = 13,313. Sheets: 552/4 = 138 UI sheets, ceil(12,761/16) = 798 icon sheets, total 936, matching the note.
- The `lab/reports/image-descriptions/index.jsonl` output path (`repo:scripts/image_search.py:15`).
- The `project/` prefix is correct: the repo root is `project`, with `lab` as its sibling (`repo:scripts/check-community-pack.py:25-26`).

**Unsure:**
- The kind counts (4,745 mask, 2,689 clothing, and so on), the 552 / 12,761 / 13,313 totals as data, "Ten Sonnet agents", "about 3M tokens" and "~50,000 world and model textures". These live in the `lab/` tree, which is not in the repo, so I could not check them.
- Caveat on encounter start-screen portraits "not found under these prefixes". `repo:notes/Reviews/Native Round5 050310.md:175` names the overhead encounter icon `icon_minigame_combat_encounter_start_hard_free_64` (image 11970). That is an `icon_` file, so it falls in the icon set, not the UI set, which does not contradict the caveat. But the caveat concerns the start-screen portrait itself, and `Native Round5 050310.md:213` says this build's start screen has no icon clip. I could not confirm from the repo whether the portrait is in the index.
