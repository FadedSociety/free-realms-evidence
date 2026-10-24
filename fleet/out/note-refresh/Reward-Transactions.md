<!-- fleet job=note-refresh id=Reward-Transactions status=done turns=23 usd=0.0279 tokens(read,write,in,out)=[835627, 76638, 48, 19885] model=claude-haiku-5-5 -->
# notes/Research/Reward Transactions.md

**Verdict:** minor-to-moderate drift. The W10 API section (`rewards.rs`), the packet order, the `Inventory`/`Profiles` writers, the test claims and the reader offsets hold at the tip. The stale parts are the save-envelope version and the migration sink list, which still describe the pre-integration code.

**Corrections:**

1. `old:` Existing `game_store.rs::save` serializes one version-3 character/gameplay snapshot and replaces the file atomically.
   `new:` Existing `game_store.rs::save` serializes one version-7 character/gameplay snapshot, with optional housing and pet blocks, and replaces the file atomically through `character_store::replace_bytes`.
   `why:` repo:prototype/osfr-tools/src/game_store.rs:17 (`SCHEMA_VERSION: u32 = 7`), :30-42 (Document with `housing`/`pets`), :178-183 (`write_document` → `replace_bytes`).

2. `old:` migrates the current version-3 JSON envelope
   `new:` migrates the current version-7 JSON envelope
   `why:` repo:prototype/osfr-tools/src/game_store.rs:15-18 (`GAMEPLAY_SCHEMA_VERSION = SCHEMA_VERSION = 7`; base 5, pet 6).

3. `old:` Migrate `gameplay.rs::apply_smelting`, `gameplay.rs::apply_mining`, `gameplay.rs::apply_harvesting`, `gameplay.rs::apply_cooking` and `gameplay.rs::apply_forging` through `grant_reward`.
   `new:` Migrate the crafting and gathering settlements in `gameplay/crafting.rs::apply_craft` (forging, cooking and smelting, through `grant_reward` at line 367) and `gameplay/crafting.rs::apply_type8` (mining and harvesting, through `grant_reward` at line 464).
   `why:` repo:prototype/osfr-tools/src/gameplay/crafting.rs:24-80 (Movie dispatch to `apply_craft` and `apply_type8`), :367, :464. No `apply_smelting`, `apply_mining`, `apply_harvesting`, `apply_cooking` or `apply_forging` exists anywhere under `prototype/osfr-tools`.

4. `old:` The quest path currently clones inventory and quest state, uses `Inventory::grant_bundle`, then acknowledges the reward; the new state and acknowledgement must still commit together.
   `new:` The NPC turn-in (49/14) already stages `QuestEngine::finish_turnin`, which calls `rewards::apply_grant` with key `quest:{character_id}:{quest_id}` and clears the pending turn-in. `gameplay.rs::apply_quest` still clones inventory and quest state and uses `Inventory::grant_bundle` for the remaining quest outcomes; those must still commit together with the acknowledgement.
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:326-329 (`RewardState::new` → `finish_turnin`); repo:prototype/osfr-tools/src/quest_engine.rs:2032-2035 (`apply_grant`, key, `clear_pending_turnin`); repo:prototype/osfr-tools/src/gameplay.rs:5408-5416 (`apply_quest` with `grant_bundle`, still called at :5274, :5285, :5385-5399).

**Checked and holding (no change):**
- `rewards.rs::apply_grant` exists (:93). Its validation, duplicate-key no-op, packet order (38/19, then 38/18 before 38/14, then 38/2 or 38/3, then 50/1), 256-byte key bound, 34-byte base minimum and bag check all match the note.
- `Inventory::grant_coins` emits 38/19 (inventory.rs:859-873). `Inventory::grant` emits 38/2 for a new stack and 38/3 for an update via `item_update` (inventory.rs:953-1042, 1484; inventory_v2_fixes.rs:108-109).
- `Profiles::experience_packets` emits 38/18 before 38/14 (profiles.rs:333-363).
- Reader `008e7930` stores the success byte at `+0x74`, coins at `+0x50` and stars at `+0x48` (client fn `008e7930`: `param_1[0x1d]`, `[0x14]`, `[0x12]`).
- Opening adds 25 XP in a separate call (gameplay.rs:4838-4848). `mystery_chest_loot.rs::MysteryChests::handle` (:97), `gameplay.rs::handle_mystery_chest` (:5114), `grant_reward` (:5196), `apply_identity` (:5237), `mystery_chest.rs::item_reward` (:164), `kart_rewards.rs::claim_race_reward` (:252) and `reward_bundle_toast` (:212) all exist. The kart payout is still manually staged, as the note says.
- The `tests/rewards.rs` claims hold: six tests, including the combined grant, same-key retry, bag refusal, wallet overflow, the 69-byte empty body plus 3-byte header (72 bytes total), and row framing inside the first test (lines 153-164).
- The save-before-send ordering is still in place (`bin/osfr_gateway/quest_reward_save_failure.rs:1-12`).

**Unsure:**
- Step 1 still holds: `applied_grant_keys` is not in `GameplayState` or `game_store.rs`. `gameplay.rs::adopt_reward_state` (:2569-2586) copies only inventory and profiles into the live state. The note's "copies … key set into GameplayState" line is future tense and still accurate.
- I could not run `scripts/native_map/nmq.py dis 008e7930 256`, so the disassembly claim is only indirectly confirmed through the client pseudocode.
- The "no injected write-failure seam" claim is true for the game store. `character_store.rs:106-110` has a rename-injection seam that the game store does not use.
