<!-- fleet job=citem-infer id=cshinobi-ninja-cowl-133243-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6126, 8518, 6, 2343] model=claude-haiku-5-5 -->
# Shinobi Ninja Cowl

{"item": {"name": "Shinobi Ninja Cowl", "locale_id": 133243, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coiled Viper, human NPC merchant who sells only Ninja job items; listed under Sells as 'Shinobi Ninja Cowl'", "where": "West of the Robgoblin Treasure Trove", "price": "unknown (no captured NPC quote)", "currency": null, "source": "https://freerealms.fandom.com/wiki/Coiled_Viper (Sells section, revision 2025-03-15); repo:prototype/osfr-tools/data/content/vendors.json:41327-41335 (price_basis: no captured retail NPC quote)"},
  {"type": "coin_shop", "detail": "Coin store reference price for item 76235 (category 101, tint group 1); not a captured vendor quote. Purchasability in the coin store is not verified by a source.", "where": "coin store", "price": "627 coins (member price 564 coins, 10% member discount; sell-back 62 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 76235 (repo:prototype/osfr-tools/data/content/stores.json:15922); client definition coin_store_prices [627]"},
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel, named in the Howling Hills wiki list alongside Battle Item Mystery Pack and Ninja's Scythe of 1000 Storms; the wheel's spin cost is shown as 343 coins but is not confirmed as this item's cost; no item ID in the repo", "where": "Howling Hills", "price": "unconfirmed (wheel spin 343 coins per wiki snippet)", "currency": "coins", "source": "Howling Hills wiki page (Ninja Prize Wheel section); repo:prototype/osfr-tools/data/content/dungeons/howling_hills.json:2706 (target_id null)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 133243 is 'Shinobi Ninja Cowl'", "source": "locale:133243"},
  {"claim": "Coiled Viper wiki page sells exclusively Ninja job items and lists Shinobi Ninja Cowl under Sells (no price on the wiki)", "source": "https://freerealms.fandom.com/wiki/Coiled_Viper"},
  {"claim": "stores.json item 76235 has purchase 627, member 564, sell 62, category 101", "source": "repo:data/content/stores.json item 76235 (repo:prototype/osfr-tools/data/content/stores.json:15922)"},
  {"claim": "vendors.json marks the 627 price as a stores.json reference, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:41331-41335"},
  {"claim": "Howling Hills wiki page lists Shinobi Ninja Cowl in the Ninja Prize Wheel list next to a 343 Coins line", "source": "Howling Hills wiki page"},
  {"claim": "Howling Hills prize wheel entry has no item ID", "source": "repo:prototype/osfr-tools/data/content/dungeons/howling_hills.json:2706"},
  {"claim": "Video frame lists 'Shinobi Ninja Cowl' among ninja cowls in an inventory view; undated", "source": "video:BJy3sgpdqpw/00588"},
  {"claim": "Client text cluster locale 133238-133248 is the Ninja gear set (Shinobi/Nusumi/Kanja)", "source": "locale:133238-133248"}
 ],
 "confidence": 0.5,
 "open": [
  "No captured Coiled Viper price exists; the 627-coin figure is a coin-store reference and is not confirmed as the vendor price.",
  "Whether the item is currently purchasable in the coin store (stores.json category 101) is unverified.",
  "Prize wheel: the 343-coin figure is a wheel spin cost from a wiki snippet; the cowl's per-item wheel odds and cost are unknown, and there is no item ID to wire to.",
  "Retirement and era: no source in the pack dates the cowl to 2009-2014 or says it was retired. The Coiled Viper revision is 2025-03-15 and the video frame is undated, so live is set to unsure.",
  "No client description text (empty)."
 ]}
