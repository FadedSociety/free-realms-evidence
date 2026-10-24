<!-- fleet job=citem-infer id=cn-landfill-miner-boots-pl-landfill-miner-boots-133153-v2 status=done turns=5 usd=0.0025 tokens(read,write,in,out)=[27291, 8400, 12, 2354] model=claude-haiku-5-5 -->
# {n}Landfill Miner Boots{pl="Landfill Miner Boots"}

{"item": {"name": "Landfill Miner Boots", "locale_id": 133153, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Yanaco (NPC 9500000323, Miner gear; wiki Sells list)", "where": "Greenwood Forest area (repo npc file greenwood_forest.json); the Southvale Quarry crafting-station location is not confirmed by the evidence read here", "price": "378 coins reference price (member 340, sell-back 37); not a captured in-game NPC quote", "currency": "coins", "source": "wiki page Yanaco, Sells section, https://freerealms.fandom.com/wiki/Yanaco (lists [Landfill] [Miner] [Boots]); repo:prototype/osfr-tools/data/content/vendors.json:17243-17262 (Yanaco item_ids include 76145) and :17523-17546 (stock row, stock_source wiki revision 2025-07-04T18:36:37Z); price: repo:prototype/osfr-tools/data/content/stores.json:15847 item 76145 purchase_price_coins 378, member_price_coins 340, sell_price_coins 37"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client defines Landfill Miner Boots as locale 133153, definition 76145, feet slot 5, class 12, shared worker feet model.", "source": "client definition in evidence pack (locale:133153)"},
  {"claim": "The wiki Yanaco page's Sells list includes [Landfill] [Miner] [Boots] alongside the other Landfill Miner pieces and Miner's shards, ring and pickaxe.", "source": "wiki page Yanaco, https://freerealms.fandom.com/wiki/Yanaco (confirmed via lookup)"},
  {"claim": "vendors.json records Yanaco stock including item 76145 with the wiki Sells listing as source, revision 2025-07-04.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:17243-17262, 17523-17546"},
  {"claim": "Store reference price 378 coins, member 340, sell-back 37. vendors.json labels this a reference price, not a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15847; vendors.json:17531"},
  {"claim": "The wiki excerpt does not show a price for the boots; the 378 figure is the stores.json reference only.", "source": "wiki Yanaco excerpt; vendors.json:17531"}
 ],
 "confidence": 0.7,
 "open": [
  "Price is a stores.json reference (378 coins, member 340, sell-back 37), not a captured NPC quote. Treat as unverified until an in-game quote is seen.",
  "The 'added 15 Oct 2013' date from the earlier answer is removed: no cited source supports it.",
  "The Southvale Quarry crafting-station location from the earlier answer is not supported by the evidence read here; only the Greenwood Forest npc file is cited.",
  "No wiki page exists for the Landfill Miner Boots itself; the vendor source rests on the Yanaco Sells list alone.",
  "Retirement not established: no source says Yanaco stopped selling it. Live status rests on the wiki Sells list and store data, not an in-game check.",
  "The Yanaco vendor stock list in vendors.json includes the other Miner items; they are outside this item's evidence."
 ]}
