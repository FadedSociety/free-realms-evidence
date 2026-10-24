<!-- fleet job=note-refresh id=Harvest-Nodes status=done turns=13 usd=0.0122 tokens(read,write,in,out)=[283391, 38889, 28, 9073] model=claude-haiku-5-5 -->
# notes/Research/Harvest Nodes.md

**Verdict:** badly stale on scope and integration. The data import checks out (counts, IDs, model and item IDs, loader path), but the note still describes W57 as import-only, before the W171 node-interaction work landed. Three statements about `lib.rs`, the test wiring and the absence of interaction are now false.

**Corrections:**

1. `old:` It does not implement node interaction or claim that these placements and policies were recovered from the client.
   `new:` Since W171 it also carries an ordinary node-click path in `src/harvest_nodes.rs` (`GatheringNodes` with `admit`, `begin`, `paid` and `sync`), wired into `gameplay.rs`. The range, job gate, depletion and respawn rules are reconstructed policy (R). The placements and policies are not claimed as recovered from the client.
   `why:` repo:prototype/osfr-tools/src/harvest_nodes.rs:1-7 (W171 header: 26/8 click starts the Type8 run); :202-315 (`GatheringNodes`, `admit`, `begin`, `paid`, `sync`); repo:prototype/osfr-tools/src/gameplay.rs:2495-2535 (26/8 click → `nodes.admit` → `begin(target)`); repo:prototype/osfr-tools/src/gameplay.rs:1093 (`GatheringNodes::load`).

2. `old:` `tests/harvest_nodes.rs` includes the module by `#[path]`; `lib.rs` is unchanged. Lead integration needs `pub mod harvest_nodes;` in `src/lib.rs` before crate code can import it normally.
   `new:` `tests/harvest_nodes.rs` imports `osfr_tools::harvest_nodes::HarvestNodesContent` from the library. `src/lib.rs:37` already registers `pub mod harvest_nodes;`.
   `why:` repo:prototype/osfr-tools/tests/harvest_nodes.rs:1 (`use osfr_tools::harvest_nodes::HarvestNodesContent;`); repo:prototype/osfr-tools/src/lib.rs:37 (`pub mod harvest_nodes;`). Corroborated by repo:notes/Research/Integration Round 4.md:11 (test-only `#[path]` copies removed).

3. `old:** The Rust loader is not registered in `lib.rs` or connected to a world-spawn/interaction system.`
   `new:` The Rust loader is registered in `src/lib.rs:37` and connected to the world through `GatheringNodes` (`src/harvest_nodes.rs:206`), `gameplay.rs:1093` and the 26/8 click path (`gameplay.rs:2495-2535`). Its visibility is drawn via `NodeChange` (`gameplay.rs:392`).
   `why:` repo:prototype/osfr-tools/src/lib.rs:37; repo:prototype/osfr-tools/src/harvest_nodes.rs:206-315; repo:prototype/osfr-tools/src/gameplay.rs:392, 1093, 2495-2535.
   (Note: the `old:` text is the bullet's body, without the leading `- `.)

**Checked and holding (no change):**
- `src/harvest_nodes.rs` exists and `HarvestNodesContent::load_from(path)` is at line 37.
- `data/content/harvest_nodes.json`: 2 node types, 2 pools, zone 1. Pool `briarwood-mushrooms` has max 12 and respawn 60. Pool `briarwood-mushrooms-rare` has max 2 and respawn 300. Spawn IDs 1–78 with 15 and 16 absent, 76 spawns (per the `spawns.len()==76` assertion). Row spacing puts 66 rows in the normal pool and 10 in the rare pool.
- Model 249 is `sg_collection_node_mushrooms_01.adr` and model 674 is `sg_collection_node_mushrooms_rare_01.adr` (`client:Resources/Models.txt:250, 675`).
- Drop item IDs are 11081–11088 (eight distinct) in the JSON.
- Locale 17056 resolves ("Purple Mushroom").
- The test file has one test (`loaded_harvest_nodes_have_valid_references_and_finite_spawns`).

**Unsure:**
- The Validation table's test counts (6 progression, 1 content, 1 harvest-node, 0 failures) and the rustfmt/python results are from an earlier run. I did not re-run them.
- Line 39 says the tests do not cover "collection interaction". That is true of `tests/harvest_nodes.rs`. Interaction is now covered elsewhere, e.g. `gameplay/t013_objective_events.rs:799` (`ordinary_harvest_nodes_advance_gather_twice_through_gameplay`) and `type8_harvesting_gateway`. Whether to amend the sentence is a judgement call, so I did not include it as a correction.
- The rest of the Open gaps (native packet evidence, the four effect/cursor IDs) are not checkable from the repo.
