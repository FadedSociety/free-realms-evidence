<!-- fleet job=note-refresh id=Integration-Round-5 status=done turns=26 usd=0.0286 tokens(read,write,in,out)=[1061214, 65119, 54, 19745] model=claude-haiku-5-5 -->
# notes/Research/Integration Round 5.md

**Verdict:** Moderate drift. The dialogue (26/3, 26/6 to 26/4), save schema 7, `movement` being public, the Knocker filter, recipe and quest-engine wiring, and the 49/13 bundle sizes hold at the tip. Five statements about the 66/43 vendor status, the developer-teleport standoff, the Goodbye row, and the 49/2 length are false now, plus one seed list that is missing an entry.

**Corrections:**

1. `old:` The developer command arrives 2 m from the target facing it
   `new:` The developer command arrives 5 m from the target facing it
   `why:` repo:prototype/osfr-tools/src/dev_teleport.rs:11 (`pub const STANDOFF: f32 = 5.0;`, with the comment that 2.0 put the player on top of the NPC). The arrival is 5 m out, not 2 m.

2. `old:` Name matching, 2 m placement, candidate deduplication
   `new:` Name matching, 5 m standoff placement, candidate deduplication
   `why:` repo:prototype/osfr-tools/src/dev_teleport.rs:8-11 (STANDOFF = 5.0 m, interaction radius and facing).

3. `old:` 66/43 is bounded, open-shop-gated, parsed and logged only.
   `new:` 66/43 is open-shop-gated, validated against local stock and proximity policy, and runs through the Coin Store `buy_vendor` path, returning a transaction result; the client price is ignored.
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:787-855 (`npc_merchant_buy_66_43` calls `validate_merchant_item_66_43`, then `shop.buy_vendor(...)`, and sets `self.inventory` from the shop) and repo:prototype/osfr-tools/src/npc_interaction.rs:675-683 (the open-shop gate).

4. `old:` 66/43 remains non-transactional because its client field meanings are unresolved.
   `new:` 66/43 is transactional through the local CoinShop buy path (stock, active-shop and proximity checks); only its client field meanings remain reconstructed (R).
   `why:` repo:prototype/osfr-tools/src/gameplay/npc.rs:799-855 (`(R)` comment on field use, then `buy_vendor` / `refuse_vendor_buy`).

5. `old:` the 26/3 choice row is now `[300, 17, 8075, 0, 0]` (little-endian dwords).
   `new:` the 26/3 choice row is now `[300, 17, 8075, 0, 18]` (little-endian dwords).
   `why:` repo:prototype/osfr-tools/src/npc_interaction.rs:1165-1167 (`goodbye_dialogue_choice` returns `[300, 17, GOODBYE_STRING_ID, 0, 18]`), and repo:prototype/osfr-tools/tests/npc_interaction.rs:632-635 (asserts `[300, 17, 8075, 0, 18]`).

6. `old:` The display string occupies dword 3; the two image parameters are zero.
   `new:` The display string occupies dword 3; dword 4 (image) is zero and dword 5 (background set) is 18.
   `why:` repo:prototype/osfr-tools/src/npc_interaction.rs:1150-1155 (DWORDs 5 and 4 are background set and image; `DialogTest` uses set 18) and repo:prototype/osfr-tools/src/npc_interaction.rs:1162 (quest row also uses 18). This also matches `ui:ScriptsBase.lua:12511-12513`.

7. `old:` The client 49/2 accept/decline decoder now accepts the native 9-byte request
   `new:` The client 49/2 accept/decline decoder accepts the native 11-byte request (six-byte header, u32 quest ID, u8 accept flag)
   `why:` repo:prototype/osfr-tools/src/npc_interaction.rs:1171-1173 (`decode_quest_reply_49_2` requires `packet.len() == 11`; the wire example is 11 bytes). No 9-byte path exists in repo:prototype/osfr-tools/src/gameplay/npc.rs:262-300.

8. `old:` Opening saves seed IDs 11, 70 and local Copper sample 2002
   `new:` Opening saves seed IDs 11, 70, 4 (the client Copper Bar row) and local Copper sample 2002
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:866-867 (`learned_recipes.extend([11, 70, 4, 2002])`).

**Unsure:**

- The Talk claim "sends a 26/3 with one localized Goodbye response" is true for non-quest NPCs. For a quest NPC the 26/3 holds the quest row plus Goodbye (`npc.rs:1182-1183`), and an offer sends 49/1 alone (`npc.rs:1071-1073`). I left it unchanged because "one" is accurate for the ordinary case.
- Test counts in the verification tables are run snapshots, so I did not correct them. Current `#[test]` attributes: `tests/npc_interaction.rs` has 20, and `tests/dev_teleport.rs` has 10 with 8 `#[ignore]` (the note says 13/14 and "1 passed / 7 ignored"). These may be worth refreshing if the tables are meant to be current.
- The W62 line "Goodbye's response tuple reuses the recovered end-screen `(300,17,3)` action" predates W63's change to `[300,17,8075,0,18]`. W63 supersedes it, so I did not edit it.
- I did not verify the "50 zone-less NPC rows", "403/33/215/651" quest-link counts, the 14,982-update movement replay, or the native-only evidence (`0x...` addresses, `lab/` paths).
