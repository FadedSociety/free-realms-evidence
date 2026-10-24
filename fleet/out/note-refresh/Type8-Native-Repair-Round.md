<!-- fleet job=note-refresh id=Type8-Native-Repair-Round status=done turns=15 usd=0.0143 tokens(read,write,in,out)=[390772, 42794, 32, 9985] model=claude-haiku-5-5 -->
# notes/Research/Type8 Native Repair Round.md

**Verdict:** minor drift. The repair itself matches the tip: the produce helpers, the 400-block values, the 601-era collectable removal, the shared engine chain path, and the Leave/Quit arms all check out. One completion figure is wrong.

**Corrections:**

- `old:` completing every quota (15 tiles, 5 per bundle) stops the level and then the normal
  `new:` completing every quota (four baskets at 25 tiles each, 100 tiles in all; each 5-tile cluster grants one bundle) stops the level and then the normal
  `why:` `prototype/osfr-tools/src/harvesting.rs:780` sets `RECONSTRUCTED_QUOTA_TILES = 25` (its doc says "Five visible bundles at five tiles per bundle"), and `board_spec` at `harvesting.rs:955` applies that quota to each of the four goals. `harvesting.rs:782` gives `per_reward = 5`. Four goals at 25 is 100 tiles, not 15. The win check in `mining.rs:1664-1668` requires every goal to reach its quota.

**Checked and holding (no change):**
- `harvesting.rs:100-116`: `produce_value`, `produce_index` and `produce_value_for` implement `400 + 1-based index`. `REGULAR_TILE_VALUES` no longer appears anywhere in `src/`.
- `harvesting.rs:306-321`: region 111 is `stickfruit, stainberry, tumtumnip, spiralmint`, giving 411/413/416/403. `PRODUCE` (`harvesting.rs:168+`) has item definitions 2875 onward and locale ids 23285 onward, which fits the note's 2885/2887/2890/2877 outputs.
- `harvesting.rs:930-1014`: `board_spec` emits selectable goals and outputs, four category-400 tile kinds, `collectable: Vec::new()`, and `RECONSTRUCTED_COLLECTABLE_PERCENT = 0` (`harvesting.rs:791`).
- `harvesting.rs:1053-1215`: `validate_content` refuses goals off the produce values (1180), unregistered selectable kinds (1186), non-empty collectables (1208), and a selectable set that is not one-per-produce (1215).
- `mining.rs:1130-1167`: `validate_spec` accepts goals on a selectable or collectable value, and an empty collectable list passes.
- `mining.rs:694-775`: the `OnChainMsg` path counts every chain tile through `collect_chain_goals` (1622), adopts the chain value for wildcards, emits `OnQuotaUpdateMsg`, and ends in the shared `settle_after_collect` (1656). The selectable path adds only the chain score, as the note says.
- `mining.rs:1722-1763`: `validate_chain` returns `Option<u16>`, the chain's matching value.
- `mining.rs:894` and `904`: the `FRServer_GameClose` and `FRServer_GameQuit` arms exist.
- `tests/type8_native_repairs.rs` exists (498 lines).
- `Resources/CodeStringMappings.txt:4784-4799` (client root) holds the sixteen `farmingValue401..416` entries with the note's ids.

**Unsure:**
- The lab artifacts (`../lab/reports/type8-native-repair-20261009/`: logs, `final-hashes.txt`, `content-probe.json`, the native-package hash) are outside the repo, so I could not check the RED/GREEN counts, the suite totals, the SHA-256 values or the content probe output.
- The Leave/Quit claim that `GameClient.as:94` wires Leave to `SoeInterface.Quit()`, and that `SoeInterfaceFreeRealms.as` maps it to `fscommand("FR_event","Quit()")`. My client SQL and `ui` searches did not reach that file, so I could not confirm it.
- The claim that `GameLevel.QuotasInit` sends selectable quotas first, and that `HandleSelectableTile` counts every tile, is about original client code I could not reach in the decompiled database.
- The "Recovered original" name and icon table (`GameClient.as::OnQuotaInitMsg`, `TileGenerator.as::SetTileInfo`) is client-side, so I checked only the `CodeStringMappings` ids and not the resolved names.</result>
