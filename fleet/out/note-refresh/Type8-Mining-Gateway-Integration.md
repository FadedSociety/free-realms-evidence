<!-- fleet job=note-refresh id=Type8-Mining-Gateway-Integration status=done turns=18 usd=0.0188 tokens(read,write,in,out)=[461133, 49449, 38, 16070] model=claude-haiku-5-5 -->
# notes/Research/Type8 Mining Gateway Integration.md

**Verdict:** badly stale on two load-bearing points (the reward outputs and the entry paths), with minor drift in names and the test count. The wiring claims (`pub mod mining;`, the `GameplayState.mining` serde attributes, the `realm mine` dev gate, the 250 ms tick, the block list, the 18/14 content binding, the 18_000_001 namespace, the `write_content` game-18 refusal) still hold at the tip.

**Corrections:**

1. `old:` command is the only entry; nothing here claims a historical way into Mining18.
   `new:` command and the reconstructed Copper Vein nodes are the entries (a player clicks an in-range `mining_nodes.json` node in 26/8 to start the Miner run); nothing here claims a historical way into Mining18.
   `why:` repo:prototype/osfr-tools/src/harvest_nodes.rs:226 loads `("mining_nodes.json", Gather::Mining, 2)`; repo:notes/Design/Build Ledger.md:104 (W171, `0e5d122`) records the Copper Vein node entry; repo:prototype/osfr-tools/src/gameplay/t013_objective_events.rs:933 uses "Copper Vein".

2. `old:` No world entry, quest trigger or gathering binding was added; the
   `new:` A Copper Vein gathering binding was added later (W171, via `mining_nodes.json`); no quest trigger was added, and the
   `why:` repo:prototype/osfr-tools/src/harvest_nodes.rs:226; repo:notes/Design/Build Ledger.md:104. (The following "existing opening gather interactions are untouched" clause may still be true; I did not check it.)

3. `old:` Mining outputs ship as `outputs: []` in the prepared default content until the lead accepts a mapping.
   `new:` Mining outputs ship as two reconstructed entries in the prepared default content (601 → definition 2739 ×1, 602 → definition 2739 ×2), labelled as an unaccepted placeholder until the lead accepts a mapping.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1022-1033 (`outputs: vec![Type8Output { value: 601, definition_id: 2739, cluster_quantity: 1 }, … 602 … cluster_quantity: 2]`), with the comment at :1020-1021 saying the catalogued ore is reused; `write_content` at :1065 writes `mining_spec()`. repo:notes/Autopilot/F267.md:93-94 pins that the real `mining.json` outputs Copper Ore 2739.

4. `old:` `game_id 18`, `profile_id 14`, `preload_file MiningAssets.txt`, `launch_movie game_mining.gfx`,
   `new:` (keep, but see correction 5 for the outputs text on the next line)
   `why:` checked and correct: repo:prototype/osfr-tools/src/mining.rs:49, :54, :80, :83. Listed here only so the next correction can be applied in place; no change needed to this line.

5. `old:` `reconstructed_rules: true`, no outputs. To run natively
   `new:` `reconstructed_rules: true`, two catalogued ore outputs (601 → 2739, 602 → 2739). To run natively
   `why:` repo:prototype/osfr-tools/src/mining.rs:1022-1033, :1041 (`reconstructed_rules: true`).

6. `old:` mapping (empty by default). No world entry, quest trigger or gathering binding was added; the
   `new:` mapping (two catalogued ore entries by default, `mining_spec()` `outputs`). A Copper Vein gathering binding via `mining_nodes.json` was added later (W171); no quest trigger was added, and the
   `why:` repo:prototype/osfr-tools/src/mining.rs:1022-1033; repo:prototype/osfr-tools/src/harvest_nodes.rs:226. (Sentence continues on the next line: "existing opening gather interactions are untouched.")

7. `old:` 4. A recovered or explicitly accepted Mining18 output mapping; until then `outputs: []` grants nothing.
   `new:` 4. A recovered or explicitly accepted Mining18 output mapping; until then the catalogued placeholder (601 and 602 → definition 2739) grants Copper Ore.
   `why:` repo:prototype/osfr-tools/src/mining.rs:1022-1033; repo:notes/Autopilot/F267.md:93-94.

8. `old:` `apply_mining` stages the engine outcome;
   `new:` `apply_type8(Gather::Mining, …)` stages the engine outcome;
   `why:` no `fn apply_mining` exists in repo:prototype/osfr-tools/src (search returned none); the applier is `apply_type8` at repo:prototype/osfr-tools/src/gameplay/crafting.rs:437, called at :40 and :76.

**Unsure:**

- **Test count.** `tests/type8_gateway.rs` now has 13 `#[test]` functions (lines 375, 383, 403, 434, 449, 464, 555, 607, 660, 711, 755, 807, 882), not the 10 the note lists. The note's "10 passed, 0 failed" is a dated log, and the three unnamed tests at 434, 449 and 464 may be later additions. I did not run the suite. Consider adding "(13 tests now)" or leaving it as a historical record.
- **SHA-256 table.** I cannot hash files with these tools, so I did not verify the four digests. `mining.rs` and `gameplay.rs` have changed since the review (the outputs and the `gameplay/` split), so the frozen digests are probably no longer the tip's.
- **Reward path.** The note says the grant goes through `consume_materials` + `grant_reward`. The applier calls `crate::mining::lifecycle::reward_grant` (repo:prototype/osfr-tools/src/gameplay/crafting.rs:445; `reward_grant` is at repo:prototype/osfr-tools/src/mining_lifecycle.rs:399). I did not trace whether that calls `consume_materials` / `grant_reward`.
- **`realm mine` gates.** The dev path (gameplay.rs:4346-4352, `developer_gather` at :4174-4222) checks dev tools, content loaded, the encounter, unlocked job and active job. The note's "no live mining run; no live forging/smelting/cooking" gates are likely enforced by the movie gate in `handle_opening_inner` (gameplay.rs:4276-4304), not checked directly here.
- **Tick timing.** The 250 ms bound is confirmed (`MOVIE_TICK_MS` at repo:prototype/osfr-tools/src/gameplay/movie.rs:8, `tick_gather` at gameplay/crafting.rs:87-94), but the note's "same write bound as forging" was not checked against the forging path beyond that.
