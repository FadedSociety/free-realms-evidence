<!-- fleet job=note-refresh id=NPC-Interaction status=done turns=18 usd=0.0273 tokens(read,write,in,out)=[638298, 76714, 38, 22608] model=claude-haiku-5-5 -->
# notes/Research/NPC Interaction.md

**Verdict:** minor-to-moderate drift. The module, the 26/8 decoder and the 12 m radius are current. The vendor-stock sections are stale, the test-status line is superseded, and several path:line citations moved.

**Corrections:**

1. `old:` it is intentionally empty because
   no NPC-to-item IDs were verified.
   `new:` it now holds 64 vendor entries with explicit item-ID mappings (see Vendor stock, W47c). `NpcInteraction::load` rejects any ID that has no `stores.json` price.
   `why:` `data/content/vendors.json` is non-empty (47,640 lines, with `npc_id` and `item_ids` rows, e.g. line 18097 for 9500000339). `src/npc_interaction.rs:337-370` reads it and rejects IDs without a price (line 362).

2. `old:` `merchant_buy_66_43_is_parsed_only_for_an_open_vendor_session` expects Alexander's shop
   (`9500000339`) to be empty, but the verified wiki/client-name mapping adds priced item 75475. The
   `new:` `merchant_buy_66_43_is_parsed_only_for_an_open_vendor_session` opens Alexander's shop (`9500000339`) and asserts only `NpcSelection::Shop`. Stock contents are covered by `npc_interaction_vendors.rs`, so the empty-stock expectation is gone.
   `why:` `tests/npc_interaction.rs:529-538` (the comment at 537 says "Stock contents are covered by `npc_interaction_vendors.rs`"; the only assertion is `matches!(opened, NpcSelection::Shop(_))`).

3. `old:` `npc_interaction` passed 8/9 with the fixture
   `new:` `npc_interaction` now has 18 `#[test]` functions. The W47c 8/9 result is superseded. Not re-run here.
   `why:` `tests/npc_interaction.rs` has `#[test]` at lines 92–721 (18 tests), and the fixture mismatch named in the note no longer exists (see correction 2).

4. `old:` `QuestInfo` intent still contains only a quest ID and is not passed into this raw-wire struct.
   `new:` `QuestInfo` intent still contains only a quest ID. The live offer does build `QuestOfferPacket49_1` from `QuestEngine` title, intro and description IDs in `quest_offer_packet_with`, which calls `encode_quest_offer_49_1`.
   `why:` `src/gameplay/npc.rs:1240-1258` (`quest_offer_packet_with`) and `:1251` (`npc_interaction::encode_quest_offer_49_1(&QuestOfferPacket49_1 {...})`).

5. `old:` `gameplay.rs` independently checks the exact 13-byte shape
   `new:` `npc_interaction.rs:1035` (`decode_npc_interact_26_8`, called from `gameplay/npc.rs:391`) checks the exact 13-byte shape.
   `why:` `src/npc_interaction.rs:1034-1041` is the single check. `src/gameplay.rs:1508` is now `reset_session`, and `gameplay.rs:2503` only delegates to the decoder.

6. `old:` `gameplay.rs:1508` independently enforces length 13 and bool `0..=1`.
   `new:` `npc_interaction.rs:1035` enforces length 13 and bool `0..=1`; `gameplay/npc.rs:391` calls it.
   `why:` `src/gameplay.rs:1508` is `pub fn reset_session`; the length and bool check is at `src/npc_interaction.rs:1035`.

7. `old:` it does not mutate inventory.
   `new:` the module's parser does not mutate inventory. The gateway path does: `Gameplay::npc_merchant_buy_66_43` runs validated buys through `CoinShop::buy_vendor` and writes `self.inventory`.
   `why:` `src/gameplay/npc.rs:787-839` (`validate_merchant_item_66_43` at 812, `shop.buy_vendor` at 831, `self.inventory = shop.inventory().clone()` at 839).

**Unsure:**
- "This leaves 62 of the 64 mapped vendors with runtime item IDs" and "1,199 regional NPC rows" / "192 vendor roles": I could not count these with the search cap. `vendors.json` is non-empty, and the W47c test prints these counts, but I did not verify the numbers.
- Line 89–90, "Offers already marked offered, active or completed are hidden": `build_options` (`src/npc_interaction.rs:813-884`) adds only Active turn-ins from `quests_accepted`. Offers go through `offerable_quest_for_talk` (line 758) and the Talk→26/3 path in `gameplay/npc.rs:1035-1044`. I did not confirm that `can_offer` hides all three states.
- Line 140–143 ("The existing accepted opening files do not serialize…"): still true for `opening_world.rs::menu` (writes only 26/9), and `QuestMessage::encode_exact` still returns `None` for `QuestInfo` (`src/quest_engine.rs:580`). The gameplay path now emits 26/3 and 49/1 (`gameplay/npc.rs:1184`, `:1251`), so the note may want a sentence on that.
- Test pass/fail status at tip was not run; I only checked the source and test text.
