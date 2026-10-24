<!-- fleet job=citem-infer id=cearth-digger-helmet-6070-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[10860, 11065, 8, 2364] model=claude-haiku-5-5 -->
# Earth Digger Helmet

{"item": {"name": "Earth Digger Helmet", "locale_id": 6070, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale of Earth Digger Helmet (item_id 4, category 101, tint group 1) from the Legacy CoinStoreItems row; the specific coin vendor NPC is not named in any source in the pack", "where": null, "price": "828 coins (member price 745 coins, 10% member discount; resale 82 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:65 (item 4, purchase_price_coins 828; provenance tags L1, L2, L4, R2, T633)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name is 'Earth Digger Helmet', locale id 6070, item class 12, slot 1, 13 definitions (variants) in the client", "source": "locale:6070"},
  {"claim": "Coin store price of 828 coins for item_id 4 (category 101, tint group 1); the same 828 price appears for other helmet/clothing rows of the same family (items 576-578, 10616-10618, 10696-10698)", "source": "repo:prototype/osfr-tools/data/content/stores.json:65"},
  {"claim": "Wiki file tooltip for the Elite Pink Earth Digger Helmet shows Resell Value 945, Required Level 20 and Miner, and says it is equippable now; this is a sister variant, not this base name", "source": "image:item_tooltip (File:Elite Pink Earth Digger Helmet.jpg)"},
  {"claim": "Name cluster: Gold Farmer Helmet (6066), Elite Black Earth Digger Helmet (6067), Elite Pink Earth Digger Helmet (6068) sit beside it in the locale; the Earth Digger set also includes Coveralls, Boots and Gloves (locale 6080, 6099, 6119)", "source": "locale:6066, locale:6067, locale:6068, locale:6080, locale:6099, locale:6119"}],
 "confidence": 0.55,
 "open": ["No wiki article, article fact, or video frame names the base Earth Digger Helmet; the only wiki tooltip is for the Elite Pink variant, so the 828-coin price is from the repo store data (Legacy reference), not a wiki-verified price.",
  "The coin vendor that stocks item 4 is not identified in the repo answers; the vendor_stock list in the pack is empty. Need the vendor NPC and zone to complete the 'where' field.",
  "Price conflict: the wiki Elite Pink tooltip shows resell 945, while the store row sell_price for item 4 is 82 coins; the 945 figure may belong to the Elite Pink variant (its store row would need checking). Not reconciled here.",
  "The 828 price may apply to one tint (tint group 1); the store row does not confirm that the base 'Earth Digger Helmet' name maps to item 4 and not to another of the 13 definition ids. Mapping is inferred from the definition_ids list in the pack.",
  "Retirement status unknown: no wiki or article source states whether the coin sale ended."]}
