<!-- fleet job=citem-infer id=cslope-miner-shirt-133158-v1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[26699, 15586, 10, 2609] model=claude-haiku-5-5 -->
# Slope Miner Shirt

{"item": {"name": "Slope Miner Shirt", "locale_id": 133158, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale (vendor not named in our data); the stores.json reference price is 403 coins, 362 for members (10% discount). Stores data marks it as a reference price, not a captured NPC quote.", "where": null, "price": "403 coins (member price 362 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 76150 (purchase_price_coins 403, member_price_coins 362, sell_price_coins 40)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name 'Slope Miner Shirt' is locale 133158, item class 12, slot 3, model worker_<race>_<gender>_chest_rolledslvshirt.adr", "source": "locale:133158"},
  {"claim": "Slope Miner set (Shirt, Hat, Kerchief, Pants, Gloves, Boots) sits in the same locale block as the Landfill Miner set (133153-133163), the Miner job gear line", "source": "locale:133153-133163"},
  {"claim": "Store price 403 coins for item 76150 (the Slope Miner Shirt definition id), with a 10% member discount", "source": "repo:data/content/stores.json item 76150"},
  {"claim": "Sibling Landfill Miner Shirt (item 76144) is listed in the wiki Yanaco 'Sells' section, a Southvale Quarry crafting-station merchant who sells Miner job items", "source": "wiki Yanaco (https://freerealms.fandom.com/wiki/Yanaco); repo:prototype/osfr-tools/data/content/vendors.json:17482"},
  {"claim": "The wiki Merchants page places Yanaco at the crafting station near the Southvale Quarry", "source": "wiki Merchants"}],
 "confidence": 0.4,
 "open": ["No source names the Slope Miner Shirt as sold by Yanaco or any other vendor. The wiki Yanaco Sells list we retrieved is truncated and shows only Landfill Miner items, so the Slope set may be a separate coin store item, not a Yanaco stock item. Vendor attribution is unverified.",
  "The 403-coin price comes from our store data (a reference price, not a captured in-game quote). No wiki price, article or video confirms it.",
  "Whether the Slope Miner set is still sold, or was retired, is unknown. No wiki, article or video source covers it.",
  "Pack's vendor_stock was empty; the Landfill Miner Shirt sibling's 378-coin price (item 76144) does not apply to this item.",
  "No quest, drop, event or crafting source found for the Slope set. Not confirmed; the Slope set may also be a crafting output at the Southvale Quarry station, which is unverified."]}
