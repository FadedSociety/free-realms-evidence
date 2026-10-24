<!-- fleet job=citem-infer id=cstone-bookcase-147676-v2 status=done turns=4 usd=0.0031 tokens(read,write,in,out)=[23572, 13308, 10, 2402] model=claude-haiku-5-5 -->
# Stone Bookcase

{"item": {"name": "Stone Bookcase", "locale_id": 147676, "kind": "furniture"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash furniture listing: 'Stone Bookcase - SC 22' (section 'Furniture' in the wiki's Station Cash item list)", "where": "SC Marketplace", "price": "22 Station Cash", "currency": "station_cash", "source": "refs: freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:392 (the same list gives Stone Roundtop Coffee Table SC 22 and Snowhill Lodge Chair SC 22)"},
  {"type": "vendor", "detail": "Coin store vendor, not identified by name; store category 53, tint group 2, item 36477", "where": null, "price": "50 coins (member price 45 coins, 10% member discount); not sellable back (no_sale true)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:11948; client definition 36477 coin_store_prices 50"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item definition 36477 is named 'Stone Bookcase' (locale 147676), description 'Stone Age Style', furniture model hsg_bookcase_03.adr, single definition, no tint variants", "source": "locale:147676; client definition 36477 as supplied in the pack"},
  {"claim": "Our store data has a row for item 36477 in category 53 with purchase_price_coins 50, member price 45, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:11948"},
  {"claim": "The wiki's Station Cash furniture list prices 'Stone Bookcase' at SC 22. This conflicts with the 50-coin row. Other coin-priced items also sit in category 53, so the row does not name a currency or vendor by itself", "source": "refs: freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki:392"},
  {"claim": "The wiki Items page lists '[Stone] [Bookcase]' among furniture, so the wiki covers the item, but the Items listing gives no price", "source": "wiki page ns0 'Items' (lookup result)"},
  {"claim": "Community server resource files carry a 'Stone Bookcase' StoreBundles comment. The bundle records are SKU/bundle entries, not confirmed as coin sales, so this is not used as price evidence", "source": "refs: FreeRealms-Legacy/src/Resources/StoreBundles.json:14957; Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:14899"},
  {"claim": "Client text 'Curious Stone Bookcase' (locale 147680) is a sibling item in the same cluster; it is not part of this item's sources", "source": "locale:147680"}
 ],
 "confidence": 0.4,
 "open": [
  "Price conflict: the store row says 50 coins (category 53, no vendor named), while the wiki furniture list says SC 22 (Station Cash). Both are kept as sources. Neither is confirmed as the only sale channel. Check which store category 53 maps to, and which vendor stocks it, before trusting either price.",
  "The vendor NPC/location for the coin store row is not identified in the repo data.",
  "Retirement status is not established. The store row has no sell price and no_sale true, which does not show that the item was retired.",
  "Quest rewards, enemy drops, events, Prize Wheel, crafting and collections were not checked against this item. None was named in the pack or found in the searched sources.",
  "Live status is 'yes' from the client definition, the wiki listing and the store row, but no dated source confirms it is still sold."
 ]}
