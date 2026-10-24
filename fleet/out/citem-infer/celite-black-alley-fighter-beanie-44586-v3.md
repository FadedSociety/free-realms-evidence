<!-- fleet job=citem-infer id=celite-black-alley-fighter-beanie-44586-v3 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[5916, 14488, 6, 1958] model=claude-haiku-5-5 -->
# Elite Black Alley Fighter Beanie

{"item": {"name": "Elite Black Alley Fighter Beanie", "locale_id": 44586, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store row for item 9585 (category 101, no tint group). Only source with any evidence; the price is a shared tier, not confirmed for this item. Same 9453/8507/945 row also appears on item_ids 9583, 9618, 9620, 9653.", "where": "Coin Shop (category 101 store data)", "price": "9453 coins purchase; 8507 coins member price (10% discount); 945 coins sell-back. Unverified: a shared tier, not a wiki or capture price.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:2756; client definition coin_store_prices [9453]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for definition 9585 is 'Elite Black Alley Fighter Beanie', locale 44586; sister names are 'Alley Fighter Beanie' (44581) and 'Elite Pink Alley Fighter Beanie' (44584)", "source": "locale:44586; locale:44581; locale:44584"},
  {"claim": "Store row for item 9585 exists in category 101 with purchase 9453, member 8507, sell 945, no tint group, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json:2756"},
  {"claim": "The identical 9453/8507/945 price appears on other rows (9583, 9618, 9620, 9653), so the price looks like a default tier rather than an item-specific price", "source": "repo:prototype/osfr-tools/data/content/stores.json:2755, 2759, 2760, 2767"},
  {"claim": "A repo-wide search for the id 9585 finds only the stores.json row (plus unrelated id 29585 and text noise); no vendors.json entry stocks item 9585 in this repo", "source": "search repo '9585'"},
  {"claim": "Lookup of the name in client, wiki, articles and video returns only the three client locale lines; no wiki page, article fact or video frame names this beanie", "source": "lookup 'Alley Fighter Beanie' (client, wiki, articles, video)"}
 ],
 "confidence": 0.3,
 "open": [
  "The 9453-coin price is a shared category-101 tier in our store data, not a verified in-game or wiki price. Do not treat 9453/8507/945 as this item's confirmed price.",
  "The coin_shop source rests on one repo store row. No wiki, article, video or FreeRealms-Legacy capture confirms it was sold in the Coin Shop, or when. The earlier 'via FreeRealms-Legacy' attribution is not supported; refs has no CoinStoreItems row for 9585.",
  "Live status and retirement date are unknown. The generic source_tags (L1, L2, L4, R2, T633, R1) are shared across the tier and do not show current sale.",
  "No vendor, quest, drop, event, prize wheel, marketplace, crafting, collection or promotion source is evidenced. The earlier vendor claim was not re-verified beyond the repo id search above.",
  "The client description is empty, so use and any set bonus are unknown. Sister items 44581 and 44584 were not checked for sources.",
  "Wireable should be false until a price is confirmed by a wiki page, article or Legacy store capture."
 ]
}
