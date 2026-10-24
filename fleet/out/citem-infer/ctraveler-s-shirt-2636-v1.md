<!-- fleet job=citem-infer id=ctraveler-s-shirt-2636-v1 status=done turns=5 usd=0.0033 tokens(read,write,in,out)=[27358, 11415, 12, 3262] model=claude-haiku-5-5 -->
# Traveler's Shirt

{"item": {"name": "Traveler's Shirt", "locale_id": 2636, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of Traveler's Shirt (store item 268, category 103, tint group 1); 270 coins, member price 243 coins (10% member discount)", "where": "Coin store (Legacy CoinStoreItems)", "price": "270 coins (member price 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 165 (item_id 268)"},
  {"type": "coin_shop", "detail": "Same coin store listing family also covers definition 1495 (tint group 2), which is one of the 33 variants sharing the name", "where": "Coin store", "price": "270 coins (member price 243 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 5788 (item_id 1495)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Traveler's Shirt' is client text id 2636, item class, slot 3, shared by 33 definitions", "source": "locale:2636"},
  {"claim": "Client definition id 268 is the Traveler's Shirt and has a coin store entry at 270 coins, member price 243, sell price 27, with source tags L1, L2, L4, R2, T633, R1", "source": "repo:prototype/osfr-tools/data/content/stores.json line 165"},
  {"claim": "The wiki Adventurer page lists Traveler's Shirt as part of the Traveler's clothing set, with Traveler's Wristband noted as acquired via a Yo-yos collection (the shirt's own acquisition is not stated)", "source": "wiki page: Adventurer"},
  {"claim": "A wiki file page exists for 'Traveler's Shirt (Guys)', confirming the item is a documented wiki item", "source": "wiki file: File:Traveler's Shirt (Guys).png"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin_store_prices value 270 in the pack is a price, not a store item id; the matching store row is item_id 268 (definition 268). Store item 270 is a different item (category 101) and is not this shirt.",
  "No wiki page states the coin store price or sale window for the shirt; the 270-coin price rests on repo stores.json (Legacy-derived), not a wiki category, so the price should be checked against a live wiki or forum source.",
  "Retirement status is unknown: the store row's source tags (R1, T633) do not say whether the listing was removed; no source states the shirt was retired or unobtainable later.",
  "Adventurer wiki page lists the shirt in the Traveler's clothing set but gives no acquisition method for the shirt itself; possible additional sources (set collection, quest, or drop) are unverified.",
  "Pack's vendor_stock is empty; no coin vendor other than the coin store was confirmed.",
  "Variants: 33 definitions share the name (races, tints). Only definitions 268 and 1495 were checked against store data; the rest (1496-1499, 17145-17151, 17151 and others) were not individually verified."
 ]}
