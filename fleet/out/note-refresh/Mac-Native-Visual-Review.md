<!-- fleet job=note-refresh id=Mac-Native-Visual-Review status=nothing_found turns=6 usd=0.0065 tokens(read,write,in,out)=[58101, 28730, 14, 4577] model=claude-haiku-5-5 -->
# notes/Research/Mac Native Visual Review.md

**Verdict:** current. The one claim about our code (the configured Mac content row) holds at the tip, and the review's evidence chain agrees with the sibling Bartle/Artifacts review. No correction is needed.

**Checked and holding:**
- Configured content row: `prototype/osfr-tools/tests/fixtures/quests/opening.json:423-429` has the Mac row (`definition_id` 920002, `name_id` 5100344, `name` "Mac", `model_id` 3897, `model_file_name` "human_m_hooligan_boss_02.agr", `kind` "enemy", `interaction_radius` 12.0). The generator agrees: `scripts/prepare-opening-content.py:102` creates `actor(20, 920002, ..., model=3897, name_id=5100344, kind='enemy')`.
- Defeat targets: `prototype/osfr-tools/tests/test_quest_coverage.py:177` expects `{3156, 920001, 920002}`, so 920002 (Mac) is a defeat target as the note implies.
- Source hash and run identity: the original `artifacts-mac-queen.mkv` SHA256 `de808edabf…` and the run 193318 Mac fight match `notes/Reviews/Native Bartle and Artifacts 193318.md:52` (same video hash, same frame numbers 0045/0055/0059, same 775 HP outcome).
- Proof cross-reference: the "Finalized Bartle/artifacts/Mac wire and checkpoint proof" link and SHA256 `a0da5d58…` match `notes/Reviews/Native Bartle and Artifacts 193318.md:60`.
- Frame timing: 80 frames at 2 fps over 1175–1214.5 s is internally consistent. Each frame number in the table maps to its nominal time (for example frame0041 = 1195 s, frame0059 = 1204 s).
- Scope limits (no unobscured swing or corpse claim) match the sibling review's wording.

**Unsure:**
- Helper duration: the note gives the helper run as `20:23:50.051198–20:24:08.672837UTC, 18.625s`. Those two timestamps differ by 18.621639 s, not 18.625 s (a 3.4 ms gap). `MODLOG.md:366` and `notes/Reviews/Native Bartle and Artifacts 193318.md:46` both say 18.625 s, so the discrepancy may come from the source log rather than this note. I did not change it because the raw helper log is in `lab/`, which I cannot read.
- Lab-only items I could not reach from the repo: the reviewed frames, the contact sheets, the `visual-review.json` hash (`c4fcd726…`), the "adjacent clean-stop marker", the "rehash" of all review sources, and the claim that no source, save, release, or decoder output changed. These sit outside the repo and were not verified.
