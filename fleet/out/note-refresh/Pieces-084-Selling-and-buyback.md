<!-- fleet job=note-refresh id=Pieces-084-Selling-and-buyback status=nothing_found turns=24 usd=0.0254 tokens(read,write,in,out)=[902289, 66400, 50, 16140] model=claude-haiku-5-5 -->
# notes/Research/Pieces/084 Selling and buyback.md

**Verdict:** current. Every checkable claim about our code and its status I could reach still holds at the tip; no correction is needed.

**Corrections:** none.

What I checked and confirmed:
- Module and tests exist and match the note: `prototype/osfr-tools/src/restoration/piece_084.rs` (526 lines) defines `sell_payout` (l.214), `buyback_cost` (l.224), `VendorLedger` with `grant`, `adjust_coins`, `sell`, `buy_back`, `record_purchase`, `clear_transaction_history`, `snapshot`, `restore`, and `buyback_rows` (l.278–525), plus `BUYBACK_ROWS_FILTER_RECOVERED`, `BUYBACK_RESULT_REJECTED = 2`, and the `VendorError` to wire-code mapping (l.173–211).
- Behaviour claims match the code: `buy_back(id, 0)` buys the outstanding amount (l.438–441); partial buyback decrements `quantity_remaining` and only sets `bought_back` at zero (l.459–460); `sell` checks every refusal before mutating (l.364–413); restore keeps the GUID (serde, l.234–284); clear keeps ids counting, since `next_transaction_id` is not reset (l.513–515).
- Test counts: `prototype/osfr-tools/tests/piece_084.rs` has 16 `#[test]` (matches "16 passed"); `tests/pieces/test_piece_084.py` has 16 `test_` methods (matches "Ran 16 tests").
- Not yet registered: no `pub mod piece_084` or `#[path]` include for it in `src/`; the `#[path]` include in `tests/piece_084.rs` is still the only wiring, as the note says.
- `scripts/pieces/piece_084.py` and `tests/pieces/test_piece_084.py` exist.
- Client facts: `ScriptsBase.lua` has `CoinStore_TransactionHistory_DS.BoughtBack = 7` (l.3720), `ItemDefinitionSelect_DS.CoinSellPrice = 26` (l.3749), `CoinStore_PlayerSell_DS` ItemGuid 0 / Quantity 4 / Price 27 / NoSale 28 (l.3681–3709), `NpcMerchantV2:BuyBackItem` forwarding the id alone (l.54152), `PopulateBuyBackData` keeping `BoughtBack == 0` (l.54113), and `GetValidBuyBackItems` dropping `BoughtBack` "1" (l.53591). Locale 30148, 436335 and 428367 match the note's text. `FUN_00c76c60`, `FUN_00c76dd0`, `FUN_00c77030` and `FUN_00c78a10` exist in the client decompile with the shapes described.
- Community claims: the Sanctuary sell handler (`CoinStoreBuyFromClientRequestPacketHandler.cs`) sets `Result = 1`, `TransactionRecord.Type = 2`, pays `ResellValue * Quantity`, and never sets `TransactionRecord.Price` (l.42–170). The Sanctuary and FreeRealms-Legacy handler directories have no buyback handler, and the Sanctuary dispatcher (`BaseCoinStorePacketHandler.cs` l.31–38) has no case for opcode 12. The `12 => "CoinStoreBuyBackRequestPacket"` reader mapping and the emulator's `CoinStoreBuyBackRequestPacket = 15` both match the Conflict section. Result-code comments match `CoinStoreTransactionCompletePacket.cs` l.10–19.
- The wiki-vs-catalogue split holds: "Zipped Leather Jacket" and "Rugged Winterwear Jacket" appear in the community catalogue, and the other eight wiki-only rows (Buckled, the Strapped and Tattered shirts, four Proof of Training) do not, so "eight of them have no counterpart" is correct.

**Unsure:**
- Hashes in the Evidence and Artifacts tables were not recomputed (no hashing tool here). The note already says the bundle hash changes on every run.
- The 1,383-row emulator file, the 1,229-of-1,230 `max(1, cost/10)` count, the 58,800-row catalogue count, and "4 gaps" in the checker output were not recounted.
- The leaked server enum at `lab/decompiled/server/LibSOE/SOE/BaseCoinStorePackets.cs` is not in the searchable roots. The `= 15` value was confirmed only in the community emulator's `PacketCodes.cs`, which the note also cites.
- Context, not a correction: the tip already has a live buyback path. `prototype/osfr-tools/src/npc_interaction.rs` defines `COIN_STORE_BUY_BACK = 12` (l.44), routes it at l.582–641, and `prototype/osfr-tools/src/coin_shop.rs` implements `buy_back_with_context` (l.897–957). The note's "every pinned server ... unreachable buyback half" is scoped to the community references and stays true. A reader could still take "the gap this piece fills" to mean our server lacks buyback, so the lead may want to say explicitly that `coin_shop.rs` is a separate, existing authority that this ledger has not been wired into.
