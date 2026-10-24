<!-- fleet job=citem-infer id=cboiling-lakeshore-water-sample-41155-v2 status=done turns=4 usd=0.0027 tokens(read,write,in,out)=[26157, 10379, 10, 2370] model=claude-haiku-5-5 -->
# Boiling Lakeshore Water Sample

{"item": {"name": "Boiling Lakeshore Water Sample", "locale_id": 41155, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Collection entry for the Lakeshore Water Samples collection (wiki category 8, key wiki:8:222). The item's client description reads 'This item can be added to the Lakeshore Water Samples Collection'. Collection entry list and reward are unknown in our data (entries_known false, entries empty, reward null).", "where": null, "price": null, "currency": null, "source": "locale:41155; repo:prototype/osfr-tools/data/content/collections.json:11243-11260; https://freerealms.fandom.com/wiki/List_of_Collections"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text for locale 41155 is 'Boiling Lakeshore Water Sample' with description 'This item can be added to the Lakeshore Water Samples Collection'; item definition 3939, no models, no coin_store_prices in the client definition.", "source": "locale:41155; client definition"},
  {"claim": "The Lakeshore Water Samples collection exists as wiki:8:222 and is listed on the wiki's List of Collections; our record has no entry list and no reward.", "source": "repo:prototype/osfr-tools/data/content/collections.json:11243-11260; https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "stores.json has a row for item 41155 in category 105 (tint group 1) at purchase_price_coins 1027, member_price_coins 924, sell_price_coins 102. The row names no store or vendor id, and the same price is shared by many items, so it is not counted as a confirmed vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12568"},
  {"claim": "Lakeshore quest 'Lakeshore Don't Drink the Water!' has Embir and Merri De'Flor dialog and objectives telling the player to get Merri to boil any water used for cooking. The text does not name the Boiling Lakeshore Water Sample item, so any link from the quest to this item is an inference.", "source": "locale:91196; locale:91208; locale:91194; locale:91195 (quest title)"},
  {"claim": "Sibling client items 41150-41160 are the same water-sample family (Lakeshore, Sanctuary, Snowhill).", "source": "client cluster locale:41150-41160"}
 ],
 "confidence": 0.35,
 "open": [
  "Coin store row: repo stores.json:12568 lists item 41155 at 1027 coins (member 924, sell 102) in category 105 with no store or vendor id. This is not a vendor sale until the store that carries category 105 is identified. The client definition lists no coin_store_prices. Do not treat this as confirmed purchasable until resolved.",
  "Acquisition is unproven. The client text only says the item can be added to the collection. The quest's boil step may make it, but no quest reward, item-grant row or drop names item 41155 or definition 3939.",
  "Collection reward for wiki:8:222 is null in collections.json; no reward is known.",
  "The prior answer's citations (entry 871 / catalogue line 9893, index 5, video:pjvw6oAT-zQ/00084.jpg, NPCs - Lakeshore.md:132) were not confirmed and are dropped here.",
  "Wireable: false. The only evidenced source is collection membership, with no evidenced price, quest, drop or event acquisition.",
  "Retired status not established; no source says it was removed or made unobtainable."
 ]}
