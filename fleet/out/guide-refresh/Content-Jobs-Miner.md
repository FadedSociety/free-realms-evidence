<!-- fleet job=guide-refresh id=Content-Jobs-Miner status=done turns=28 usd=0.0272 tokens(read,write,in,out)=[1022948, 68357, 58, 16901] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Miner.md

**Verdict:** minor drift. Most code-facing claims hold at the tip (the Type8 protocol, queue rules, board size, duration, reshuffle and chain messages). One sentence states the smelting grant wrongly, and one open conflict is now answered by our recipe data.

**Corrections:**

1. `old:` our server grants ten bars per win for 5 Copper Ore and 3 Singing Coal
   `new:` our server grants five bars per win for 5 Copper Ore and 3 Singing Coal (the recipe's output count is 5; the movie's reported quantity is only checked to be at most 10)
   `why:` repo:prototype/osfr-tools/src/smelting.rs:511-514 (the grant is `recipe.product_quantity`, not the reported quantity); repo:prototype/osfr-tools/data/content/recipes.json:3538-3553 (`minigame_id` 77, ingredients 2739x5 and 879x3, `output.count` 5); repo:prototype/osfr-tools/src/smelting.rs:765 (`product_quantity: row.output.count`)

2. `old:` The 5 plus 3 inputs and the output count per run are unresolved.
   `new:` The 5 plus 3 inputs and the output count per run come from client recipe row 4 (Copper Bar, output 5 for Copper Ore x5 and Singing Coal x3). The wiki's "per bar" wording is the only point still open.
   `why:` repo:prototype/osfr-tools/data/content/recipes.json:3550-3569 (output count 5; source list cites the client recipe row and the locale 1772250646 tutorial). Our tip uses 5 bars per run, so the grant and the client row agree.

**Unsure:**

- **Node data gap (Gaps, "Node data").** The note says node positions and respawn times are unknown. Our tip has reconstructed Copper Vein placements in `data/content/mining_nodes.json` with a configurable respawn (`repo:prototype/osfr-tools/src/harvest_nodes.rs:333-359`). The Build Ledger row for Mining (`notes/Design/Build Ledger.md:104`) describes the reconstructed five placements and the 60 s respawn. I did not open `mining_nodes.json` to confirm the values. The gap is about original data, so I left it as is.
- **Smelting tuning numbers.** The 65 percent measure target, the 57 to 73 percent window and the "90 second" row value could not be found in any file under `data/content`. `smelting.rs` only shows `duration: 90` in a test fixture (line 848). The live smelting phase table is not in the repo, so these could not be checked.
- **Collected powerups (900 to 902).** The note describes their effects from the movie. Our `mining.rs:1072-1075` says collected powerups in 900..=949 are explicitly deferred and only the clickable 950 to 953 are serviced. The note does not claim we implement them, so I made no correction; a reader could still assume they work.
- **Client-side claims** (locale ids, MiniGameData rows, `MEMBERS_ONLY = 0`, quest wording, NPC names and places, video frame keys) were not checked. They need the client tables, not the repo.
- **Protocol handshake names** (`OnConnectMsg`, `OnServerReadyMsg`, `OnStartLevelMsg`, `OnQuotaInitMsg`) match `mining.rs:8-11`, `633-676`. The route `39` sub-numbers (14, 16 to 19, 47) match the module header at `mining.rs:5-7`. The sub-codes 5, 6 and 7 were not checked.
