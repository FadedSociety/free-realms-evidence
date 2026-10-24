<!-- fleet job=citem-infer id=cfrozen-orchid-17544-v1 status=done turns=10 usd=0.0102 tokens(read,write,in,out)=[214720, 43954, 22, 5038] model=claude-haiku-5-5 -->
# Frozen Orchid

{"item": {"name": "Frozen Orchid", "locale_id": 17544, "kind": "collection"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (vendor/NPC not identified in our data; stock list records a 10,000-coin price for item 17544, tint group 1, store category 200, marked no_sale)", "where": null, "price": "10000 coins (member price 9000 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 17544 (line 4335; source FreeRealms-Legacy CoinStoreItems)"},
  {"type": "collection", "detail": "Snowhill Orchids collection (wiki list entry 'Snowhill Orchids', name_id 17578; the Frozen Orchid is one of the Snowhill Orchids collection items, per its client description 'This item can be added to the Snowhill Orchids Collection')", "where": "Snowhill", "price": null, "currency": null, "source": "wiki:List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections, rev 27852, 2013-07-13); locale:1423 / locale:132497; repo:prototype/osfr-tools/data/content/collections.json wiki:3:87"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Frozen Orchid is client item name_id 17544, definition 9176, kind collection-type item with description 'This item can be added to the Snowhill Orchids Collection'", "source": "locale:17544; locale:132497; repo:prototype/osfr-tools/data/content/collections.json wiki:3:87"},
  {"claim": "Snowhill Orchids is a wiki-listed collection under Snowhill, on the List of Collections page", "source": "wiki:List of Collections"},
  {"claim": "Store data lists client item 17544 in coin store category 200 at 10000 coins, member price 9000, no_sale true, with the same 10000-coin entry for the sibling orchid/carnation items 17539-17549", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 4305-4340"},
  {"claim": "The Frozen Orchid is one of a 11-item cluster (Glacial Lily through Wintery Carnation, locale 17539-17549) that shares the same coin store entries and collection description", "source": "locale:17539 to locale:17549; repo:stores.json lines 4330-4340"},
  {"claim": "The first-pass tag (live yes, kind collection) matches the client text and the collection listing", "source": "jev_first_pass in the evidence pack"}
 ],
 "confidence": 0.5,
 "open": [
  "The client definition field coin_store_prices is empty, but stores.json lists a 10000-coin entry for item 17544. Treated the stores.json entry as the coin store price; the discrepancy needs checking against CoinStoreItems.json.",
  "The coin vendor/NPC that sells item 17544 is not identified. Store category 200 is not named in our data, and the stores.json entry gives no vendor name.",
  "Our store data marks the item no_sale, so it is probably not resold to vendors. Whether it is still purchasable, and when it was retired, has no source here.",
  "How the Frozen Orchid itself is obtained (harvesting Snowhill flowers, a quest, or a drop) is not sourced. The wiki collection entry shows only the collection membership. The rare-flower wording ('1 out of every 9 flowers found is rare', locale:2221723942) suggests a flower harvest source, but that is not confirmed for this item.",
  "Wiki price data for this item was not found, so no sale-price or second-price check was possible.",
  "The wiki list is a 2013 revision; the item's live status after 2013 is unknown."
 ]}
