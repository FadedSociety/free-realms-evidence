<!-- fleet job=citem-infer id=copen-pit-miner-shirt-133170-v1 status=done turns=5 usd=0.0029 tokens(read,write,in,out)=[32912, 11534, 12, 2341] model=claude-haiku-5-5 -->
# Open-Pit Miner Shirt

{"item": {"name": "Open-Pit Miner Shirt", "locale_id": 133170, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Vaal (Miner gear merchant, Miner job; sells the Open-Pit Miner set)", "where": "Snowhill, crafting station near the Singing Crystal Mines", "price": "528 coins (stores.json reference price; member price 475 coins)", "currency": "coins", "source": "wiki:Vaal (Sells: Open-Pit Miner Shirt); repo:prototype/osfr-tools/data/content/vendors.json (Vaal, npc 9500000777, item 76162); repo:prototype/osfr-tools/data/content/stores.json item 76162 (purchase_price_coins 528)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133170 is 'Open-Pit Miner Shirt', definition 76162, slot 3, class 12, model worker_<race>_<gender>_chest_rolledslvshirt.adr", "source": "locale:133170; client definition in pack"},
  {"claim": "Wiki page Vaal lists Open-Pit Miner Shirt (with Kerchief, Overalls, Helmet, Gloves, Boots) under Sells", "source": "wiki:Vaal (Sells section, revision 2025-03-26)"},
  {"claim": "Vaal is a human NPC merchant at the crafting station near the Singing Crystal Mines in Snowhill; the Miner set was added 15 Oct 2013", "source": "wiki:Vaal; repo:notes/Build Guides/Content/Jobs/Miner.md:63,72"},
  {"claim": "Coin store reference price 528 coins, member price 475 coins, sell price 52 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76162 (category 103)"},
  {"claim": "Sibling items of the Open-Pit Miner set (Boots, Gloves, Helmet, Overalls, Kerchief; locale 133171-133175) share the same Vaal source", "source": "locale:133171-133175; repo:vendors.json Vaal stock"}
 ],
 "confidence": 0.8,
 "open": [
  "The 528-coin price is a stores.json reference price, not a captured NPC quote (vendors.json price_basis); the wiki Vaal page text retrieved did not show a price for the shirt, so confirm the live price against the wiki or a screenshot.",
  "No retirement date found; the wiki source retrieved does not say whether Vaal still sells the set, so retired is left null.",
  "Client description is empty; no wiki article page of its own, and no video frame confirms the shirt at Vaal.",
  "The stores.json entry has source_tags L1, L2, L4, R1, R2, T633 and category 103, which are not explained in the pack; the Vaal vendor link is the only sale source recorded."
 ]}
