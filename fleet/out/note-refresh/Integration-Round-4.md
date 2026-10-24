<!-- fleet job=note-refresh id=Integration-Round-4 status=done turns=18 usd=0.0212 tokens(read,write,in,out)=[579539, 55707, 38, 16897] model=claude-haiku-5-5 -->
# notes/Research/Integration Round 4.md

**Verdict:** badly stale in the NPC-interaction, quest, CoinShop and open-gap sections (several claims are now false at the tip). Module registration, `LegacyData`, the startup-actor index range, the bundled-NPC fallback, the `35/2` AddNpc path and the admin-false login value still hold.

**Corrections:**

1. `old:` 66/43 is parsed only behind an open vendor session; it is not translated to CoinShop because item, quantity, and merchant fields have not been identified in client evidence.
   `new:` 66/43 is parsed only behind an open vendor session and is routed to `CoinShop::buy_vendor` (item from the first initial dword, quantity and transaction key from the trailing dwords, under the (R) field policy); the merchant fields remain unidentified in client evidence.
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:787-831 (`npc_merchant_buy_66_43` decodes the request, validates the item, calls `shop.buy_vendor`); repo:prototype/osfr-tools/src/coin_shop.rs:335 (`pub fn buy_vendor`).

2. `old:` The new NPC quest engine is session-only: its state is not part of `GameplayState`, and the gateway does not yet route the client quest-accept 49/2 request into it. Offers are therefore not a persistent end-to-end quest flow.
   `new:` The NPC quest engine's state is part of `GameplayState` (`npc_quests`, serialized by `self.npc_quest_state()`), and client 49/2 accept requests are routed into the engine (`npc_quest_reply_49_2`). Native acceptance and persistence still lack evidence.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:93 and :1353; repo:prototype/osfr-tools/src/gameplay/npc.rs:99-100 and :262 (`npc_quest_reply_49_2`); repo:prototype/osfr-tools/src/gameplay/npc_quests.rs:63-70.

3. `old:` `CoinShop` currently owns an inventory snapshot. Gameplay copies shop inventory back after a shop transaction, but does not refresh the shop's private copy after unrelated inventory/reward changes. The shop/gameplay inventory can diverge within a session; a narrow CoinShop inventory-sync API is needed for safe mixed gameplay.
   `new:` `CoinShop` owns an inventory snapshot, refreshed through `CoinShop::sync_inventory` from gameplay before each 165 buy/sell, before the 66 preview, and before 66/43. Gameplay copies the inventory back after each transaction.
   `why:` repo:prototype/osfr-tools/src/coin_shop.rs:311 (`pub fn sync_inventory`); repo:prototype/osfr-tools/src/gameplay/npc.rs:710 (165 path), :772 (66 preview), :827 (66/43), and copy-back at :726, :776, :839.

4. `old:` - NPC quest acceptance/state persistence and CoinShop inventory synchronization are not wired through the whole session lifecycle.
   `new:` - NPC quest acceptance and state persistence are wired (`gameplay/npc.rs:99`, `gameplay.rs:1353`) but have no native evidence. CoinShop inventory is synced before each shop transaction (`gameplay/npc.rs:710`).
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:99, :710; repo:prototype/osfr-tools/src/gameplay.rs:1353.

5. `old:` The crate-wide test command remains blocked by `tests/piece_012.rs`; an individually run target sweep found one stale assertion in `tests/piece_050.rs`.
   `new:` The crate-wide test command was blocked by `tests/piece_012.rs` when this round ran. At the tip the two `CookingTransaction` literals there set `experience_points: 0`, so that blocker appears fixed (re-run to confirm). An individually run target sweep found one stale assertion in `tests/piece_050.rs`.
   `why:` repo:prototype/osfr-tools/tests/piece_012.rs:86 and :133.

6. `old:` - `cargo.ps1 test --no-fail-fast`: blocked at compile time by `tests/piece_012.rs:82` and `:127`, where two `CookingTransaction` literals omit the newly required `experience_points` field. That file was outside W59 ownership and was left unchanged.
   `new:` - `cargo.ps1 test --no-fail-fast`: was blocked at compile time by `tests/piece_012.rs:82` and `:127` when the round ran. At the tip those literals are at `:86` and `:133` and both set `experience_points: 0`, so the compile blocker is no longer present in the file.
   `why:` repo:prototype/osfr-tools/tests/piece_012.rs:82-88 and :129-134.

7. `old:` - The crate-wide suite needs its external `piece_012` test literals updated for the concurrent `experience_points` field. The stale `piece_050` list expectation also needs review against the intended `Payload` fix.
   `new:` - The `piece_012` literals now carry `experience_points` (`tests/piece_012.rs:86`, `:133`). The `piece_050` expectation still needs review against the `Payload` fix (see Unsure).
   `why:` repo:prototype/osfr-tools/tests/piece_012.rs:86, :133.

8. `old:` The source pattern is in `src/bin/osfr-gateway.rs`; the radius and cap are local choices, not recovered retail values.
   `new:` The constants `NPC_VISIBILITY_RADIUS` and `NPC_VISIBILITY_LIMIT` are in `src/world.rs:21-22` and applied in `NpcVisibility::shared_view` (`src/world.rs:202-213`). The gateway's view loop that calls it is in `src/bin/osfr-gateway.rs:3245-3305`. The radius and cap are local choices, not recovered retail values.
   `why:` repo:prototype/osfr-tools/src/world.rs:21-22, :202-213; `src/bin/osfr-gateway.rs` has no `100.0`/`64` constant (grep on `interest|100.0|64` returned nothing there).

**Unsure:**

- `piece_050`: the test `production_check_name_preserves_the_saved_native_appearance` (`tests/piece_050.rs:513-552`) now ends with a `[11]` selection request compared against `login::selection_reply(Some(&saved))`. It no longer has an explicit character-list step, so I could not confirm the reported failure at the tip without running it.
- The extra-row zone statistics (3,265 rows, 1,095 anchors, distance percentiles) and the test counts in the table were not re-run.
- Whether the NPC quest flow is complete across the whole session lifecycle (the rebind and persistence paths exist at `gameplay/npc_quests.rs:12-45`), and whether 66/43 should be called "cannot safely map" given that the (R) mapping now exists. Both are judgement calls for the note's author.
- Confirmed as current: `src/lib.rs:24,37,60,71,76` (all five modules registered); `SourceTag::LegacyData` with `#[serde(rename = "legacy-data")]` at `src/content.rs:26-27`; bundled NPC fallback at `src/gameplay.rs:869-885`; `NpcVisibility` AddNpc via `startup_world::build_add_npc` at `src/world.rs:223`, `:621`; startup indices 10..=32 at `src/startup_snapshot.rs:323`, `:505` and `src/gateway.rs:1905`; `admin` passed as `false` at `src/login.rs:624`.
