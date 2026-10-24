<!-- fleet job=citem-infer id=crusty-spoon-1320-v1 status=done turns=9 usd=0.0080 tokens(read,write,in,out)=[142138, 29823, 20, 5767] model=claude-haiku-5-5 -->
# Rusty Spoon

{"item": {"name": "Rusty Spoon", "locale_id": 1320, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Collection piece (entry 3 of 8) of the Spoons collection (collection id 34, name locale 38713, item definitions 3170-3177: Bent Spoon 1318, Silver Spoon 1319, Rusty Spoon 1320, Primitive Spoon 1321, Fancy Spoon 1322, Soup Spoon 1323, Musical Spoon 1324, Wooden Spoon 1325). The item's description, locale 132294 'Spoons Collection', says it can be added to the Spoons Collection. No vendor, drop or quest that hands out this spoon was found.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1428-1508 (collection id 34, entry index 3 = item_definition_id 3172); locale:38713; locale:38714; locale:132294; wiki:List of Collections ('Spoons' entry)"},
  {"type": "collection", "detail": "Completing the Spoons collection (reward block for collection 34): 7 coins, item definition 23238 x1, 50 XP, and collection_add 154. This is the set-completion reward, not the way to get the individual spoon.", "where": null, "price": "7 coins (set reward)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1510-1528"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for locale 1320 is 'Rusty Spoon'; item definition 3172 has the description 'This item can be added to the Spoons Collection' (locale 132294 = ui 'Spoons Collection').", "source": "locale:1320; locale:132294"},
  {"claim": "Rusty Spoon is entry index 3 of the 8-piece Spoons collection (collection id 34, name_id 38713, description 38714 'You'll always be ready to stir up some trouble with this collection in your pockets!'), with item_link 'sanctuary'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1428-1508"},
  {"claim": "The Spoons collection appears as an entry in the wiki's List of Collections page, so the collection exists on the wiki, but the page lists no source for the individual spoons.", "source": "wiki:List of Collections (page_id 2038, revision 27852)"},
  {"claim": "The collection's set-completion reward is 7 coins, item 23238 x1, 50 XP, collection_add 154.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:1510-1528"},
  {"claim": "Client text 'Old Rusty Spoon' (locale 140824) is a separate item name, not Rusty Spoon.", "source": "locale:140824"},
  {"claim": "No coin store price, vendor stock, quest reward, drop or wiki article was found for item 3172 or 'Rusty Spoon'.", "source": "repo stores.json/vendors.json search; lookup wiki/articles/video; refs search"}
 ],
 "confidence": 0.5,
 "open": [
  "How a player obtains an individual Rusty Spoon is not established. The collection entry says item_link 'sanctuary', which points to the Sanctuary server's data, not to a vendor or drop. Needs a Sanctuary/refs or wiki source for the spoon itself.",
  "No coin store price in the client definition (coin_store_prices is empty) and no stores.json row for 3172, so no vendor sale is cited.",
  "Retired and live status unknown. The collection is listed on the wiki, but no date or retirement note was found.",
  "Reward item 23238 (collection completion reward) was not named; it is not this item and was not looked up.",
  "The cheap model's first pass says 'live: yes'. That is a hint only and not used as evidence; the sources above support 'collection' kind but not a live status.",
  "Locale text 'Old Rusty Spoon' (140824) exists and may be a separate item or a later variant; not checked."
 ]}
