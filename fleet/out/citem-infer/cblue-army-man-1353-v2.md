<!-- fleet job=citem-infer id=cblue-army-man-1353-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5198, 7008, 6, 1796] model=claude-haiku-5-5 -->
# Blue Army Man

{"item": {"name": "Blue Army Man", "locale_id": 1353, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Army Men collection (8 entries: Green, Tan, Blue, Red, Orange, Purple, Gold, Grey Army Man). Collection-level spawn: Robgoblin enemies. Per-item drop odds and any direct Robgoblin drop for Blue Army Man are not verified. Completion reward listed as Gold Doll plus 21 coins, which belongs to the collection, not to this item.", "where": "Southern Wilds", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json lines 6172-6256 (key wiki:4:102, client_id 1073741926, entries incl. 'Blue Army Man', spawn_type Robgoblin, area Southern Wilds, quality Common); wiki https://freerealms.fandom.com/wiki/Toys_(Collections) rev 31048 (2013-08-21), which lists Blue Army Man in the Army Men group"}],
 "retired": null,
 "live": "yes",
 "evidence": [{"claim": "Client definition: locale:1353 'Blue Army Man', definition id 3205, description 'This item can be added to the Army Men Collection'. It is a collection item, not a wearable or weapon.", "source": "locale:1353; client definition 3205"},
  {"claim": "The wiki Toys (Collections) page lists 'Blue Army Man' in the Army Men group (8 colour variants).", "source": "https://freerealms.fandom.com/wiki/Toys_(Collections) rev 31048; lookup of wiki page 'Toys (Collections)'"},
  {"claim": "The Army Men collection record gives spawn type Robgoblin, area Southern Wilds, quality Common, and reward Gold Doll plus 21 coins. These are collection-level fields.", "source": "repo:prototype/osfr-tools/data/content/collections.json lines 6172-6256"},
  {"claim": "No coin store price exists for definition 3205, so no coin vendor sale is evidenced.", "source": "client definition coin_store_prices: []"}],
 "confidence": 0.5,
 "open": ["The Robgoblin / Southern Wilds spawn is collection-level. Nothing verified says Blue Army Man itself drops from Robgoblins, so the item-level drop source and its odds are unverified.",
  "The Gold Doll and 21-coin reward is a collection completion reward and is not a source for Blue Army Man.",
  "No coin price, vendor, or marketplace listing was found for Blue Army Man.",
  "Retirement status is unknown. The absence of a retirement note is not evidence of live status. The 'yes' rests on the client definition and a 2013 wiki listing.",
  "The earlier citation of repo quest-lines/item-packs.json line 1952 was not verified and is dropped. Client cluster membership (locale:1350-1357) only shows naming proximity, not acquisition.",
  "Dirty Bottle (locale:1358) shares the client cluster but is not in the Army Men list; not checked."]}
