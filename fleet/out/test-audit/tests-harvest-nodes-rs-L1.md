<!-- fleet job=test-audit id=tests-harvest-nodes-rs-L1 status=done turns=7 usd=0.0053 tokens(read,write,in,out)=[68026, 19811, 16, 4236] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/harvest_nodes.rs lines 1-85 of 85

Window: `prototype/osfr-tools/tests/harvest_nodes.rs` lines 1-85 (single test `loaded_harvest_nodes_have_valid_references_and_finite_spawns`). Code under test read: `src/harvest_nodes.rs:26-102` (`HarvestNodeType.drop_table` is `#[serde(default)]`, so a missing or emptied table deserializes as an empty `Vec`). Data read: `data/content/harvest_nodes.json` has `drop_table` arrays at lines 25 and 95, so both node types currently carry drops.

- **[medium] tests/harvest_nodes.rs:60-69 loaded_harvest_nodes_have_valid_references_and_finite_spawns - the drop-table reference check is vacuous when the table is empty.**
  - Why it cannot catch a regression: `node_type.drop_table.iter().all(...)` (line 65-66) and `.all(|drop| drop.weight > 0)` (line 68) both return `true` for an empty vector. If a change drops the `drop_table` key from `harvest_nodes.json`, or the serde default or a loader change empties it, every node type passes the loop and the test still succeeds. The test also never checks that the item IDs resolve to anything, because it never asserts that a table is non-empty.
  - Fix: before the loop, assert that each node type has a non-empty drop table, e.g. `assert!(!node_type.drop_table.is_empty(), "{}", node_type.key)`, and optionally assert the total drop count (currently 8 distinct loot IDs per `notes/Research/Harvest Nodes.md:25`) so an emptied table fails.

- **[low] tests/harvest_nodes.rs:45-47 loaded_harvest_nodes_have_valid_references_and_finite_spawns - exact counts of 2 node types, 2 pools and 76 spawns pin a content snapshot unrelated to the reference and finiteness checks the name describes.**
  - Why it causes churn: any legitimate content edit (adding or removing one spawn) fails this test even when every reference is still valid. The counts say nothing about references or finite positions.
  - Fix: keep a lower bound (e.g. `assert!(!content.spawns.is_empty())`) for the reference checks, and move the exact 76 count into a separate content-snapshot test if it is wanted.

Checked and not reported: the spawn-to-pool lookup (`pools[...]` at line 80) panics on a dangling key, so it fails loudly. The zone agreement check (line 81), finiteness checks (lines 82-83), the model-ID set built from `Models.txt` (lines 36-43), and the item-ID set (lines 25-35) each compare against independently loaded data and can fail. The `lab/` fixture paths (lines 20, 27-38) are missing-file `unwrap` panics, not silent early returns, so they are not a skip.
