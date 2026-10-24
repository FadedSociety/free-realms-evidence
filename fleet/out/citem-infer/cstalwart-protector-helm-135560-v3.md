<!-- fleet job=citem-infer id=cstalwart-protector-helm-135560-v3 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[16971, 13001, 8, 2594] model=claude-haiku-5-5 -->
# Stalwart Protector Helm

{"item": {"name": "Stalwart Protector Helm", "locale_id": 135560, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of the helm's tint variants (store item ids 46560, 46561, 46562; tint groups 1, 2, 3). Link to the helm is by the Legacy client's own Comment/Id pairing, not by a wiki listing.", "where": "Coin store, category_id 101 (wiki/in-game category name not confirmed)", "price": "715 coins (member price 643 coins at 10% member discount; sell-back 71 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13025-13027; refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 957932-957933 (Comment 'Stalwart Protector Helm', Id 46560) and 957955-957956 (Id 46561); refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json lines 58848 and 58853 (Ids 46560, 46561)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Store rows for item 46560, 46561, 46562 are category 101 at purchase 715 coins, member 643, sell 71, no_sale false, tint groups 1-3, with source tags L1, L2, L4, R2, T633, R1.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13025-13027 (re-read and confirmed)"},
  {"claim": "Client text entry 135560 is 'Stalwart Protector Helm'.", "source": "locale:135560 (confirmed via lookup)"},
  {"claim": "Legacy client definitions carry Comment 'Stalwart Protector Helm' with Id 46560 and 46561, and Legacy CoinStoreItems lists 46560 and 46561 in category 101 with the helm's tint groups.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json 957932-957956; refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json 58848-58861 (confirmed by grep)"},
  {"claim": "Store row 46554 (715 coins, category 101) and rows 46530/46531 (9453 coins) are in the same category but are not tied to this helm by any source; the Legacy grep shows 46554 is not a helm id.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13022-13024"},
  {"claim": "No wiki page, article, or video names the helm; no vendor, quest, drop, crafting, or event source was found.", "source": "lookup (wiki, client, articles) returned only the client text line"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin shop source is supported by the Legacy Comment/Id pairing for 46560-46561 and by the store rows; it still has no wiki or in-game confirmation. The 'Coin Shop' label is an internal name; the wiki category was not found.",
  "Variant count is unresolved. The pack says 35 definitions and lists 12 ids (46560-46571); the Legacy ClientItemDefinitions grep shows at least 20 entries with the helm's Comment. Neither count is verified; the true number needs a full pass over the Legacy file.",
  "Id 46562 has the store row and the 'Stalwart Protector Helm' pairing is not checked line by line in Legacy (only 46560 and 46561 were confirmed by grep).",
  "The 'Hats' category label for category 101 is an unverified research-note label (notes/Research/Pieces/045 Cosmetic equipment.md:46, not re-read) and is not used as a source.",
  "Retirement and live status are unknown. Live-era source tags (L1, L2, L4, R2, T633, R1) and no_sale=false are weak support only. No sale-end date was found.",
  "The pack's coin_store_prices value 715 matches these rows; the store item 715 (9453 coins) is a different item and was not used.",
  "No vendor, quest, drop, crafting, or event source was found for the helm. The Stalwart Protector Hammer recipe is a separate item and was not used as evidence."
 ]}
