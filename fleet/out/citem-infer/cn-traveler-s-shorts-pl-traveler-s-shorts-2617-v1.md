<!-- fleet job=citem-infer id=cn-traveler-s-shorts-pl-traveler-s-shorts-2617-v1 status=done turns=9 usd=0.0053 tokens(read,write,in,out)=[83387, 19682, 20, 3985] model=claude-haiku-5-5 -->
# {n}Traveler's Shorts{pl="Traveler's Shorts"}

{"item": {"name": "Traveler's Shorts", "locale_id": 2617, "kind": "clothing"},
 "sources": [
  {"type": "collection", "detail": "Briarwood Rare Exploration collection (rare coins placed throughout Sacred Grove; reward is Traveler's Shorts, both genders)", "where": "Briarwood (Sacred Grove)", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/12373-46070-836d3b412072.wiki lines 92-106 (CollectInfobox reward); video:4_QPQeGcivU/00042.jpg (\"You receive 1 [Traveler]'s [Shorts]\" during Briarwood rare exploration); video:CXeswcNcDTM/00076.jpg (\"Collection complete! Merry Vale Rare Exploration\" showing the shorts)"},
  {"type": "collection", "detail": "Listed in the Traveler's Clothing set on the Adventurer page (set of Traveler's Cap, Shirt, Wristband, Shorts, Boots, Backpack; Wristband specifically from Yo-yos collection in a Meta collection)", "where": null, "price": null, "currency": null, "source": "wiki page Adventurer (page:ns0, Traveler's Shorts listed in set); freerealms-wiki/wikitext/2101-46030-93596a5e3d45.wiki lines 94-110"},
  {"type": "vendor", "detail": "Coin store sale listed in client definition (coin_store_prices 270); the store row is item_id 270 in stores.json, purchase 270 coins, member price 243 coins, sell-back 27 coins", "where": "Coin store (category 101)", "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:166 (item_id 270); client definition coin_store_prices"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is locale 2617, '{n}Traveler's Shorts', with 66 variant definitions and 2 models (hiking shorts for female race model, cuffed cargo shorts for male)", "source": "locale:2617; client definition"},
  {"claim": "Wiki gallery lists 'Traveler's Shorts (Girls)' and '(Guys)' as Traveler's Clothing; shorts available for both genders", "source": "freerealms-wiki/wikitext/2101-46030-93596a5e3d45.wiki lines 94-110; wiki page File:Traveler's Shorts (Girls).png"},
  {"claim": "Video shows the shorts as 'Girls only' with resell value 27 and collection-complete message", "source": "video:CXeswcNcDTM/00076.jpg"},
  {"claim": "Coin store price 270 coins, member 243, sell 27 is attached to store item 270 in category 101, the same price as many other shorts/clothing rows", "source": "repo:prototype/osfr-tools/data/content/stores.json:166"},
  {"claim": "Traveler's Shorts appears in the Adventurer page set and the Briarwood rare exploration reward", "source": "wiki page Adventurer; freerealms-wiki/wikitext/12373-46070-836d3b412072.wiki:100"}
 ],
 "confidence": 0.55,
 "open": [
  "The coin store price 270 is not verified to belong to this item: stores.json item_id 270 is only a row ID, and the definition IDs (249, 267, 1435-1439, 1515-1519) were not mapped to store item IDs. Many other clothing items share the same 270 price, so the coin-shop source needs a definition-to-store-item check before it is trusted.",
  "The wiki gives no date or price for the Briarwood Rare Exploration collection; the collection reward may no longer be obtainable. Retired status is unknown.",
  "The Adventurer page does not state which collection gives the shorts; only the Briarwood Rare Exploration collection reward is tied to Traveler's Shorts by wiki and video.",
  "The Adventurer page and the Traveler's Clothing gallery are the only sources for the set. Whether the set was also a Coin Shop or Marketplace item is not evidenced.",
  "No wiki price, Station Cash price, or quest/drop source was found. The first-pass 'vendor' guess is unconfirmed beyond the store row above.",
  "Client definition has no description (empty)."
 ]}
