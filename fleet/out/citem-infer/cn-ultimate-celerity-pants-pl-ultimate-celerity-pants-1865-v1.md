<!-- fleet job=citem-infer id=cn-ultimate-celerity-pants-pl-ultimate-celerity-pants-1865-v1 status=done turns=10 usd=0.0072 tokens(read,write,in,out)=[134917, 29710, 22, 4258] model=claude-haiku-5-5 -->
# {n}Ultimate Celerity Pants{pl="Ultimate Celerity Pants"}

{"item": {"name": "Ultimate Celerity Pants", "locale_id": 1865, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop sale, tint group 1 (definition 2078; item_id 2078, category 104)", "where": "Coin Shop", "price": "1266 coins (regular); member price 1139 coins (10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2078 (line 587; purchase_price_coins 1266, member_price_coins 1139, rows built from Legacy CoinStoreItems per source_tags L1/L2/L4)"},
  {"type": "coin_shop", "detail": "Coin Shop sale, tint groups 2 and 3 (definitions 2084, 2085; item_ids 2084 and 2085, category 104)", "where": "Coin Shop", "price": "957 coins (regular); member price 861 coins (10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json items 2084 (line 590) and 2085 (line 591)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 1865 is '{n}Ultimate Celerity Pants' (item kind), slot 4, item class 24, model freestyle_<race>_<gender>_legs_bootcutpants.adr", "source": "locale:1865; client definition pack"},
  {"claim": "Store rows exist for this item: item 2078 at 1266 coins, items 2084 and 2085 at 957 coins, all category 104 with member discount 10%", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 587, 590, 591"},
  {"claim": "stores.json documents that item rows with L1 tags come from Legacy CoinStoreItems (Coin Shop) with Legacy ClientItemDefinitions.Cost as the price", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 26-30 (source_tags L1, L2)"},
  {"claim": "Sibling items 'Elite Black Ultimate Celerity Pants' (locale:1862) and 'Elite Pink Ultimate Celerity Pants' (locale:1857) are separate names and are not this item", "source": "locale:1862; locale:1857"},
  {"claim": "No wiki page, article fact, video frame, or coin vendor stock entry names this item", "source": "lookup over wiki, articles, video returned no matches for 'Ultimate Celerity Pants' / 'Celerity Pants'"}
 ],
 "confidence": 0.4,
 "open": [
  "The first-pass tag called the source a vendor. The store row is a Coin Shop (CoinStoreItems) row, not a vendor stock entry; no vendor in the repo stocks definition 2078, 2084 or 2085, so no vendor source is recorded.",
  "The client definition says 14 definitions but lists 12 definition_ids. The extra 15062-15077 IDs (15062, 15063, 15064, 15067, 15069, 15072, 15075, 15076, 15077) have no stores.json row in the repo, so their sale status is unknown.",
  "The coin_store_prices in the pack (957, 1266) are the purchase prices from stores.json, not item IDs. The pack's cited 'store item' references were checked against stores.json rows 2078, 2084, 2085.",
  "No wiki page, article, or video confirms the Coin Shop listing or its date. Live status is unconfirmed; the store data may be the Legacy (2009-2014) price rather than a verified retail price.",
  "The Feb 11th Hotfix note (locale:1864) concerns member-only flagging and does not name this item, so it is not used as a source.",
  "No quest reward, drop, event, prize wheel, crafting, collection, or membership source found in the pack or repo. Retirement date unknown."
 ]}
