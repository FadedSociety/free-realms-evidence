<!-- fleet job=citem-infer id=cn-top-speed-shoes-pl-top-speed-shoes-1691-v1 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[18211, 10898, 10, 2913] model=claude-haiku-5-5 -->
# {n}Top Speed Shoes{pl="Top Speed Shoes"}

{"item": {"name": "Top Speed Shoes", "locale_id": 1691, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale, tint group 1 (item_id 14132, store category 105); the store's vendor/NPC name is not recorded in the repo data", "where": null, "price": "1266 coins (member price 1139 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3735 (item_id 14132)"},
  {"type": "vendor", "detail": "Coin store sale, tint group 2 (item_id 14133, store category 105); the store's vendor/NPC name is not recorded in the repo data", "where": null, "price": "715 coins (member price 643 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3736 (item_id 14133)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name string for item is 'Top Speed Shoes' (no description text)", "source": "locale:1691"},
  {"claim": "Two store entries for variants of this item exist, priced 1266 and 715 coins; these match the pack's coin_store_prices, which are the purchase prices of item_ids 14132 and 14133 (not the item ids 715 and 1266, which are unrelated items)", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 3735-3736"},
  {"claim": "Sibling shoe names in the same client cluster: High Velocity Shoes (1686), Elite Black Top Speed Shoes (1688), Elite Pink Top Speed Shoes (1689), Steady Pace Shoes (1696); same-family items share the Top Speed name prefix", "source": "locale:1686, locale:1688, locale:1689, locale:1696"},
  {"claim": "Other definition ids in the pack (1882, 1888, 14117-14131, etc.) have no store entries in stores.json, so the coin sale covers only item_ids 14132 and 14133", "source": "repo:prototype/osfr-tools/data/content/stores.json (search on item_id)"},
  {"claim": "Store rows carry source tags L1, L2, L4, R2, T633, R1 (same as other stocked items); these are data tags, not a dated release record", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 3735-3736"}],
 "confidence": 0.5,
 "open": ["No wiki page, article, image or video names Top Speed Shoes, so the wiki/official source for the coin sale is missing. The vendor NPC and store name for category 105 are not in the repo data; the sale is recorded only as a coin store entry.",
  "The 'Top Speed' item family (client cluster) has no quest, drop, event, prize wheel or crafting evidence in the pack; the pack's 'vendor' guess is supported only by the coin store data.",
  "The 1266 and 715 coin prices belong to tint variants (tint_group 1 and 2). Which tint matches which name variant (Top Speed vs Elite Black/Pink) is not established.",
  "Live status is unverified: jev's first pass says live, but no date or retirement source confirms it. The store tags suggest it was sold in several client builds (L1, L2, L4, R2, T633, R1); this does not prove it is sold today.",
  "The pack's 'client_name' and the 'title' field are the same string with the {n}/{pl} markup; the item name was taken as 'Top Speed Shoes'.",
  "Jev's first-pass source guess ('vendor') is a hint only and is backed only by the coin store entries."]}
