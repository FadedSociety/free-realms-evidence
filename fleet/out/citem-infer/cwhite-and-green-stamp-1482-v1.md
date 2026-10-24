<!-- fleet job=citem-infer id=cwhite-and-green-stamp-1482-v1 status=done turns=12 usd=0.0082 tokens(read,write,in,out)=[171981, 24587, 26, 6775] model=claude-haiku-5-5 -->
# White and Green Stamp

{"item": {"name": "White and Green Stamp", "locale_id": 1482, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 1482 (item definition 23607) of the 8-stamp colour-stamp set (catalogue collection id 200, name_id 67566, wiki-less). Completing the set (Multicolor, Brown and Green, Pink and Green, White and Green, White and Honey, Blue and Purple, Red and Orange, Black and Brown Stamps) gives 2 coins, item 23613 x1, and adds collection 201.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:16242-16337 (collection 200 entries at 16249-16321, reward at 16323-16337)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item 1482 'White and Green Stamp' is name_id 67220 with item_definition_id 23607 and icon 2181, an entry of collection 200.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:16287-16294; locale:1482"},
  {"claim": "Client definition for item 3334 carries no coin store price, no models, and only the generic text 'This item can be added to a collection.'", "source": "client definition in pack; locale:1482"},
  {"claim": "The stamp set is a sibling of the wiki-documented Postman Stamps collection (Wilds, Briarwood, Chugawug, Penguin, Free Realms, Robgoblin, Ayani, Snowhill Stamps; catalogue ids 1470-1477), which the wiki lists under the Postman job's collections, spawn type 'Job Material'.", "source": "wiki: Job Specific (Collections); repo:prototype/osfr-tools/data/content/collections.json:4538-4610; collection_catalogue.json:16150-16240"},
  {"claim": "The client's only collection named for stamps is 'Postman Stamps Collection' (locale:132354), which is the wiki set of 8 Postman stamps, not the colour set this item belongs to.", "source": "locale:132354 via lookup client"},
  {"claim": "Wiki 'Job Specific (Collections)' and 'Postman' list only the Postman Stamps set and the Postman Postcards/Packages sets; no page names the colour stamps, their drop or purchase method.", "source": "wiki: Job Specific (Collections); wiki: Postman"}
 ],
 "confidence": 0.35,
 "open": [
  "How a player obtains a single White and Green Stamp is not documented anywhere in the pack: no wiki page, article, video frame, vendor, quest, or drop names it. The 'Job Material' spawn type on the sibling set suggests Postman job gathering, but that is unconfirmed for this colour set.",
  "Name of collection 200 (name_id 67566) is not resolved in the locale lookup; the 'colour stamp' collection name is inferred from its entries.",
  "No coin store price in the client definition (coin_store_prices empty), so no vendor sale is cited.",
  "Pack's 'vendor_stock' and 'mentioned_by_other_answers' are empty; nothing to cross-check.",
  "Retired/live status unknown: the first-pass 'live: yes' is a hint only and no wiki or article source confirms it.",
  "The collection-200 reward (2 coins, item 23613, adds collection 201) is from repo data; item 23613 is not identified."
 ]}
