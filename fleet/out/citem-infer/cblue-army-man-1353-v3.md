<!-- fleet job=citem-infer id=cblue-army-man-1353-v3 status=done turns=4 usd=0.0019 tokens(read,write,in,out)=[18434, 6980, 10, 1775] model=claude-haiku-5-5 -->
# Blue Army Man

{"item": {"name": "Blue Army Man", "locale_id": 1353, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Army Men collection (8 entries: Green, Tan, Blue, Red, Orange, Purple, Gold, Grey Army Man). This item is a collection member only; no item-level acquisition source is verified.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Toys_(Collections) (wiki page 'Toys (Collections)', Army Men group lists [Blue Army Man]); repo:prototype/osfr-tools/data/content/collections.json lines 6172-6200 (key wiki:4:102, name 'Army Men', entry_count 8, entry 'Blue Army Man' at line 6194)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: locale:1353 'Blue Army Man', definition id 3205, description 'This item can be added to the Army Men Collection'. It is a collection item (slot 0, class 0), not a wearable or weapon.", "source": "locale:1353; client definition 3205"},
  {"claim": "The wiki Toys (Collections) page lists 'Blue Army Man' in the Army Men group of 8 colour variants.", "source": "https://freerealms.fandom.com/wiki/Toys_(Collections)"},
  {"claim": "The repo Army Men collection record (key wiki:4:102, entry_count 8) includes 'Blue Army Man' as an entry.", "source": "repo:prototype/osfr-tools/data/content/collections.json lines 6172-6200"},
  {"claim": "No coin store price exists for definition 3205, so no coin vendor sale is evidenced.", "source": "client definition coin_store_prices: []"}
 ],
 "confidence": 0.4,
 "open": [
  "Item-level acquisition is unknown. The Robgoblin / Southern Wilds / Common spawn in collections.json belongs to the whole Army Men collection (wiki:4:102), not to Blue Army Man; it is not recorded as an item drop here.",
  "The Gold Doll plus 21 coins completion reward belongs to the collection, not to this item.",
  "No coin price, vendor, marketplace, crafting, or quest source found for Blue Army Man.",
  "Retirement status unknown. Live status is unsure: the client definition exists, and the only later-dated evidence is the 2013-08-21 wiki revision (rev 31048). No retirement note was found, but absence is not proof of live status.",
  "Dirty Bottle (locale:1358) shares the client cluster but is not in the Army Men list; not checked. Cluster adjacency (locale:1350-1357) shows naming proximity only, not acquisition.",
  "wireable: false. Collection membership is the only evidence; a per-item drop, vendor or event source needs verification before a builder can wire an acquisition."
 ]}
