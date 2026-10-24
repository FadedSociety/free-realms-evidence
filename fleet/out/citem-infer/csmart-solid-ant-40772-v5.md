<!-- fleet job=citem-infer id=csmart-solid-ant-40772-v5 status=nothing_found turns=2 usd=0.0025 tokens(read,write,in,out)=[6498, 10327, 6, 2347] model=claude-haiku-5-5 -->
# Smart Solid Ant

{"item": {"name": "Smart Solid Ant", "locale_id": 40772, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 3556 is named 'Smart Solid Ant' (locale 40772, npc_name tag). Its description says it can be added to the Solid Ants Collection. The client definition has no coin_store_prices, models, or slots beyond [0].", "source": "locale:40772; pack client_definition (definition_ids [3556])"},
  {"claim": "Collection 71 'Solid Ants' (name_id 7722) lists this item as entry 488 (definition 3556). This is collection membership, not an acquisition source.", "source": "prototype/osfr-tools/data/content/collection_catalogue.json lines 5099-5107 (per pack)"},
  {"claim": "Collection 71's completion reward (coins 5, item 23072 x1, xp profile 49) is a reward for finishing the collection, not a source of this item.", "source": "prototype/osfr-tools/data/content/collection_catalogue.json (collection 71 reward block, per pack)"},
  {"claim": "stores.json has a coin-store row with item_id 40772, category 101, tint group 1, purchase 320 coins, member price 288, sell 32. The pack's earlier 'no store hits' claim was wrong. This row is NOT adopted as a source (see open).", "source": "repo:prototype/osfr-tools/data/content/stores.json:12517"},
  {"claim": "The row's item_id mapping is unverified. The pack's check against item_id 5245 fails: stores.json:6131 prices item_id 5245 at 270 coins, while locale 5245 is '1,000 Coin', so that row does not show store item_ids are locale ids. The source_tags (L1, L2, L4, R2, T633, R1) are identical across unrelated rows (e.g. 40703, 40777), so they do not identify a vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6131, :12510-12522; locale:5245"},
  {"claim": "Lookup of 'Solid Ant' in wiki, articles and video returned no matches. No quest, drop, event, prize wheel, or crafting source was found.", "source": "lookup(wiki, articles, video) 'Solid Ant': no matches"}
 ],
 "confidence": 0.2,
 "open": [
  "UNCONFIRMED CANDIDATE: stores.json:12517 (item_id 40772, category 101, 320 coins, member 288, sell 32). It is not listed as a source because the client definition has no coin_store_prices entry to corroborate it, the item_id keying is unproven (the 5245 check fails), and the category 101 tag set is generic. If confirmed, it would be a coin-store vendor sale; the vendor, zone and date are unknown.",
  "No wiki page, article, video, quest, drop, event, prize wheel or crafting source names this item. The wiki 'List of Collections' names a Solid Ants collection but gives no member or reward data.",
  "Retired and live status unknown. No dated source exists. The first-pass 'live: yes' is only a hint.",
  "Collection membership is not an acquisition source and is not listed as one.",
  "Critique fixes: the stores.json row is now recorded as an unconfirmed candidate, not a vendor source. The 'no store hits' claim is withdrawn. The 5245 keying check is marked as failed. Wireable is not set; the item has no confirmed acquisition source."
 ]}
