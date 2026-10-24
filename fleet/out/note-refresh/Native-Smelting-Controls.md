<!-- fleet job=note-refresh id=Native-Smelting-Controls status=done turns=14 usd=0.0161 tokens(read,write,in,out)=[396802, 58169, 30, 9719] model=claude-haiku-5-5 -->
# notes/Research/Native Smelting Controls.md

**Verdict:** minor drift. Most checkable claims hold: the four Smelting77 stage IDs 101–104, the server accepting bounded movie statistics without simulating physics, the 1–10 quantity check, and the reconstructed phase rows. One stated fact is stale: the server grants five Copper Bars, not ten.

**Corrections:**

1. Line 5, in the paragraph beginning "At1280x960":
   - `old:` Current reconstructed tuning and fixed10-bar output remain disclosed.
   - `new:` Current reconstructed tuning remains disclosed; the five-bar output is client-tutorial backed (locale 1772250646) and supersedes the old ten-bar sample.
   - `why:` repo:prototype/osfr-tools/src/smelting.rs:514 grants `recipe.product_quantity`, which comes from the Miner row's `output.count`. repo:prototype/osfr-tools/data/content/recipes.json:3552 sets that count to 5, with the client-locale evidence at :3604. repo:prototype/osfr-tools/tests/smelting.rs:315-316 asserts `grants == [(21785, 5)]` and cites the same locale. repo:notes/Research/Recipe Content.md:64 records the change from 10 to 5.

2. Line 17, the paragraph beginning "The Rust server currently accepts":
   - `old:` Phase tuning, target65%, heat100, scoring and fixed10-bar server output are explicitly reconstructed.
   - `new:` Phase tuning, target65%, heat100 and scoring are explicitly reconstructed; the server's Copper Bar output is five (recipe row output count 5, client locale 1772250646), not a reconstructed ten.
   - `why:` repo:prototype/osfr-tools/src/smelting.rs:510-514 (recipe-driven grant, no fixed ten); repo:prototype/osfr-tools/data/content/recipes.json:3552; repo:prototype/osfr-tools/tests/smelting.rs:315-316.

**Unsure:**

- Line 3 says the "recipe transaction" was independently accepted in the 103605 native run. MODLOG.md:327 and :432 and Research/Original Smelting.md describe ten bars in that era. Whether the native acceptance was at the ten-bar or five-bar value is not settled by the repo; the five-bar value is untested natively.
- Phase-1 hit counts (one per layer, three for high power, two for medium) and the Timer.FRAME_RATE35 / speed-20 meter figures are client-side and sit in `../lab/decompiled`, which is outside the repo. Not checked. The repo shows only the reconstructed rows at scripts/prepare-smelting.py:46-49 (speed column 20 and hit counts 1/1 match).
- Adjacent drift outside this note: scripts/prepare-smelting.py:54 and :68 still say "fixed ten-bar" and write `product_quantity: 10` into smelting.json. The server ignores that field (its Content struct reads only `recipe.key`, smelting.rs:70-74). Repo:notes/Research/Original Smelting.md:7 and :9 also still say "ten Copper Bars". Those lines should be fixed by their owners, but I did not propose changes to them.
- The lab evidence paths (line 19) and the 65%/57–73% and 62–68% measurement windows cannot be checked from the repo.
