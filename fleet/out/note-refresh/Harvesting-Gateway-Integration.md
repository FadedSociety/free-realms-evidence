<!-- fleet job=note-refresh id=Harvesting-Gateway-Integration status=done turns=18 usd=0.0183 tokens(read,write,in,out)=[506535, 53259, 38, 13199] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Gateway Integration.md

**Verdict:** minor drift. The core wiring (`pub mod harvesting`, `GameplayState.harvesting`, `Gameplay.harvesting`, game 111 / Chef 45 / namespace 58_000_001, the `realm harvest` gate, routing, the shipped outputs and quotas) still holds. Four names and counts are stale, and the status line about Harvesting is superseded. The failure mode in Finding 1 is also wrong.

**Corrections:**

1. `old:` A live `harvesting.json` run would therefore fail its grant with `unknown reward definition`.
   `new:` A campaign with `harvesting.json` would therefore refuse to load with `harvesting reward definition N is not in the loaded inventory`.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:1015-1021 checks every output definition against the loaded inventory at load time. `unknown reward definition` is the grant-time message in src/inventory.rs:981, which is not reached.

2. `old:` `apply_harvesting`: the only reward path is
   `new:` `apply_type8(Gather::Harvesting, …)`: the only reward path is
   `why:` repo:prototype/osfr-tools/src/gameplay/crafting.rs:437-443 defines the single `apply_type8`, and crafting.rs:446 calls `harvesting::lifecycle::reward_grant` from it. `apply_harvesting` was deleted in the D007 merge (notes/Autopilot/D007.md:27).

3. `old:` Dev-only `realm harvest` (`developer_harvesting`)
   `new:` Dev-only `realm harvest` (`developer_gather(Gather::Harvesting)`)
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4355-4361 dispatches `"harvest"` to `developer_gather(Gather::Harvesting, …)`, defined at gameplay.rs:4174. No `developer_harvesting` exists in the tree.

4. `old:` The eleven gateway tests cover:
   `new:` The fourteen gateway tests cover:
   `why:` repo:prototype/osfr-tools/tests/type8_harvesting_gateway.rs has 14 `#[test]` functions (lines 438, 450, 470, 501, 516, 607, 693, 744, 778, 825, 887, 951, 1029, 1135). Later runs report 14 passed (notes/Autopilot/T371.md:56, F366.md:220). The "11 passed" lines in the GREEN bullet are a dated log and can stay.

5. `old:` Harvesting stays an unregistered separate candidate:
   `new:` Harvesting was an unregistered separate candidate when this change landed. It is now wired: `realm harvest` (dev) and Mushroom nodes start a Harvesting111 run (native round still unverified).
   `why:` repo:notes/Design/Build Ledger.md:105 ("Wired; native round unverified"); repo:prototype/osfr-tools/src/harvest_nodes.rs:104 and :225 (`harvest_nodes.json` starts Harvesting111); gameplay.rs:4361. The engine itself still loads only when `harvesting.json` exists (gameplay.rs:979).

**Unsure:**

- Dev-gate wording "no competing activity (forging/smelting/cooking/mining/encounter)". `developer_gather` (gameplay.rs:4187-4193) refuses only an active encounter. The other busy states look to be handled by the movie gate, which the code comment at gameplay.rs:4170-4172 says owns live movies. I did not trace that gate, so I left the sentence alone.
- Finding 3 cites "`gameplay.rs` Chef gather branch". The Gather dispatch now lives in `gameplay/crafting.rs` (lines 79-80, 114, 421-455). I did not find the quest-gather code the sentence means, so I could not confirm or correct the citation.
- Finding 1's claim that `inventory.json` lacks 2885/2887/2890/2877 cannot be checked: the campaign content is private (`lab/`). In the repo, `data/content/harvesting.json:195-216` ships those four outputs, and `tests/type8_harvesting_gateway.rs:1136` asserts that the fixture definitions exist in the private campaign.
- The pre-edit and post-edit SHA prefixes and the `lab/reports` paths cannot be checked from the repo.
- The `realm exit` routing claim is consistent with gameplay.rs:4298, but I did not trace the full cancel path.
