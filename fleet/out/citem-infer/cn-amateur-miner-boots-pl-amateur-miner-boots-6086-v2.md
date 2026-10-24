<!-- fleet job=citem-infer id=cn-amateur-miner-boots-pl-amateur-miner-boots-6086-v2 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[31958, 16817, 10, 2337] model=claude-haiku-5-5 -->
# {n}Amateur Miner Boots{pl="Amateur Miner Boots"}

{"item": {"name": "Amateur Miner Boots", "locale_id": 6086, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin vendor. The client definition carries a coin store price (store row for item 2452, category 105, tint group 1). The row has no vendor, NPC or store-name field, so the vendor is not identified.", "where": null, "price": "291 coins (member price 261 coins, 10% member discount; sell-back 29 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:656 (item_id 2452)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 6086, 'Amateur Miner Boots'; slot 5, class 12, model worker_<race>_<gender>_feet_strappedboots.adr; one definition (2452).", "source": "locale:6086"},
  {"claim": "Coin store row for item 2452 exists: category 105, tint group 1, purchase 291 coins, member 261, sell 29, no_sale false. Source tags L1, L2, L4, R2, T633, R1 show legacy coin-store presence only.", "source": "repo:prototype/osfr-tools/data/content/stores.json:656"},
  {"claim": "The same 291/261/29 price, category 105 and tint group 1 appear on other rows in the same block (e.g. item 2239 at stores.json:650, and 2235 at 649 at a different price), so the price does not single out 2452 or name its vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json:649-650"},
  {"claim": "Wiki Miner job vendors sell tier-named Miner boots: Witts ('Strip [Miner] [Boots]', 'Slop [Miner] [Boots]'), Boddington ('Long Wall [Miner] [Boots]', 'Mountaintop [Miner] [Boots]'), Grasberg ('Quarry [Miner] [Boots]'), Yanaco ('Landfill [Miner] [Boots]'), Kallie ('Subsurface [Miner] [Boots]'), Cortez ('Drift [Miner] [Boots]'), Vaal ('Open-Pit [Miner] [Boots]'). Amateur Miner Boots is not in these listed sales. Only the lookup listings were read, not the full vendor pages, so this does not rule any vendor in or out.", "source": "wiki pages Witts, Boddington, Grasberg, Yanaco, Kallie, Cortez, Vaal (lookup wiki 'Miner Boots')"},
  {"claim": "No wiki page, article, or video names Amateur Miner Boots (lookup client/wiki/articles/video 'Amateur Miner Boots' returns only locale:6086). No quest reward, drop, crafting or event source found.", "source": "lookup client/wiki/articles/video 'Amateur Miner Boots'"}
 ],
 "confidence": 0.35,
 "open": [
  "Vendor not identified. The store row has no vendor link, and the coin-store price is the only evidence of a coin sale. The vendor-to-store link must be found in the repo before this is published.",
  "Live status unknown. Legacy store tags only; no wiki or article confirms current sale or retirement.",
  "No quest reward, enemy drop, crafting, or event source found for the Amateur tier.",
  "Client definition description is blank. The Amateur set (Boots 6086, Gloves 6106, Pants 35474, Shirt 6063, Hat 35358, Shovel 2180) is named in the cluster, but its sources were not checked here.",
  "Critiques addressed: the unnamed-vendor claim is kept only as a price-only lead; the shared-price issue is stated; live and retired are left unknown; the Miner-vendor absence claim is limited to the listings read."
 ]}
