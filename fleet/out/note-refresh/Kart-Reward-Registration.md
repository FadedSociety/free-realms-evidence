<!-- fleet job=note-refresh id=Kart-Reward-Registration status=done turns=16 usd=0.0184 tokens(read,write,in,out)=[459890, 47423, 34, 15661] model=claude-haiku-5-5 -->
# notes/Research/Kart Reward Registration.md

**Verdict:** Core facts hold (module and test paths, the 48 class id, the five speedway rows and their prices, the error variants, the 11 test count, the `claim_race_reward` signature and its staged order). The "Exact lead hooks" and the limits now describe integration work that has landed, so that section is stale.

**Corrections:**

1. `old:` `1. **Finish.** When the lead's finish path marks a session finished, call`
   `new:` `1. **Finish (wired).** \`KartGateway::claim_reward_with_event\` already makes this call on a staged clone of the gateway, inventory and profiles, and \`src/gameplay.rs\` routes both finish paths through it. The call shape is`
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:724-765` (calls `crate::kart_rewards::claim_race_reward` at :743, commits all three only on success); `repo:prototype/osfr-tools/src/gameplay.rs:1941` and `:2698`. The gateway passes the player guid as both source and player, which differs from the hook's `source_guid, character_guid` wording.

2. `old:` fallback; build the table from a package `content/` row set when one exists.
   `new:` fallback for tests only. The live table is built from the content race row's `reward` (`RewardRegistration::reconstructed(r.speedway, price.coins, price.xp)`), and save state may not override it.
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:355-374`; `starter_defaults()` is referenced only from `repo:prototype/osfr-tools/tests/kart_rewards.rs` (lines 247-453).

3. `old:` The player-side job gate and the finish packet order remain the lead's integration work.
   `new:` The finish packet order is wired through `KartGateway::claim_reward_with_event` (`src/kart_gateway.rs:724-765`), and the seam's own job gate is in place (`src/kart_rewards.rs:265-268`).
   `why:` the seam refuses non-Kart-Driver payouts at `repo:prototype/osfr-tools/src/kart_rewards.rs:265-268`; the gateway call site is above.

4. `old:` `src/gameplay.rs` (`apply_mining` → `grant_reward` → `Inventory::grant_bundle`)
   `new:` `src/gameplay.rs` (`grant_reward` at gameplay.rs:5196 → `Inventory::grant_bundle` at inventory.rs:1045; e.g. the gather-drop caller at gameplay.rs:4575)
   `why:` no `apply_mining` function exists in `prototype/osfr-tools/src` (search returned none); `grant_reward` is at `repo:prototype/osfr-tools/src/gameplay.rs:5196-5208` and `grant_bundle` at `repo:prototype/osfr-tools/src/inventory.rs:1045`.

5. `old:` `SessionSnapshot.reward_claimed` is the only one-shot marker
   `new:` `SessionSnapshot.reward_claimed` is the one-shot marker, mirrored by a saved gateway `reward_taken` flag that must match it on restore
   `why:` `repo:prototype/osfr-tools/src/kart_gateway.rs:327-329` (`if saved.reward_taken != saved.session.reward_claimed { return Err(... "kart payout markers differ") }`); `repo:prototype/osfr-tools/src/kart_racing.rs:415` and `:713-716`.

**Unsure:**
- Lead hook 3 (line 87-89): "The lead should also deny a class change while a race is live". I did not find this gate in the code. I did not search exhaustively, so I am not calling it false; it may still be open.
- The `lab/reports/kart-rewards-20261009/` evidence logs (`green.log`, `red-compile.log`, `red-behavior.log`, `focused-neighbors.log`) and `lab/decompiled/client/FreeRealms/pseudocode.c`: `lab/` is not present at the repo root, so I could not check them. The "87 passed, 5 ignored" focused-suite figure was not re-run.
- "natively accepted `50/1` writer" in `src/mystery_chest.rs`: `item_reward` exists at `mystery_chest.rs:164`, but I did not verify the native-acceptance claim.
- "Restart" and "Persist SessionSnapshot": `SessionSnapshot` derives `Serialize` (`kart_racing.rs:399`). The gateway's restore path is at `kart_gateway.rs:325-334`, but I did not check whether the save state persists the snapshot end to end.
